import sys
import requests
import numpy as np
import pandas as pd
from ui_main import*
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

datetime = []
temp = []
humidity = []
windspeed = []
link = ""
mode = 0

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        #Nhận biết kích hoạt button
        self.ui.load_button.clicked.connect(self.bt_load)
        self.ui.start_button.clicked.connect(self.bt_start)
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.show()    

    #Hàm vẽ biểu đồ lên màn hình   
    def draw(self):
        self.grafica = Canvas_grafica()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()
        self.ui.grafica_uno.addWidget(self.grafica)
        self.ui.grafica_dos.addWidget(self.grafica1)
        self.ui.grafica_tres.addWidget(self.grafica2)
        self.ui.grafica_cuatro.addWidget(self.grafica3)

    #Hàm thiết lập lại editLine
    def seteditline(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please input city name", None))
        self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : black")

    #Thiết lập hoạt động cho load_button
    def bt_load(self):
        global link
        diachi = QFileDialog.getOpenFileNames()
        chuanhoa = str(diachi)[:-20]
        chuanhoa = chuanhoa[3:] 
        link = chuanhoa
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow",link, None))
        self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : red")

    #Thiết lập hoạt động cho start_button
    def bt_start(self):
        global link
        global datetime
        global temp
        global humidity
        global windspeed
        global mode
        #Xóa data cũ, đặt trong try sẽ trừ trường hợp lỗi
        try:
            self.ui.grafica_uno.removeWidget(self.grafica)
            self.ui.grafica_dos.removeWidget(self.grafica1)
            self.ui.grafica_tres.removeWidget(self.grafica2)
            self.ui.grafica_cuatro.removeWidget(self.grafica3)
        except:
           pass
        #Nếu nhấn start_button mà chưa nhập file mà tên thành phố thì sẽ ưu tiên nhập file
        if (link == "") and (self.ui.lineEdit.text() == ""):
            self.bt_load()
            i = 0
            #Đặt trong try để trừ trường hợp bị lỗi phần mềm do data không đúng khi load dữ liệu vẽ
            try:
                self.draw()
                link = ""
            except:
                pass
        #Nếu đã có link thì sẽ ưu tiên vẽ link
        elif link != "":
            try:
                self.draw()
                link = ""
                self.seteditline()
            except:
                pass
        #Trường hợp còn lại lấy dữ liệu API thời gian thực theo tên thành phố để vẽ
        else:
            try:
                api_key = 'ba6a67a16c5be47d1383d19b93965582'
                city = self.ui.lineEdit.text()
                url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + api_key
                time_to_get = 15
                response = requests.get(url).json()
                for i in range(time_to_get):
                    datetime.append(str(response['list'][i]['dt_txt']))
                    temp.append(round(float(response['list'][i]['main']['temp'])-273.15))
                    humidity.append(float(response['list'][i]['main']['humidity']))
                    windspeed.append(float(response['list'][time_to_get]['wind']['speed']))
                mode = 1
                self.draw()
                mode = 0
                datetime = []
                temp= []
                humidity = []
                windspeed = []
                self.seteditline()
            #Vẽ không thành công sẽ thông báo data lỗi
            except:
                print("Data loi")
                #self.ui.lineEdit.setText("Error: Please input right city name")
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Error: Please right input city name", None))
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : red")


#Biêu đồ line
class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 
        global link
        global mode
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
            plt.xticks(fontsize = 6, rotation = 29)
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
                plt.xticks(fontsize = 6, rotation = 29)
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
            plt.xticks(fontsize = 6, rotation = 29)
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
                plt.xticks(fontsize = 6, rotation = 29)
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
            plt.xticks(fontsize = 6, rotation = 29)
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
                plt.xticks(fontsize = 6, rotation = 29)
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