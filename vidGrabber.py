from pytube import YouTube
import PySimpleGUI as sg
import math

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
        layout2 = [
            [sg.Text("Video Information")],
            [sg.Text('Title: ' + yt.title), sg.Text('  View Count: ' + str(yt.views))],
            [sg.Button('Download Now'), sg.Text("Video Length: " + str(math.ceil(yt.length/60)) + " minutes")]
        ]
        window2 = sg.Window('VideoTracker', layout2)
        window.close()
        while True:
            event, values = window2.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Download Now':
                if yt.length <= 1200:
                    yd = yt.streams.get_highest_resolution()
                    yd.download('videos')
                    sg.popup('Process Complete!')
                else:
                    sg.popup('Error: Video over 20 minutes.')

    if event == 'Download Video':
        link = values['userInput']
        yt = YouTube(link)
        if yt.length <= 1200:
            yd = yt.streams.get_highest_resolution()
            yd.download('videos')
            sg.popup('Process Complete!')
        else:
            sg.popup('Error: Video over 20 minutes.')

window.close()
