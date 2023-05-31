import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel, QFileDialog, QLineEdit, QMessageBox


class VideoAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Analyzer")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.file_radio = QRadioButton("File Explorer")
        self.file_radio.setChecked(True)
        self.file_radio.toggled.connect(self.on_radio_toggled)
        layout.addWidget(self.file_radio)

        self.url_radio = QRadioButton("YouTube URL")
        self.url_radio.toggled.connect(self.on_radio_toggled)
        layout.addWidget(self.url_radio)

        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        self.analyze_button = QPushButton("Analyze")
        self.analyze_button.clicked.connect(self.analyze_video)
        layout.addWidget(self.analyze_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

    def on_radio_toggled(self):
        if self.file_radio.isChecked():
            self.input_line.clear()
            self.input_line.setPlaceholderText("Enter file path...")
        else:
            self.input_line.clear()
            self.input_line.setPlaceholderText("Enter YouTube URL...")

    def analyze_video(self):
        if self.file_radio.isChecked():
            file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File")
            if file_path:
                self.result_label.setText(f"File path: {file_path}")
        else:
            url = self.input_line.text()
            if url:
                self.result_label.setText(f"YouTube URL: {url}")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    analyzer = VideoAnalyzer()
    analyzer.show()
    sys.exit(app.exec_())