import matplotlib.pyplot as plt
import os

from PIL import Image

from src.api import Detector


class ModelGestion:
    def __init__(self, model_name, weights_path, using_cuda, conf_thres, ):
        self.detector = Detector(model_name, weights_path, use_cuda=using_cuda)
        self.conf_thres = conf_thres

    def show_zenital_box(self, img_dir, input_size):
        # Liste tous les fichiers dans le dossier
        for filename in os.listdir(img_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Filtre pour les fichiers image
                img_path = os.path.join(img_dir, filename)  # Chemin complet vers l'image
                print(f"Processing {img_path}...")

                # Utiliser la méthode detect_one du détecteur
                result_image = self.detector.detect_one(
                    img_path=img_path,
                    input_size=input_size,  # Spécification de la taille d'entrée
                    conf_thres=self.conf_thres,  # Seuil de confiance
                    return_img=True,  # Supposons que cela retourne l'image avec des boîtes
                    visualize=False  # Désactivation de l'affichage automatique dans detect_one
                )

                # Affichage des résultats
                if result_image is not None:
                    plt.figure(figsize=(10, 10))
                    plt.imshow(result_image)
                    plt.title(f"Detection for {filename}")
                    plt.show()

    def show_2d_plot(self, img_dir, input_size):
        # Liste des fichiers image
        image_files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        if not image_files:
            print("No images found in the directory.")
            return

        # Utiliser les dimensions de la première image
        first_image_path = os.path.join(img_dir, image_files[0])
        with Image.open(first_image_path) as img:
            max_width, max_height = img.size

        # Créer une seule figure et des axes
        fig, ax = plt.subplots()
        ax.imshow(Image.new('RGB', (max_width, max_height), (255, 255, 255)))  # Fond blanc
        ax.set_xlim([0, max_width])
        ax.set_ylim([max_height, 0])

        # Traiter chaque fichier image dans le répertoire
        for filename in image_files:
            img_path = os.path.join(img_dir, filename)
            print(f"Processing {img_path}...")

            detections = self.detector.detect_one(
                img_path=img_path,
                input_size=input_size,
                conf_thres=self.conf_thres,
                return_img=False
            )

            # Ajouter les centres des détections sur le plan
            if detections is not None and detections.numel() > 0:
                for detection in detections:
                    x, y, w, h, angle, conf = detection
                    center_x, center_y = x + w / 2, y + h / 2
                    ax.plot(center_x, center_y, 'ro')

        plt.title("Detection centers for all images")
        plt.show()