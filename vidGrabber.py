from pytube import YouTube
import PySimpleGUI as sg

layout = [
    [sg.Text("Welcome to YouGrab, a tool for tracking video information and downloading videos!")],
    [sg.Text('Paste Video Here: '), sg.Input(key='userInput')],
    [sg.Button('Display Information'), sg.Button('Download Video')],
]

window = sg.Window('VideoTracker', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Display Information':
        link = values['userInput']
        yt = YouTube(link)
        print("Title: ", yt.title)
        print("View: ", yt.views)
        """Display this info in a new popup"""
    if event == 'Download Video':
        link = values['userInput']
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download('videos')
        print('Done! Check your files to see the video.')

window.close()