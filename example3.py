import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QLineEdit, QFileDialog


class VideoAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer")
        self.setGeometry(100, 100, 400, 200)

        self.input_label = QLabel("Video Input:")
        self.input_radio_youtube = QRadioButton("YouTube URL")
        self.input_radio_file = QRadioButton("File Explorer")
        self.input_text = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.analyze_button = QPushButton("Analyze")

        self.radio_button_group = []
        self.radio_button_group.append(self.input_radio_youtube)
        self.radio_button_group.append(self.input_radio_file)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_radio_youtube)
        input_layout.addWidget(self.input_radio_file)

        layout.addLayout(input_layout)
        layout.addWidget(self.input_text)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.analyze_button)

        self.setLayout(layout)

        # Connect signals
        self.input_radio_youtube.toggled.connect(self.toggle_youtube_input)
        self.browse_button.clicked.connect(self.browse_file)
        self.analyze_button.clicked.connect(self.analyze)

    def toggle_youtube_input(self):
        if self.input_radio_youtube.isChecked():
            self.input_text.setPlaceholderText("Enter YouTube URL")
            self.browse_button.setEnabled(False)
        else:
            self.input_text.setPlaceholderText("Select a video file")
            self.browse_button.setEnabled(True)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select a video file", "", "Video Files (*.mp4 *.avi *.mkv)")
        self.input_text.setText(file_path)

    def analyze(self):
        video_input = self.input_text.text()
        if self.input_radio_youtube.isChecked():
            # Analyze YouTube URL
            print("Analyzing YouTube URL:", video_input)
        else:
            # Analyze video file
            print("Analyzing video file:", video_input)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoAnalyzer()
    window.show()
    sys.exit(app.exec_())