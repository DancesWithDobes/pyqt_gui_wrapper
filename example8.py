import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QFileDialog, QMessageBox

class VideoAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer")
        
        self.input_file = None
        
        self.url_textbox = QLineEdit()
        self.url_textbox.setPlaceholderText("Enter YouTube URL")
        
        self.file_radio = QRadioButton("File Explorer")
        self.url_radio = QRadioButton("YouTube URL")
        
        self.file_radio.setChecked(True)
        self.file_radio.toggled.connect(self.file_radio_selected)
        self.url_radio.toggled.connect(self.url_radio_selected)
        
        self.analyze_button = QPushButton("Analyze")
        self.analyze_button.clicked.connect(self.analyze)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select Video Source:"))
        layout.addWidget(self.file_radio)
        layout.addWidget(self.url_radio)
        layout.addWidget(self.url_textbox)
        layout.addWidget(self.analyze_button)
        
        self.setLayout(layout)
    
    def file_radio_selected(self, checked):
        if checked:
            self.url_textbox.setEnabled(False)
            self.analyze_button.setEnabled(True)
    
    def url_radio_selected(self, checked):
        if checked:
            self.url_textbox.setEnabled(True)
            self.analyze_button.setEnabled(True)
    
    def analyze(self):
        if self.file_radio.isChecked():
            self.input_file, _ = QFileDialog.getOpenFileName(self, "Select Video or Image File", "", "Video Files (*.mp4 *.avi);;Image Files (*.jpg *.png)")
            if not self.input_file:
                QMessageBox.warning(self, "Error", "Please select a valid video or image file.")
                return
        else:
            url = self.url_textbox.text()
            if not url:
                QMessageBox.warning(self, "Error", "Please enter a YouTube URL.")
                return
            self.input_file = url
        
        # Perform analysis on self.input_file
        print(f"Input file: {self.input_file}")
        
        # Reset input file variable for future use
        self.input_file = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoAnalyzer()
    window.show()
    sys.exit(app.exec_())