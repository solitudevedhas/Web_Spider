import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout)
from PyQt5.QtCore import Qt

class AppDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(600, 500)
		self.setWindowTitle('Update LCD with slider')

		self.lcd = QLCDNumber()
		slider = QSlider(Qt.Horizontal)
		slider.setMaximum(500)
		slider.setMinimum(-500)
		slider.valueChanged.connect(self.updateLCD)

		layout = QVBoxLayout()
		layout.addWidget(self.lcd)
		layout.addWidget(slider)
		self.setLayout(layout)

	def updateLCD(self, event):
		print(event)
		self.lcd.display(event)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

	sys.exit(app.exec_())