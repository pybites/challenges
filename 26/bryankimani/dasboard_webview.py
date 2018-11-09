from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class DashboardWebView(QWidget):
    def __init__(self, parent: object = None) -> object:
        super(DashboardWebView, self).__init__(parent)
        self.load()

    def load(self):
        view = QWebView()
        view.load(QUrl("https://codechalleng.es"))
        view.showMaximized()
        vbox = QVBoxLayout()
        vbox.addWidget(view)

        self.setLayout(vbox)
