from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
import cv2
from vidgear.gears import NetGear

class CameraThread(QThread):
    frame_updated = pyqtSignal(QImage)

    def __init__(self, parent=None):
        super(CameraThread, self).__init__(parent)
        self.client = NetGear(
            address="192.168.1.197",
            port="5555",
            protocol="tcp",
            pattern=2,
            receive_mode=True,
            logging=True,
        )

    def run(self):
        while True:
            frame = self.client.recv()
            if frame is not None:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                q_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
                self.frame_updated.emit(q_image)

class Camera(QMainWindow):
    def __init__(self, camera, fps):
        super(Camera, self).__init__()
        self.camera_label = camera
        # self.setCentralWidget(self.camera_label)
        self.camera_thread = CameraThread()
        self.camera_thread.frame_updated.connect(self.update_frame)
        self.camera_thread.start()

    def update_frame(self, frame):
        pixmap = QPixmap.fromImage(frame)
        self.camera_label.setPixmap(pixmap)
