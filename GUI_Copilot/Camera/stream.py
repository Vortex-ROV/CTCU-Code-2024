from PyQt5.QtCore import QThread
import time
import cv2

class Stream(QThread):
    def __init__(self, fps_label, stream_id=0):
        super().__init__()
        self.stream_id = stream_id
        self.vcap = cv2.VideoCapture(0)
        if not self.vcap.isOpened():
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.vcap.get(5))
        print("FPS of input stream: {}".format(fps_input_stream))
        self.grabbed, self.frame = self.vcap.read()
        if not self.grabbed:
            print('[Exiting] No more frames to read')
            exit(0)
        self.stopped = True
        self.fps = 0
        self.fps_label = fps_label

    def start(self):
        self.stopped = False
        super().start()

    def run(self):
        start_time = time.time()
        while True:
            if self.stopped:
                break
            grabbed, frame = self.vcap.read()
            self.grabbed, self.frame = grabbed, frame
            if not grabbed:
                print('[Exiting] No more frames to read')
                self.stopped = True
                break
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time != 0:
                self.fps = 1 / elapsed_time
                self.fps = round(self.fps)
                # self.fps_label.setText(f"  - {self.fps}FPS")
                # print(self.fps)
            start_time = time.time()
        self.vcap.release()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
        self.wait()
