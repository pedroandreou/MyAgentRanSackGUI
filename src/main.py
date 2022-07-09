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


# event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
              
    elif event == 'OK':
        folder_path = values['-FOLDER-']
        
        # empty windows
        files_lst = []
        window['-FILE LIST-'].update(files_lst)
        window['-OUTPUT-'].update('')
        window['-WARNING-'].update('NO WARNING')
    
        
        # check the directory exists if it the directory was entered manually
        if os.path.isdir(folder_path) == True:
            
            no_file = True
            
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"): 
                    filepath = os.path.join(folder_path, filename).replace("\\","/")
                    string = values['-INPUT-']    
                    
                    if conditions.check_string_exists_in_file(filepath, string) == 1:   
                        files_lst.append(filename)
                        window['-FILE LIST-'].update(files_lst)
                        no_file = False
                        
            if no_file == True:
                window['-WARNING-'].update('WARNING: no file exists')
        else:
            window['-WARNING-'].update('WARNING: the given directory does not exist')
            continue
                    
    elif event == '-FILE LIST-':
        
        # empty windows
        window['-OUTPUT-'].update('')
        window['-WARNING-'].update('NO WARNING')
        
        # get lines that the given string appears in the txt file
        filepath = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
        lines_found_lst, file_len = conditions.get_lines_the_given_string_appears(filepath, values['-INPUT-']) 
        
        
        if file_len == 1:
            window['-OUTPUT-'].update(lines_found_lst)
            window['-WARNING-'].update('WARNING: the whole text file is one line long')
        else:
            window['-OUTPUT-'].update(*lines_found_lst)

    
    
window.close()