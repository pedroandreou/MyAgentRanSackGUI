# import files
import window_setup
import conditions

# import libs
import PySimpleGUI as sg
import os


# create the Window
window = sg.Window('Search for a string in a specific directory', window_setup.layout(), background_color='black', finalize=True)


# list to append the files that contain the given string
files_lst = []

# create list to append the lines that the given string appears in a specific txt file
lines_found_lst = []

# boolean for checking if there is no file in the given dir
no_file = True

# boolean for checking if the regular expression checkbox is ticked
re_checkbox_flag = False


# event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
              
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

            if values['-RE-'] == True:
                re_checkbox_flag = True
            else:
                re_checkbox_flag = False
            
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"): 
                    filepath = os.path.join(folder_path, filename).replace("\\","/")
                    string = values['-INPUT-']    

                    if conditions.check_string_exists_in_file(filepath, string, re_checkbox_flag) == 1:
                        files_lst.append(filename)
                        window_files.update(files_lst)
                        no_file = False

            if no_file == True:
                window_warning.update('WARNING: no file exists')
        else:
            window_warning.update('WARNING: the given directory does not exist')
            continue
                    
    elif event == '-FILE LIST-':
        
        # empty windows
        window_output.update('')
        window_warning.update('NO WARNING')

        filepath = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])

        # check if the checbox is ticked and a regular expression is given
        string = values['-INPUT-']
        if values['-RE-'] == True:
            lines_found_lst, file_len = conditions.get_lines_the_given_string_appears(filepath, string, re_checkbox=True)
                
        else: 
            # get lines that the given string appears in the txt file
            lines_found_lst, file_len = conditions.get_lines_the_given_string_appears(filepath, string, re_checkbox=False) 


        # check if the length of the file is one line long
        if file_len == 1:
            window_warning.update('WARNING: the whole text file is one line long')

        window_output.update(lines_found_lst)
    
    
window.close()