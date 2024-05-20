import cv2
import os

def extract_key_frames(video_path, output_dir, frame_interval=30):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    success = True
    
    while success:
        success, frame = cap.read()
        if frame_count % frame_interval == 0 and success:
            cv2.imwrite(os.path.join(output_dir, f"frame_{frame_count}.jpg"), frame)
        frame_count += 1
    
    cap.release()