# AI Content Repurposer

## Overview

The **AI Content Repurposer** is a web application that leverages AI to transform content into different formats tailored for specific platforms. Whether you need a concise summary, an engaging Twitter thread, or a professional LinkedIn post, this tool helps you repurpose your content efficiently.

## Features

- **Content Summarization**: Generate a 3–5 sentence summary of your content.
- **Twitter Threads**: Create concise and engaging Twitter threads (up to 8 tweets).
- **LinkedIn Posts**: Craft professional and informative LinkedIn posts.
- **YouTube URL Support**: Paste a YouTube URL and automatically transcribe the audio using OpenAI Whisper.
- **Video File Upload**: Upload a video file (with audio) and transcribe it using Whisper.
- **Automatic Temp File Handling**: All temporary files are cleaned up after processing, even if errors occur.
- **User-Friendly Interface**: Simple and intuitive web interface for content input and output.

## Technologies Used

- **Python**: Backend logic and AI integration.
- **Flask**: Web framework for building the application.
- **Anthropic Claude API**: AI model for content generation.
- **OpenAI Whisper**: For audio transcription from YouTube and video files.
- **MoviePy**: For extracting audio from video files.
- **Pytubefix**: For downloading YouTube videos.
- **HTML/CSS**: Frontend design and styling.

## Setup Instructions

### Prerequisites

- Python 3.12 or higher
- Pipenv for dependency management
- An API key for the Anthropic Claude API

### Installation

1. Clone the repository:
   ```powershell
   git clone https://github.com/jsramirezg2/content-repurposer.git
   cd content-repurposer
   ```

2. Install dependencies:
   ```powershell
   pipenv install
   ```

3. Create a `.env` file in the root directory and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```powershell
   pipenv run python app/main.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Choose your input type: Text, YouTube URL, or Video File.
- For YouTube or video files, the app will extract and transcribe the audio using Whisper.
- Select the target platform (Summary, Twitter Thread, LinkedIn Post).
- Click "Generate" to receive your repurposed content.

## Notes

- Uploaded and downloaded files are stored temporarily in the `temp/` directory and are deleted after processing.
- Only video files with audio tracks are supported for transcription.
- If a video has no audio, you will receive a clear error message.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Anthropic Claude API](https://www.anthropic.com/) for powering the AI content generation.
- [OpenAI Whisper](https://github.com/openai/whisper) for audio transcription.
- [MoviePy](https://zulko.github.io/moviepy/) for video/audio processing.
- [Pytubefix](https://github.com/nficano/pytube) for YouTube video downloads.
- Flask for providing a lightweight and flexible web framework.
- ChatGPT for writing this readme file