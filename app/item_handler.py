#pylint:disable=I1101
from random import choice
from PyQt6 import QtCore, QtWidgets
import file_handler as fh



def select_item(window):
    item_indices = list(list(range(0, window.list_widget.count())))
    selected_items = []

    window.list_widget.clearSelection()

    if window.list_widget.count() > 0:
        for item in range(int(window.combo_box.currentText())):    # With this for loop, the program selects as many random items as user wants
            selected_item = choice(item_indices)    # Selects random item
            selected_items.append(window.list_widget.item(selected_item).text())    # Adds random item to the 'selected_items' list
            window.list_widget.item(selected_item).setSelected(True)    # Shows random item in 'self.list_widget'
            item_indices.remove(selected_item)    # Deletes random item from 'item_indices' so it can't be selected again

        fh.save_history(window.list_widget, selected_items)

        QtWidgets.QMessageBox.information(window, 'Selected item(s)', f'''
                                          <ul>
                                          {''.join([f'<li>{item}</li>' for item in selected_items])}
                                          </ul>''')    # Lists 'selected_items' list elements


def add_item(window):
    item, ok = QtWidgets.QInputDialog.getText(window, 'Add item', 'Item name:')
    if item and ok:
        window.list_widget.addItem(item)
        window.combo_box.clear()
        window.combo_box.addItems([str(item) for item in list(range(1, window.list_widget.count()))])


def edit_item(window):
    item_to_edit = window.list_widget.currentItem()

    new_item, ok = QtWidgets.QInputDialog.getText(window,
                                                  'Edit item',
                                                  'New item name:',
                                                  QtWidgets.QLineEdit.EchoMode.Normal,
                                                  item_to_edit.text())
    if new_item and ok:
        item_to_edit.setText(new_item)


def delete_item(window):
    item_list_to_delete = [item.text() for item in window.list_widget.selectedItems()]

    are_you_sure = QtWidgets.QMessageBox.question(window, 'Delete item(s)', f'''
                                                  Are you sure you want to delete the following item(s)?<br>
                                                  <ul>
                                                  {''.join([f'<li>{item}</li>' for item in item_list_to_delete])}
                                                  </ul>''')

    if are_you_sure == QtWidgets.QMessageBox.StandardButton.Yes:
        for item in item_list_to_delete:
            window.list_widget.takeItem(window.list_widget.row(window.list_widget.findItems(item, QtCore.Qt.MatchFlag.MatchExactly)[0]))

        window.combo_box.clear()
        window.combo_box.addItems([str(item) for item in list(range(1, window.list_widget.count()))])
