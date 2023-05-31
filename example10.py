import sys
import os
import urllib.parse
import pafy
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLineEdit, QPushButton, QFileDialog, QMessageBox


class VideoAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.input_file = ''
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Video Analyzer')

        vbox = QVBoxLayout()

        # Radio buttons for input selection
        self.radio_file = QRadioButton('File Explorer')
        self.radio_file.setChecked(True)
        self.radio_file.toggled.connect(self.on_radio_toggled)
        vbox.addWidget(self.radio_file)

        self.radio_youtube = QRadioButton('YouTube URL')
        self.radio_youtube.toggled.connect(self.on_radio_toggled)
        vbox.addWidget(self.radio_youtube)

        # Input text box for YouTube URL
        self.youtube_textbox = QLineEdit()
        vbox.addWidget(self.youtube_textbox)

        # Analyze button
        analyze_button = QPushButton('Analyze')
        analyze_button.clicked.connect(self.analyze)
        vbox.addWidget(analyze_button)

        self.setLayout(vbox)

    def on_radio_toggled(self):
        if self.radio_file.isChecked():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_dialog = QFileDialog()
            file_dialog.setWindowTitle('Select Video or Image File')
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter('Video files (*.mp4 *.avi *.mkv);;Image files (*.png *.jpg *.jpeg)')
            if file_dialog.exec_():
                selected_files = file_dialog.selectedFiles()
                self.input_file = selected_files[0]
        else:
            self.input_file = ''

    def analyze(self):
        if self.radio_youtube.isChecked():
            youtube_url = self.youtube_textbox.text()
            if not self.is_valid_youtube_url(youtube_url):
                QMessageBox.warning(self, 'Invalid YouTube URL', 'Please enter a valid YouTube URL.')
                return
            video = pafy.new(youtube_url)
            best = video.getbest()
            self.input_file = best.url

        print('Input File:', self.input_file)  # You can modify this line to save the input_file path to a variable or perform further analysis

    @staticmethod
    def is_valid_youtube_url(url):
        parsed_url = urllib.parse.urlparse(url)
        return parsed_url.netloc == 'www.youtube.com' and parsed_url.path == '/watch'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoAnalyzer()
    window.show()
    sys.exit(app.exec_())