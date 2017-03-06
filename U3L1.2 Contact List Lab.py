
contact_list = []

new_contact = []


def contact():
	y_n = raw_input("Do you want to add a new contact?"
		" Reply with y for yes, and n if you want to delete" + '\n')
	if y_n == "y":
		add_contact()
		print "1: " + str(contact_list)
		
		#print "after del" + str(new_contact)
	if y_n == "n":
		delete_contact()

	elif y_n != "y" or "n":
		invalid_input()
		
	print "conatct_list = " + str(contact_list) 
	contact()


def add_contact():
	info() 
	contact_list.extend(new_contact)
	del new_contact[:]


def info():
    first = raw_input("What is your first name?" + '\n')
    last = raw_input("What is your last name?" + '\n')
    phone_number = raw_input("What your phone number?" + '\n')
    new_contact.append(first + " " + last + " #: " + phone_number)
    


def delete_contact():
	print contact_list
	response = raw_input("which contact do you want to DELETE from your contacts?"\
					" type the position of the name" + '\n')
	
	if type(int(response)) == int and (0 < int(response) <= len(contact_list)):
		#print "before pop" + str(contact_list)
		contact_list.pop(int(response) - 1)
	else:
		invalid_input()
		delete_contact()
		print contact_list


def invalid_input():
    print "That\'s not a valid input, try again. "


contact()
# pass by ref and fun parameters/arguments
