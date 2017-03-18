 # -*- coding: UTF-8 -*-

# Copyright 2017 Ramon Vila Ferreres <ramonvilafer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#IMPORTS
import gui
import sys
from PyQt4.QtCore import *
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QApplication,QDialog,QMainWindow

#Graphical Interface
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 485)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 485))
        MainWindow.setMaximumSize(QtCore.QSize(600, 485))
        MainWindow.setBaseSize(QtCore.QSize(600, 485))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 271, 401))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.input = QtGui.QPlainTextEdit(self.groupBox)
        self.input.setGeometry(QtCore.QRect(10, 20, 251, 361))
        self.input.setObjectName(_fromUtf8("input"))
        self.index_selector = QtGui.QSpinBox(self.centralwidget)
        self.index_selector.setGeometry(QtCore.QRect(100, 420, 51, 21))
        self.index_selector.setMinimum(1)
        self.index_selector.setMaximum(25)
        self.index_selector.setObjectName(_fromUtf8("index_selector"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 420, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 10, 271, 401))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.output = QtGui.QPlainTextEdit(self.groupBox_2)
        self.output.setGeometry(QtCore.QRect(10, 20, 251, 361))
        self.output.setObjectName(_fromUtf8("output"))
        self.encode_btn = QtGui.QPushButton(self.centralwidget)
        self.encode_btn.setGeometry(QtCore.QRect(260, 420, 75, 23))
        self.encode_btn.setObjectName(_fromUtf8("encode_btn"))
        self.decode_btn = QtGui.QPushButton(self.centralwidget)
        self.decode_btn.setGeometry(QtCore.QRect(170, 420, 75, 23))
        self.decode_btn.setObjectName(_fromUtf8("decode_btn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuConfiguration = QtGui.QMenu(self.menubar)
        self.menuConfiguration.setObjectName(_fromUtf8("menuConfiguration"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_text_file = QtGui.QAction(MainWindow)
        self.actionOpen_text_file.setObjectName(_fromUtf8("actionOpen_text_file"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionEdit_alphabet = QtGui.QAction(MainWindow)
        self.actionEdit_alphabet.setObjectName(_fromUtf8("actionEdit_alphabet"))
        self.actionAbout_Creator = QtGui.QAction(MainWindow)
        self.actionAbout_Creator.setObjectName(_fromUtf8("actionAbout_Creator"))
        self.menuFile.addAction(self.actionOpen_text_file)
        self.menuFile.addAction(self.actionSave)
        self.menuConfiguration.addAction(self.actionEdit_alphabet)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pyROT", None))
        self.groupBox.setTitle(_translate("MainWindow", "Input", None))
        self.label.setText(_translate("MainWindow", "Cipher Index", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output", None))
        self.encode_btn.setText(_translate("MainWindow", "Encode", None))
        self.decode_btn.setText(_translate("MainWindow", "Decode", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionOpen_text_file.setText(_translate("MainWindow", "Open text file", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionEdit_alphabet.setText(_translate("MainWindow", "Edit alphabet", None))
        self.actionAbout_Creator.setText(_translate("MainWindow", "Information", None))

#Main class
class MainWindow(QtGui.QMainWindow,Ui_MainWindow,object):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent) #Superclass needed to initialize the all the elements
        self.setupUi(self)
        self.abc = [
                    '1','2','3','4','5','6','7','8','9','0',
                    'A','B','C','D','E','F','G','H','I','J',
                    'K','L','M','N','O','P','Q','R','S','T',
                    'U','V','W','X','Y','Z','/',"'",':','_',
                    '=','.','?',' ',',','a','b','c','d','e',
                    'f','g','h','i','j','k','l','m','n','o',
                    'p','q','r','s','t','u','v','w','x','y',
                    'z','(',')','ñ','Ñ'
                   ]

        self.text_list = []
        self.trye = []
        self.cipher = []
        self.result = []
        
        self.decode_btn.clicked.connect(self.decode)
        self.encode_btn.clicked.connect(self.encode)
        self.menuAbout.hovered.connect(self.credits)
        
    def encode(self):
        self.text = self.input.toPlainText()
        self.ROT = int(self.index_selector.value())
        for a in self.text:
            for p in a:
                self.text_list.append(str(p))
                #print 'text_list = ',self.text_list
                if (len(self.text) == len(self.text_list)):
                    self.generate_encode(self.text_list,self.ROT)
                else:
                    pass
                 
    def decode(self):
        self.text = self.input.toPlainText()
        self.ROT = -int(self.index_selector.value())
        for a in self.text:
            for p in a:
                self.text_list.append(str(p))
                #print 'text_list = ',text_list
                if (len(self.text) == len(self.text_list)):
                    self.generate_encode(self.text_list,self.ROT)
                else:
                    pass 

    def generate_encode(self,list,ROT):

        for element in self.text_list:
            if str(element) in self.abc:
                    for e in self.abc:
                        if (element == e):

                            z = self.abc.index(element)
                            self.trye.append(z)
                            if len(self.trye) == len(self.text):

                               for char in self.trye:

                                   char = int(char)
                                   char = char + ROT
                                   self.cipher.append(char)

                                   if len(self.trye) == len(self.cipher):
                                       self.def_encode(self.cipher)
                                   else:
                                        pass
                               else:
                                    pass
                    else:
                         continue
            else:
                pass

    def def_encode(self,ROT_list):
        salsa = ''
        try:
            for a in ROT_list:
                 self.result.append(self.abc[self.fixIndex(self.abc,a)])
                 if len(ROT_list) == len(self.result):
                    for m in self.result:
                            salsa = salsa + m

                            if len(salsa) == len(ROT_list):
                                if m != None:

                                    self.output.setPlainText(salsa) 
                                    self.text_list = []
                                    self.trye = []
                                    self.cipher = []
                                    self.result = []
                                else:
                                    pass

        except IndexError:
            pass
        except:
        	pass

    def fixIndex(self,lista,index): #NEEDS A REVIEW
        longitud = len(lista)-1
        if index >= longitud:
            newIndex = index-longitud
            while (newIndex > longitud):
                newIndex = newIndex - longitud
            else:
                return newIndex
        else:
            return index
        return newIndex

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    app.exec_()

main()
