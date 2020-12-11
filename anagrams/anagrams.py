def reverse(input_string):
	try:
		if not isinstance(input_string, str):  # check if input is string; numbers-only is acceptable
			raise TypeError
			return  # removed 'None'
		temp = []
		for word in input_string.split():
			letters = []
			nonletters = []
			for ind, char in enumerate(word):
				if not char.isalpha():
					nonletters.append((ind, char))  # creating tuples of nonletters with indices
				else:
					letters.append(char)  # adding letters to a separate list
			letters.reverse()

			for item in nonletters:
				letters.insert(*item)  # *"unpacking" tuples to provide two args; letters var becomes result string
			temp.append("".join(letters))  # append resulting words one by one, joining chars to strings
		output = " ".join(temp)  # convert list to string
		return output
	except TypeError as err:
		print(f"Type error! String expected. Got {type(input_string)}")
		return (err)


if __name__ == '__main__':
	cases = [
		("abcd efgh", "dcba hgfe"),
		("a1bcd efg!h", "d1cba hgf!e"),
		("", ""),
	]

	for text, reversed_text in cases:
		assert reverse(text) == reversed_text
