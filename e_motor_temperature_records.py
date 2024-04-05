import sys
import random

from PySide6 import QtCharts
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from PySide6.QtCharts import (
QBarCategoryAxis,
QBarSet,
QChart,
QChartView,
QStackedBarSeries,
QValueAxis
)



class TemperatureRecords(QMainWindow):
    def __init__(self):
        super().__init__()

        low = QBarSet('Min')
        high = QBarSet('Max')

        low.append(random.randint(50, 61))

        high.append(random.randint(60, 71))

        series = QStackedBarSeries()
        series.append(low)
        series.append(high)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Temperature records in celcius')
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimaitons)

        categories = ['Rob. Arm 1', 'Rob. Arm 2', 'Rob. Arm 3',
                      'Rob. Arm 4', 'Rob. Arm 5', 'Rob. Arm 6',
                      'Wheel 1', 'Wheel 2', 'Wheel 3', 'Wheel 4']

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setTitleText('Motor')
        chart.addAxis(axis_x, Qt.AlignBottom)
        axis_y = QValueAxis()
        axis_y.setRange(0, 75)
        axis_y.setTitleText('Temperature [&deg;C]')
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TemperatureRecords()
    window.resize(600, 300)
    window.show()
    sys.exit(app.exec())