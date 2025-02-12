import streamlit as st
from model import load_model, generate_image

# Load model
pipe = load_model()

st.title("AI Clothing Image Generator using Stable Diffusion")

# Text input for user prompt
prompt = st.text_input("Enter a prompt:", "A red satin evening gown with sweetheart neckline and lace sleeves")

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image = generate_image(pipe, prompt)
        st.image(image, caption="Generated Image", use_column_width=True)
        image.save("generated_image.png")

        # Download button
        with open("generated_image.png", "rb") as file:
            st.download_button("Download Image", file, "generated_image.png", "image/png")

