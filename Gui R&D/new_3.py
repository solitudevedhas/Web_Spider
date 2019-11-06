from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle('Web Crawler')
    
    label = QtWidgets.QLabel(win)
    label.setText("sample test button")

    
    win.show()
    sys.exit(app.exec_())