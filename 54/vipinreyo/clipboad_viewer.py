import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from clipboard import ClipBoard


class ClipBoardApp(QWidget):
    """A Simple PyQT5 based class to display the Clipboard data (historically)"""

    def __init__(self):
        super().__init__()
        self.title = 'Clipboard viewer'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        """Helper method to call the ClipBoard class method to get historical data and display the data in a table"""
        cb = ClipBoard()
        clips = cb.get_clipboard_history()

        row_count = len(clips)

        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Date', 'Clipboard data'])

        for row, data in enumerate(clips):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(data[0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(data[1]))

        self.tableWidget.move(0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClipBoardApp()
    sys.exit(app.exec_())
