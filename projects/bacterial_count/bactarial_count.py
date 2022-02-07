import sys

import cv2 as cv

import os

import numpy as np

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *

class MainWindow(QDialog, Ui_Form):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # Variables for initialization statistics
        self.path_list = []
        self.path_list_i = 0
        self.count = 0
        self.bias_sum = 0
        
        # Define control parameters
        self.CENTER_X = 900
        self.CENTER_Y = 900
        self.RADIUS = 680
        
        # Define image parameters
        self.THRESH = 170
        self.MAXVAL = 255
        
        # Initializing auxiliary lines
        self.left_line = 600
        self.right_line = 1200
        self.up_line = 600
        self.down_line = 1200
       
        # Initialization signal and slot connection
        ##Initialization open file operation button
        self.open_folder_button.clicked.connect(self.get_file_path)
        self.next_button.clicked.connect(self.press_next)
        self.pre_button.clicked.connect(self.press_pre)
        
        ## Initialize gray value adjustment connection
        self.min_spin.valueChanged.connect(self.change_min_grayscale_spin)
        self.max_spin.valueChanged.connect(self.change_max_grayscale_spin)
        self.min_slider.valueChanged.connect(self.change_min_grayscale_slider)
        self.max_slider.valueChanged.connect(self.change_max_grayscale_slider)
        
        ## Initialization guide line, mask connection
        self.left_spin.valueChanged.connect(self.change_left)
        self.right_spin.valueChanged.connect(self.change_right)
        self.up_spin.valueChanged.connect(self.change_up)
        self.down_spin.valueChanged.connect(self.change_down)
        self.center_x_spin.valueChanged.connect(self.change_center_x)
        self.center_y_spin.valueChanged.connect(self.change_center_y)
        self.r_spin.valueChanged.connect(self.change_r)
        
        ##Initialize nine offset connections
        self.bias_1.valueChanged.connect(self.bias_change)
        self.bias_2.valueChanged.connect(self.bias_change)
        self.bias_3.valueChanged.connect(self.bias_change)
        self.bias_4.valueChanged.connect(self.bias_change)
        self.bias_5.valueChanged.connect(self.bias_change)
        self.bias_6.valueChanged.connect(self.bias_change)
        self.bias_7.valueChanged.connect(self.bias_change)
        self.bias_8.valueChanged.connect(self.bias_change)
        self.bias_9.valueChanged.connect(self.bias_change)

    def get_file_path(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "Select Folder", os.getcwd())
        temp_list = os.listdir(dir_choose)
        for i in temp_list:
            self.path_list.append(dir_choose + "/" + i)
        self.path_list_i = 0
        self.shulaibao()

    def press_next(self):
        if self.path_list_i == len(self.path_list) - 1:
            pass
        else:
            self.path_list_i += 1
            self.shulaibao()

    def press_pre(self):
        if self.path_list_i == 0:
            pass
        else:
            self.path_list_i -= 1
            self.shulaibao()

    def change_min_grayscale_slider(self):
        self.THRESH = self.min_slider.value()
        self.min_spin.setValue(self.THRESH)
        self.shulaibao()

    def change_min_grayscale_spin(self):
        self.THRESH = self.min_spin.value()
        self.min_slider.setValue(self.THRESH)
        self.shulaibao()

    def change_max_grayscale_slider(self):
        self.MAXVAL = self.max_slider.value()
        self.max_spin.setValue(self.MAXVAL)
        self.shulaibao()

    def change_max_grayscale_spin(self):
        self.MAXVAL = self.max_spin.value()
        self.max_slider.setValue(self.MAXVAL)
        self.shulaibao()

    def change_center_x(self):
        self.CENTER_X = self.center_x_spin.value()

        self.shulaibao()

    def change_center_y(self):
        self.CENTER_Y = self.center_y_spin.value()
        self.shulaibao()

    def change_r(self):
        self.RADIUS = self.r_spin.value()
        self.shulaibao()

    def change_left(self):
        self.left_line = self.left_spin.value()
        self.shulaibao()

    def change_right(self):
        self.right_line = self.right_spin.value()
        self.shulaibao()

    def change_down(self):
        self.right_line = self.right_spin.value()
        self.shulaibao()

    def change_up(self):
        self.right_line = self.right_spin.value()
        self.shulaibao()

    def bias_change(self):
        self.bias_sum = self.bias_1.value() + self.bias_2.value() + self.bias_3.value() + self.bias_4.value() + \
                        self.bias_5.value() + self.bias_6.value() + self.bias_7.value() + self.bias_8.value() + \
                        self.bias_9.value()
        self.count_label.setText(f"The total is:{self.count + self.bias_sum}")

def shulaibao(self):
        cv.destroyAllWindows()
        img = cv.imread(self.path_list[self.path_list_i])
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_gray = cv.blur(img_gray, (3, 3))
        # The circular mask is drawn and the target image is synthesized with gray image
        mask = np.zeros_like(img_gray)
        mask = cv.circle(mask, (self.CENTER_X, self.CENTER_Y), self.RADIUS, (255, 255, 255), -1)
        mask = mask // 255
        img_with_mask = mask * img_gray
        # Binarization
        _, img_threshold = cv.threshold(img_with_mask, self.THRESH, self.MAXVAL, cv.THRESH_BINARY)
        # Connect the region to get the border
        contours, _ = cv.findContours(img_threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        img_1 = cv.drawContours(img, contours, -1, (0, 0, 255))
        img_1 = cv.circle(img_1, (self.CENTER_X, self.CENTER_Y), self.RADIUS, (0, 255, 0), 5)
        img_1 = cv.putText(img_1, "{}".format(len(contours)), (100, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),5)
        # Draw guides
        cv.line(img_1, (self.left_line, 0), (self.left_line, 1800), (0, 255, 0), 3, 8)
        cv.line(img_1, (self.right_line, 0), (self.right_line, 1800), (0, 255, 0), 3, 8)
        cv.line(img_1, (0, self.up_line), (1800, self.up_line), (0, 255, 0), 3, 8)
        cv.line(img_1, (0, self.down_line), (1800, self.down_line), (0, 255, 0), 3, 8)
        # Display picture, record number
        img_1 = cv.resize(img_1, (0, 0), fx=0.5, fy=0.5)
        self.count = len(contours)
        self.bias_change()
        cv.imshow("COUNT", img_1)
        cv.waitKey(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
    cv.destroyAllWindows()
    sys.exit()