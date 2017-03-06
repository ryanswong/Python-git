shopping_list = [] # pylint: disable=locally-disabled, invalid-name

def invalid_input():
    
    print "That\'s not a valid answer, try again. "

def print_list():

    print '\n' + 'Grocery List: [' + ', ' .join(shopping_list) + ']' '\n'

def appender():
    response = raw_input("What item do you want to add to your list?" + '\n')
    if len(response) > 0:
        shopping_list.append(response)
    else:
    	invalid_input()

def deleter():
    '''this code if to delete items from the list'''
    response = raw_input("what item do you want to DELETE from your list?"\
						" type name, or the position number" + '\n')

    if  (response.isalpha()) and (response in shopping_list):
        item_index = shopping_list.index(response)
        shopping_list.pop(item_index)
        print shopping_list
    elif (response.isalpha()) and (response not in shopping_list):
        invalid_input()
        deleter()
    elif  type(int(response)) == int and (0 < int(response) <= len(shopping_list)):
        item_index = response
        shopping_list.pop(int(item_index) - 1)
        print shopping_list
    else:
        invalid_input()
        deleter()

def del_empty():
    y_n = raw_input("Do you want to delete an item (type 1)," \
					" or empty the entire list (type 2)?" + '\n')
    if y_n == "1":
        deleter()
        print_list()
        modify_list()
    if y_n == "2":
        y_n = raw_input("Are you sure you want to delete the whole list?" + '\n')
        if y_n == "y":
            del shopping_list[:]
            print_list()
            make_list()
        elif y_n == "n":
            modify_list()

def modify_list():
    y_n = raw_input("Do want want to add another item? " \
    	"Reply with y for yes, and n if you want to delete" + '\n')
    if y_n == "y":
        appender()
        print_list()
        modify_list()
    elif y_n == "n":
	    del_empty()
    invalid_input()
    modify_list()

def make_list():
    y_n = raw_input("Do you want to make a grocery list? Reply with y or n" + '\n')
    if y_n == "y":
        appender()
        print_list()
        modify_list()
    invalid_input()
    make_list()

make_list()


