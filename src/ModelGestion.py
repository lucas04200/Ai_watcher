import cv2
from src.KeypointsDrawing import *
class ModelGestion:
    def __init__(self, kd):
        self.cap = cv2.VideoCapture(0)
        self.kd = kd

    def loop_through_people(self, frame, keypoints_with_scores, confidence_threshold):
        for person in keypoints_with_scores:
            self.kd.draw_connections(frame, person, confidence_threshold)
            self.kd.draw_keypoints(frame, person, confidence_threshold)