arr = []

def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

code = ''
print ('Script Builder - Kyle Lamkin')
print ('\n')
print ('Instructions \n')
print ('1. Copy output (ctrl + c) from desired game in EGM commander \n')
print ('2. Paste into this program (ctrl + v) \n')
print ('3. Hit Enter \n')
print ('4. Type "q" and hit Enter \n')
print ('NOTE - Remember to rename your script to something descriptive \n')
print ('Paste output here: ' + '\n')
while (code != 'q'):
	code = input()
	if code != 'q':
		code = only_numerics(code)
		arr.append(code)
	if not code:
		arr.pop()
	
try:
	f= open("RenameMeToSomethingUsefulAndNotAsLong.script","w+")	

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