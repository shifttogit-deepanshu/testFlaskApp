import numpy as np
import os
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt


# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return "Hello World Let's see!!!!!"

if __name__ == '__main__':
    app.run(debug=True)