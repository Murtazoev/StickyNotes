from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Sticky Notes")
        self.resize(300 , 300)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)
        self.content_widget = QWidget(self)
        self.content_widget.setStyleSheet("""
            background-color: rgba(255, 255, 0, 150);  # Yellow with some transparency
            border: 5px solid rgba(255, 255, 0, 255);   # Yellow border with full opacity
            border-radius: 10px;                        # Rounded corners
        """)
        
        self.text_edit = QTextEdit(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
    
    def EscKeyPressed(self , event):
        if event.key() == Qt.Key_Escape:
            print("Closing the window beatch")
            self.close()

if (__name__ == '__main__'):
    windows = QApplication()
    sticky_notes_app = Window()
    sticky_notes_app.show()
    sys.exit(windows.exec())