
from PySide import QtGui, QtCore
from hola import Ui_Dialog
import sys

class Ventana(QtGui.QDialog):
	def __init__(self):
		super(Ventana, self).__init__()
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)
		self.show()
def run():
    app = QtGui.QApplication(sys.argv)
    main = Ventana()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
