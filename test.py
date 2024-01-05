import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_names = ["MainConfigWindow.ui", "GlobalSettingsWindow.ui"]

    ui_files = [QFile(ui_file_name) for ui_file_name in ui_file_names]

    # if not ui_file.open(QIODevice.ReadOnly):
    #     print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
    #     sys.exit(-1)
    loader = QUiLoader()
    main_window = loader.load(ui_files[0])
    global_settings_window = loader.load(ui_files[1])
    for ui_file in ui_files:
        ui_file.close()

    if not main_window:
        print(loader.errorString())
        sys.exit(-1)

    main_window.show()

    sys.exit(app.exec())
