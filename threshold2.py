# Noise detection settings
settings = {
    "normal": {
        "threshold": 65,
        "duration": 5
    },
    "very_loud": {
        "threshold": 85,
        "duration": 2
    },
    "cooldown": 5
}

# Noise levels measured every second
noise_levels = [
    45, 100, 45,
    65, 68, 70, 72, 71,
    44, 47, 46, 45, 50,
    90, 93, 50
]


# Function to detect noise
def detect_noise(noise_levels, settings):

    normal_seconds = 0
    loud_seconds = 0
    cooldown = 0

    for second, noise in enumerate(noise_levels, 1):

        # Wait before detecting another noise
        if cooldown > 0:
            cooldown -= 1
            continue

        # Check normal noise threshold
        if noise >= settings["normal"]["threshold"]:
            normal_seconds += 1
        else:
            normal_seconds = 0

        # Check very loud noise threshold
        if noise >= settings["very_loud"]["threshold"]:
            loud_seconds += 1
        else:
            loud_seconds = 0

        # Detect very loud continuous noise
        if loud_seconds >= settings["very_loud"]["duration"]:
            print("Very Loud Noise Detected!", second)
            cooldown = settings["cooldown"]
            normal_seconds = 0
            loud_seconds = 0

        # Detect normal continuous noise
        elif normal_seconds >= settings["normal"]["duration"]:
            print("Noise Detected!", second)
            cooldown = settings["cooldown"]
            normal_seconds = 0
            loud_seconds = 0


# Run the noise detector
detect_noise(noise_levels, settings)