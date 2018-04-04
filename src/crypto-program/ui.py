# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ENDEPrograms.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def EncryptCheck(self):
        print ("Button encrypt have been clicked! ")

    def DecryptCheck(self):        
        print ("Button decrypt have been clicked! ")

    def HashCheck(self):
        print ("Button Hash have been clicked! ")  

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')
        self.editor()
        with file:
            text = file.read()
            self.textEdit.setText(text)
    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)     
   

    
    #########################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(579, 435)       
     
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 471))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.encrypt = QtGui.QWidget()
        self.encrypt.setObjectName(_fromUtf8("encrypt"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.encrypt)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 551, 111))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radiobuttonDES = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.radiobuttonDES.setObjectName(_fromUtf8("radiobuttonDES"))
        self.verticalLayout_4.addWidget(self.radiobuttonDES)
        self.radiobuttonAES = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.radiobuttonAES.setObjectName(_fromUtf8("radiobuttonAES"))
        self.verticalLayout_4.addWidget(self.radiobuttonAES)
        self.radiobuttonRSA = QtGui.QRadioButton(self.verticalLayoutWidget_4)
        self.radiobuttonRSA.setObjectName(_fromUtf8("radiobuttonRSA"))
        self.verticalLayout_4.addWidget(self.radiobuttonRSA)
        self.labelfile1 = QtGui.QLabel(self.encrypt)
        self.labelfile1.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.labelfile1.setObjectName(_fromUtf8("labelfile1"))
        self.file_encrypt = QtGui.QComboBox(self.encrypt)
        self.file_encrypt.setGeometry(QtCore.QRect(100, 170, 441, 22))
        self.file_encrypt.setObjectName(_fromUtf8("file_encrypt"))
        self.labelkey1 = QtGui.QLabel(self.encrypt)
        self.labelkey1.setGeometry(QtCore.QRect(10, 230, 71, 21))
        self.labelkey1.setObjectName(_fromUtf8("labelkey1"))
        self.key_encrypt = QtGui.QComboBox(self.encrypt)
        self.key_encrypt.setGeometry(QtCore.QRect(100, 230, 441, 22))
        self.key_encrypt.setObjectName(_fromUtf8("key_encrypt"))
        self.Encryptbutton = QtGui.QPushButton(self.encrypt)
        self.Encryptbutton.setGeometry(QtCore.QRect(350, 300, 151, 41))
        self.Encryptbutton.setObjectName(_fromUtf8("Encryptbutton"))
        ########## encrypt button action#############
        self.Encryptbutton.clicked.connect(self.EncryptCheck)
        #############################################
        self.tabWidget.addTab(self.encrypt, _fromUtf8(""))
        self.decrypt = QtGui.QWidget()       
        self.decrypt.setObjectName(_fromUtf8("decrypt"))            
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.decrypt)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 551, 111))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radiobuttonDES_2 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radiobuttonDES_2.setObjectName(_fromUtf8("radiobuttonDES_2"))
        self.verticalLayout_2.addWidget(self.radiobuttonDES_2)
        self.radiobuttonAES_2 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radiobuttonAES_2.setObjectName(_fromUtf8("radiobuttonAES_2"))
        self.verticalLayout_2.addWidget(self.radiobuttonAES_2)
        self.radiobuttonRSA_2 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radiobuttonRSA_2.setObjectName(_fromUtf8("radiobuttonRSA_2"))
        self.verticalLayout_2.addWidget(self.radiobuttonRSA_2)
        self.labelfile2 = QtGui.QLabel(self.decrypt)
        self.labelfile2.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.labelfile2.setObjectName(_fromUtf8("labelfile2"))
        self.labelkey2 = QtGui.QLabel(self.decrypt)
        self.labelkey2.setGeometry(QtCore.QRect(10, 230, 71, 21))
        self.labelkey2.setObjectName(_fromUtf8("labelkey2"))
        self.file_decrypt = QtGui.QComboBox(self.decrypt)
        self.file_decrypt.setGeometry(QtCore.QRect(100, 170, 441, 22))
        self.file_decrypt.setObjectName(_fromUtf8("file_decrypt"))
        self.key_decrypt = QtGui.QComboBox(self.decrypt)
        self.key_decrypt.setGeometry(QtCore.QRect(100, 230, 441, 22))
        self.key_decrypt.setObjectName(_fromUtf8("key_decrypt"))
        self.Decryptbutton = QtGui.QPushButton(self.decrypt)
        self.Decryptbutton.setGeometry(QtCore.QRect(360, 290, 151, 41))
        ################### decryp button action###########
        self.Decryptbutton.setObjectName(_fromUtf8("Decryptbutton"))
        self.Decryptbutton.clicked.connect(self.DecryptCheck)
        ##################################################
        self.tabWidget.addTab(self.decrypt, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 551, 81))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioButton_7 = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_3.addWidget(self.radioButton_8)

        self.labelHash = QtGui.QLabel(self.tab)
        self.labelHash.setGeometry(QtCore.QRect(10, 130, 61, 20))
        self.labelHash.setObjectName(_fromUtf8("labelHash"))

        self.listViewhash = QtGui.QListView(self.tab)
        self.listViewhash.setGeometry(QtCore.QRect(30, 170, 511, 121))
        self.listViewhash.setObjectName(_fromUtf8("listViewhash"))

        self.buttonhash = QtGui.QPushButton(self.tab)
        self.buttonhash.setGeometry(QtCore.QRect(430, 310, 91, 41))
        self.buttonhash.setObjectName(_fromUtf8("buttonhash"))
        ############## action button hash###################
        self.buttonhash.clicked.connect(self.HashCheck)
        #######################################################
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuImport = QtGui.QMenu(self.menuFile)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuEdits"))

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuite = QtGui.QAction(MainWindow)
        self.actionQuite.setObjectName(_fromUtf8("actionQuite"))
        self.actionFile = QtGui.QAction(MainWindow)
        #######################action import file##################
        self.actionFile.setObjectName(_fromUtf8("actionFile")) 
        self.actionFile.triggered.connect(self.file_open)          
        ###########################################################
        self.actionKey_EN_DE = QtGui.QAction(MainWindow)
        ######################## action import key ################
        self.actionKey_EN_DE.setObjectName(_fromUtf8("actionKey_EN_DE"))
        self.actionKey_EN_DE.triggered.connect(self.file_open)
        ###########################################################
        self.actionRead_me = QtGui.QAction(MainWindow)
        self.actionRead_me.setObjectName(_fromUtf8("actionRead_me"))
        self.menuImport.addAction(self.actionFile)
        self.menuImport.addAction(self.actionKey_EN_DE)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuite)
        self.menuHelp.addAction(self.actionRead_me)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DE-CE Programs", None))
        self.radiobuttonDES.setText(_translate("MainWindow", "DES algorithm", None))
        self.radiobuttonAES.setText(_translate("MainWindow", "AES algorithm", None))
        self.radiobuttonRSA.setText(_translate("MainWindow", "RSA algorithm", None))
        self.labelfile1.setText(_translate("MainWindow", "File import", None))
        self.labelkey1.setText(_translate("MainWindow", "key import", None))
        self.Encryptbutton.setText(_translate("MainWindow", "Encrypt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encrypt), _translate("MainWindow", "ENCRYPT", None))
        self.radiobuttonDES_2.setText(_translate("MainWindow", "DES algorithm", None))
        self.radiobuttonAES_2.setText(_translate("MainWindow", "AES algorithm", None))
        self.radiobuttonRSA_2.setText(_translate("MainWindow", "RSA algorithm", None))
        self.labelfile2.setText(_translate("MainWindow", "File import", None))
        self.labelkey2.setText(_translate("MainWindow", "key import", None))
        self.Decryptbutton.setText(_translate("MainWindow", "Decrypt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decrypt), _translate("MainWindow", "DECRYPT", None))
        self.radioButton_7.setText(_translate("MainWindow", "MD5", None))
        self.radioButton_8.setText(_translate("MainWindow", "SHA", None))
        self.labelHash.setText(_translate("MainWindow", "Hash result:", None))
        self.buttonhash.setText(_translate("MainWindow", "Hash", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "HASH FUNCTION", None))
        self.menuFile.setTitle(_translate("MainWindow", "File ", None))
        self.menuImport.setTitle(_translate("MainWindow", "Import", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Editors", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))        
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionQuite.setText(_translate("MainWindow", "Quite", None))
        self.actionFile.setText(_translate("MainWindow", "Open File", None))
        self.actionKey_EN_DE.setText(_translate("MainWindow", "Key(EN,DE)", None))
        self.actionRead_me.setText(_translate("MainWindow", "Read me!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

