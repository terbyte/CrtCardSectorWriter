
from sqlite3 import DatabaseError
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import QTimer,QDateTime
from datetime import datetime
import time
import re
import pytz
import pyperclip

TIME_FORMAT = ('%Y-%m-%d %H:%M:%S')
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 427)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 601, 81))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color:#a8dadc")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 100, 601, 311))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("background-color:#457b9d ")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(490, 270, 89, 31))
        self.pushButton.setStyleSheet("background-color:#006d77;color:white; ")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(430, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(460, 40, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color:white;")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(190, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 161, 41))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(190, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(30, 150, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:white")
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(30, 90, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 100, 211, 26))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 50, 51, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 100, 51, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(460, 80, 121, 23))
        self.checkBox.setStyleSheet("color:white;")
        self.checkBox.setObjectName("checkBox")
        self.dateTimeEdit.setDisplayFormat('yyyy-MM-dd hh:mm:ss')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.TimeSetter)
        self.parse_date_time()
        self.timer.start(1000)
        
        currentTime = QDateTime.currentDateTime()
        # dt_string = currentTime.toString(self.dateTimeEdit.displayFormat(self,TIME_FORMAT))
        self.dateTimeEdit.setDateTime(currentTime)
        
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        cp = QDesktopWidget().availableGeometry().center()
        qr = Form.frameGeometry()
        qr.moveCenter(cp)
        Form.move(qr.topLeft())
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CARDSECTOR WRITER"))
        self.label.setText(_translate("Form", "CARDCODE:"))
        self.label_2.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "WRITE"))
        self.label_3.setText(_translate("Form", "Current Time:"))
        self.label_4.setText(_translate("Form", "Sector"))
        self.label_5.setText(_translate("Form", "Current Time:"))
        self.label_6.setText(_translate("Form", "Current Epoch Time:"))
        self.label_7.setText(_translate("Form", "Current Epoch Time:"))
        self.label_8.setText(_translate("Form", "Write Data of 0-3 Blocks:"))
        self.label_9.setText(_translate("Form", "Pick Date & Time:"))
        self.pushButton_3.setText(_translate("Form", "Copy"))
        self.pushButton_4.setText(_translate("Form", "Copy"))
        self.checkBox.setText(_translate("Form", "ALL SECTORS"))
        for i in range (3,17):
            self.comboBox.addItem(f"SECTOR {i}")
            
            
        ################ BUTTONS ########################
        self.pushButton.clicked.connect(lambda checked: Write_It(self))
        self.pushButton_3.clicked.connect(lambda checked: copy_Epoch(self))
        self.pushButton_4.clicked.connect(lambda checked: GetDatetime(self))
        ################ COMBO BOX ######################
        self.comboBox.activated.connect(lambda checked: do_something(self))
        
    def TimeSetter(self):
        
        cur_time = datetime.strftime(datetime.now(), TIME_FORMAT)
        self.label_5.setText(cur_time)

        epoch = int(time.mktime(time.strptime(cur_time, TIME_FORMAT)))
        timeinID = str(epoch)
        self.label_7.setText(timeinID)

    def parse_date_time(self):
        timenow=datetime.now()
        # timenow=timenow.strftime(TIME_FORMAT)	
        localize = pytz.utc.localize(timenow)
        parsed_datetime= localize.strftime(TIME_FORMAT)
        self.label_5.setText(parsed_datetime)
        self.epoch_it(parsed_datetime)
        return parsed_datetime
    
    def epoch_it(self,parsed_datetime):
        epoch = int(time.mktime(time.strptime(parsed_datetime, TIME_FORMAT)))
        timeinEpoch = str(epoch)
        self.label_7.setText(timeinEpoch)
        return timeinEpoch

       
def copy_Epoch(self):
    content = self.label_7.text()
    to_copy = self.epoch_it(self.parse_date_time())
    pyperclip.copy(to_copy)


def GetDatetime(self):
    dt = self.dateTimeEdit.dateTime()
    dt_string = dt.toString(self.dateTimeEdit.displayFormat())
    to_copy = self.epoch_it(dt_string)
    pyperclip.copy(to_copy)


def do_something(self):
    #getting combobox value
    reComSectNum = re.compile("(\d\d|\d)")
    SectNum = str(self.comboBox.currentText()) 
    whatfound = reComSectNum.search(SectNum)
    print(whatfound.group())
    




def Write_It(self):
    DaTa = self.lineEdit.text().strip()
    print("write!", DaTa)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
