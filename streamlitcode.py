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

#Streamlit application setup
st.set_page_config(page_title="Cancer Detection", page_icon="https://logos-world.net/wp-content/uploads/2022/03/Breast-Cancer-Logo.png", layout="wide")
st.markdown("<h1 style='text-align: center; color: dark grey;'>Breast Cancer Detection API</h1>", unsafe_allow_html=True)
st.markdown("""<style>
 label {
     font-weight : bold;
     }
    </style>""",unsafe_allow_html=True)
# Check if the button is clicked
uploaded_file = st.file_uploader("Kindly Upload your Radiographic Image...", type=["jpg", "jpeg", "png", "jfif"])
if uploaded_file:
     #Display the uploaded image
    image = Image.open(io.BytesIO(uploaded_file.getvalue()))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    #Convert the uploaded file to bytes for the request
    img_bytes = uploaded_file.getvalue()
    prediction = get_prediction(img_bytes)

    #Display the prediction result
    if prediction == "positive":
        st.markdown(f"<h1 style='text-align: center; color: red;'>{prediction}</h1>", unsafe_allow_html=True)
    if prediction == "negative":
        st.markdown(f"<h1 style='text-align: center; color: green;'>{prediction}</h1>", unsafe_allow_html=True)
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/free-vector/clean-medical-background-vector_53876-166662.jpg?w=360&t=st=1709820731~exp=1709821331~hmac=0db852673da32cfcf635ba208130b8182f85c169aea982e137fee2d93197ee40");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
st.video('https://www.youtube.com/watch?v=zhKnW2ri33E')
button_clicked = st.button("Make a Donation to Breast Cancer Research!")
if button_clicked:
    st.markdown("[Visit the website](https://www.contrelecancer.ma/fr/)")
