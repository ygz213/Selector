#pylint:disable=I1101
from os import path
from shutil import rmtree
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets
import item_handler as ih
import file_handler as fh



class Selector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selector')
        self.setWindowIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/icon.png'))
        self.showMaximized()
        self.draw_widgets()


    def draw_widgets(self):
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)

        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.addItems(['Item 1', 'Item 2', 'Item 3'])
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.SelectionMode.MultiSelection)
        self.list_widget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self.show_context_menu)
        layout.addWidget(self.list_widget, 0, 0)

        self.save_list_button = QtWidgets.QPushButton('     Save list...', self)
        self.save_list_button.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/save.png'))
        self.save_list_button.setIconSize(QtCore.QSize(20, 20))
        self.save_list_button.setFixedHeight(35)
        self.save_list_button.clicked.connect(lambda: fh.save_list(self))
        layout.addWidget(self.save_list_button, 1, 0)

        self.load_list_button = QtWidgets.QPushButton('     Load list...', self)
        self.load_list_button.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/load.png'))
        self.load_list_button.setIconSize(QtCore.QSize(20, 20))
        self.load_list_button.setFixedHeight(35)
        self.load_list_button.clicked.connect(lambda: fh.load_list(self))
        layout.addWidget(self.load_list_button, 2, 0)

        self.add_button = QtWidgets.QPushButton('     Add item...', self)
        self.add_button.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/add.png'))
        self.add_button.setIconSize(QtCore.QSize(20, 20))
        self.add_button.setFixedHeight(35)
        self.add_button.setFixedWidth(125)
        self.add_button.clicked.connect(lambda: ih.add_item(self))
        layout.addWidget(self.add_button, 0, 3)

        layout.addWidget(QtWidgets.QLabel('Select', self), 1, 2)
        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.addItems([str(item) for item in list(range(1, self.list_widget.count()))])
        layout.addWidget(self.combo_box, 1, 3)
        layout.addWidget(QtWidgets.QLabel('items from list', self), 1, 4)

        self.select_button = QtWidgets.QPushButton('SELECT', self)
        self.select_button.clicked.connect(lambda: ih.select_item(self))
        layout.addWidget(self.select_button, 2, 3)


    def show_context_menu(self, position):
        item_list = self.list_widget.selectedItems()
        context_menu = QtWidgets.QMenu(self)

        if len(item_list) == 1:
            edit_action = QtGui.QAction('Edit...', self)
            edit_action.triggered.connect(lambda: ih.edit_item(self))
            context_menu.addAction(edit_action)

            delete_action = QtGui.QAction('Remove...', self)
            delete_action.triggered.connect(lambda: ih.delete_item(self))
            context_menu.addAction(delete_action)
        if len(item_list) > 1:
            delete_action = QtGui.QAction('Remove...', self)
            delete_action.triggered.connect(lambda: ih.delete_item(self))
            context_menu.addAction(delete_action)

        context_menu.exec(self.list_widget.viewport().mapToGlobal(position))



application = QtWidgets.QApplication(argv)
application.aboutToQuit.connect(lambda: rmtree(f'{path.join(path.dirname(argv[0]))}/__pycache__'))
window = Selector()
window.show()
application.exec()
