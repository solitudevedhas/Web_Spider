import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

class MenuBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menubar Demo')
        self.resize(600, 500)

        self.menuBar = self.menuBar()

        fileMenu = self.menuBar.addMenu('File')
        editMenu = self.menuBar.addMenu('Edit')
        undoDeleteMenu = editMenu.addMenu('Undo delete')

        newfile_Menu = fileMenu.addAction('New')
        openfile_menu = fileMenu.addAction('Open')
        savefile_menu = fileMenu.addAction('Save')

        exit_action = QAction('Exit App', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(lambda:QApplication.quit())

        fileMenu.addAction(exit_action)

        yes_action = QAction('Yes', self)
        no_action = QAction('No', self)
        undoDeleteMenu.addAction(yes_action)
        undoDeleteMenu.addAction(no_action)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = MenuBarDemo()
    demo.show()

    sys.exit(app.exec_())
