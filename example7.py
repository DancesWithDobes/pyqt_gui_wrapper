import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt


class VideoAnalyzerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer")
        self.setGeometry(100, 100, 400, 200)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Input section
        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)

        input_label = QLabel("Input:")
        input_layout.addWidget(input_label)

        self.url_radio = QRadioButton("YouTube URL")
        self.file_radio = QRadioButton("File Explorer")
        input_layout.addWidget(self.url_radio)
        input_layout.addWidget(self.file_radio)

        self.url_radio.setChecked(True)  # Default selection

        self.file_edit = QLineEdit()
        self.file_edit.setEnabled(False)
        input_layout.addWidget(self.file_edit)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)
        input_layout.addWidget(browse_button)

        # Extra options section
        extra_options_layout = QVBoxLayout()
        main_layout.addLayout(extra_options_layout)

        extra_options_label = QLabel("Extra Options:")
        extra_options_layout.addWidget(extra_options_label)

        self.option1_radio = QRadioButton("Option 1")
        self.option2_radio = QRadioButton("Option 2")
        extra_options_layout.addWidget(self.option1_radio)
        extra_options_layout.addWidget(self.option2_radio)

        # Analyze button
        analyze_button = QPushButton("Analyze")
        analyze_button.clicked.connect(self.analyze)
        main_layout.addWidget(analyze_button)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Video or Image File", "", "Video or Image Files (*.mp4 *.mkv *.avi *.jpg *.jpeg *.png)")
        self.file_edit.setText(file_path)

    def analyze(self):
        if self.url_radio.isChecked():
            input_type = "YouTube URL"
        else:
            input_type = "File Explorer"
            file_path = self.file_edit.text()

            if not file_path:
                QMessageBox.warning(self, "Error", "Please select a file.")
                return

            # Check if the selected file is a video or image
            valid_extensions = [".mp4", ".mkv", ".avi", ".jpg", ".jpeg", ".png"]
            if not any(file_path.lower().endswith(ext) for ext in valid_extensions):
                QMessageBox.warning(self, "Error", "Please select a valid video or image file.")
                return

        # Perform analysis with the selected input
        # Implement your analysis code here

        QMessageBox.information(self, "Analysis", f"Analysis complete!\nInput Type: {input_type}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoAnalyzerWindow()
    window.show()
    sys.exit(app.exec_())