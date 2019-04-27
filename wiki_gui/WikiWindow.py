from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class WikiWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Edukt with Wikipedia"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QIcon("wiki_gui/encyclopedia.png"))

        self.main_menu = self.menuBar()

        window_menu = self.main_menu.addMenu("File")
        window_menu.addAction(self.add_button_to_menu("exit.png", "Exit", "Ctrl+E"))

        quit_button = self.add_button("Quit", 560, 450, "<h5>For close window</h5>")
        quit_button.clicked.connect(self.quit)

        about_button = self.add_button("About Edukt", 20, 40, "<h4>For know more of Edukt</h2>")
        about_button.clicked.connect(self.about)

        search_label = self.add_label("Search label", 120, 40)
        search_label.setGeometry(50, 50, 100, 100)

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def quit(self):
        reply = QMessageBox.question(self, "Close message", "Are you sure to close app?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()

    def about(self):
        QMessageBox.about(self, "About Edukt", "Edukt is an application that facilitates searches of wikipedia in the "
                                               "Spanish and English languages...")

    def make_search(self):
        wants_connect = QMessageBox.question(self, "Connect with app", "Do you want to connect with app?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if wants_connect == QMessageBox.Yes:
            self.statusBar().showMessage("Connecting with app... you're connected with app")
        else:
            self.statusBar().showMessage("Application not connected")

    def add_button(self, name, x, y, tool_tip):
        button = QPushButton(name, self)
        button.move(x, y)
        button.setToolTip(tool_tip)
        return button

    def add_button_to_menu(self, icon, name, shortcut):
        menu_button = QAction(QIcon(icon), name, self)
        menu_button.setShortcut(shortcut)
        menu_button.triggered.connect(self.quit)
        return menu_button

    def add_label(self, text, x, y):
        label = QLabel(text, self)
        label.move(x, y)
        return label
