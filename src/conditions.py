import re


def check_string_with_no_pattern(file, text, casefold):

    if casefold == True:
        file_read = file.read().casefold()
        counter = file_read.count(text.casefold())
    else:
        file_read = file.read()
        counter = file_read.count(text)


    return file_read, counter


def check_string_with_pattern(file, text, casefold):

    if casefold == True:
        file_read = file.read().casefold()
        counter = len(re.findall(text.casefold(), file_read))
    else:
        file_read = file.read()
        counter = len(re.findall(text, file_read))


    return file_read, counter


def get_lines_with_no_pattern(text, lines, casefold):
        
    new_list = []
    counter = 0

    if casefold == True:
        for line in lines:
            counter += 1

            if text.casefold() in line.casefold():
                new_list.append(f"Line {counter}: {line}")
    else:
        for line in lines:
            counter += 1

            if text in line:
                new_list.append(f"Line {counter}: {line}")
    

    return new_list


def get_lines_with__pattern(text, lines, casefold):
        
    new_list = []
    counter = 0

    if casefold == True:
        for line in lines:
            counter += 1

            pattern_exists = re.search(text.casefold(), line.casefold())
            if pattern_exists:
                new_list.append(f"Line {counter}: {line}")
    else:
        for line in lines:
            counter += 1

            pattern_exists = re.search(text, line)
            if pattern_exists:
                new_list.append(f"Line {counter}: {line}")
    

    return new_list


def check_string_exists_in_file(filepath, text, matchcase_checkbox=False, re_checkbox=False):
    
    file = open(filepath, "r")

    counter = 0
    
    # case-insensitive
    if matchcase_checkbox == False:
        # no pattern given
        if re_checkbox == False: 
            counter = check_string_with_no_pattern(file, text, casefold=True)
        # pattern given
        else:
            counter = check_string_with_pattern(file, text, casefold=True)
    # case-sensitive
    else:
        # no pattern given
        if re_checkbox == False:
            counter = check_string_with_no_pattern(file, text, casefold=False)
        # pattern given
        else:
            counter = check_string_with_pattern(file, text, casefold=False)

    if counter >= 1:
        return 1
    
    
    return 0


def get_lines_the_given_string_appears(filepath, text, matchcase_checkbox=False, re_checkbox=False):
    
    file_read = open(filepath, "r")
    
    lines = file_read.readlines()


    # case-insesitive
    if matchcase_checkbox == False:
        # no pattern given
        if re_checkbox == False:
            new_list = get_lines_with_no_pattern(text, lines, casefold=True)
        # pattern given
        else:
            new_list = get_lines_with__pattern(text, lines, casefold=True)
    # case-sensitive
    else:
        # no pattern given
        if re_checkbox == False:
            new_list = get_lines_with_no_pattern(text, lines, casefold=False)
        # pattern given
        else:
            new_list = get_lines_with__pattern(text, lines, casefold=False)


    file_read.close()

    return new_list, len(lines)
