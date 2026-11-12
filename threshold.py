# Noise Detector - Threshold Settings

# Store noise thresholds for different locations
thresholds = {
    "library": 40,
    "classroom": 60,
    "cafeteria": 75
}

# Select the location
location = "classroom"

# Current noise level in dB
current_noise = 65

# Get the threshold from the dictionary
threshold = thresholds[location]

# Check if the noise exceeds the threshold
if current_noise > threshold:
    print("Too Loud!")
else:
    print("Normal")