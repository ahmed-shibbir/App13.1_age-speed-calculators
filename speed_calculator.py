
from PyQt6.QtWidgets import QApplication,QBoxLayout, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QComboBox

import sys
from datetime import datetime


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")

        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_label_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_label_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metric (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_level = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_level, 3, 0, 1, 2)

        self.setLayout(grid)


    def calculate_speed(self):
        global unit
        distance = float(self.distance_label_edit.text())
        time = float(self.time_label_edit.text())

        # Calculate average speed
        speed = distance / time

        # Check what user choose in the combo
        if self.unit_combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.unit_combo.currentText() == "Imperial (miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        # Display the result
        self.output_level.setText(f"Average speed is {speed} {unit}")


# Programme main loop/running loop of app:-
app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())

