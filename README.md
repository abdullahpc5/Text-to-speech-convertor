# Text to Speech Converter

This is a simple Python script to convert text input into speech using the `pyttsx3` library.

## Prerequisites

Ensure you have the following libraries installed:

- `pyttsx3`
- `simpleaudio` (if you want to play the saved sound)

You can install them using pip:

```bash
pip install pyttsx3 simpleaudio
```

 # Usage
1. Run the script:

```bash 
python TextSpeech.py
```
2. Enter the text you want to convert to speech when prompted.

3. The script will convert the text to speech and save it as my_sound.mp3.

4. The script will then play the saved sound file.

# Code Explanation
The script initializes the pyttsx3 engine.
Prompts the user to enter text.
Converts the entered text to speech.
Saves the speech as my_sound.mp3.
Plays the saved sound file using simpleaudio.

# Notes

Ensure that you have the necessary permissions to save and play sound files in your environment.
Modify the script as needed for different languages or save formats.
