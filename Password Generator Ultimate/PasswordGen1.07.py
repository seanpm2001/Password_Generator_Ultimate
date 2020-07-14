# start of program
print ("/=======================\\")
print ("| ðŸ”‘  Password generator | ")
print ("| Version 1.07          |")
print ("| By Sean               |")
print ("\\=======================/")
print ("\n\n")
print ("Password options: ")
print ("Character replacement [ID: 1]")
print ("Normal password [ID: 2]")
print ("Keywords [ID: 3]")
print ("Passcode [ID: 4]")
passwordTypeID = int(input("Enter an ID: "))
if (passwordTypeID == 1):
	password = str(input("Enter a password: "))
	if (len(password) >= 7):
		loopCon1 = int(1)
		while (loopCon1 == 1):
			print ("Select characters to replace: ")
			print ("a | replace with @ | ID: A001  |")	
			print ("a | replace with & | ID: A002  |")
			print ("a | replace with % | ID: A003  |")
			print ("A | replace with @ | ID: A001A |")
			print ("A | replace with & | ID: A002A |")
			print ("A | replace with % | ID: A003A |")
			print ("b | replace with [b] | ID: B001  |")
			print ("b | replace with d   | ID: B002  |")
			print ("b | replace with [B] | ID: B003  |")
			print ("B | replace with [b] | ID: B001A  |")
			print ("B | replace with d   | ID: B002A  |")
			print ("B | replace with [B] | ID: B003A  |")
			print ("c | replace with < | ID: C001 |")
			print ("c | replace with © | ID: C002 |")
			print ("c | replace with ¢ | ID: C003 |")
			print ("C | replace with < | ID: C001A |")
			print ("C | replace with © | ID: C002A |")
			print ("C | replace with ¢ | ID: C003A |")
			print ("d | replace with b | ID: D001 |")
			print ("D | replace with D | ID: D001A |")
			print ("e | replace with 3 | ID: E001 |")
			print ("E | replace with 3 | ID: E001A |")
			print ("f |")
			print ("g | replace with")
			print ("h | replace with b | ID: H001 |")
			print ("H | replace with b | ID: H001A |")
			print ("i | replace with ! | ID: I001 |")
			print ("i | replace with l | ID: I002 |")
			print ("I | replace with ! | ID: I001A |")
			print ("I | replace with l | ID: I002A |")
			print ("j |")
			print ("k |")
			print ("l | replace with i | ID: L001 |")
			print ("L | replace with i | ID: L001A |")
			print ("m |")
			print ("n |")
			print ("o | replace with 0 | ID: O001 |")
			print ("o | replace with ° | ID: O002 |")
			print ("O | replace with 0 | ID: O001A |")
			print ("O | replace with ° | ID: O002A |")
			print ("p | replace with q | ID: P001 |")
			print ("P | replace with q | ID: P001A |")
			print ("q | replace with µ | ID: Q001 |")
			print ("Q | replace with O | ID: Q001A |")
			print ("r | replace with ® | ID: R001 |")
			print ("R | replace with ® | ID: R001A |")
			print ("s | replace with $ | ID: S001 |")
			print ("s | replace with z | ID: S002 |")
			print ("s | replace with 8 | ID: S003 |")
			print ("S | replace with $ | ID: S001A |")
			print ("S | replace with z | ID: S002A |")
			print ("S | replace with 8 | ID: S003A |")
			print ("t | replace with + | ID: T001 |")
			print ("T | replace with + | ID: TOO1A |")
			print ("u | replace with µ | ID: UOO1 |")
			print ("U | replace with V | ID: U001A |")
			print ("v | replace with ^ | ID: V001 |")
			print ("V | replace with \/ | ID: V001A |")
			print ("w | replace with m | ID: W001 |")
			print ("W | replace with VV | ID: WOO1A |")
			print ("x | replace with * | ID: X001 |")
			print ("x | replace with + | ID: X002 |")
			print ("X | replace with * | ID: X001A |")
			print ("X | replace with + | ID: X002A |")
			print ("y | replace with ¥ | ID: YOO1 |")
			print ("Y | replace with ¥ | ID: YOO1A |")
			print ("z | replace with s | ID: Z001 |")
			print ("Z | replace with 2 | ID: Z001A |")
			print ("Your current password is: " + str(password))
			IDEnter = str(input("Enter an ID, type CON1 to skip: "))
			if (IDEnter == "A001"):
				password = password.replace("a", "@")
			if (IDEnter == "A002"):
				password = password.replace("a", "&")
			if (IDEnter == "A003"):
				password = password.replace("a", "%")
			if (IDEnter == "A001A"):
				password = password.replace("A", "@")
			if (IDEnter == "A002A"):
				password = password.replace("A", "&")
			if (IDEnter == "A003A"):
				password = password.replace("A", "%")
			if (IDEnter == "B001"):
				password = password.replace("b", "[b]")
			if (IDEnter == "B002"):
				password = password.replace("b", "d")
			if (IDEnter == "B003"):
				password = password.replace("b", "[B]")
			if (IDEnter == "B001A"):
				password = password.replace("B", "[b]")
			if (IDEnter == "B002A"):
				password = password.replace("B", "d")
			if (IDEnter == "B003A"):
				password = password.replace("B", "[B]")
			if (IDEnter == "C001"):
				password = password.replace("c", "<")
			if (IDEnter == "C002"):
				password = password.replace("c", "©")
			if (IDEnter == "C003"):
				password = password.replace("c", "¢")
			if (IDEnter == "C001A"):
				password = password.replace("C", "<")
			if (IDEnter == "C002A"):
				password = password.replace("C", "©")
			if (IDEnter == "C003A"):
				password = password.replace("C", "¢")
			if (IDEnter == "D001"):
				password = password.replace("d", "b")
			if (IDEnter == "D001A"):
				password = password.replace("D", "D")
			if (IDEnter == "E001"):
				password = password.replace("e", "3")
			if (IDEnter == "E001A"):
				password = password.replace("E", "3")
			if (IDEnter == "CON1"):
				(loopCon1 == 2)
if (passwordTypeID == 4):
		print ("Passcode creator")
		print ("Average passcode length is 4 characters. Max length is 8 characters")
noMore = input("\nPress [ENTER] key to quit")
'''
if (passwordTypeID == 1):
pas1 = str(input("Enter your word: "))
pas2 = int(input("Enter a number: "))
password1 = str(pas1 + str(pas2))
if (len(password1) >= 8):
    password1 = password1.replace("t", "+")
    password1 = password1.replace("T", "+")
    password1 = password1.replace("s", "$")
    password1 = password1.replace("S", "$")
    password1 = password1.replace("e", "@")
    # password1 = password1.replace("E", "3")
    password1 = password1.capitalize()
    print ("Password: " + password1)
else: 
    # print ("(!) Password not long enough")
    print ("Password not long enough.")
'''
'''
ADD FEATURES:
LOG original and modified passwords to a text file
Also save separate capitalized version
'''
# end of program
