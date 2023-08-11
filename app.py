import speech_recognition as sr
import time

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print('---------------------')
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            time.sleep(1)
            try:
                print("Transcribing...")
                text = recognizer.recognize_google(audio, language='en-US')  # English language
                print("Recognized Text:", text)
                return text
            except sr.UnknownValueError:
                print("I didn't understand.")
            except sr.RequestError:
                print("Request error, check your connection.")
            time.sleep(1)

if __name__ == "__main__":
    while True:
        speech_to_text()

