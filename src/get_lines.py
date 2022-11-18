import re


def get_lines_with_pattern(lines, text, case_insesitive=False):
        
    new_list = []
    counter = 0

    text = '^' + text + '$'

    if case_insesitive == True:
        for line in lines:
            counter += 1

            for i in line.lower().split():
                match = re.search(text.lower(), i)
                if match is not None:
                    new_list.append(f"Line {counter}: {line}")
    else:
        for line in lines:
            counter += 1

            for i in line.split():
                match = re.search(text, i)
                if match is not None:
                    new_list.append(f"Line {counter}: {line}")
    

    return new_list


def get_lines_with_no_pattern(lines, text, case_insesitive=False):
        
    new_list = []
    counter = 0
    
    if case_insesitive == True:
        for line in lines:
            counter += 1

            for i in line.lower().split():
                 if i == text.lower():
                    new_list.append(f"Line {counter}: {line}")
    else:
        for line in lines:
            counter += 1

            for i in line.split():
                 if i == text:
                    new_list.append(f"Line {counter}: {line}")

    return new_list


def get_lines_the_given_string_appears(filepath, text, matchcase_checkbox=False, re_checkbox=False):
    
    file = open(filepath, "r")
    
    lines = file.read().splitlines()


    new_list = []

    # case-insesitive
    if matchcase_checkbox == False:
        # no pattern given
        if re_checkbox == False:
            new_list = get_lines_with_no_pattern(lines, text, case_insesitive=True)
        # pattern given
        else:
            new_list = get_lines_with_pattern(lines, text, case_insesitive=True)
    # case-sensitive
    else:
        # no pattern given
        if re_checkbox == False:
            new_list = get_lines_with_no_pattern(lines, text)
        # pattern given
        else:
            new_list = get_lines_with_pattern(lines, text)


    file.close()

    return new_list, len(lines)
