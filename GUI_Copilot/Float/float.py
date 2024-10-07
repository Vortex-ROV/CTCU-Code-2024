from  PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import csv
import pandas as pd
from .plot import plotting
from serial import Serial
from PyQt5.QtCore import QTimer,QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Float(QMainWindow):
    def __init__(self, float_table, display_float):
        super(Float, self).__init__()

        self.profile_num = 0
        self.float_table = float_table
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
        url = QUrl.fromLocalFile("Float/mixkit-arcade-magic-notification-2342.wav")  # Change "sound_file.mp3" to your sound file path
        content = QMediaContent(url)
        self.mediaPlayer.setMedia(content)
        self.display_float = display_float
        self.display_float.clicked.connect(self.plot_data)

        # self.mediaPlayer.play()
        QTimer.singleShot(2000, self.mediaPlayer.stop)
        # print(type(serial))
        self.arduino = Serial(port='COM5', baudrate=9600, timeout=.1)

        self.headers = ['Company No.', 'Time', 'Pressure', 'Depth (m)']

        self.data = []
        self.allData = []
        self.index = 0
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start()

        rows = len(self.data)
        columns = len(self.headers)

        self.float_table.setRowCount(rows)
        self.float_table.setColumnCount(columns)
        self.float_table.setHorizontalHeaderLabels(self.headers)

        self.float_table.setColumnWidth(0, 90)
        self.float_table.setColumnWidth(1, 65)
        self.float_table.setColumnWidth(2, 65)
        self.float_table.setColumnWidth(3, 75)

        self.profiles = []


    def read_data(self):
        response = []
        response = self.return_data()
        if response:
            # print(f"Response list:    {response}")
            # print(type(response))
            # if response[3]:
            #     print(f"Response 3: {response[3]}")
                # response[3] = int(response[3]) / 10.0
                # response[3] = str(response[3]) + "KPa"
                # if response[4]:
                #     response[4] = response[4] + "m"
            
            self.profile = response[-1]
            self.profiles.append(self.profile)
            if len(self.profiles) > 1:
                if not self.profiles[-1]  == self.profiles[-2]:
                    # self.plot_data()
                    # self.profile_num +=1
                    # plot(frame_self.profile_num - 1)
                    # print("calling read data function")
                    # self.erase_csv_file()
                    self.mediaPlayer.play()
                    QTimer.singleShot(2000, self.mediaPlayer.stop)
        if response[ : -1]:
            if len(response[ : -1]) == len(self.headers):
                row = self.float_table.rowCount()
                self.float_table.insertRow(row)
                for i, data in enumerate(response[ : -1]):
                    item = QTableWidgetItem(data)
                    self.float_table.setItem(row, i, item)
                self.save_data()

    def erase_csv_file(self):
        print("erase function called")
        #self.clear_table()
        f = open(f"float_{self.profile}.csv", "w+")
        f.close()
    
    def clear_table(self):
        print("clear function called")
        self.float_table.clearContents()  
        self.float_table.setRowCount(0)

    def save_data(self):
        with open(f"float_{self.profile}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)
            for row in range(self.float_table.rowCount()):
                row_data = []
                for column in range(self.float_table.columnCount()):
                    item = self.float_table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                writer.writerow(row_data)

    def load_data(self):
        self.data = pd.read_csv(f"float_{self.profile}.csv")
        if(self.index == 0):
            self.index = len(self.data)
            # print('Condition 1 : ', self.index)
        else:
            self.data = self.data.iloc[self.index:,:]
            self.index += len(self.data)
            # print('Condition 2 : ',self.index)

    def return_data(self):
        if self.arduino is not None:
            # print(self.arduino)
            try:
                response = self.arduino.readline().decode().strip()
                if response:
                    if response[0:2].isalpha() or response[0:2].isnumeric():
                        # print(f"Response string:    {response}")
                        return response.split()
            except UnicodeDecodeError:
                print("UnicodeDecodeError: Unable to decode data.")
                raw_data = self.arduino.readline()
                print("Raw data received:", raw_data)
        return []

        
    def plot_data(self):
        try:
            # self.save_data()
            self.load_data()
            rows = self.data.shape[0]
            session = 1
            # if not session == 
            if self.data.shape[1] == 4:
                time = self.data.iloc[:, 1].values
                #time = self.data.iloc[0:, 1].values

                #time = np.array([i for i in range(7)])

                # hrs,mins,sec = time.split(":")
                depth = (self.data.iloc[:, 3].values) 
                print(depth, time)
                self.graph = plotting(depth, time, rows)
        except Exception as e:
            print("Failed to Plot Data:", e)