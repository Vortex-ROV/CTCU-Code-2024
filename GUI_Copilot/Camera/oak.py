# import required libraries
from vidgear.gears import NetGear
from PyQt5.QtCore import QThread
class FrameReceiver(QThread):
    def __init__(self):
        super().__init__()
        self.frame = None
        self.client = NetGear(
            address="192.168.1.197",
            port = 5656,
            protocol = "tcp",
            pattern = 2,
            receive_mode = True,
            logging = True
        )
        # self.run()
    def run(self):
        # receive data from server
        self.frame = self.client.recv()
        return self.frame
    

oak = FrameReceiver()