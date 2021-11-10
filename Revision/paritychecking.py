practice = input("do you want to practice parity checking?")
while practice in ["yes","Yes","YES"]:
	

	choice = input("which parity do you want to practice? odd/even: ")
	answer = ""
	import random
	key = ""
	for i in range(7):
		temp = str(random.randint(0, 1))
		key += temp


	parity = [char for char in key]
	print(parity)
	one = ["1"]
	zero = ["0"]
	totalone = 0
	totalzero = 0
	num = len(parity)
	for i in range(num):
		if parity[i] in one:
			totalone = totalone+1
		elif parity[i] in zero:
			totalzero = totalzero+1

	if choice == "odd":
   	 if totalone != [0, 2, 3, 6, 8]:
   	 	answer = "1"
   	 elif totalone in [0, 2, 3, 6, 8]:
   	 	answer = "0"

	if choice == "even":
   	 if totalone != [0, 2, 3, 6, 8]:
   	 	answer = "1"
   	 elif totalone in [0, 2, 3, 6, 8]:
   	 	answer = "0"

	useranswer = input("what is the parity digit?: ")
	if useranswer == answer:
   	 print("you are right")
	else:
   	 print("you are wrong. the answer is", answer)
   	
	practice = input("do you want to continue practicing?")
