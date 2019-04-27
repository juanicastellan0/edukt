import sys
from PyQt5.QtWidgets import QApplication

from wiki_gui.WikiWindow import WikiWindow


class Edukt:
    @staticmethod
    def launch():
        q_app = QApplication(sys.argv)
        wiki_window = WikiWindow()
        sys.exit(q_app.exec())


edukt = Edukt()
edukt.launch()
