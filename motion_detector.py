import cv2
import tkinter as tk
from tkinter import filedialog

MIN_CONTOUR_AREA = 200 #contour area threshold

def choose_source():
    root = tk.Tk()
    root.title("motion")
    root.geometry("300x150")

    def use_webcam():
        root.destroy()
        run(0)

    def use_file():
        path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mov")]
        )
        if path:
            root.destroy()
            run(path)

    tk.Button(root, text="webcam", command=use_webcam, width=20).pack(pady=10)
    tk.Button(root, text="file", command=use_file, width=20).pack(pady=10)
    root.mainloop()

def run(source):
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print("Couldn't open the source")
        return
    ret, prev_frame = cap.read()
    if not ret:
        print("Couldn't read the first frame")
        return
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (3, 3), 0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < MIN_CONTOUR_AREA:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Motion", frame)
        prev_gray = gray
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

choose_source()