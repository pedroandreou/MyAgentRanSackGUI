import PySimpleGUI as sg


def layout():
    # add a touch of color
    sg.theme('DarkAmber')

    first_col = [[sg.Text('Folder'), sg.In(size=(25,15), enable_events=True , key='-FOLDER-'), sg.FolderBrowse(enable_events=True , key='-BROSWER-')],
                [sg.Text('Enter a string'), sg.InputText(enable_events=True, key='-INPUT-')],
                [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"), sg.Checkbox('Match case', size = (10, 5), default=False, key='-MATCHCASE-'), sg.Checkbox('Regular expression', size = (20, 5), default=False, key='-RE-')],
                [sg.Text(''), sg.InputText(key='-WARNING-', text_color='black', background_color='red', justification='center')]]

    second_col = [[sg.Button('OK', pad=(110, 2), size=(5, 1)), sg.Button('Cancel', pad=(116, 2), size=(5, 1))]]

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

    return layout