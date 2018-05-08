arr = []

def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

code = ''

print ('Paste output here: ')
while (code != 'q'):
	code = input()
	if code != 'q':
		code = only_numerics(code)
		arr.append(code)
	if not code:
		arr.pop()
	

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
print(arr)


code = input()