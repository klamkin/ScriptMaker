import os
isThere = True

# Creates the scripts folder if not already there
if not os.path.exists('scripts'):
    os.makedirs('scripts')

# Declaring the array used to store the values
arr = []

# Method to filter out any non numeric chars
def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

code = ''

# Print out of instructions 
print ('Script Builder - Kyle Lamkin')
print ('\n')
print ('Instructions \n')
print ('1. Enter a name for your script (Be sure to be descriptive)')
print ('2. Copy output (ctrl + c) from desired game in EGM commander \n')
print ('3. Paste into this program (ctrl + v) \n')
print ('4. Hit Enter \n')
print ('5. Type "q" and hit Enter \n')
print ('NOTE - Remember to rename your script to something descriptive \n')

# Asking for a name for the file to be created
name = input('Please enter a name for your script: \n')

# While loop continues until a name has been entered that does not match an existing file
while (isThere):
	if os.path.isfile("scripts/" + name + ".script"):
		isThere = True
		print ("That name already exists, Please choose a different name")
	else:
		isThere = False
		
	

print ('Paste output here: ' + '\n')

# The while loop that accepts input for the script
while (code != 'q'):
	code = input()
	
	# If the input is 'q' then the program ends and compiles the script
	if code != 'q':
		code = only_numerics(code)
		arr.append(code)
	
	# This pops off any blank lines in the array. This can happen when a line with no numeric chars is entered.
	if not code:
		arr.pop()
#Attempts to write to a file	
try:
	f= open("scripts/" + name + ".script","w+")	

	f.write("rng vals" + "\n")
	f.write("\n")


	f.write("1" + "\n")
	f.write(str(len(arr)) + "\n")
	for i in range(len(arr)):
		f.write("1" + "\n")
	f.write("\n")

	for i in range(len(arr)):
		f.write(str(arr[i]) + "\n")

	f.write("deal")

	f.close()
	print('Script Created')
except:
	print('Something went wrong sorry!')


code = input()