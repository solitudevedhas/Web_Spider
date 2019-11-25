import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("Sample test Run")
    mbox.setDetailedText("Now you are watching sample test run")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(800,600)
    w.setWindowTitle('Web Crawler')
    
    label = QLabel(w)
    label.setText("sample test button")
    label.move(10,10)
    label.show()

    btn = QPushButton(w)
    btn.setText('click')
    btn.move(20,30)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())