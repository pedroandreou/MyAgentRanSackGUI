# import files
import window_setup
from conditions import check_string_exists_in_file as check_string_exists_in_file
from conditions import get_lines_the_given_string_appears as get_lines_the_given_string_appears

# import libs
import PySimpleGUI as sg
import os


files_lst = []                  # list to append the files that contain the given string
lines_found_lst = []            # create list to append the lines that the given string appears in a specific txt file
no_file = True                  # boolean for checking if there is no file in the given dir
matchcase_checkbox_flag = False # boolean for checking if the matchcase checkbox is ticked
re_checkbox_flag = False        # boolean for checking if the regular expression checkbox is ticked
files_lst_window = False        # boolean for checking if the files list window is filled so it can be pressed

# start off with 1 window open
window1, window2 = window_setup.make_win1(), None


# event loop 
while True:
    window, event, values = sg.read_all_windows()
    
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    
    elif event == '...' and not window2:
        window2 = window_setup.make_win2()
    
    elif event == '-MATCHCASE-':
        matchcase_checkbox_flag = values['-MATCHCASE-']

    elif event == '-RE-':
        re_checkbox_flag = values['-RE-']

    elif event == 'OK':
        
        # get windows
        window_files = window['-FILE LIST-']
        window_output = window['-OUTPUT-']
        window_warning = window['-WARNING-']

        # empty windows
        files_lst = []
        window_files.update(files_lst)
        window_output.update('')
        window_warning.update('NO WARNING')

        folder_path = values['-FOLDER-']
        string = values['-INPUT-']  

        if not folder_path and not string:
            window_warning.update('WARNING: no directory and string provided')
            continue
        elif not string:
            window_warning.update('WARNING: no string provided')
            continue
        elif not folder_path:
            window_warning.update('WARNING: no directory provided')
            continue
    
        
        # check if the directory exists -> that's because the directory can be entered manually
        if os.path.isdir(folder_path) == True:
            no_file = True
            
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"): 
                    filepath = os.path.join(folder_path, filename).replace("\\","/") 

                    if check_string_exists_in_file(filepath, string, matchcase_checkbox_flag, re_checkbox_flag) == 1:
                        files_lst.append(filename)
                        window_files.update(files_lst)
                        no_file = False
                        files_lst_window = True
                        

            if no_file == True:
                window_warning.update('WARNING: no file exists that contains the given string')
        else:
            window_warning.update('WARNING: the given directory does not exist')
                    
    elif event == '-FILE LIST-' and files_lst_window == True:
        window_output.update('')
        window_warning.update('NO WARNING')
        

        filepath = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
        string = values['-INPUT-']


        # get lines that the given string appears in the txt file
        lines_found_lst, file_len = get_lines_the_given_string_appears(filepath, string, matchcase_checkbox_flag, re_checkbox_flag) 


        # check if the length of the file is one line long
        if file_len == 1:
            window_warning.update('WARNING: the whole text file is one line long')
        
        # print the found lines on the output window
        window_output.update(lines_found_lst)