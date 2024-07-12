#pylint:disable=I1101
from random import choice
from PyQt6 import QtWidgets



def select_item(self):
    item_indices = list(list(range(0, self.list_widget.count())))
    selected_items = []

    if self.list_widget.count() > 0:
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.SelectionMode.MultiSelection)
        for item in range(int(self.combo_box.currentText())):
            selected_item = choice(item_indices)
            selected_items.append(self.list_widget.item(selected_item).text())
            self.list_widget.item(selected_item).setSelected(True)
            item_indices.remove(selected_item)

        QtWidgets.QMessageBox.information(self, 'INFO', f'''
                                          <b>Randomly selected item(s)</b>:
                                          <ul>
                                          {''.join([f'<li>{item}</li>' for item in selected_items])}
                                          </ul>''')
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.SelectionMode.SingleSelection)


def add_item(self):
    item, ok = QtWidgets.QInputDialog.getText(self, 'Add item', 'Item name:')
    if item and ok:
        self.list_widget.addItem(item)
        self.combo_box.clear()
        self.combo_box.addItems([str(item) for item in list(range(1, self.list_widget.count()))])
