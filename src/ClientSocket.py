import socket
import time

class ClientSocket:

    def __init__(self, host, port, scale_factor_x, scale_factor_y):
        self.host = host
        self.port = port
        self.scale_factor_x = scale_factor_x
        self.scale_factor_y = scale_factor_y

    def send_data(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.host, self.port))
            sock.sendall(data.encode("utf-8"))
            print(f"Sent: {data}")
        finally:
            sock.close()

    def format_data(self, index, x, y, w, h, a):
        return f"{index};{x:.2f},{y:.2f},{w:.2f},{h:.2f};{a:.2f}"

    def start(self, boxes):
        for i, box in enumerate(boxes):
            x_camera, y_camera, w_camera, h_camera, angle = box['bbox']
            #print(box['bbox'])
            #print(x_camera, y_camera, w_camera, h_camera, angle)
            x_unity = x_camera * self.scale_factor_x
            y_unity = y_camera * self.scale_factor_y
            w_unity = w_camera * self.scale_factor_x
            h_unity = h_camera * self.scale_factor_y

            data = self.format_data(i, x_unity, y_unity, w_unity, h_unity, angle)
            self.send_data(data)
            time.sleep(1)