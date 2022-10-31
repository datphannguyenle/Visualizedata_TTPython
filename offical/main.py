import sys
import numpy as np
from ui_main import*
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
import requests
datetime = []
temp = []
humidity = []
link = ""
mode = 0


class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
#Làm ẩn thanh close, minimized, maximized 
#        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#Nhận biết kích hoạt button
        self.ui.load_button.clicked.connect(self.bt_load)
        self.ui.start_button.clicked.connect(self.bt_start)
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.show()    
#################################################################################Thiết lập hoạt động cho button
    def bt_load(self):
        global link
        diachi = QFileDialog.getOpenFileNames()
        chuanhoa = str(diachi)[:-20]
        chuanhoa = chuanhoa[3:] 
        link = chuanhoa
        self.ui.lineEdit.setText(link)
        self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : red")
############################################################################################################
    def bt_start(self):
        global link
        global datetime
        global temp
        global humidity
        global mode
        try:
            self.ui.grafica_uno.removeWidget(self.grafica)
            self.ui.grafica_dos.removeWidget(self.grafica1)
            self.ui.grafica_tres.removeWidget(self.grafica2)
            self.ui.grafica_cuatro.removeWidget(self.grafica3)
        except:
           pass
        if (link == "") and (self.ui.lineEdit.text() == ""):
            diachi = QFileDialog.getOpenFileNames()
            chuanhoa = str(diachi)[:-20]
            chuanhoa = chuanhoa[3:] 
            link = chuanhoa
            self.ui.lineEdit.setText(link)
            self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : red")
            i = 0
            try:
                self.grafica = Canvas_grafica()
                self.grafica1 = Canvas_grafica2()
                self.grafica2 = Canvas_grafica3()
                self.grafica3 = Canvas_grafica4()
                self.ui.grafica_uno.addWidget(self.grafica)
                self.ui.grafica_dos.addWidget(self.grafica1)
                self.ui.grafica_tres.addWidget(self.grafica2)
                self.ui.grafica_cuatro.addWidget(self.grafica3)
                link = ""
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : black")
            except:
                pass
        elif link != "":
            try:
                self.grafica = Canvas_grafica()
                self.grafica1 = Canvas_grafica2()
                self.grafica2 = Canvas_grafica3()
                self.grafica3 = Canvas_grafica4()
                self.ui.grafica_uno.addWidget(self.grafica)
                self.ui.grafica_dos.addWidget(self.grafica1)
                self.ui.grafica_tres.addWidget(self.grafica2)
                self.ui.grafica_cuatro.addWidget(self.grafica3)
                link = ""
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : black")
            except:
                pass
        else:
            try:
                api_key = 'ba6a67a16c5be47d1383d19b93965582'
                city = self.ui.lineEdit.text()
                url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + api_key
                time_to_get = 5
                response = requests.get(url).json()
                for i in range(time_to_get):
                    datetime.append(str(response['list'][i]['dt_txt']))
                    temp.append(round(float(response['list'][i]['main']['temp'])-273.15))
                    humidity.append(float(response['list'][i]['main']['humidity']))
                mode = 1
                self.grafica = Canvas_grafica()
                self.grafica1 = Canvas_grafica2()
                self.grafica2 = Canvas_grafica3()
                self.grafica3 = Canvas_grafica4()
                mode = 0
                self.ui.grafica_uno.addWidget(self.grafica)
                self.ui.grafica_dos.addWidget(self.grafica1)
                self.ui.grafica_tres.addWidget(self.grafica2)
                self.ui.grafica_cuatro.addWidget(self.grafica3)
                datetime = []
                temp= []
                humidity = []
                self.ui.lineEdit.clear()
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : black")
            except:
                print("Data loi")
                self.ui.lineEdit.setText("Please input right city name")
                self.ui.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border-radius:5px;\n""color : red")
                
                #self.ui.lineEdit.clear()


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
        if mode == 1:
            plt.clf()
            self.fig.suptitle('Weather index in Ho Chi Minh city for 14 days',size=9)
            plt.plot(datetime, np.array(humidity), 'b', label='Humidity (%)')
            plt.plot(datetime, np.array(temp), 'r', label='Temp (℃)')
            plt.xticks(fontsize = 6, rotation = 29)
            plt.legend(loc='best')
            plt.xlabel("Time")
            plt.ylabel("Index")     
        else:
            try:
                df = pd.read_csv(link) 
                self.fig.suptitle('Weather index in Ho Chi Minh city for 14 days',size=9)
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


class Canvas_grafica2(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1,dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        nombres = ['Fresa', 'Piña', 'Lima', 'Uva']
        colores = ['blue','yellow','aqua','fuchsia']
        tamaño = [20, 26, 30, 24]
        explotar = [0.05, 0.05, 0.05, 0.05] 

        plt.title("Cantidad de Frutas Disponibles",
            color='black',size=9)

        self.ax.pie(tamaño, explode = explotar, labels = nombres, 
            colors = colores,
                autopct = '%1.0f%%', pctdistance = 0.6,
                shadow=True, startangle=90, radius = 0.8, 
                labeldistance=1.1)  
        self.ax.axis('equal')


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
        if mode == 1:
            plt.clf()
            self.fig.suptitle('Weather index in Ho Chi Minh city for 14 days',size=9)
            plt.plot(datetime, np.array(humidity), 'b', label='Humidity (%)')
            plt.plot(datetime, np.array(temp), 'r', label='Temp (℃)')
            plt.xticks(fontsize = 6, rotation = 29)
            plt.legend(loc='best')
            plt.xlabel("Time")
            plt.ylabel("Index") 
        else:
            try:
                df2 = pd.read_csv(link)
                plt.bar(df2['datetime'],df2['precip'],width=-0.4,align='edge',label='Precip(mm)')
                plt.bar(df2['datetime'],df2['precipcover'],width=0.4,align='edge',label='Precip-cover (%)')
                plt.plot(df2['datetime'],df2['temp'])
                plt.legend(loc='best')
                plt.xticks(fontsize = 6, rotation = 29)
                self.fig.suptitle("Raining precipitaion in Ho Chi Minh city for 14 days",size=9)
                plt.xlabel("Time")
                plt.ylabel("Index")
            except:
                pass


class Canvas_grafica4(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        x = [1, 2, 3, 4, 5,6,7]
        y1 = [1, 0, 1, 3, 2,4,3]
        y2 = [0, 2, 2, 3, 4,6,5]
        y3 = [3, 1, 3, 4, 2,7,6]

        y = np.vstack([y1, y2, y3])

        labels = ["Y1 ", "Y2", "Y3"]
        color = ["orange","blue","green"]

        self.ax.stackplot(x, y1, y2, y3, labels=labels,colors=color)
        self.ax.legend(loc='upper left')
        self.ax.stackplot(x, y)
        self.fig.suptitle('Grafica Stackplot',size=9)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  