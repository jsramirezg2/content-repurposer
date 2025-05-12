import os
import logging
from pytubefix import YouTube
import moviepy.editor as mp
from whisper import load_model

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_youtube_url(url: str) -> str:
    """
    Download the YouTube video, extract audio, and convert it to text using Whisper.
    """
    yt = YouTube(
        url,
        use_oauth=False,
        allow_oauth_cache=False
    )

    video = yt.streams.get_lowest_resolution()
    output_path = "./temp"
    os.makedirs(output_path, exist_ok=True)
    video_file = video.download(output_path=output_path)

    # Convert video to audio
    audio_path = "./temp/temp_audio.wav"
    video_clip = mp.VideoFileClip(video_file)
    video_clip.audio.write_audiofile(audio_path)
    video_clip.close()  # Ensure the video file is released

    text = None
    try:
        # Convert audio to text using Whisper
        model = load_model("base")
        result = model.transcribe(audio_path)
        text = result['text']
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        text = f"An unexpected error occurred: {e}"
    finally:
        # Clean up temporary files
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(video_file):
            os.remove(video_file)

    return text

def process_video_file(file_path: str) -> str:
    """
    Extract audio from a video file and convert it to text.
    """
    audio_path = "temp/temp_audio.wav"
    video = mp.VideoFileClip(file_path)
    if video.audio is None:
        video.close()
        if os.path.exists(audio_path):
            os.remove(audio_path)
        return "The uploaded video does not contain an audio track."
    video.audio.write_audiofile(audio_path)
    video.close()  # Ensure the video file is released

    text = None
    try:
        # Convert audio to text
        model = load_model("base")
        result = model.transcribe(audio_path)
        text = result['text']
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        text = f"An unexpected error occurred: {e}"
    finally:
        # Clean up temporary files
        if os.path.exists(audio_path):
            os.remove(audio_path)
    return text


if __name__ == "__main__":
    # Example usage

    mode = input("Enter mode (youtube/video): ").strip().lower()
    match mode:
        case "youtube":
            youtube_url = input("Enter YouTube URL: ").strip()
            text = process_youtube_url(youtube_url)
            print("YouTube Text:", text)
        case "video":
            video_file_path = input("Enter video file path: ").strip()
            text = process_video_file(video_file_path)
            print("Video File Text:", text)
        case _:
            print("Invalid mode selected.") 

    # remember to fix the file path for the video file in the above examples