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
def read_excel(filename):
  # Read the data from the Excel file using pandas
  df = pd.read_excel(filename)

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
    [sg.Button("Generate QR Codes"), sg.Exit()],
  ]
  window = sg.Window("QR Code Generator").layout(layout)

  # Loop until the user exits the GUI
  while True:
    # Get the next event from the GUI
    event, values = window.read()

    # If the user clicked the "Generate QR Codes" button
    if event == "Generate QR Codes":
      # Read the data from the Excel file
      qr = read_excel(values[0])

      # Display the QR code image
      sg.popup_scrolled(
        "QR Code",
        image_data=qr,
        image_size=(400, 400),
        image_filename="qr.png",
      )

    # If the user clicked the "Exit" button or closed the window
    elif event in (None, "Exit"):
      break

# Run the main function
if __name__ == "__main__":
  main()
