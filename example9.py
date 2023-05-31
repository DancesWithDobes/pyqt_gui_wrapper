import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QRadioButton, QFileDialog, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer")
        self.resize(400, 200)
        
        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create layout for central widget
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Create radio buttons for video input options
        self.file_radio_button = QRadioButton("File Explorer")
        self.file_radio_button.setChecked(True)
        self.file_radio_button.toggled.connect(self.toggle_file_input)
        
        self.youtube_radio_button = QRadioButton("YouTube URL")
        self.youtube_radio_button.toggled.connect(self.toggle_youtube_input)
        
        self.layout.addWidget(self.file_radio_button)
        self.layout.addWidget(self.youtube_radio_button)
        
        # Create file path input
        self.file_input = QLineEdit()
        self.layout.addWidget(self.file_input)
        
        # Create analyze button
        self.analyze_button = QPushButton("Analyze")
        self.analyze_button.clicked.connect(self.analyze)
        self.layout.addWidget(self.analyze_button)
        
    def toggle_file_input(self, checked):
        if checked:
            self.file_input.setEnabled(True)
            self.file_input.clear()
        else:
            self.file_input.setEnabled(False)
            self.file_input.clear()
            
    def toggle_youtube_input(self, checked):
        if checked:
            self.file_input.setEnabled(True)
            self.file_input.clear()
            self.file_input.setPlaceholderText("Enter YouTube URL")
        else:
            self.file_input.setEnabled(False)
            self.file_input.clear()
            
    def analyze(self):
        input_file = self.file_input.text()
        if self.youtube_radio_button.isChecked():
            if not input_file.startswith("https://www.youtube.com/"):
                QMessageBox.warning(self, "Invalid URL", "Please enter a valid YouTube URL.")
                return
        elif self.file_radio_button.isChecked():
            if not input_file.endswith((".mp4", ".avi", ".mkv", ".jpeg", ".jpg", ".png")):
                QMessageBox.warning(self, "Invalid File", "Please select a valid video or image file.")
                return
        
        # Perform analysis on the input file
        # TODO: Add your analysis code here
        
        QMessageBox.information(self, "Analysis Complete", "Analysis finished successfully!")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())