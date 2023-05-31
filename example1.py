import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, QMessageBox


class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")
        self.setGeometry(200, 200, 300, 200)
        
        self.input_label = QLabel("Video File:")
        self.input_field = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_clicked)
        
        self.radio_label1 = QLabel("Set 1:")
        self.radio_button1_1 = QRadioButton("Option 1")
        self.radio_button1_2 = QRadioButton("Option 2")
        
        self.radio_label2 = QLabel("Set 2:")
        self.radio_button2_1 = QRadioButton("Option 1")
        self.radio_button2_2 = QRadioButton("Option 2")
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.radio_label1)
        self.layout.addWidget(self.radio_button1_1)
        self.layout.addWidget(self.radio_button1_2)
        self.layout.addWidget(self.radio_label2)
        self.layout.addWidget(self.radio_button2_1)
        self.layout.addWidget(self.radio_button2_2)
        
        self.setLayout(self.layout)
    
    def submit_clicked(self):
        video_file = self.input_field.text()
        
        if video_file:
            message = f"Video file selected: {video_file}"
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.warning(self, "Error", "Please enter a video file path.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    sys.exit(app.exec_())