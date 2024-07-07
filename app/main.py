#pylint:disable=I1101
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets
import item_handler as ih



class Selector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selector')
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.showMaximized()
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
        self.add_button.clicked.connect(lambda: ih.add_item(self))
        layout.addWidget(self.add_button, 0, 2)

        layout.addWidget(QtWidgets.QLabel("Select", self), 1, 1)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItems([str(item) for item in [item for item in range(1, self.list_widget.count())]])
        layout.addWidget(self.comboBox, 1, 2)
        layout.addWidget(QtWidgets.QLabel("items from list", self), 1, 3)

        self.select_button = QtWidgets.QPushButton('SELECT', self)
#        self.add_button.clicked.connect(lambda: ih.add_item(self))
        layout.addWidget(self.select_button, 2, 2)

    def show_context_menu(self, position):
        context_menu = QtWidgets.QMenu(self)

        context_menu.addAction(QtGui.QAction("Edit...", self))
        context_menu.addAction(QtGui.QAction("Remove...", self))

        context_menu.exec(self.list_widget.viewport().mapToGlobal(position))



application = QtWidgets.QApplication(argv)
window = Selector()
window.show()
application.exec()
