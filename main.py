# string_formatting_examples.py

def main():
    # Introduction to String Formatting
    def intro():
        print("1. Intro to String Formatting, both literals and methods")
        print("String formatting allows you to create dynamic strings by inserting values into placeholders(variables and dictionaries).")
    # intro()

    def fmtMethod():
        # Basic String Formatting using the formatting method
        name = "John"
        age = 25
        formatted_string_1 = "Hello, my name is {} and I am {} years old.".format(name, age)
        print(formatted_string_1)
    # fmtMethod()

    def fmtString():
        # F-string 
        amount = 45.67
        formatted_string_2 = f"The total amount is ${amount:.2f}"
        print(formatted_string_2)
    # fString()
    
    def specPositions():
        # Specifying Positions
        item1 = "apple"
        item2 = "banana"
        formatted_string_3 = "I like {1} more than {0}".format(item1, item2)
        print(formatted_string_3)
    # specPositions()

    def placeHolders():
        # Named placeholders, needs to be a dict variable
        person = {"name": "Alice", "age": 30}
        formatted_string_4 = "My name is {name} and I am {age} years old.".format(**person) #selects all objects, and their values, inside the dict
        print(formatted_string_4)
    # placeHolders()




if __name__ == "__main__":
    main()
