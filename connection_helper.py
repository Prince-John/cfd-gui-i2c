import sys
import re
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

from MainConfigWindow import Ui_MainWindow
from GlobalSettingsWindow import Ui_Dialog


def camel_case_split(s):
    """https://stackoverflow.com/a/58996565"""
    idx = list(map(str.isupper, s))
    # mark change of case
    l = [0]
    for (i, (x, y)) in enumerate(zip(idx, idx[1:])):
        if x and not y:  # "Ul"
            l.append(i)
        elif not x and y:  # "lU"
            l.append(i + 1)
    l.append(len(s))
    # for "lUl", index of "U" will pop twice, have to filter that
    return [s[x:y] for x, y in zip(l, l[1:]) if x < y]


def split_camelcase_to_underscore(text):
    return "_".join(camel_case_split(text))


def remove_underscore(string, index):
    return string.split("_")[index]


class GlobalSettingsWindow(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self):
        super(GlobalSettingsWindow, self).__init__()
        self.setupUi(self)

        buttons = self.findChildren(QtWidgets.QPushButton)
        function_names = []
        print("\n#Button Connections\n")

        for button in buttons:
            function_name = "on_{0}_clicked".format(str(button.objectName()))
            print("self.{0}.clicked.connect(self.{1})".format(str(button.objectName()), function_name))
            function_names.append(function_name)

        print("\n#Button slot function declarations\n")

        for function_name in function_names:
            print('def {0}(self):\n\tprint("{1} Clicked.")\n\tpass\n'
                  .format(function_name, remove_underscore(function_name, 1)))

        ############################################################
        checkBoxes = self.findChildren(QtWidgets.QCheckBox)
        function_names = []
        print("\n#CheckBox Connections\n")

        for comboBox in checkBoxes:
            function_name = "on_{0}_clicked".format(remove_underscore(str(comboBox.objectName()), 0))
            print("self.{0}.stateChanged.connect(self.{1})".format(str(comboBox.objectName()),
                                                                   function_name))
            function_names.append(function_name)

        print("\n#Checkbox slot function declarations\n")

        for function_name in function_names:
            print(
                f'def {function_name}(self):\n\tprint("{remove_underscore(function_name, 1)} State Changed.")\n\tpass\n')

        # COMBO BOX DECLARATIONS
        #############################################################
        comboBoxes = self.findChildren(QtWidgets.QComboBox)
        function_names = []
        print("\n#ComboBox Connections\n")

        for comboBox in comboBoxes:
            function_name = "on_{0}_clicked".format(remove_underscore(str(comboBox.objectName()), 0))
            print("self.{0}.currentTextChanged.connect(self.{1})".format(str(comboBox.objectName()),
                                                                         function_name))
            function_names.append(function_name)

        print("\n#ComboBox slot function declarations\n")

        for function_name in function_names:
            print(
                f'def {function_name}(self, text):\n\tprint("{remove_underscore(function_name, 1)} '
                f'selection changed to {{0}}".format(text))\n'
                f'\tpass\n')



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ This is the class inheriting the Qt designer UI and adding functionality """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #        self.editGlobalSettings.clicked.connect(self.on_edit_global_settings)

        buttons = self.findChildren(QtWidgets.QPushButton)
        function_names = []
        print("\n************************MAIN WINDOW************************\n\n#Button Connections\n")

        for button in buttons:
            function_name = "on_{0}_clicked".format(str(button.objectName()))
            print("self.{0}.clicked.connect(self.{1})".format(str(button.objectName()), function_name))
            function_names.append(function_name)

        print("\n#Button slot function declarations\n")

        for function_name in function_names:
            print('def {0}(self):\n\tprint("{1} Clicked.")\n\tpass\n'
                  .format(function_name, remove_underscore(function_name, 1)))

        ############################################################
        checkBoxes = self.findChildren(QtWidgets.QCheckBox)
        function_names = []
        print("\n#CheckBox Connections\n")

        for comboBox in checkBoxes:
            function_name = "on_{0}_clicked".format(remove_underscore(str(comboBox.objectName()), 0))
            print("self.{0}.stateChanged.connect(self.{1})".format(str(comboBox.objectName()),
                                                                   function_name))
            function_names.append(function_name)

        print("\n#Checkbox slot function declarations\n")

        for function_name in function_names:
            print(
                f'def {function_name}(self):\n\tprint("{remove_underscore(function_name, 1)} State Changed.")\n\tpass\n')

        # COMBO BOX DECLARATIONS
        #############################################################
        comboBoxes = self.findChildren(QtWidgets.QComboBox)
        function_names = []
        print("\n#ComboBox Connections\n")

        for comboBox in comboBoxes:
            function_name = "on_{0}_clicked".format(remove_underscore(str(comboBox.objectName()), 0))
            print("self.{0}.currentTextChanged.connect(self.{1})".format(str(comboBox.objectName()),
                                                                         function_name))
            function_names.append(function_name)

        print("\n#ComboBox slot function declarations\n")

        for function_name in function_names:
            print(
                f'def {function_name}(self, text):\n\tprint("{remove_underscore(function_name, 1)} '
                f'selection changed to {{0}}".format(text))\n'
                f'\tpass\n')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w1 = GlobalSettingsWindow()
    w = MainWindow()