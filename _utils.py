import time
import pytz
import threading
from datetime import datetime
import re
import pyperclip


TIME_FORMAT = ('%Y-%m-%d %H:%M:%S')
    
class utilities:
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





class functionalities():
    def do_something(self):
        #getting combobox value
        reComSectNum = re.compile("(\d\d|\d)")
        SectNum = str(self.comboBox.currentText()) 
        whatfound = reComSectNum.search(SectNum)
        print(whatfound.group())
        
    def Write_It(self):
        DaTa = self.lineEdit.text().strip()
        print("write!", DaTa)
