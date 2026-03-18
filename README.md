# Face-Detection-
This project detects a person’s face in real time using OpenCV and analyzes facial features to determine whether the person is smiling and whether their eyes are open. It uses Haar Cascade classifiers and displays results with bounding boxes and labels on the live video feed.

Features
Real-time face detection
Eye detection (checks if eyes are open)
Smile detection with reduced false positives
Works on live webcam feed
Lightweight and fast

Technologies Used
Python
OpenCV
Haar Cascade Classifiers

📂 Project Structure
project/
│── main.py
│── haarcascade_frontalface_default.xml
│── haarcascade_eye.xml
│── haarcascade_smile.xml


⚙️ Installation
-Install dependencies
         "pip install opencv-python"
-Download Haar Cascade files
  Face
  Eye
  Smile
  (Place them in the project folder)

▶️ Usage
-Run the script:
        "python FaceEyeSmile_Detection.py"
-Press 'q' to exit the program

⚠️ Limitations
-May give false positives in poor lighting
-Smile detection may vary with facial angles
-Performance depends on camera quality

📈 Future Improvements
-Use deep learning models (CNN, DNN)
-Add emotion detection
-Improve accuracy in low-light conditions

