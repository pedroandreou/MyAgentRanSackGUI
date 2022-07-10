import re


def check_string_exists_in_file(filepath, text, matchcase_checkbox=False, re_checkbox=False):
    
    file = open(filepath, "r")

    file_read = ''
    counter = 0
    
    # case-insensitive
    if matchcase_checkbox == False:
        # no pattern given
        if re_checkbox == False: 
            file_read = file.read().casefold()
            counter = file_read.count(text.casefold())
        # pattern given
        else:
            file_read = file.read().casefold()
            counter = len(re.findall(text.casefold(), file_read))
    # case-sensitive
    else:
        # no pattern given
        if re_checkbox == False:
            file_read = file.read()
            counter = file_read.count(text)
        # pattern given
        else:
            file_read = file.read()
            counter = len(re.findall(text, file_read))

    if counter >= 1:
        return 1
    
    return 0


def get_lines_the_given_string_appears(filepath, text, matchcase_checkbox=False, re_checkbox=False):
    
    file_read = open(filepath, "r")
    
    lines = file_read.readlines()

    
    new_list = []
    counter = 0

    # case-insesitive
    if matchcase_checkbox == False:
        # no pattern given
        if re_checkbox == False:
            for line in lines:
                counter += 1

                if text.casefold() in line.casefold():
                    new_list.append(f"Line {counter}: {line}")
        # pattern given
        else:
            for line in lines:
                counter += 1

                pattern_exists = re.search(text.casefold(), line.casefold())
                if pattern_exists:
                    new_list.append(f"Line {counter}: {line}")
    # case-sensitive
    else:
        # no pattern given
        if re_checkbox == False:
            for line in lines:
                counter += 1

                pattern_exists = re.search(text, line)
                if pattern_exists:
                    new_list.append(f"Line {counter}: {line}")
        # pattern given
        else:
            for line in lines:
                counter += 1

                pattern_exists = re.search(text, line)
                if pattern_exists:
                    new_list.append(f"Line {counter}: {line}")


    file_read.close()

    return new_list, len(lines)
