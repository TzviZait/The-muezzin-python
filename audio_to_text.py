import speech_recognition as sr


class AudioToText:

    def __init__(self):
        pass

    def audio_converter(self,file_path):

        # Initialize the recognizer
        r = sr.Recognizer()

        # Path to your audio file (e.g., WAV format)
        # Open the audio file
        with sr.AudioFile(file_path) as source:
            # Listen for the data (load audio to memory)
            audio_data = r.record(source)

            # Recognize speech using Google Speech Recognition (requires internet connection)
            try:
                text = r.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

