import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QFileDialog, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer")
        self.setGeometry(100, 100, 300, 200)

        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # File explorer button
        self.file_button = QPushButton("Select Video File")
        self.file_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.file_button)

        # Radio buttons
        self.radio_button1 = QRadioButton("Option 1")
        self.radio_button2 = QRadioButton("Option 2")
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)

        # Analyze button
        self.analyze_button = QPushButton("Analyze")
        self.analyze_button.clicked.connect(self.analyze_video)
        layout.addWidget(self.analyze_button)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                print("Selected file:", file_path)  # Replace with your logic for the selected file

    def analyze_video(self):
        # Replace with your logic for analyzing the video
        print("Analyzing video...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())