import PySimpleGUI as sg

def make_win1():
    sg.theme('DarkAmber')

    first_col = [[sg.Text('Folder'), sg.In(size=(25,15), enable_events=True , key='-FOLDER-'), sg.FolderBrowse(enable_events=True , key='-BROSWER-')],
                [sg.Text('Enter a string'), sg.InputText(enable_events=True, key='-INPUT-'), sg.Button("...")],
                [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
                [sg.Text(''), sg.InputText(size=(50, 1), text_color='black', justification='center', default_text='NO WARNING', disabled=True, key='-WARNING-')]]

    second_col = [[sg.Button('OK', pad=(96, 2), size=(5, 1)), sg.Button('Cancel', pad=(98, 2), size=(5, 1))]]

    third_col = [[sg.Listbox(values=[], enable_events=True, size=(50, 20), horizontal_scroll=True, key="-OUTPUT-")]]


    frame_1 = [[sg.Column(first_col, element_justification='center')]]
    frame_2 = [[sg.Column(second_col, element_justification='center')]]
    frame_3 = [[sg.Column(third_col, element_justification='center')]]


    layout_frame = [
                        [sg.Frame('', frame_1, background_color='yellow', pad=(20, 0)), sg.Frame('', frame_3, background_color='yellow')],
                        [sg.Frame('', frame_2, background_color='yellow')]
                    ]


    layout = [
                [sg.Push(), layout_frame, sg.Push()]
            ]


    return sg.Window('Search for a string in a specific directory', layout, background_color='black', finalize=True)


def make_win2():
    layout = [[sg.Checkbox('Match case', enable_events=True, size = (10, 5), default=False, key='-MATCHCASE-'), sg.Checkbox('Regular expression', enable_events=True, size = (20, 5), default=False, key='-RE-')]]


    return sg.Window('Settings Window', layout, background_color='black', finalize=True)