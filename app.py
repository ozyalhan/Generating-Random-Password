import string
import random


# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
LETTERS = string.ascii_letters

# 0123456789
NUMBERS = string.digits

# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
PUNCTUATION = string.punctuation


def get_password_lenght():
    """
    Retrieves the lenght of password between 8 and 64
    :returns number <class 'int'>
    """
    try:

        # Get the user input and convert it to integer value.
        lenght = int(
            input("How long do you want your password?\n[between 8-64]: "))

    except ValueError:

        # If the value is not numeric, error message will prompt and function will call again.
        print("\n--------\nERROR: Please enter a numberic value.")
        get_password_lenght()

    else:

        # If everything is under desired circumstances, lenght value as integer will be returned.
        if lenght >= 8 and lenght <= 64:
            # print("you choose " + str(lenght)) #for debuggin purposes
            return lenght

        else:
            # If the value is not between 8 and 64, error message will prompt and function will call again.
            print("\n--------\nERROR: Choose a value between 8 and 64.")
            get_password_lenght()


def password_combination_selection():
    """
    Prompt a user to choose password combination which
    could be digits, letters, punctuation or combination of
    either of them.
    :returns list <class 'list'>, example: [True,True,False]
            0 item ---> digit choice
            1 item ---> letter choice
            2 item ---> punctuation choice
    """
    # return list retrieve a user's password character combination choice
    selection_list = []

    # user response for digits <class 'bool'>
    digits_answer_bool = digits_wants()
    selection_list.append(digits_answer_bool)

    # user response for letters <class 'bool'>
    letters_answer_bool = letters_wants()
    selection_list.append(letters_answer_bool)

    # user response for punctuations <class 'bool'>
    punctuations_answer_bool = punctuations_wants()
    selection_list.append(punctuations_answer_bool)

    if True not in selection_list:
        print("\n--------\nERROR: All selections cant be no.")
        return password_combination_selection()
    return selection_list


def digits_wants():
    """
    Get user input and decide for return value
    Check that it matchs as 'y' or 'yes' to True, 'n' or 'no" to False,
    If none of them function call again.

    :returns boolean <class 'bool'>.
    """

    response = str(input("Do you want digits ? (yes or no) : ")
                   ).lower().strip()

    if response == "y" or response == "yes":
        return True
    elif response == "n" or response == "no":
        return False
    else:
        print("\n--------\nERROR: Please anwer the questions yes or no.")
        return digits_wants()  # WOW, returnig the function I have never thought!!!!!!!!!!!!!!!


def letters_wants():
    """
    Get user input and decide for return value
    Check that it matchs as 'y' or 'yes' to True, 'n' or 'no" to False,
    If none of them function call again.

    :returns boolean <class 'bool'>.
    """

    response = str(input("Do you want letters ? (yes or no) : ")
                   ).lower().strip()

    if response == "y" or response == "yes":
        return True
    elif response == "n" or response == "no":
        return False
    else:
        print("\n--------\nERROR: Please anwer the questions yes or no.")
        return letters_wants()


def punctuations_wants():
    """
    Get user input and decide for return value
    Check that it matchs as 'y' or 'yes' to True, 'n' or 'no" to False,
    If none of them function call again.

    :returns boolean <class 'bool'>.
    """

    response = str(
        input("Do you want punctuations ? (yes or no) : ")).lower().strip()

    if response == "y" or response == "yes":
        return True
    elif response == "n" or response == "no":
        return False
    else:
        print("\n--------\nERROR: Please anwer the questions yes or no.")
        return punctuations_wants()


def password_generator(string_constant_password, length=8):
    """
    Generates a random password having the specified length
    : selection_list list includes respectively boolean values of digits, letters, punctuations 
    : lenght -> lenght of password to be generated. Defaults to 8 if nothing is specified
    : return string < class 'str' >
    """

    # password <str>, return value
    password = ""

    # convert string_constant_password from string to list and shuffle
    string_constant_password_list = list(string_constant_password)
    random.shuffle(string_constant_password_list)

    # generate random password
    password = random.choices(string_constant_password_list, k=length)

    # convert generated password to string
    password = ''.join(password)
    return password


def fetch_string_constant(selection_list):
    '''
    Returns a string constant based on users selection_list.
    string constant can either be digits, letters, punctuation or
    combination of them.
    : selection_list -> list <class 'list'> of boolean
            0 item --> digits    
                    True to add digits to constant False otherwise
            1 item --> letters   
                    True to add letters to constant False otherwise
            2 item --> punctuation
                    True to add punctuations to constant False otherwise
    '''
    string_constant = ""

    string_constant += NUMBERS if selection_list[0] else ""
    string_constant += LETTERS if selection_list[1] else ""
    string_constant += PUNCTUATION if selection_list[2] else ""

    return string_constant


def work_again():
    """
    Asks to user for reuse the program
    if yes, main function will call
    if no, terminate_program function will call
    """
    try:
        "w_quest <str> : should be y,yes,yeah,n,no,nope"
        w_quest = input(
            "Do you want to generate password again?\n(yes or no): ").lower()

    except ValueError as e:
        print("Wrong Input Value. Error: " + str(e))
        work_again()

    else:
        if w_quest == "y" or w_quest == "yes" or w_quest == "yeah":
            main()
        elif w_quest == "n" or w_quest == "no" or w_quest == "nope":
            terminate_program()
        else:
            print("\nPlease answer the question with yes or no.")
            work_again()


def terminate_program():
    """Terminates the program"""
    print("\nThank you and goodbye.")
    exit()


def main():
    """Runs main function"""

    length = get_password_lenght()
    print("log: lenght: " + str(length))  # for debugging

    selection_list = password_combination_selection()
    print("log: selection_list: ")  # for debugging
    print(selection_list)  # for debugging

    string_constant_password = fetch_string_constant(selection_list)
    print("log: string_constant_password: " +
          string_constant_password)  # for debugging

    password = password_generator(string_constant_password, length)
    print(password)

    work_again()


if __name__ == '__main__':
    main()
