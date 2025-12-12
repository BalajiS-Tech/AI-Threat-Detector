# NOX EYE – AI Based Threat Detection System

NOX EYE is an AI-powered smart surveillance system that detects abnormal activity, compares faces in real-time, and alerts the user using automated notifications.  
It uses Flask, OpenCV, TensorFlow, MySQL, and image processing techniques.

---

## 🚀 Features
- Real-time video monitoring (OpenCV)
- Face capture and comparison using image hashing
- Deep Learning–based DCNN classifier
- Automatic alert generation with SMS API
- Admin & User login system
- MySQL database for logs, users, and captured faces
- Image preprocessing (denoising, segmentation, thresholding)

---

## 📂 Project Structure
AI-Threat-Detector/
│── main.py
│── camera.py
│── DCNN.py
│── static/
│── templates/
│── dataset/
│── requirements.txt
│── README.md

## 🔧 Installation
pip install -r requirements.txt


## ▶️ Run the Project
python main.py
Copy code
Visit in browser:
http://127.0.0.1:5000

## 🗄 Database
Create a MySQL database: