from flask import Flask, render_template, request
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = load_model('path/to/your/model.h5')

# Define the classes
classes = ['Non-cancerous', 'Cancerous']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    # Get the uploaded file
    uploaded_file = request.files['file']

    # Save the uploaded file
    file_path = 'uploads/' + uploaded_file.filename
    uploaded_file.save(file_path)

    # Load and preprocess the image
    img = image.load_img(file_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the class of the uploaded image
    predictions = model.predict(img_array)
    predicted_class = classes[int(predictions[0][0])]

    # Delete the uploaded file
    os.remove(file_path)

    return render_template('result.html', predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
