# [2015-09-14] Challenge #232 [Easy] Palindromes
# Place input in file named 'input'

def make_one_string(list_of_lines):
	single_line = ''
	for i in range(len(list_of_lines)):
		single_line += list_of_lines[i]

	return single_line

def remove_non_letters(string):
	just_alpha = ''	
	for character in string:
		if (character.isalpha()):
			just_alpha += character.lower()
	return just_alpha

def palindrome(string):
	if (len(string) == 1 or (len(string) == 2 and string[0] == string[1])):
		return 'Palindrome'
	elif (string[0] == string[len(string) - 1]):
		return palindrome(string[1:len(string)-1])
	else:
		return 'Not a palindrome'

f = open('input', 'r')

number_of_lines = int(f.readline())

lines = []

for i in range(number_of_lines):
	lines.append(f.readline())

for i in range(len(lines)):
	# Deletes newline
	lines[i] = lines[i][:-1]

string = make_one_string(lines)

string = remove_non_letters(string)

# print string

print palindrome(string)
