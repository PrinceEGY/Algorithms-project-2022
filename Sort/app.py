import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtGui import QTextCursor
from PySide6.QtUiTools import loadUiType
from copy import copy

from main_ui import Ui_MainWindow as MainUI


class Window(QMainWindow, MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list = []
        self.is_sep = True
        self.sep = self.le_sep.text()
        self.old_sep = self.sep
        self.btn_sort.clicked.connect(self.show_sorted)
        self.te_input.textChanged.connect(self.change_text)
        self.le_sep.textChanged.connect(self.update_sep)
        self.cb_asc.stateChanged.connect(self.show_sorted)

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            j = i-1
            key = arr[i]
            while j >= 0 and (arr[j] > key if self.cb_asc.isChecked() else arr[j] < key):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def merge_sort(self, arr):

        def merge(arr1, arr2):
            merged = []
            ptr1 = ptr2 = 0
            while ptr1 < len(arr1) or ptr2 < len(arr2):
                if ptr1 == len(arr1):
                    merged.extend(arr2[ptr2:])
                    break
                elif ptr2 == len(arr2):
                    merged.extend(arr1[ptr1:])
                    break
                if arr1[ptr1] < arr2[ptr2] if self.cb_asc.isChecked() else arr1[ptr1] > arr2[ptr2]:
                    merged.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    merged.append(arr2[ptr2])
                    ptr2 += 1
            return merged

        length = len(arr)
        mid = length//2

        if length == 1:
            return arr

        arr1, arr2 = arr[:mid], arr[mid:]

        return merge(self.merge_sort(arr1), self.merge_sort(arr2))

    # Called when there is a change on input text field

    def change_text(self):
        self.assert_text()
        self.update_list()
        if self.btn_autosort.isChecked():
            self.show_sorted()

    # Show sorted array on the output text field
    def show_sorted(self):
        if self.rb_insertion.isChecked():
            sorted_ls = self.insertion_sort(self.list)
        elif self.rb_merge.isChecked():
            sorted_ls = self.merge_sort(self.list)

        self.te_output.setPlainText((self.sep + ' ').join(map(str, sorted_ls)))

    # Assert text is entered in the correct form
    def assert_text(self):
        self.te_input.blockSignals(True)
        text = self.te_input.toPlainText()
        curr_cursor = self.te_input.textCursor()
        pos = curr_cursor.position()-1

        if text:  # If the text is not empty
            curr_input = text[pos]
            if curr_input.isnumeric():
                self.is_sep = False
            #
            elif curr_input == '-':
                if not self.is_sep:
                    self.te_input.setPlainText(text[:pos] + text[pos+1:])
                self.te_input.setTextCursor(curr_cursor)
                self.is_sep = False
                self.te_input.blockSignals(False)
                return
            else:
                new = text.replace(curr_input, self.sep).replace(' ', self.sep)
                new = [str.strip(i) for i in new.split(self.sep) if i != '']
                self.te_input.setPlainText(
                    (self.sep+' ').join(new)+self.sep+' ')
                self.te_input.setTextCursor(curr_cursor)

                self.is_sep = True

        self.te_input.blockSignals(False)

    # Called when number's seperator is changed
    def update_sep(self):
        if(self.le_sep.text()):
            self.sep = self.le_sep.text()
            curr_text = self.te_input.toPlainText()
            text_ls = [str.strip(i) for i in curr_text.split(',')]
            self.te_input.setPlainText((self.sep+' ').join(text_ls))
            self.old_sep = self.sep

    # Update numbers list in the correct form whenever new number is added/removed
    def update_list(self):
        self.list = self.te_input.toPlainText().split(self.sep + ' ')
        try:
            self.list = [float(i) for i in self.list if i]
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec())
