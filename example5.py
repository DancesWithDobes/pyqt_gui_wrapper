import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QFileDialog


class VideoAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Video input section
        input_label = QLabel("Video Input:")
        layout.addWidget(input_label)

        self.youtube_radio = QRadioButton("YouTube URL")
        self.youtube_radio.setChecked(True)
        layout.addWidget(self.youtube_radio)

        self.file_radio = QRadioButton("File Explorer")
        layout.addWidget(self.file_radio)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.openFileDialog)
        layout.addWidget(browse_button)

        # Additional options section
        options_label = QLabel("Additional Options:")
        layout.addWidget(options_label)

        option1_radio = QRadioButton("Option 1")
        layout.addWidget(option1_radio)

        option2_radio = QRadioButton("Option 2")
        layout.addWidget(option2_radio)

        # Analyze button
        analyze_button = QPushButton("Analyze")
        analyze_button.clicked.connect(self.analyze)
        layout.addWidget(analyze_button)

        self.setLayout(layout)

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov)", options=options)
        if file_name:
            self.url_input.setText(file_name)

    def analyze(self):
        video_input = self.url_input.text()

        if self.youtube_radio.isChecked():
            # Handle YouTube URL input
            print("Analyzing video from YouTube URL:", video_input)
        else:
            # Handle file explorer input
            print("Analyzing video from file:", video_input)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    analyzer = VideoAnalyzer()
    analyzer.show()