from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()
tableWidget = QTableWidget()
tableWidget.setRowCount(10)
tableWidget.setColumnCount(2)
item = QTableWidgetItem('Test 1')
tableWidget.setItem(1, 1, item)
layout.addWidget(tableWidget)
window.setLayout(layout)
window.show()
app.exec_()