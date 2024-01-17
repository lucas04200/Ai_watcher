from src.ModelGestion import *
from src.KeypointsDrawing import *
from src.ModelGenerating import *
import cv2

class App:
    def __init__(self):
        pass

    def execute(self):
        kd = KeypointsDrawing()
        model = ModelGenerating("models/saved_model")
        mg = ModelGestion(kd)

        while mg.cap.isOpened():
            ret, frame = mg.cap.read()

            # Resize image
            img = frame.copy()
            img = tf.image.resize_with_pad(tf.expand_dims(img, axis=0), 192,
                                           256)  # largeur minimum 256px, largeur et longueur doivent eêtre des multiples de 32, faire attention à conserver un aspect ratio similaire à la caméra tout en ayant la condition précédente remplie (pour se faire s'occuper de la longueur puis pour la hauteur diviser le ratio et chercher le multiple de 32 le plus proche du résultat
            input_img = tf.cast(img, dtype=tf.int32)

            # Detection section
            results = model.movenet(input_img)
            keypoints_with_scores = results['output_0'].numpy()[:, :, :51].reshape((6, 17, 3))

            # Render keypoints
            mg.loop_through_people(frame, keypoints_with_scores, 0.3)

            # print("---------Frame Data---------")
            # print(keypoints_with_scores)

            cv2.imshow('Movenet Multipose', frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        mg.cap.release()
        cv2.destroyAllWindows()