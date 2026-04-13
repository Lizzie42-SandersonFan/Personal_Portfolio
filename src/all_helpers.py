# Helper functions
import time
import os
import re

def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

# function that will check if the passed in time is greater than 24. If it is, get it back down to proper time and update the day
def check_time(time):
    if time > 24:
        time = time % 24
        # Returning 1 because it will tell me to add one to the day
        return 1
    elif time < 0:
        # This should not happen. Returning 0
        return 0
    else:
        time = time
        return 0
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_number(string_check):
    if string_check.isdigit() == True:
        return True, int(string_check)
    else:
        return False

def is_valid_hexa_code(string):
    hexa_code = re.compile(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')
    return bool(re.match(hexa_code, string))

def get_midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)