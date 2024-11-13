import os
import torch
from dotenv import load_dotenv
import google.generativeai as genai
from diffusers import StableDiffusionPipeline

# Load environment variables
load_dotenv()
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize Gemini text generation model
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize Stable Diffusion for image generation
sd_pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
sd_pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

# Function to generate text using Gemini
def generate_text(input_text, image=None):
    try:
        # If image is provided, convert it to text or use it as a context
        inputs = []
        if input_text.strip():
            inputs.append(input_text)
        if image:
            inputs.append(image)  # Pass the PIL image directly if supported

        response = model.generate_content(inputs)
        return response.text
    except Exception as e:
        return f"Error generating text: {str(e)}"

# Function to generate an image using Stable Diffusion
def generate_image(prompt, image=None):
    try:
        if image:
            # Optionally modify the prompt using the uploaded image (if required)
            prompt = f"{prompt} based on the uploaded image"
        image = sd_pipeline(prompt).images[0]
        return image
    except Exception as e:
        return f"Error generating image: {str(e)}"


