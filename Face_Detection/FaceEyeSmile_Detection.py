import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 6, minSize=(80,80))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(20,20))
        if len(eyes) >= 2:
            cv2.putText(frame, "Eyes Detected", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        # 🔥 UPDATED SMILE DETECTION (STRICT)
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            1.3,
            30,
            minSize=(30,30)
        )

        for (sx, sy, sw, sh) in smiles:
            # filter small false detections
            if sw > w * 0.4:
                cv2.putText(frame, "Smile Detected", (x, y+h+30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                break

    cv2.imshow("Face, Eye and Smile Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()