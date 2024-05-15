"""
Les coordonnées du coin supérieur gauche (x, y) : Ces coordonnées spécifient l'emplacement du coin supérieur gauche de la boîte englobante dans l'image.
La largeur (w) : Il s'agit de la largeur de la boîte englobante, mesurée horizontalement à partir du coin supérieur gauche.
La hauteur (h) : Il s'agit de la hauteur de la boîte englobante, mesurée verticalement à partir du coin supérieur gauche.
L'angle (a) : Il représente l'orientation de la boîte englobante par rapport à l'axe horizontal de l'image. Cet angle est souvent mesuré en degrés et peut être positif ou négatif, selon la rotation de la boîte englobante par rapport à l'axe horizontal.
"""

import socket
import time

def send_data(data, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.sendall(data.encode("utf-8"))
        print(f"Sent: {data}")
    finally:
        sock.close()

def format_data(index, x, y, w, h, a):
    return f"{index};{x:.2f},{y:.2f},{w:.2f},{h:.2f};{a:.2f}"

# Adapter échelle
host, port = "127.0.0.1", 25001  # Unity server IP and port
scale_factor_x = 10 / 1920  # 10 est l'espace des coordonnées qu'on détermine dans Unity (z scale)
scale_factor_y = 10 / 1080

# Données de boîtes englobantes
boxes = [
    {'image_id': 'frame_0', 'bbox': [793.57, 861.21, 90.50, 213.26, 14.56], 'score': 0.9966567754745483, 'segmentation': []},
    {'image_id': 'frame_0', 'bbox': [1072.76, 363.40, 118.73, 225.67, 57.25], 'score': 0.9827636480331421, 'segmentation': []},
    {'image_id': 'frame_0', 'bbox': [880.02, 321.29, 235.35, 309.56, 18.17], 'score': 0.9785738587379456, 'segmentation': []},
    {'image_id': 'frame_0', 'bbox': [999.67, 712.73, 145.93, 230.21, -18.48], 'score': 0.9660441875457764, 'segmentation': []},
    {'image_id': 'frame_0', 'bbox': [883.57, 84.39, 89.87, 170.08, 2.90], 'score': 0.9392904043197632, 'segmentation': []},
    {'image_id': 'frame_0', 'bbox': [1220.21, 647.42, 138.17, 296.75, 123.75], 'score': 0.6300101280212402, 'segmentation': []},
    {'image_id': 'frame_0', 'bbox': [637.15, 608.07, 123.37, 169.75, 96.78], 'score': 0.5811617374420166, 'segmentation': []},
    {'image_id': 'frame_1', 'bbox': [805.19, 864.83, 94.10, 217.59, 8.65], 'score': 0.9955612421035767, 'segmentation': []},
    {'image_id': 'frame_1', 'bbox': [1089.32, 349.94, 122.09, 210.54, 38.59], 'score': 0.9918177127838135, 'segmentation': []}
]


for _, box in enumerate(boxes):
    x_camera, y_camera, w_camera, h_camera, angle = box['bbox']
    print(box['bbox'])
    print(x_camera,y_camera, w_camera, h_camera,angle)
    x_unity = x_camera * scale_factor_x
    y_unity = y_camera * scale_factor_y
    w_unity = w_camera * scale_factor_x
    h_unity = h_camera * scale_factor_y

    data = format_data(0,x_unity, y_unity, w_unity, h_unity, angle)
    send_data(data, host, port)
    time.sleep(1)  
