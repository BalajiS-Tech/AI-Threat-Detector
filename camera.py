# camera.py

import cv2
from PIL import Image
import argparse
import shutil
import os

class VideoCamera(object):
    def __init__(self):
        # Initialize webcam safely
        self.video = cv2.VideoCapture(0)

        if not self.video.isOpened():
            raise Exception("Error: Unable to access webcam.")

        self.k = 1

    def __del__(self):
        if self.video.isOpened():
            self.video.release()

    def safe_read_text(self, filename, default=""):
        """Reads a file safely and returns default if missing."""
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return f.read().strip()
        return default

    def get_frame(self):
        success, image = self.video.read()

        if not success:
            print("Warning: Failed to capture frame.")
            return None

        cv2.imwrite("getimg.jpg", image)

        # Load face cascade safely
        face_cascade_path = 'haarcascade_frontalface_default.xml'
        if not os.path.exists(face_cascade_path):
            print("Error: Missing Haar Cascade XML file.")
        else:
            face_cascade = cv2.CascadeClassifier(face_cascade_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Read required text files safely
        user_name = self.safe_read_text("user.txt", "user")
        photo_mode = self.safe_read_text("photo.txt", "0")

        # Save resized images only for first 40 frames
        if self.k <= 40:
            self.k += 1
            filename = f"{user_name}_{self.k}.jpg"

            with open("det.txt", "w") as d:
                d.write(str(self.k))

            if photo_mode == "2":
                if os.path.exists("getimg.jpg"):
                    img = Image.open("getimg.jpg")
                    resized = img.resize((300, 300))
                    resized.save("image.jpg")
                    shutil.copy("image.jpg", f"static/frame/{filename}")

        # Encode frame for web streaming
        ret, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()
