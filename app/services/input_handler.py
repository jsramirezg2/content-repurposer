import os
from pytube import YouTube
import moviepy.editor as mp
import speech_recognition as sr

def process_youtube_url(url: str) -> str:
    """
    Download the YouTube video, extract audio, and convert it to text.
    """
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    output_path = "temp_audio"
    os.makedirs(output_path, exist_ok=True)
    audio_file = video.download(output_path)

    # Convert audio to text
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    # Clean up temporary files
    os.remove(audio_file)
    return text

def process_video_file(file_path: str) -> str:
    """
    Extract audio from a video file and convert it to text.
    """
    audio_path = "temp_audio.wav"
    video = mp.VideoFileClip(file_path)
    video.audio.write_audiofile(audio_path)

    # Convert audio to text
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    # Clean up temporary files
    os.remove(audio_path)
    return text