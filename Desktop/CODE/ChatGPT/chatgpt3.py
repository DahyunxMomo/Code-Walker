import pandas as pd
import qrcode
import PySimpleGUI as sg

# buscar el archivo excel
layout = [[sg.Text('Selecciona el archivo excel')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Ventana de PySimpleGUI').Layout(layout)
event, values = window.Read()
window.Close()

if event == 'Cancel':
    sg.Popup('Has cancelado el proceso')
    exit()

# leer la información del archivo y mostrarla en la ventana de PySimpleGUI
df = pd.read_excel(values[0])
sg.Popup('Información del archivo excel:', df)

# asignar los valores de la primer celda de cada columna como título para los códigos QR
qr_titles = [df.columns[i] for i in range(df.shape[1])]

# crear códigos QR con la información del archivo excel
for i in range(df.shape[0]):
    # obtener la información del renglón
    qr_data = [df.iloc[i,j] for j in range(df.shape[1])]
    
    # crear el código QR
    img = qrcode.make(qr_data)
    
    # exportar la imagen como archivo PNG
    img_name = f"{qr_data[0]}_{qr_data[1]}.png"
    img.save(img_name)

# mostrar mensaje de agradecimiento
sg.Popup('¡Gracias por utilizar este código!')
