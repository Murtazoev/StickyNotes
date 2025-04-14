import sys
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QSystemTrayIcon, QPushButton, QMenu, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon

active_windows = {}
windows = QApplication()

class Window(QWidget):
    def __init__(self , note = None):
        super().__init__()
        self.setWindowTitle("My Sticky Notes")
        self.resize(300 , 300)
        self.setWindowFlags( self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowOpacity(0.9)
        self.setStyleSheet(
            "background: #FFFF99; color: #62622f; border: 0; font-size: 16pt;"
        )

        layout = QVBoxLayout()

        buttons = QHBoxLayout()
        self.close_btn = QPushButton("×")
        self.close_btn.setStyleSheet(
            "font-weight: bold; font-size: 25px; width: 25px; height: 25px;"
        )
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        buttons.addStretch()
        buttons.addWidget(self.close_btn)
        layout.addLayout(buttons)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        active_windows[id(self)] = self
    
    def EscKeyPressed(self , event):
        if event.key() == Qt.Key_Escape:
            print("Closing the window beatch")
            self.close()

    def mousePressEvent(self, e):
        self.previous_pos = e.globalPosition()

    def mouseMoveEvent(self, e):
        delta = e.globalPosition() - self.previous_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previous_pos = e.globalPosition()

def create_note(note=None):
    note = Window(note)
    note.show()

icon = QIcon('sticky-note.png')

windows.setQuitOnLastWindowClosed(False)

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

def handle_tray_click(reason):
    if (QSystemTrayIcon.ActivationReason(reason) == QSystemTrayIcon.ActivationReason.Trigger ):
        create_note()

tray.activated.connect(handle_tray_click)

menu = QMenu()
add_action = QAction("Add Note")
add_action.triggered.connect(create_note)
menu.addAction(add_action)

quit_action = QAction('Quit')
quit_action.triggered.connect(windows.quit)
menu.addAction(quit_action)

tray.setContextMenu(menu)

windows.exec()