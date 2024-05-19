import cv2
import os

class VideoToImages:
    def __init__(self, video_path, output_folder):
        self.video_path = video_path
        self.output_folder = output_folder

    def start(self):
        cap = cv2.VideoCapture(self.video_path)

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        if not cap.isOpened():
            print("Erreur: Impossible d'ouvrir la vidéo.")
            exit()

        fps = cap.get(cv2.CAP_PROP_FPS)
        print(f"FPS de la vidéo : {fps}")
        second_count = 0
        frame_saved_count = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Fin de la vidéo ou erreur de lecture.")
                break

            current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            current_second = int(current_frame / fps)

            if current_second >= second_count:
                output_filename = os.path.join(self.output_folder, f'frame_{frame_saved_count}.jpg' if frame_saved_count > 9 else f'frame_0{frame_saved_count}.jpg')
                cv2.imwrite(output_filename, frame)
                frame_saved_count += 1
                second_count += 1

        cap.release()