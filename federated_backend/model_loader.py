import tensorflow as tf
from utils import preprocess_image
import numpy as np

MODEL_PATH = "models/best_global_model.weights.h5"

def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(224, 224, 3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = build_model()
model.load_weights(MODEL_PATH)

def predict_stroke(image_path):
    img_array = preprocess_image(image_path)
    prob = model.predict(np.expand_dims(img_array, axis=0))[0][0]
    return "Stroke" if prob >= 0.5 else "Normal"
