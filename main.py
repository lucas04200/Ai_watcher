import os

from src.DataManager import DataManager
from src.ModelGestion import ModelGestion
from src.VideoToImages import VideoToImages
from src.ClientSocket import ClientSocket

if __name__ == '__main__':
    video_path = "data/input/first_video.mp4"
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    data_manager = DataManager(video_name)

    video_to_images = VideoToImages(video_path, data_manager.frames_folder)
    model = ModelGestion(model_name='rapid', weights_path='models/weights/pL1_MWHB608_Mar11_4500.ckpt', using_cuda=True,
                         conf_thres=0.3)
    socket = ClientSocket("127.0.0.1", 25001, 10 / 1920, 10 / 1080)
    cube = ClientSocket("127.0.0.1", 25002, 0, 0)

    if not os.listdir(data_manager.frames_folder):  # pour charger les frames si le dossier est vide ;)
        video_to_images.start()

    results = model.detector.detect_imgSeq(img_dir=data_manager.frames_folder, input_size=1024, conf_thres=0.3)
    cube.send_data(f"{len(results)}")

    data_manager.results = results
    data_manager.save_data()

    socket.start(results)
