# Building Selector

**1-** Move `app/icons/icon.png` to `app/` directory.


**2-** Make sure that PyInstaller is installed.


**3-** Replace first 15 lines of 'main.py' with the following code
```python
#pylint:disable=I1101
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets
import item_handler as ih
import sys
import os
if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), "icon.png")
else:
    datafile = os.path.join(sys.prefix, "icon.png")
def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class Selector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selector')
        self.setWindowIcon(QtGui.QIcon(resource_path(datafile)))
        self.showMaximized()
        self.draw_widgets()
```


**5-** `cd app/` and run `py -m PyInstaller --onefile --noconsole --add-data "icon.png;." --icon=icon.ico main.py`