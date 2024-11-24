def get_lst():
    lst = []  # Initialize an empty list
    elem = input("Enter the element or press enter to stop: ")  # Get the first input
    
    while elem != "":  # Loop continues until the user presses enter without typing anything
        lst.append(elem)  # Add the input to the list
        elem = input("Enter the element or press enter to stop: ")  # Ask for the next input
    
    return lst  # Return the list

def get_first_elem(lst):
    print(f"The first element of the list is: {lst[0]}")  # Print the first element

def main():
    lst = get_lst()  # Get the list from the user
    get_first_elem(lst)  # Print the first element of the list

if __name__ == "__main__":
    main()  # Call the main function to start the program
