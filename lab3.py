import sys
from PyQt5.QtWidgets import QApplication
from dialog import MainWindow


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())