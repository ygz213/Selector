#pylint:disable=I1101
from random import choice
from PyQt6 import QtWidgets



def select_item(self):
    item_indices = list(list(range(0, self.list_widget.count())))
    selected_items = []

    self.list_widget.clearSelection()

    if self.list_widget.count() > 0:
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.SelectionMode.MultiSelection)
        for item in range(int(self.combo_box.currentText())):    # With this for loop, the program selects as many random items as user wants
            selected_item = choice(item_indices)    # Selects random item
            selected_items.append(self.list_widget.item(selected_item).text())    # Adds random item to the 'selected_items' list
            self.list_widget.item(selected_item).setSelected(True)    # Shows random item in 'self.list_widget'
            item_indices.remove(selected_item)    # Deletes random item from 'item_indices' so it can't be selected again
        self.list_widget.setSelectionMode(QtWidgets.QListWidget.SelectionMode.SingleSelection)

        QtWidgets.QMessageBox.information(self, 'Selected item(s)', f'''
                                          <ul>
                                          {''.join([f'<li>{item}</li>' for item in selected_items])}
                                          </ul>''')    # Lists 'selected_items' list elements


def add_item(self):
    item, ok = QtWidgets.QInputDialog.getText(self, 'Add item', 'Item name:')
    if item and ok:
        self.list_widget.addItem(item)
        self.combo_box.clear()
        self.combo_box.addItems([str(item) for item in list(range(1, self.list_widget.count()))])


def edit_item(self):
    item_to_edit = self.list_widget.currentItem()

    new_item, ok = QtWidgets.QInputDialog.getText(self,
                                                  'Edit item',
                                                  'New item name:',
                                                  QtWidgets.QLineEdit.EchoMode.Normal,
                                                  item_to_edit.text())
    if new_item and ok:
        item_to_edit.setText(new_item)


def delete_item(self):
    item_to_delete = self.list_widget.currentItem()
    are_you_sure = QtWidgets.QMessageBox.question(self, 'Delete item', f'Are you sure you want to delete "<b>{item_to_delete.text()}</b>"?')

    if are_you_sure == QtWidgets.QMessageBox.StandardButton.Yes:
        self.list_widget.takeItem(self.list_widget.row(item_to_delete))
        self.combo_box.clear()
        self.combo_box.addItems([str(item) for item in list(range(1, self.list_widget.count()))])