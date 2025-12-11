# DCNN.py

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os

# ============================
# Image Data Preprocessing
# ============================

# Train data generator with augmentation
train_data_preprocess = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# Test data generator (only normalization)
test_data_preprocess = ImageDataGenerator(rescale=1.0 / 255)

# Load training dataset
train = train_data_preprocess.flow_from_directory(
    'dataset/training',
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary'
)

# Load testing dataset
test = test_data_preprocess.flow_from_directory(
    'dataset/test',
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary'
)

# ============================
# Building the CNN Model
# ============================

cnn = Sequential()

# Convolution + Pooling Layer 1
cnn.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
cnn.add(MaxPooling2D(pool_size=(2, 2)))

# Convolution + Pooling Layer 2
cnn.add(Conv2D(32, (3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten layer
cnn.add(Flatten())

# Fully connected layers
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=1, activation='sigmoid'))

# Compile model
cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ============================
# Training the model
# ============================

history = cnn.fit(
    train,
    epochs=10,
    validation_data=test
)

# ============================
# Plotting Accuracy
# ============================

plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid()
plt.show()

# ============================
# Plotting Loss
# ============================

plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()

# ============================
# Testing on a Single Image
# ============================

test_image_path = os.path.join('dataset', 'single_prediction', '9. what-does-it-mean-when-cat-wags-tail.jpg')

test_image = load_img(test_image_path, target_size=(128, 128))
test_image = img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
test_image = test_image / 255.0  # Normalize

result = cnn.predict(test_image)
print("Prediction Score:", result)

if result[0][0] >= 0.5:
    print("Result: Dog")
else:
    print("Result: Cat")
