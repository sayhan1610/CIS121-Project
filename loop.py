def check_audio_level(audio_level, duration):
    """Return the alert for an audio level and its duration."""
    if audio_level <= 20 and duration >= 30:
        return "The software appears to be broken: audio level stayed very low for 30 seconds."
    if (
        (audio_level >= 100 and duration >= 1)
        or (audio_level >= 90 and duration >= 2)
        or (audio_level >= 80 and duration >= 3)
    ):
        return "Trigger activated."
    return "No trigger."


def run_noise_detector():
    audio_text = input("Enter the audio level: ").strip()
    duration_text = input("Enter the time at that level (seconds): ").strip()

    try:
        audio_level = float(audio_text)
        duration = float(duration_text)
    except ValueError:
        print("Please enter valid numbers for the audio level and time.")
        return

    print(check_audio_level(audio_level, duration))


if __name__ == "__main__":
    run_noise_detector()