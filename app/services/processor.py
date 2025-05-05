import os
import re
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env file
load_dotenv()

# Initialize Claude API client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Generate full prompt for Claude
import os
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env file
load_dotenv()

# Initialize Claude API client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Generate full prompt for Claude based on selected platform
def generate_full_prompt(content: str, platform: str) -> str:
    if platform == "summary":
        return f"""
        Summarize the following content in 3–5 sentences:
        \"\"\"
        {content}
        \"\"\"
        """
    elif platform == "twitter":
        return f"""
        Write a Twitter thread (max 8 tweets) based on the following content. Each tweet should be concise and engaging:
        \"\"\"
        {content}
        \"\"\"
        """
    elif platform == "linkedin":
        return f"""
        Write a professional LinkedIn post based on the following content. It should be informative and suitable for LinkedIn:
        \"\"\"
        {content}
        \"\"\"
        """
    else:
        return ""


# Call Claude API and get the response
def call_claude(prompt: str) -> str:
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # change claude model if needed
        max_tokens=1024,
        temperature=0.5,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


# Function to repurpose text based on platform (summary, twitter, linkedin)
def repurpose_text(text: str, platform: str) -> str:
    if platform in ['summary', 'twitter', 'linkedin']:
        prompt = generate_full_prompt(text, platform)  # Generate prompt for the selected platform
        return call_claude(prompt)  # Call the Claude API with the generated prompt
    else:
        return "Invalid platform selected. Please choose 'summary', 'twitter', or 'linkedin'."

# Example usage
text = """
    Artificial intelligence (AI) is transforming the way we work, create, and communicate. From generating content to automating repetitive tasks, AI tools have become essential for boosting productivity. One major impact is on content creation: marketers can now generate articles, social media posts, and even video scripts in minutes. Meanwhile, customer support is being enhanced through AI chatbots that provide instant responses around the clock. As these tools become more sophisticated, the role of human creativity will shift toward editing, refining, and guiding the AI — not just producing from scratch. Understanding how to leverage AI without losing authenticity will be a key skill for professionals in the coming years.
    """

# Call Claude API and get the response
def call_claude(prompt: str) -> str:
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        temperature=0.5,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


# Function to repurpose text based on platform (summary, twitter, linkedin)
def repurpose_text(text: str, platform: str) -> str:
    return call_claude(generate_full_prompt(text, platform)) if platform in ['summary', 'twitter', 'linkedin'] else None


# example usage
if __name__ == "__main__":
    text = """
        Artificial intelligence (AI) is transforming the way we work, create, and communicate. From generating content to automating repetitive tasks, AI tools have become essential for boosting productivity. One major impact is on content creation: marketers can now generate articles, social media posts, and even video scripts in minutes. Meanwhile, customer support is being enhanced through AI chatbots that provide instant responses around the clock. As these tools become more sophisticated, the role of human creativity will shift toward editing, refining, and guiding the AI — not just producing from scratch. Understanding how to leverage AI without losing authenticity will be a key skill for professionals in the coming years.
        """

    result = repurpose_text(text, 'twitter')
    print(result)