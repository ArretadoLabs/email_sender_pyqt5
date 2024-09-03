from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
import sys
from email_sender import send_email

class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("main.ui", self)
        
        self.emailButton.clicked.connect(self.send_email)
        
    def send_email(self):
        if self.lineEdit.text():
            send_email(destinatario=self.lineEdit.text(), email=self.textEdit.toPlainText())
        else:
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("Destinatario vazio")
            message.setWindowTitle("Erro!!")
            message.exec()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()    

