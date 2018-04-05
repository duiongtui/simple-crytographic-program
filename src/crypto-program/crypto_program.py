import os
import sys
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import algorithms_rsa as rsa
import file.file_handle as file_handle

AES = 0
DES3 = 1

qtCreatorFile = "main_ui.ui" # Enter file here. 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #ENCRYPT TAB
        self.enc_address_origin_button.clicked.connect(lambda: self.getFileNametoTextBox(self.enc_address_origin_text))
        self.enc_address_key_button.clicked.connect(lambda: self.getFileNametoTextBox(self.enc_address_key_text))
        self.enc_address_save_button.clicked.connect(lambda: self.getFileNametoTextBox(self.enc_address_save_text,True))
        self.encryptButton.clicked.connect(self.encryptFile)
        self.enc_gen_key_button.clicked.connect(self.generateRSAKey)

        #DECRYPT TAB
        self.dec_address_enc_button.clicked.connect(lambda: self.getFileNametoTextBox(self.dec_address_enc_text))
        self.dec_address_key_button.clicked.connect(lambda: self.getFileNametoTextBox(self.dec_address_key_text))
        self.dec_address_save_button.clicked.connect(lambda: self.getFileNametoTextBox(self.dec_address_save_text,True))
        self.decryptButton.clicked.connect(self.decryptFile)


    def decryptFile(self):
        #Kiem tra thong tin duong dan da duoc dien day du
        if self.dec_address_enc_text.text() and self.dec_address_key_text.text() and \
            self.dec_address_save_text.text():

            #Kiem tra 1 trong so cac radio option duoc chon
            #
            if self.dec_radio_des.isChecked() or self.dec_radio_aes.isChecked() or self.dec_radio_rsa.isChecked():
                if self.dec_radio_des.isChecked():
                    success = file_handle.decrypt_file(self.dec_address_enc_text.text(),self.dec_address_save_text.text(),self.dec_address_key_text.text(),DES3)
                elif self.dec_radio_aes.isChecked():
                    success = file_handle.decrypt_file(self.dec_address_enc_text.text(),self.dec_address_save_text.text(),self.dec_address_key_text.text(),AES)
                else:

                    success = file_handle.decrypt_file_rsa(self.dec_address_enc_text.text(),self.dec_address_key_text.text(),self.dec_address_save_text.text())
                
                if success:
                    self.showdialog("Decrypt file success, hash value is correct. This is origin file")
                else:
                    self.showdialog("Decrypt file success, hash value is incorrect. This is not origin file")
            else:
                self.showdialog("No algorithms is chosen")
        else:
            self.showdialog("Missing some file/folder path")

    def encryptFile(self):
        #Kiem tra thong tin duong dan da duoc dien day du
        if self.enc_address_origin_text.text() and self.enc_address_key_text.text() and \
            self.enc_address_save_text.text():

            #Kiem tra 1 trong so cac radio option duoc chon
            #
            if self.enc_radio_des.isChecked() or self.enc_radio_aes.isChecked() or self.enc_radio_rsa.isChecked():
                if self.enc_radio_des.isChecked():
                    file_handle.encrypt_file(self.enc_address_origin_text.text(),self.enc_address_save_text.text(),self.enc_address_key_text.text(),DES3)
                    toBigFile = False
                elif self.enc_radio_aes.isChecked():
                    file_handle.encrypt_file(self.enc_address_origin_text.text(),self.enc_address_save_text.text(),self.enc_address_key_text.text(),AES)
                    toBigFile = False
                else:
                    try:
                        file_handle.encrypt_file_rsa(self.enc_address_origin_text.text(),self.enc_address_key_text.text(),self.enc_address_save_text.text())
                    except ValueError:
                        toBigFile = True
                if toBigFile:
                    self.showdialog("RSA Algorithms: This size of currnet file is to big")
                else:
                    self.showdialog("Encrypt file success")

            else:
                self.showdialog("No algorithms is chosen")
        else:
            self.showdialog("Missing some file/folder path")

    def generateRSAKey(self):
        str = self.getFolderName()
        rsa.generate_key(str)
        self.showdialog("Key have been save at ..." + str)

    def showdialog(self,message):
        dialog = QDialog()
        button = QPushButton("OK")
        text = QLabel(message)
        text.setAlignment(Qt.AlignCenter)
        text.setWordWrap(True)

        vbox = QVBoxLayout()
        vbox.addWidget(text)
        vbox.addStretch()
        vbox.addWidget(button)

        dialog.setLayout(vbox)
        dialog.setMaximumSize(250,150)
        dialog.setMinimumSize(250,150)
        dialog.setWindowTitle("Notification")
        dialog.setWindowModality(2)

        button.clicked.connect(dialog.reject)

        dialog.exec_()

    def getFileNametoTextBox(self,textBox,isFolder = False):
        dialog = QFileDialog()
        if isFolder:
            dialog.setFileMode(QFileDialog.Directory)
        else:
            dialog.setFileMode(QFileDialog.AnyFile)
        
        filenames = []
        if dialog.exec():
            filenames = dialog.selectedFiles()
        if (filenames):
            textBox.setText(filenames[0])
   
    def getFolderName(self):
        return str(QFileDialog.getExistingDirectory(self, "Select Directory"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())