import pandas as pd
import qrcode
import PySimpleGUI as sg

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
def read_excel(filename, columns, rows):
  # Read the data from the Excel file using pandas
  df = pd.read_excel(filename, usecols=columns, nrows=rows)

  # Iterate over the rows in the dataframe
  for index, row in df.iterrows():
    # Extract the data from each cell in the row
    data = row.values

    # Generate a QR code using the data
    qr = generate_qr_code(data)

    # Return the QR code image
    return qr

# Main function to run the script
def main():
  # Create the GUI using PySimpleGUI
  layout = [
    [sg.Text("QR Code Generator")],
    [sg.Text("Enter the name of the Excel file:")],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button("Preview"), sg.Exit()],
  ]
  window = sg.Window("QR Code Generator").layout(layout)

  # Loop until the user exits the GUI
  while True:
    # Get the next event from the GUI
    event, values = window.read()

    # If the user clicked the "Preview" button
    if event == "Preview":
  # Read the data from the Excel file
     data = pd.read_excel(values[0])

  # Display a preview of the data
    sg.popup_scrolled(data.head())

  # Prompt the user to select the columns and rows to use
    columns = sg.popup_get_text("Enter the columns to use (comma-separated):")
    rows = sg.popup_get_text("Enter the number of rows to use:")

  # Convert the columns and rows to a list and an integer, respectively
    columns = columns.split(",")
    rows = int(rows)

  # Read the data from the Excel file using the selected columns and rows
    qr = read_excel(values[0], columns, rows)

  # Display the QR code image
    sg.popup_scrolled(
     "QR Code",
     image=qr,
     image_size=(400, 400),
     image_filename="qr.png",
  )
