#pylint:disable=I1101
from PyQt6 import QtWidgets



def save_list(window):
    list_fname = QtWidgets.QFileDialog.getSaveFileName(window, 'Save list', '', 'Selector File (*.selector)')

    with open(f'{list_fname[0]}.selector', 'w', encoding = 'utf-8') as list_file:
        for item in [window.list_widget.item(x).text() for x in range(window.list_widget.count())]:
            list_file.write(f'{item}\n')

    QtWidgets.QMessageBox.information(window, 'INFO', 'List has been saved.')



def load_list(window):
    list_fname = QtWidgets.QFileDialog.getOpenFileName(window, 'Load list', '', 'Selector File (*.selector)')

    try:
        with open(list_fname[0], encoding = 'utf-8') as list_file:
            window.list_widget.clear()
            for item in list_file.read().splitlines():
                window.list_widget.addItem(item)
            window.combo_box.clear()
            window.combo_box.addItems([str(item) for item in list(range(1, window.list_widget.count()))])
    except FileNotFoundError:
        QtWidgets.QMessageBox.critical(window, 'ERROR', 'No such file.')
