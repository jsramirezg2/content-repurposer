# AI Content Repurposer

## Overview

The **AI Content Repurposer** is a web application that leverages AI to transform content into different formats tailored for specific platforms. Whether you need a concise summary, an engaging Twitter thread, or a professional LinkedIn post, this tool helps you repurpose your content efficiently.

## Features

- **Content Summarization**: Generate a 3–5 sentence summary of your content.
- **Twitter Threads**: Create concise and engaging Twitter threads (up to 8 tweets).
- **LinkedIn Posts**: Craft professional and informative LinkedIn posts.
- **User-Friendly Interface**: Simple and intuitive web interface for content input and output.

## Technologies Used

- **Python**: Backend logic and AI integration.
- **Flask**: Web framework for building the application.
- **Anthropic Claude API**: AI model for content generation.
- **HTML/CSS**: Frontend design and styling.

## Setup Instructions

### Prerequisites

- Python 3.12 or higher
- Pipenv for dependency management
- An API key for the Anthropic Claude API

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jsramirezg2/content-repurposer.git
   cd content-repurposer
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Create a `.env` file in the root directory and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```bash
   pipenv run python app/main.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Anthropic Claude API](https://www.anthropic.com/) for powering the AI content generation.
- Flask for providing a lightweight and flexible web framework.
- ChatGPT for writing this readme file