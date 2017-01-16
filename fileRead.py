#!/usr/bin/env python3
file_name = 'English_Dictionary_Full.txt'

# this function checks to see if the chosen word exists in the file
def checkPWD1(pwd, full_filename):
    try:
        text_file = open(full_filename, 'r')
        for line in text_file:
            if line.lower().strip('\n') == pwd.lower():
                return True
        return False
    finally:
        text_file.close()

def checkPWD2(pwd,full_filename):
    import mmap
    try:
        text_file = open(full_filename, 'rb', 0)
        s = mmap.mmap(text_file.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(pwd.encode()) != -1:
            return True
        return False
    finally:
        text_file.close()

def checkmmap_exists():
    try:
        import mmap
        return True #Module is installed
    except ImportError:
        return False #There is no such module installed


print(checkPWD1('help',file_name))
print(checkPWD2('help',file_name))
