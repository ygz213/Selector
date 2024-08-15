# Building Selector

**1-** Move `app/icons/icon.png`, `app/icons/add.png`, `app/icons/load.png`, and `app/icons/save.png` to `app/` directory.


**2-** Convert `app/icons/icon.png` to `.ico` via the Internet and download the `.ico` file to `app/` directory."


**3-** Make sure that PyInstaller is installed.


**4-** Replace first 46 lines of `main.py` with the following code
```python
#pylint:disable=I1101
from os import path
from shutil import rmtree
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets
import item_handler as ih
import file_handler as fh
import sys
if not hasattr(sys, "frozen"):
    icon = path.join(path.dirname(__file__), "icon.png")
else:
    icon = path.join(sys.prefix, "icon.png")
if not hasattr(sys, "frozen"):
    add = path.join(path.dirname(__file__), "add.png")
else:
    add = path.join(sys.prefix, "add.png")
if not hasattr(sys, "frozen"):
    load = path.join(path.dirname(__file__), "load.png")
else:
    load = path.join(sys.prefix, "load.png")
if not hasattr(sys, "frozen"):
    save = path.join(path.dirname(__file__), "save.png")
else:
    save = path.join(sys.prefix, "save.png")
def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)



class Selector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selector')
        self.setWindowIcon(QtGui.QIcon(resource_path(icon)))
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
        self.save_list_button.setIcon(QtGui.QIcon(resource_path(save)))
        self.save_list_button.setIconSize(QtCore.QSize(20, 20))
        self.save_list_button.setFixedHeight(35)
        self.save_list_button.clicked.connect(lambda: fh.save_list(self))
        layout.addWidget(self.save_list_button, 1, 0)

        self.load_list_button = QtWidgets.QPushButton('     Load list...', self)
        self.load_list_button.setIcon(QtGui.QIcon(resource_path(load)))
        self.load_list_button.setIconSize(QtCore.QSize(20, 20))
        self.load_list_button.setFixedHeight(35)
        self.load_list_button.clicked.connect(lambda: fh.load_list(self))
        layout.addWidget(self.load_list_button, 2, 0)

        self.add_button = QtWidgets.QPushButton('     Add item...', self)
        self.add_button.setIcon(QtGui.QIcon(resource_path(add)))
```


**5-** `cd app/` and run `py -m PyInstaller --onefile --noconsole --add-data "icon.png;." --add-data "add.png;." --add-data "load.png;." --add-data "save.png;." --icon=icon.ico main.py`