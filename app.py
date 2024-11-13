import streamlit as st
from main import generate_image, generate_text
from PIL import Image

# Streamlit app configuration
st.set_page_config(page_title="Multi-Mind Chatbot")
st.header("MULTI-MIND CHATBOT")

# User input fields
input_text = st.text_input("Input Prompt for Text Generation: ", key='text_input')
image_prompt = st.text_input("Input Prompt for Image Generation: ", key='image_input')
uploaded_file = st.file_uploader("Choose an image....", type=["jpg","png","jpeg"])
image = ""
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image..", use_container_width=True)

# Text generation button
if st.button("Generate Text"):
    if not input_text.strip() and not image:
        st.error("Please provide a text prompt or upload an image for generation.")
    else:
        response = generate_text(input_text, image)
        st.subheader("Generated Text:")
        st.write(response)

# Image generation button
if st.button("Generate Image"):
    if not image_prompt.strip() and not image:
        st.error("Please provide a image prompt or upload an image for generation.")
    else:
        generated_image = generate_image(image_prompt, image)
        if isinstance(generated_image, str):  # Error handling
            st.error(generated_image)
        else:
            st.subheader("Generated Image:")
            st.image(generated_image, caption="AI-Generated Image", use_container_width=True)