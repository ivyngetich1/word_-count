def words(input):

	
	tests = input.split()
	
	occurances ={}
	
	data = set(tests)
	
	
	for word in data:
		count = 0
	
		for i in tests:
	
			if word  == i:
				count = count + 1
				
				if word.isdigit() == True:
						word = int(word)
						
		occurances[word] = count

	return occurances