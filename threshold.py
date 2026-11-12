# Noise detection settings
settings = {
    "threshold": 65,
    "duration": 3
}

# Noise levels measured every second
noise_levels = [45, 100, 45, 65, 68, 70, 50]


# Function to detect continuous noise
def detect_noise(noise_levels, settings):

    threshold = settings["threshold"]
    duration = settings["duration"]

    # Count consecutive loud seconds
    loud_seconds = 0

    for noise in noise_levels:

        if noise > threshold:
            loud_seconds += 1
        else:
            loud_seconds = 0

        # Check if noise lasts long enough
        if loud_seconds >= duration:
            return True

    return False


# Call the function
result = detect_noise(noise_levels, settings)

if result:
    print("Noise Detected!")
else:
    print("Normal")