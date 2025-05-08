import os
import logging
from pytubefix import YouTube
import moviepy.editor as mp
import speech_recognition as sr

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_youtube_url(url: str) -> str:
    """
    Download the YouTube video, extract audio, and convert it to text.
    """
    yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=False
    )

    video = yt.streams.get_lowest_resolution()
    output_path = "."
    os.makedirs(output_path, exist_ok=True)
    video_file = video.download(output_path=output_path)

    # Convert video to audio
    audio_path = os.path.join(output_path, "temp_audio.wav")
    video_clip = mp.VideoFileClip(video_file)
    video_clip.audio.write_audiofile(audio_path)

    try:
        # Convert audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
    except sr.RequestError as e:
        logging.error(f"API request failed: {e}")
        text = f"API request failed: {e}"
    except sr.UnknownValueError:
        logging.error("Speech was unintelligible.")
        text = "Speech was unintelligible."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        text = f"An unexpected error occurred: {e}"

    # Clean up temporary files
    return text

def process_video_file(file_path: str) -> str:
    """
    Extract audio from a video file and convert it to text.
    """
    audio_path = "temp_audio.wav"
    video = mp.VideoFileClip(file_path)
    video.audio.write_audiofile(audio_path)

    try:
        # Convert audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
    except sr.RequestError as e:
        logging.error(f"API request failed: {e}")
        text = f"API request failed: {e}"
    except sr.UnknownValueError:
        logging.error("Speech was unintelligible.")
        text = "Speech was unintelligible."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        text = f"An unexpected error occurred: {e}"

    # Clean up temporary files
    os.remove(audio_path)
    return text


if __name__ == "__main__":
    # Example usage
    youtube_url = "https://youtu.be/PJlCM-cITDA?list=LL"
    video_file_path = "videoplayback.mp4"

    youtube_text = process_youtube_url(youtube_url)
    print("YouTube Text:", youtube_text)

    #video_text = process_video_file(video_file_path)
    #print("Video File Text:", video_text)

    # remember to fix the file path for the video file in the above examples