#pylint:disable=I1101
from PyQt6 import QtWidgets



def save_list(self):
    list_fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save list', '', '.selector File (.selector)')
    list_file = open(f'{list_fname[0]}.selector', 'w')

    for item in [self.list_widget.item(x).text() for x in range(self.list_widget.count())]:
        list_file.write(f'{item}\n')

    QtWidgets.QMessageBox.information(self, 'INFO', 'List has been saved.')
    list_file.close()


def load_list(self):
    list_fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Load list', '', 'Selector File (*.selector)')
    list_file = open(list_fname[0])

    self.list_widget.clear()
    for item in list_file.read().splitlines():
        self.list_widget.addItem(item)