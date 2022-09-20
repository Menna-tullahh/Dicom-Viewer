
from re import X
from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
import pydicom as dicom
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os
import tkinter as tk
from tkinter.filedialog import *
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.express as px
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, user_path, volume3d, img_shape):
        path = self.path_list(user_path)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        #MainWindow.setMaximumSize(QtCore.QSize(1235, 870))
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"selection-background-color: rgb(129, 86, 129);\n"
"gridline-color: rgb(255, 170, 255);\n"
"border-top-color: rgb(255, 170, 255);\n"
"border-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 460, 401, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(520, 50, 401, 301))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(520, 460, 401, 301))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 370, 361, 22))
        self.horizontalSlider.setStyleSheet("background-color: rgb(255,255,255);\n""")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(img_shape[2]-1)
        self.horizontalSlider.setSingleStep(1)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(40, 780, 361, 22))
        self.horizontalSlider_2.setStyleSheet("background-color: rgb(255,255,255);")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(img_shape[1]-1)
        self.horizontalSlider_2.setSingleStep(1)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(540, 370, 361, 22))
        self.horizontalSlider_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(img_shape[0]-1)
        self.horizontalSlider_3.setSingleStep(1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(540, 780, 361, 22))
        self.horizontalSlider_4.setStyleSheet("background-color: rgb(255,255,255);")
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.setMinimum(0)
        self.horizontalSlider_4.setMaximum(img_shape[0]-1)
        self.horizontalSlider_4.setSingleStep(1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 51, 31))
        self.label.setStyleSheet("background-color: rgb(255,255,255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 10, 61, 31))
        self.label_2.setStyleSheet("background-color: rgb(255,255,255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 420, 71, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 420, 131, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.listview = QtWidgets.QListWidget(self.centralwidget)
        self.listview.setGeometry(QtCore.QRect(1000, 35, 261, 751))
        self.listview.resize(300,800)
        self.listview.setObjectName("listview")
  

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 30))
        self.menubar.setObjectName("menubar")
        self.menuopen = QtWidgets.QMenu(self.menubar)
        self.menuopen.setObjectName("menuopen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuopen.addAction(self.action_open)
        self.action_open.triggered.connect(self.openDirectory)

        self.menubar.addAction(self.menuopen.menuAction())
        


        
        self.figure = plt.figure()
        self.figure1 = plt.figure()
        self.figure2 = plt.figure()
        self.figure3 = plt.figure()

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser2 = QtWebEngineWidgets.QWebEngineView()
        self.browser3 = QtWebEngineWidgets.QWebEngineView()


#        self.canvas1 = FigureCanvas(self.figure1)
#        self.canvas2 = FigureCanvas(self.figure2)
        self.canvas3 = FigureCanvas(self.figure3)

     

        self.verticalLayout.addWidget(self.browser)
        self.verticalLayout_2.addWidget(self.browser2)
        self.verticalLayout_3.addWidget(self.browser3)
        self.verticalLayout_4.addWidget(self.canvas3)

        x = [user_path,volume3d]
        self.horizontalSlider.valueChanged.connect(lambda sv, ov = user_path:self.plotSlider(sv, ov))
        self.horizontalSlider_2.valueChanged.connect(lambda sv, ov = x:self.plotSlider1(sv, ov))
        self.horizontalSlider_3.valueChanged.connect(lambda sv, ov = x:self.plotSlider2(sv, ov))
        self.horizontalSlider_4.valueChanged.connect(lambda sv, ov = x:self.plotSlider3(sv, ov))
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Axial"))
        self.label_2.setText(_translate("MainWindow", "Coronal"))
        self.label_3.setText(_translate("MainWindow", "Sagittal"))
        self.label_4.setText(_translate("MainWindow", "Test"))
        self.menuopen.setTitle(_translate("MainWindow", "&file"))
        self.action_open.setText(_translate("MainWindow", "&open"))

    def openDirectory(self):
        tk.Tk().withdraw() 
        fn = askdirectory()
        
        updated = fn
        #print("updated: ", updated)
        path = self.path_list(updated)
        #ct_images=self.path_list(user_path)

        slices = [dicom.read_file(updated+'/'+s,force=True) for s in path]
        #x1 = dicom.dcmread(user_path +"/"+path[value], force=True)

        for i in range(len(slices)):
            pixel_spacing = slices[0].PixelSpacing
            slices_thickess = slices[0].SliceThickness

            axial_aspect_ratio = pixel_spacing[1]/pixel_spacing[0]
            sagital_aspect_ratio = pixel_spacing[1]/slices_thickess
            coronal_aspect_ratio = slices_thickess/pixel_spacing[0]

            #     print("Pixel spacing is:",pixel_spacing)
            #     print("Slices Thickness is:",slices_thickess)

            #     print("Axial Aspect Ratio:",axial_aspect_ratio)
            #     print("Sagital Aspect Ratio:",sagital_aspect_ratio)
            #     print("Coronal Aspect Ratio:",coronal_aspect_ratio)
        img_shape = list(slices[0].pixel_array.shape)
        img_shape.append(len(slices))
        volume3d=np.zeros(img_shape)
        for i,s in enumerate(slices):
            array2D=s.pixel_array
            volume3d[:,:,i]= array2D  

            
        for i in range(len(slices)):
            array2D=slices[i].pixel_array
            volume3d[:,:,i]= array2D

        ui.setupUi(MainWindow,updated, volume3d, img_shape)
        #self.setupUi(MainWindow, updated)

    def path_list(self,p):
        if(p==' '):
            return []
        else:
            return os.listdir(p)


    def plotSlider(self, value, user_path):
        #path = "PAT014/D00"+ str(value) +".dcm"
        #print(user_path)
        path = self.path_list(user_path)
        #print(path)
        #print(value)
        x = dicom.dcmread(user_path +"/"+path[value], force=True)
        
        fig = px.imshow(x.pixel_array,color_continuous_scale='gray', width=380, height=330)
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

        self.listview.clear()
        self.listview.insertItem(0, str(x))

##sagittal
    def plotSlider1(self, value, user_path):
        path = self.path_list(user_path[0])
        #ct_images=self.path_list(user_path)
        if(value <len(path)):
            x1 = dicom.dcmread(user_path[0] +"/"+path[value], force=True)
        else:
            x1 = dicom.dcmread(user_path[0] +"/"+path[len(path)-1], force=True)


        #binary_string=True
        fig = px.imshow(user_path[1][:,value,:],color_continuous_scale='gray' , width=380, height=330)
        
        #ax1.set_aspect(sagital_aspect_ratio)

        self.browser2.setHtml(fig.to_html(include_plotlyjs='cdn'))
        
        
        self.listview.clear()
        self.listview.insertItem(0, str(x1))

 

##coronal
    def plotSlider2(self, value, user_path):
        path = self.path_list(user_path[0])
        if(value <len(path)):
            x1 = dicom.dcmread(user_path[0] +"/"+path[value], force=True)
        else:
            x1 = dicom.dcmread(user_path[0] +"/"+path[len(path)-1], force=True)
       

        fig = px.imshow(user_path[1][value,:,:].T,color_continuous_scale='gray', width=380, height=330)
        #ax1.set_aspect(sagital_aspect_ratio)

        self.browser3.setHtml(fig.to_html(include_plotlyjs='cdn'))

        #ax1.set_aspect(coronal_aspect_ratio)
        self.listview.clear()
        self.listview.insertItem(0, str(x1))

#4th plot coronal
    def plotSlider3(self, value, user_path):
        path = self.path_list(user_path[0])
        if(value <len(path)):
            x1 = dicom.dcmread(user_path[0] +"/"+path[value], force=True)
        else:
            x1 = dicom.dcmread(user_path[0] +"/"+path[len(path)-1], force=True)
       

        self.figure3.clear()
        ax1 = self.figure3.add_subplot(1,1,1)
        ax1.imshow(user_path[1][value,:,:].T,'gray')
        #ax1.set_aspect(coronal_aspect_ratio)
        self.canvas3.draw()
        self.listview.clear()
        self.listview.insertItem(0, str(x1))

if __name__ == "__main__":
    import sys
    global user_path
    user_path = " "
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, user_path, volume3d = [0,0,0], img_shape = [0,0,0])
    MainWindow.show()
    sys.exit(app.exec_())
