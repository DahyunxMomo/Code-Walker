import PySimpleGUI as sg
#sg.Window(title="hello world", layout=[[]], margins=(200,100)).read()

layout=[
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]
#Create the window
window=sg.Window("Demo", layout)

#Create an event loop
while True:
    event, values=window.read()
    #End program if user closes window or presses the OK Button
    if event =="OK" or event == sg.WIN_CLOSED:
        break
window.close()

