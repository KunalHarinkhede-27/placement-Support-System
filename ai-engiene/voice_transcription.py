import speech_recognition as sr

def transcribe_audio(audio_file):
    """
    Transcribes spoken audio to text using Google Web Speech API.
    
    :param audio_file: FileStorage object from Flask (e.g., request.files['audio'])
    :return: Transcribed text string
    """
    recognizer = sr.Recognizer()

    try:
        # Convert audio file to AudioFile format
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        # Recognize using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Audio not clear or empty. Please try again with a clearer voice."
    except sr.RequestError:
        return "Could not reach the speech recognition service."
    except Exception as e:
        return f"Error processing audio: {str(e)}"

# Optional: For quick local testing
if __name__ == "__main__":
    with sr.AudioFile("sample.wav") as source:
        recognizer = sr.Recognizer()
        audio = recognizer.record(source)
        try:
            print("Transcription:", recognizer.recognize_google(audio))
        except Exception as e:
            print("Error:", e)
