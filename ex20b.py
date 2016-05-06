# imports argv (argument variable) from the sys module
from sys import argv
# assigns the variables script and input_file to the argument variables (unpacks)
script, input_file = argv
# defines the function "print_all" which takes a function variable f and prints it.
def print_all(f):
# calls the read function on f and prints it
	print f.read()
# defines the function "rewind" which changes the position of the file to the beginning. 	
def rewind(f):
	f.seek(0)

# defines the function "print_a_line'" with multiple arguments "line_count and f"
def print_a_line(line_count, f):
# prints the result of line_count followed by f
	print line_count, f.readline()
# assigns the variable current_file to open the input_file from argv	
current_file = open(input_file)
# prints out text
print "First let's print the whole file:\n"
# prints out the variable current_file
print_all(current_file)
# prints out text
print "Now let's rewind, kind of like a tape."
# moves to the beginning of current_file
rewind(current_file)
# prints text
print "Let's print three lines:"
# assigns the number 1 to the variable current_line 
current_line = 1
# executes the function on the argument variables which are now current_line=1 and the file.
print_a_line(current_line, current_file)
# sets current_line to 2
current_line += 1
# executes print_a_line again this time it was display the next line which is 2 
print_a_line(current_line, current_file)
# sets current_line to 3
current_line += 1
# executes print_a_line again this time it was display the next line which is 3
print_a_line(current_line, current_file)
