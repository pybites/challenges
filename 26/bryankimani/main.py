from PyQt5.QtWidgets import QApplication, QMainWindow

from bite import PyBite


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle("Welcome to CodeChallenges")

    def initUI(self):
        self.createMenu()

        self.setCentralWidget(PyBite())
        self.statusbar = self.statusBar()
        self.statusbar.showMessage(
            "A Community that Masters Python through Code Challenges"
        )

        self.showMaximized()
        self.show()

    def createMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        fileMenu.addMenu("New")

        editMenu = menubar.addMenu("Edit")
        editMenu.addMenu("Copy")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
