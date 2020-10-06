from random import choice

def get_file_lines(filename):
    infile_name = filename
    infile = open(infile_name, "r")
    output = infile.readlines()
    return output

def lines_printed_backwards(lines_list):
    output = ""
    lines = get_file_lines("poetry/poem.txt")
    i = len(lines)
    while i != 0:
        output += f"{i} {lines[i - 1]}"
        i -= 1
    return output
test1 = lines_printed_backwards("poetry/poem.txt")
print(test1)

def lines_printed_random(lines_list):
    output = ""
    lines = get_file_lines("poetry/poem.txt")
    i = len(lines)
    while i != 0:
        output += f"{i} {choice(lines)}"
        i -= 1
    return output
test2 = lines_printed_random("poetry/poem.txt")
print(test2)

def lines_printed_custom(lines_list):
    output = ""
    lines = get_file_lines("poetry/poem.txt")
    i = 0
    while i <= len(lines):
        if i % 2 == 0: # within this def I choose to only print out the even numbered lines within a given poem
            output += f"{i} {lines[i - 1]}"  
        i += 1
    return output
test3 = lines_printed_custom("poetry/poem.txt")
print(test3)
    

