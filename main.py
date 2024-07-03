#pylint:disable=I1101
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets



class Selector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selector')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.draw_widgets()

    def draw_widgets(self):
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)

        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.addItems(['Item 1', 'Item 2', 'Item 3'])
        self.list_widget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self.show_context_menu)
        layout.addWidget(self.list_widget, 0, 0, 4, 1)

        self.add_button = QtWidgets.QPushButton('Add item...', self)
        layout.addWidget(self.add_button, 0, 1)

    def show_context_menu(self, position):
        context_menu = QtWidgets.QMenu(self)

        context_menu.addAction(QtGui.QAction("Edit...", self))
        context_menu.addAction(QtGui.QAction("Remove...", self))

        context_menu.exec(self.list_widget.viewport().mapToGlobal(position))



application = QtWidgets.QApplication(argv)
window = Selector()
window.show()
application.exec()
