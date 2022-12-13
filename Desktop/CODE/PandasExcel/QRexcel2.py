
import pandas as pd
import qrcode as qr
import PySimpleGUI as sg

# Mostramos un cuadro de diálogo para que el usuario seleccione el archivo Excel
file_name = sg.popup_get_file('Selecciona un archivo Excel', file_types=(("Archivos Excel", "*.xlsx"),))

for row in file_name.itertuples():
    qr_text = (f'Activo: {row.Activo}, Description: {row.Desc}, FechaCompra: {row.FechaCompra}, Entidad: {row.Entidad}, CostoV1: {row.CostoV1}, CostoV2: {row.CostoV2}, TotalInv: {row.TotalInv}, Factura: {row.Factura}, OC: {row.OC}, Proveedor: {row.Proveedor}, AñoCompra: {row.AñoCompra}')
    img = qr.make(qr_text)
    title = (f'{row.Activo,row.Entidad}.png')
    img.save(title)