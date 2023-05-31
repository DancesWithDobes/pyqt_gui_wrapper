import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Analyzer")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        # Input section
        self.radio_youtube = QRadioButton("YouTube URL")
        self.radio_youtube.setChecked(True)
        self.radio_youtube.toggled.connect(self.toggle_youtube)

        self.radio_file = QRadioButton("File Explorer")
        self.radio_file.toggled.connect(self.toggle_file)

        self.url_input = QLineEdit()
        self.url_input.setEnabled(True)

        self.browse_button = QPushButton("Browse")
        self.browse_button.setEnabled(False)
        self.browse_button.clicked.connect(self.browse_file)

        layout.addWidget(self.radio_youtube)
        layout.addWidget(self.radio_file)
        layout.addWidget(self.url_input)
        layout.addWidget(self.browse_button)

        # Analysis section
        self.radio_set1 = (QRadioButton("Option 1"), QRadioButton("Option 2"))
        self.radio_set2 = (QRadioButton("Option 3"), QRadioButton("Option 4"))

        layout.addWidget(self.radio_set1[0])
        layout.addWidget(self.radio_set1[1])
        layout.addWidget(self.radio_set2[0])
        layout.addWidget(self.radio_set2[1])

        # Analyze button
        analyze_button = QPushButton("Analyze")
        analyze_button.clicked.connect(self.analyze)
        layout.addWidget(analyze_button)

        self.input_file = ""

    def toggle_youtube(self, checked):
        self.url_input.setEnabled(checked)

    def toggle_file(self, checked):
        self.browse_button.setEnabled(checked)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if len(selected_files) > 0:
                self.input_file = selected_files[0]
                if not self.is_valid_file(self.input_file):
                    self.show_error_dialog("Invalid File", "The selected file is not a valid video or image file.")
                    self.input_file = ""

    def is_valid_file(self, file_path):
        valid_extensions = (".mp4", ".avi", ".mkv", ".jpg", ".jpeg", ".png")
        return file_path.lower().endswith(valid_extensions)

    def analyze(self):
        if self.radio_youtube.isChecked():
            url = self.url_input.text()
            if not self.is_valid_youtube_url(url):
                self.show_error_dialog("Invalid URL", "The entered URL is not a valid YouTube URL.")
                return
            self.input_file = url
        elif not self.input_file:
            self.show_error_dialog("No File", "Please select a video or image file.")
            return

        # Perform analysis with the input_file
        print("Analysis started with:", self.input_file)

    def is_valid_youtube_url(self, url):
        # Add your validation logic for YouTube URLs here
        # This is just a simple check for demonstration purposes
        return "youtube.com" in url

    def show_error_dialog(self, title, message):
        error_dialog = QMessageBox()
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
