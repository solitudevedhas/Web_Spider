from PyQt5.QtWidgets import QApplication, QWidget, QComboBox
from PyQt5.QtGui import QIcon

app = QApplication([])
window = QWidget()
window.resize(300,150)

combo = QComboBox(window)
combo.resize(100,50)
combo.move(100,50)

combo.addItem('Yes')   #combo.addItem(QIcon('.png'), 'Yes')
combo.addItem('No') #combo.addItem(QIcon('.png'), 'No')

window.show()
app.exec_()
