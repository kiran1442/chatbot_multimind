# MULTI MIND CHATBOT

Multi-Mind Chatbot is an AI-powered chatbot capable of generating both text-based content and images. It leverages the capabilities of Google's Gemini model for text generation and Stable Diffusion for image generation. Additionally, the chatbot allows users to upload images to influence the output, making it a multi-modal system that integrates visual and textual inputs seamlessly.

## Features

### 1. Text Generation:
- Uses Google Gemini (gemini-1.5-flash) to generate meaningful text based on user input and optional uploaded images.
### 2. Image Generation:
- Generates AI-powered images using Stable Diffusion with prompts and optional image inputs.
### 3. Multi-Modal Input:
- Accepts text prompts and uploaded images to create contextually enriched outputs.
### 4. Interactive Interface:
- Built with Streamlit for a user-friendly, web-based interface.

## Prerequisites

### Ensure you have the following installed:
- Python 3.7 or higher
<!-- start code-->
### Install the required dependencies using pip:
    pip install -r requirements.txt
<!-- end code-->

## Technologies Used
- Python: Core programming language.
- Streamlit: Framework for building interactive web applications.
- Google Gemini AI: For advanced text generation.
- Stable Diffusion (via Diffusers): For creating AI-generated images.
- Pillow (PIL): For handling uploaded images.
- PyTorch: Backend for running Stable Diffusion models.
- dotenv: For managing environment variables.

## How it Works

<!-- code start-->
### 1. Open the app in your browser:
    streamlit run app.py
<!-- code end-->
### 2. Text Generation:
    - Enter a text prompt in the "Input Prompt for Text Generation" field.
    - Optionally upload an image to provide additional context.
    - Click Generate Text to view the generated response.
### 3. Image Generation:
    - Enter a descriptive prompt in the "Input Prompt for Image Generation" field.
    - Optionally upload an image to influence the generated output.
    - Click Generate Image to view the generated artwork.

## Project Structure

- app.py:  Streamlit code
- main.py: Main code of project
- requirements.txt: Required Python libraries
- .env: Environment variables file
- README.md: Project documentation
