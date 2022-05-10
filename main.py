#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from sys import argv
from random import randint
from Algorithms.bfs import bfs , graph
ui, _ = loadUiType("./ui/bfs.ui")
class Mainwindow(QMainWindow, ui):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("Shortest Path") # Set title for window
        self.setStyleSheet(open("./themes/dark-orange.css").read()) # set default theme style
        self.setWindowIcon(QIcon("./icons/icon.ico")) # set icon for window
        self.setWindowFlag(Qt.FramelessWindowHint) # this will hide the title bar
        self.setGeometry(30,30,1160,680)
        self.iconChanges()
        self.tryProblem()
        self.handelGui()
    def handelGui(self):
        # Add the names of the themes
        self.comboBox.addItem("Dark Orange Mode")
        self.comboBox.addItem("Dark Blue Mode")
        self.comboBox.addItem("Dark Gray Mode")
        self.comboBox.addItem("Ubuntu Mode")
        self.comboBox.addItem("Classic Mode")
        
        self.comboBox.activated.connect(self.changeTheme) # Change the theme OnFly
        
        self.frame_3.setDisabled(True) # Disable the map change part
        
        self.pushButton_12.setIcon(QIcon("./icons/bfs.ico"))
        self.pushButton_12.setIconSize(QSize(150,150))
        self.pushButton_7.setIcon(QIcon("./icons/icon.ico"))
        self.pushButton_7.setIconSize(QSize(30,30))
        # Set image in Button
        self.label_8.setPixmap(QPixmap("./images/map.png").scaled(1420, 800))
        self.pushButton_3.clicked.connect(self.distroy) # Close Application
        self.pushButton_4.clicked.connect(self.showMaximized) # Show Maximized Application
        self.pushButton_5.clicked.connect(self.showMinimized) # Show Minimized Application
        self.pushButton_6.clicked.connect(self.showFullScreen) # Show Full Screen Application
        self.pushButton_8.clicked.connect(self.showNormal) # Show Application on normal size
        
    def iconChanges(self):
        # Icon of title bar
        self.pushButton_3.setIcon(QIcon("./icons/quit.ico"))
        self.pushButton_4.setIcon(QIcon("./icons/maxico.ico"))
        self.pushButton_5.setIcon(QIcon("./icons/min.ico"))
        self.pushButton_6.setIcon(QIcon("./icons/full.ico"))
        self.pushButton_8.setIcon(QIcon("./icons/normal.ico"))
        
    def distroy(self):
        # Close Application
        app.quit()
        

    def changeTheme(self):
        # Read themes files
        if self.comboBox.currentText() == "Dark Blue Mode":
            self.setStyleSheet(open("./themes/dark.css").read())
        elif self.comboBox.currentText() == "Dark Orange Mode":
            self.setStyleSheet(open("./themes/dark-orange.css").read())
        elif self.comboBox.currentText() == "Classic Mode":
            self.setStyleSheet(open("./themes/classic.css").read())
        elif self.comboBox.currentText() == "Dark Gray Mode":
            self.setStyleSheet(open("./themes/dark-blue.css").read())
        elif self.comboBox.currentText() == "Ubuntu Mode":
            self.setStyleSheet(open("./themes/Ubuntu.qss").read())
        
    def tryProblem(self):
        self.pushButton_2.clicked.connect(self.bfsAlgorithm)
        # listOfProblem=['A','B','C','D','E','F','G','H']
        try:
            for i in graph.keys():
                self.comboBox_2.addItem(i)
                self.comboBox_3.addItem(i)
        except:
            self.comboBox_2.addItem("undefined")
            self.comboBox_3.addItem("undefined")
            

    def bfsAlgorithm(self):
        self.start = self.comboBox_2.currentText()
        self.goal = self.comboBox_3.currentText()
        solution = bfs(graph, self.start, self.goal)
        try:
            s=""
            for i in solution:
                s+=" - "+i
            self.label_6.setText(s[3:])
        except:
            self.label_6.setText("!There is no path between the two points")

try:
    app = QApplication(argv)
    myapp = Mainwindow()
    myapp.show()
    app.exec_()
except:
    pass