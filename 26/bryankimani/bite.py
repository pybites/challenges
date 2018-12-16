from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QPushButton, QVBoxLayout,
                             QWidget, QLabel, QTableWidget, QTableWidgetItem)

from calculator import Calculator
from dasboard_webview import DashboardWebView


class PyBite(QWidget):
    def __init__(self):
        super().__init__()
        self.RightGroupBox = QGroupBox("Group 2")
        self.LeftGroupBox = QGroupBox("Group 1")
        self.dashboard_webview = DashboardWebView()
        self.calculator = Calculator()
        self.create_left_group_box()
        self.create_right_group_box()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.LeftGroupBox, 1, 0)
        mainLayout.addWidget(self.RightGroupBox, 1, 1, 1, 3)
        self.setLayout(mainLayout)

    def create_left_group_box(self):
        self.LeftGroupBox.setStyleSheet("background-color:#a41d1d; color: #ffffff;")

        introText = QLabel("Happy Coding,Ninja!")
        introText.setStyleSheet(
            """
        QLabel {
            text-align: center;
            font-size: 28px;
            background: transparent;
            margin: 20px 0px;
        }
        """
        )

        logo = QLabel(self)
        pixmap = QPixmap("assets/images/logo.png")
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        # Optional, resize window to image size
        self.resize(pixmap.width(), pixmap.height())

        calculator_button = QPushButton("Calculator")
        calculator_button.setCheckable(True)
        calculator_button.clicked.connect(self.launch_calculator)

        dash_board_button = QPushButton("Dashboard Webview")
        dash_board_button.setCheckable(True)
        dash_board_button.clicked.connect(self.load_dashboard_webview)

        bites_of_py_button = QPushButton("Bites of Py")
        bites_of_py_button.setCheckable(True)

        blog_challenges_button = QPushButton("Blog Challenges")
        blog_challenges_button.setCheckable(True)

        hundred_days_button = QPushButton("100DaysOfCode")
        hundred_days_button.setCheckable(True)

        messages_button = QPushButton("Messages")
        messages_button.setCheckable(True)

        settings_button = QPushButton("Messages")
        settings_button.setCheckable(True)

        py_bites_blog_button = QPushButton("PyBites Blog")
        py_bites_blog_button.setCheckable(True)

        layout = QVBoxLayout()
        layout.addWidget(logo)
        layout.addWidget(introText)
        layout.addWidget(dash_board_button)
        layout.addWidget(calculator_button)
        layout.addWidget(bites_of_py_button)
        layout.addWidget(blog_challenges_button)
        layout.addWidget(hundred_days_button)
        layout.addWidget(messages_button)
        layout.addWidget(settings_button)
        layout.addWidget(py_bites_blog_button)
        layout.addStretch(1)

        self.LeftGroupBox.setLayout(layout)

    def create_right_group_box(self):
        self.RightGroupBox.setStyleSheet("background-color:#ffffff; color: #000000;")
        self.create_table()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.setStretch(0, 1)
        self.RightGroupBox.setLayout(layout)

    def create_table(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(40)
        self.tableWidget.setColumnCount(20)
        self.tableWidget.move(0, 0)
        self.tableWidget.showMaximized()

    def launch_calculator(self):
        self.calculator.show()

    def load_dashboard_webview(self):
        self.dashboard_webview.show()
