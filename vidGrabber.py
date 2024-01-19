from pytube import YouTube
import PySimpleGUI as sg

layout = [
    [sg.Text('Text'), sg.Spin(['Item 1', "Item 2"])],
    [sg.Button('Button')],
    [sg.Input()]
]

window = sg.Window('VideoTracker', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Button':
        print("button pressed")

window.close()


"""
yt = YouTube(link)
print("Title: ", yt.title)
print("View: ", yt.views)



yd = yt.streams.get_highest_resolution()

yd.download('videos')
"""