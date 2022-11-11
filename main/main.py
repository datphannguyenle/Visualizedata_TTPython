import sys
import requests
import numpy as np
import pandas as pd
from ui_main import*
import seaborn as sns
import matplotlib.pyplot as plt
from PySide2 import QtGui
from PySide2.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

datetime = []
temp = []
humidity = []
windspeed = []
link = ""   
mode = 0
#Có thể chỉnh thông số
rtm0 = 29   #Góc quay trục x của mode chọn file
rtm1 = 15   #Góc quay trục x mode input name city
time_to_get = 14    #Sô kết quả lấy dữ liệu api (3 tiếng cho 1 kết quả)

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Help")
        self.setMinimumSize(QSize(778, 634))
        self.setMaximumSize(QSize(778, 634))
        self.label = QLabel("")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.label.setText(QCoreApplication.translate("HelpWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff; background-color:transparent;\">USAGE</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Mode 0: Input a city name (English) -&gt; Click </span><span style=\" font-weight:600; font-style:italic; color:#ffffff; background-color:transparent;\">Start</span><span style=\" color:#ffffff; background-color:transparent;\"> to run</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Mode 1: Click </span><span style=\" font-weight:600; font-style:italic; color:#ffffff; background-color:transparent;\">Open file</span><span style=\" color:#ffffff; background-color:transparent;\"> -&gt; Choose csv file download from </span><span style=\" font-style:italic; color:#ffffff; background-color:transparent;\">https://www.visualcrossing.com</span><span style=\" color:#ffffff; background-color:transparent;\"> -&gt; Click </span><span style=\" font-weight:600; font-style:italic; color:#f"
                        "fffff; background-color:transparent;\">Start</span><span style=\" color:#ffffff; background-color:transparent;\"> to run</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">(Mode 1 is always preferred)</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Click </span><span style=\" font-weight:600; font-style:italic; color:#ffffff; background-color:transparent;\">Exit</span><span style=\" color:#ffffff; background-color:transparent;\"> to close</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff; background-color:transparent;\">REQUERIMENTS</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">*You have to install pip if you use Linux or a similar one to run this project</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">Dowload new version Python -&gt; https://www.python.org</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install numpy</span></p><p><s"
                        "pan style=\" color:#ffffff; background-color:transparent;\">pip install pandas</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install seaborn</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install PySide2</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install requests</span></p><p><span style=\" color:#ffffff; background-color:transparent;\">pip install matplotlib</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff; background-color:transparent;\">ERROR CODE:</span></p><p><span style=\" color:#ffffff;\">Error code 1: Data is not correct</span></p><p><span style=\" color:#ffffff;\">Error code 2: File format must be a csv file</span></p><p><span style=\" color:#ffffff;\">Error code 3: File format or data is not correct</span></p><p><span style=\" color:#ffffff;\">Error code 4: City name is not correct</span></p></body></html>", None))
        self.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"")

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.w = None
        self.setWindowTitle("Visualize Data")
        self.setWindowIcon(QtGui.QIcon(":/images/images/logos/main_logo_v2_32px.png"))
        self.ui.notice_label.setStyleSheet(u"background-color: none;\n""color : red")
        self.ui.notice_label.setText("")
        #Kích thước nút mặc định
        #self.ui.logo_img.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.load_button.setFixedWidth(81)
        self.ui.load_button.setFixedHeight(31)
        self.ui.start_button.setFixedWidth(81)
        self.ui.start_button.setFixedHeight(31)
        self.ui.help_button.setFixedWidth(81)
        self.ui.help_button.setFixedHeight(31)
        self.ui.exit_button.setFixedWidth(81)
        self.ui.exit_button.setFixedHeight(31)  
        self.ui.lineEdit.setFixedHeight(31)       
        #Nhận biết kích hoạt button
        self.ui.help_button.clicked.connect(self.show_new_window)
        self.ui.load_button.clicked.connect(self.bt_load)
        self.ui.start_button.clicked.connect(self.bt_start)
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.show()    

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()

    #Hàm vẽ biểu đồ lên màn hình   
    def draw(self):
        self.grafica = Canvas_grafica()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()
        self.ui.line_chart.addWidget(self.grafica)
        self.ui.scatter_chart.addWidget(self.grafica1)
        self.ui.bar_chart.addWidget(self.grafica2)
        self.ui.histogram_chart.addWidget(self.grafica3)
    
    def remove(self):
        self.ui.line_chart.removeWidget(self.grafica)
        self.ui.scatter_chart.removeWidget(self.grafica1)
        self.ui.bar_chart.removeWidget(self.grafica2)
        self.ui.histogram_chart.removeWidget(self.grafica3)          

    #Thiết lập hoạt động cho load_button
    def bt_load(self):
        global link
        diachi = QFileDialog.getOpenFileNames()
        chuanhoa = str(diachi)[:-20]
        chuanhoa = chuanhoa[3:] 
        link = chuanhoa
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow",link, None))

    #Thiết lập hoạt động cho start_button
    def bt_start(self):
        global link
        global time_to_get
        global datetime
        global temp
        global humidity
        global windspeed
        global mode
        #Xóa data cũ, đặt trong try sẽ trừ trường hợp lỗi
        try:
            self.remove()
        except:
           pass
        #Nếu nhấn start_button mà chưa nhập file mà tên thành phố thì sẽ ưu tiên nhập file
        if (link == "") and (self.ui.lineEdit.text() == ""):
            i = 0
            self.bt_load()
            #Đặt trong try để trừ trường hợp bị lỗi phần mềm do data không đúng khi load dữ liệu vẽ
            try:
                pd.read_csv(link)
                self.ui.notice_label.setText("")
                try:
                    self.draw()
                    link = ""
                    self.ui.notice_label.setText("")
                    self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                except:
                    link = ""
                    self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                    self.ui.notice_label.setText("Error code 1")
            except:
                link = ""
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                self.ui.notice_label.setText("Error code 2")
        #Nếu đã có link thì sẽ ưu tiên vẽ link
        elif link != "":
            try:
                self.draw()
                link = ""
                self.ui.notice_label.setText("")
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
            except:
                link = ""
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                self.ui.notice_label.setText("Error code 3")
        #Trường hợp còn lại lấy dữ liệu API thời gian thực theo tên thành phố để vẽ
        else:
            api_key = 'ba6a67a16c5be47d1383d19b93965582'
            city = self.ui.lineEdit.text()
            url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + api_key
            try:
                response = requests.get(url).json()
                for i in range(time_to_get):
                    datetime.append(str(response['list'][i]['dt_txt']))
                    temp.append(round(float(response['list'][i]['main']['temp'])-273.15))
                    humidity.append(float(response['list'][i]['main']['humidity']))
                    windspeed.append(float(response['list'][i]['wind']['speed']))
                mode = 1
                self.draw()
                mode = 0
                datetime = []
                temp= []
                humidity = []
                windspeed = []
                self.ui.notice_label.setText("")
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
            #Vẽ không thành công sẽ thông báo data lỗi
            except:
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
                self.ui.notice_label.setText("Error code 4")


#Biêu đồ line
class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
        global rtm0
        global rtm1
        global datetime
        global temp
        global humidity
        global windspeed
        if mode == 1:
            plt.clf()
            self.fig.suptitle('Line Graph: Weather forecast for the next few hours',size=9)
            plt.plot(datetime, humidity, 'b', label='Humidity (%)')
            plt.plot(datetime, temp, 'r', label='Temp (℃)')
            plt.plot(datetime, windspeed, 'g', label='Wind speed (m/s)')
            plt.xticks(fontsize = 6, rotation = rtm1)
            plt.legend(loc='best')
            plt.xlabel("Time")
            plt.ylabel("Index")     
        else:
            try:
                df = pd.read_csv(link)
                self.fig.suptitle('Line Graph: Weather forecast for 14 days',size=9)
                plt.plot(df['datetime'], df['humidity'], 'b', label='Humidity (%)')
                plt.plot(df['datetime'], df['temp'], 'r', label='Temp (℃)')
                plt.plot(df['datetime'], df['windspeed'], 'g', label='Wind speed (kph)')
                plt.plot(df['datetime'], df['uvindex'], 'y', label='UV index')
                plt.xticks(fontsize = 6, rotation = rtm0)
                plt.legend(loc='best')
                plt.xlabel("Time")
                plt.ylabel("Index") 
            except:
                pass


#Biêu đồ scatter
class Canvas_grafica2(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
        global rtm0
        global rtm1        
        global datetime
        global temp
        global humidity
        global windspeed
        if mode == 1:
            plt.clf()
            self.fig.suptitle('Scatter Plot: Weather forecast for next few hours',size=9)
            plt.scatter(datetime, humidity, s=50, c='blue', label='Humidity (%)')
            plt.scatter(datetime, temp, s=50, c='red', label='Temp (℃)')
            plt.scatter(datetime, windspeed, s=50, c='green', label='Wind speed (m/s)')
            plt.xticks(fontsize = 6, rotation = rtm1)
            plt.legend(loc='best')
            plt.xlabel("Time")
            plt.ylabel("Index")     
        else:
            try:
                df = pd.read_csv(link) 
                self.fig.suptitle('Scatter Plot: Weather forecast for 14 days',size=9)
                plt.scatter(df.datetime, df.humidity, s=50, c='blue', label='Humidity (%)')
                plt.scatter(df.datetime, df.temp, s=50, c='red', label='Temp (℃)')
                plt.scatter(df.datetime, df.windspeed,s=50, c='green', label='Wind speed (kph)')
                plt.scatter(df.datetime, df.uvindex, s=50, c='yellow', label='UV index')
                plt.xticks(fontsize = 6, rotation = rtm0)
                plt.legend(loc='best')
                plt.xlabel("Time")
                plt.ylabel("Index") 
            except:
                pass


#Biêu đồ bar
class Canvas_grafica3(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
        global rtm0
        global rtm1
        global datetime
        global temp
        global humidity
        global windspeed
        if mode == 1:
            plt.clf()
            self.fig.suptitle('Bar Plot: Weather forecast for next few hours',size=9)
            plt.bar(datetime,humidity,width=-0.4,align='edge',label='Humidity (%)')
            plt.bar(datetime,temp,width=0.4,align='edge',label='Temp (℃)')
            plt.bar(datetime,windspeed,color='red',label='Wind speed (m/s)')
            plt.legend(loc='best')
            plt.xticks(fontsize = 6, rotation = rtm1)
            #plt.title("Raining precipitaion in Ho Chi Minh city for 14 days")
            plt.xlabel("Time")
            plt.ylabel("Index")  
        else:
            try:
                df2 = pd.read_csv(link)
                plt.bar(df2['datetime'],df2['precip'],width=-0.4,align='edge',label='Precip (mm)')
                plt.bar(df2['datetime'],df2['precipcover'],width=0.4,align='edge',label='Precip-cover (%)')
                plt.plot(df2['datetime'],df2['temp'])
                plt.legend(loc='best')
                plt.xticks(fontsize = 6, rotation = rtm0)
                self.fig.suptitle("Bar Plot: Raining precipitaion for 14 days",size=9)
                plt.xlabel("Time")
                plt.ylabel("Index")
            except:
                pass


#Biểu đồ histogram
class Canvas_grafica4(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
        global temp
        if mode == 1:
            temp1 = pd.Series(temp)
            temp1.plot.hist(align='mid',bins=50)
            avarange=np.median(np.array(temp1))
            plt.grid(True)
            plt.axvline(avarange,color='red',label="Avarange temperature")
            plt.xlabel('Temperature')
            plt.ylabel('Index')
            plt.xticks(fontsize = 6)
            self.fig.suptitle("Histogram: Temperature for next few hours",size=9)
            plt.legend(loc='best')
        else:
            df2 = pd.read_csv(link)
            temp1=df2['temp']
            temp1.plot.hist(align='mid',bins=50)
            avarange=np.median(np.array(df2['temp']))
            plt.axvline(avarange,color='red',label="Avarange temperature") 
            plt.xlabel('Temperature')
            plt.ylabel('Index')
            plt.xticks(fontsize = 6)
            self.fig.suptitle("Histogram: Temperature for 14 days",size=9)
            plt.legend(loc='best')


#Bắt đấu chương trình chính
if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  