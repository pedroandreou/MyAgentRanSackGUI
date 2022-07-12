# import files
import window_setup
import conditions

# import libs
import PySimpleGUI as sg
import os


# start off with 1 window open
window1, window2 = window_setup.make_win1(), None


files_lst = []                  # list to append the files that contain the given string
lines_found_lst = []            # create list to append the lines that the given string appears in a specific txt file
no_file = True                  # boolean for checking if there is no file in the given dir
matchcase_checkbox_flag = False # boolean for checking if the matchcase checkbox is ticked
re_checkbox_flag = False        # boolean for checking if the regular expression checkbox is ticked


# event loop 
while True:
    window, event, values = sg.read_all_windows()

    # get values of the second window
    second_window_vals = {}
    
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
        folder_path = values['-FOLDER-']
        
        # get windows
        window_files = window['-FILE LIST-']
        window_output = window['-OUTPUT-']
        window_warning = window['-WARNING-']

        # empty windows
        files_lst = []
        window_files.update(files_lst)
        window_output.update('')
        window_warning.update('NO WARNING')
    
        
        # check the directory exists if it the directory was entered manually
        if os.path.isdir(folder_path) == True:
            no_file = True
            
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"): 
                    filepath = os.path.join(folder_path, filename).replace("\\","/")
                    string = values['-INPUT-']    

                    if conditions.check_string_exists_in_file(filepath, string, matchcase_checkbox_flag, re_checkbox_flag) == 1:
                        files_lst.append(filename)
                        window_files.update(files_lst)
                        no_file = False

            if no_file == True:
                window_warning.update('WARNING: no file exists')
        else:
            window_warning.update('WARNING: the given directory does not exist')
            # continue
                    
    elif event == '-FILE LIST-':
        
        # empty windows
        window_output.update('')
        window_warning.update('NO WARNING')

        filepath = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
        string = values['-INPUT-']


        # get lines that the given string appears in the txt file
        lines_found_lst, file_len = conditions.get_lines_the_given_string_appears(filepath, string, matchcase_checkbox_flag, re_checkbox_flag) 


        # check if the length of the file is one line long
        if file_len == 1:
            window_warning.update('WARNING: the whole text file is one line long')
        
        # print the found lines on the output window
        window_output.update(lines_found_lst)
    
    
window.close()