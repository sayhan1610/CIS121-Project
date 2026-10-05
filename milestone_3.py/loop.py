while True:
    # Read the values as text first so invalid input can be checked without try/except.
    audio_text = input("Enter the audio level: ").strip()
    duration_text = input("Enter the time at that level (seconds): ").strip()

    # Accept whole numbers or decimals; reject empty text and other characters.
    audio_is_number = audio_text.replace(".", "", 1).isdigit()
    duration_is_number = duration_text.replace(".", "", 1).isdigit()

    if not audio_is_number or not duration_is_number:
        print("Please enter valid numbers for the audio level and time.")
        continue

    # Convert only after both entries have passed the numeric check.
    audio_level = float(audio_text)
    duration = float(duration_text)

    # Report a likely software failure if the volume stays very low for 30 seconds.
    if audio_level <= 20 and duration >= 30:
        print("The software appears to be broken: audio level stayed very low for 30 seconds.")
    # Higher audio levels can trigger with shorter durations.
    elif (
        (audio_level >= 100 and duration >= 1)
        or (audio_level >= 90 and duration >= 2)
        or (audio_level >= 80 and duration >= 3)
    ):
        print("Trigger activated.")
    else:
        print("No trigger.")