import re


def check_string(file_read, text, pattern=False):

    if pattern == False:        
        try:
            # check if the text is the first or last word of the file
            if file_read.split(" ",1)[0] == text or file_read.split(" ")[-1] == text:
                return True
        except IndexError:
            return False
        
        # check if the text is part of the file
        if not file_read.find(' ' + text + ' ') == -1:
                return True
                
    else:
        # check if the text is the first or last word of the file
        if re.search('^' + text + '$', file_read.split(" ",1)[0]) is not None or re.search('^' + text + '$', file_read.split(" ")[-1]) is not None:
            return True
        # check if the text is part of the file
        elif re.search(' ' + text + ' ', file_read) is not None:
            return True


    return False


def check_string_exists_in_file(filepath, text, matchcase_checkbox=False, re_checkbox=False):
    
    file = open(filepath, "r")
    file_read = file.read().replace('\n', ' ')

    exists = False

    # case-insensitive
    if matchcase_checkbox == False:
        # no pattern given
        if re_checkbox == False: 
            exists = check_string(file_read.lower(), text.lower())
        # pattern given
        else:
            exists = check_string(file_read.lower(), text.lower(), pattern=True)
    # case-sensitive
    else:
        # no pattern given
        if re_checkbox == False:
            exists = check_string(file_read, text)
        # pattern given
        else:
            exists = check_string(file_read, text, pattern=True)


    return exists