from PyQt4 import QtGui
import sys
import design

class App(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()