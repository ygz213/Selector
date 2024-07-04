from PyQt6 import QtWidgets



def add_item(self):
    item, ok = QtWidgets.QInputDialog.getText(self, "Add item", "Item name:")
    if item and ok:
        self.list_widget.addItem(item)