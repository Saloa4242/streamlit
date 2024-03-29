import streamlit as st
import requests
from PIL import Image
import io
#Define your classes for predictions
classes = ['positive', 'negative']
def get_prediction(image_bytes):
     #Define the correct API endpoint URL
    url = "https://breast-cancer-repo-wqs3wc3qha-uc.a.run.app/predict"
    #Create an in-memory file-like object
    files = {'img': ('image.jpg', image_bytes, 'image/jpeg')}
    headers = {'accept': 'application/json'}   #Assuming the server expects JSON responses
    try:
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
             #Assuming the server responds with JSON
            return response.json()
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.RequestException as e:
        return f"Request failed: {e}"

st.title("Breast Cancer Detection")
st.set_page_config(page_title="Cancer Detection", page_icon="https://logos-world.net/wp-content/uploads/2022/03/Breast-Cancer-Logo.png", layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Kindly Upload your Radiographic Image</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "jfif"])
if uploaded_file:
    # Display the uploaded image
    image = Image.open(io.BytesIO(uploaded_file.read()))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the uploaded file to bytes for the request
    img_bytes = uploaded_file.read()
    prediction = get_prediction(img_bytes)

    # Display the prediction result
    st.write(f"Prediction: {prediction}")

# Define background image style
background_image = """
<style>
body {
    background-image: url("https://img.freepik.com/free-vector/clean-medical-background-vector_53876-166662.jpg?w=360&t=st=1709820731~exp=1709821331~hmac=0db852673da32cfcf635ba208130b8182f85c169aea982e137fee2d93197ee40");
    background-size: cover;
    background-position: center;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
