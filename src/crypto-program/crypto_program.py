from Crypto.Hash import MD5
import os
import sys
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

AES = 0
DES3 = 1

qtCreatorFile = "main_ui.ui" # Enter file here. 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.encryptButton.clicked.connect(lambda: self.showdialog("Some text"))
        enc_origin_file_path =  self.enc_address_origin_button.clicked.connect(self.getFileName)

    def showdialog(self,message):
        dialog = QDialog()
        button = QPushButton("OK",dialog)
        text = QLabel(message)
        text.setAlignment(Qt.AlignCenter)
        
        vbox = QVBoxLayout()
        vbox.addWidget(text)
        vbox.addStretch()
        vbox.addWidget(button)

        dialog.setLayout(vbox)
        dialog.setMaximumSize(250,150)
        dialog.setMinimumSize(250,150)
        dialog.setWindowTitle("Notification")
        dialog.setWindowModality(2)

        dialog.exec_()

    def getFileName(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)

        filenames = QStringListModel()
        if dialog.exec():
            filenames = dialog.selectedFiles()
        
        return filenames

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())