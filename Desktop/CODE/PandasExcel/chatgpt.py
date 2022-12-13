import openpyxl
import qrcode
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel, QPushButton)

# Function to generate a QR code
def generate_qr_code(data):
  # Create the QR code
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
  )
  qr.add_data(data)
  qr.make(fit=True)

  # Return the QR code as an image
  return qr.make_image()

# Function to read data from an Excel file
def read_excel(filename):
  # Open the Excel file
  wb = openpyxl.load_workbook(filename)

  # Select the active sheet
  sheet = wb.active

  # Iterate over the rows in the sheet
  for row in sheet.rows:
    # Extract the data from each cell in the row
    data = [cell.value for cell in row]

    # Generate a QR code using the data
    qr = generate_qr_code(data)

    # Return the QR code image
    return qr

# Main window class
class MainWindow(QDialog):
  # Constructor
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    # Set the window title
    self.setWindowTitle("QR Code Generator")

    # Create a button to open the Excel file
    self.openButton = QPushButton("Open Excel File")
    self.openButton.clicked.connect(self.openFile)

    # Create a label to display the QR code
    self.qrLabel = QLabel()
    self.qrLabel.setAlignment(Qt.AlignCenter)

    # Set the layout of the main window
    self.setLayout(self.createLayout())

  # Function to create the layout of the main window
  def createLayout(self):
    layout = QVBoxLayout()

    # Add the button and label to the layout
    layout.addWidget(self.openButton)
    layout.addWidget(self.qrLabel)

    return layout

  # Function to open the Excel file
  def openFile(self):
    # Prompt the user for the name of the Excel file
    filename, _ = QFileDialog.getOpenFileName(
      self, "Open Excel File", "", "Excel Files (*.xlsx)"
    )

    # Read the data from the Excel file
    qr = read_excel(filename)

    # Display the QR code image
    pixmap = QPixmap.fromImage(qr)
    self.qrLabel.setPixmap(pixmap)
