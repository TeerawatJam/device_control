import sys
import serial

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QFrame
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QTimer

ser = serial.Serial('COM5', 9600, timeout=1)


class SensorDisPlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature & Humidity Monitor")
        self.setFixedSize(600, 600)
        self.setStyleSheet("background-color:#f0f4f8;")

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50)
        layout.setSpacing(30)

        self.title = QLabel("Sensor Data Monitor")
        self.title.setFont(QFont("Arial", 24, QFont.bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color:#333")

        self.data_frame = QFrame()
        self.data_frame.setStyleSheet("""
        QFrame{
                background-color:white;
                border-radius:20px;
                padding:30px;
                border:2px solid #ccc;
        }
        """)
        frame_layout = QVBoxLayout()

        self.temp_label = QLabel("Temperature :  --- C")
        self.temp_label.setFont(QFont("Arial", 20))
        self.temp_label.setAlignment(Qt.AlignCenter)

        self.hum_label = QLabel("Humidity : --- %")
        self.hum_label.setFont(QFont("Arial", 20))
        self.hum_label.setAlignment(Qt.AlignCenter)

        frame_layout.addWidget(self.temp_label)
        frame_layout.addWidget(self.hum_label)
        self.data_frame.setLayout(frame_layout)

        layout.addWidget(self.title)
        layout.addWidget(self.data_frame)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.read_serial)
        self.timer.start(2000)

    def read_serial(self):
        try:
            if ser.in_waiting:
                line = ser.readline().decode().strip()
                if "Temp:" in line and "Hum:" in line:
                    temp = line.split("Temp")[1].split(";")[0]
                    hum = line.split("Hum:")[1]
                    self.temp_label.setText(f"Temperature : {temp} c")
                    self.hum_label.setText(f"Humidity: {hum} %")
        except Exception as e:
            self.temp_label.setText("Eror Readind Data")
            self.hum_label.setText(str(e))


# การสร้าง GUI OUTPUT
if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = SensorDisPlay()
    window.show()
    sys.exit(app.exec_())