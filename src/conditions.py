import re


def check_string_exists_in_file(filepath, text):
    
    file = open(filepath, "r") 
    
    file_read = file.read().casefold()
    
    counter = file_read.count(text.casefold())

    if counter >= 1:
        return 1
    
    return 0


def get_lines_the_given_string_appears(filepath, text, re_checkbox=False):
    
    file_read = open(filepath, "r")
    
    lines = file_read.readlines()

    
    new_list = []
    counter = 0


    if re_checkbox == False:

        for line in lines:
            counter += 1
            if text.casefold() in line.casefold():
                new_list.append(f"Line {counter}: {line}")
    else:
        for line in lines:
            counter += 1

            pattern_exists = re.search(text, line)
            if pattern_exists:
                new_list.append(f"Line {counter}: {line}")


    # close file
    file_read.close()

    return new_list, len(lines)
