# Graficas Matplotlib
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
import numpy as np
from ui_main import*
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

#        self.grafica = Canvas_grafica()
#        self.grafica1 = Canvas_grafica2()
#        self.grafica2 = Canvas_grafica3()
#        self.grafica3 = Canvas_grafica4()
#
#        self.ui.grafica_uno.addWidget(self.grafica)
#        self.ui.grafica_dos.addWidget(self.grafica1)
#        self.ui.grafica_tres.addWidget(self.grafica2)
#        self.ui.grafica_cuatro.addWidget(self.grafica3)
#Làm ẩn thanh close, minimized, maximized 
#        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#Nhận biết kích hoạt button
        self.ui.load_button.clicked.connect(self.bt_load)
        self.ui.start_button.clicked.connect(self.bt_start)
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.show()    
#Thiết lập hoạt động cho button
    def bt_load(self):
        diachi = QFileDialog.getOpenFileNames()
        chuanhoa = str(diachi)[:-20]
        chuanhoa = chuanhoa[3:] 
        print(chuanhoa)
    def bt_start(self):
        self.grafica = Canvas_grafica()
        self.grafica1 = Canvas_grafica2()
        self.grafica2 = Canvas_grafica3()
        self.grafica3 = Canvas_grafica4()

        self.ui.grafica_uno.addWidget(self.grafica)
        self.ui.grafica_dos.addWidget(self.grafica1)
        self.ui.grafica_tres.addWidget(self.grafica2)
        self.ui.grafica_cuatro.addWidget(self.grafica3)
        print("start ok")  


class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 

        #self.fig.suptitle('Grafica de Datos',size=9)

        df = pd.read_csv('Ho Chi Minh.csv')
        time = []
        month = ''
        for c in df['datetime']:
            if str(c)[5:7] != month:
                time.append(str(c)[-5:])
                month = str(c)[5:7]
            else:
                time.append(str(c)[-2:])

        self.ax = plt.axes()
        plt.plot(time, df['temp'], 'r', label='Temp')
        plt.plot(time, df['humidity'], 'b', label='Humidity')
        plt.plot(time, df['windspeed'], 'g', label='Wind speed')
        plt.plot(time, df['uvindex'], 'y', label='UV index')
        plt.title("Weather index in Ho Chi Minh city for 14 days",size=9)
        plt.legend(loc='best')
        plt.xlabel("Time")
        plt.ylabel("Index")


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

        df2 = pd.read_csv('Ho Chi Minh.csv')
        time = []
        month = ''
        for c in df2['datetime']:
            if str(c)[5:7] != month:
                time.append(str(c)[-5:])
                month = str(c)[5:7]
            else:
                time.append(str(c)[-2:])
        plt.bar(time,df2['precip'],width=-0.4,align='edge',label='Precip(mm)')
        plt.bar(time,df2['precipcover'],width=0.4,align='edge',label='Precip-cover (%)')
        plt.plot(time,df2['temp'])
        plt.legend(loc='best')
        plt.title("Raining precipitaion in Ho Chi Minh city for 14 days")
        plt.xlabel("Time")
        plt.ylabel("Index")


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