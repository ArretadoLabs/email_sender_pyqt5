from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi
import sys

class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("main.ui", self)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()    

