import pyttsx3

engine = pyttsx3.init()
text = input("Enter your Text: ")
engine.say(text)
engine.runAndWait()
text = input("Enter your Text: ")
sound = pyttsx3(text, lang="en") # en = English

#save your sound (audio file format)
sound.save("my_sound.mp3")

# Play the sound
sa.simpleaudio.play("my_sound.mp3")