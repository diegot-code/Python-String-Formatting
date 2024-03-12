# string_formatting_examples.py

def main():
    # Introduction to String Formatting
    print("1. Introduction to String Formatting")
    print("String formatting allows you to create dynamic strings by inserting values into placeholders.")

    # Example 1: Basic String Formatting
    name = "John"
    age = 25
    formatted_string_1 = "Hello, my name is {} and I am {} years old.".format(name, age)
    print("Example 1:", formatted_string_1)

    # Example 2: F-string (Python 3.6+)
    amount = 45.67
    formatted_string_2 = f"The total amount is ${amount:.2f}"
    print("Example 2:", formatted_string_2)

    # Example 3: Specifying Positions
    item1 = "apple"
    item2 = "banana"
    formatted_string_3 = "I like {1} more than {0}".format(item1, item2)
    print("Example 3:", formatted_string_3)

    # Example 4: Named placeholders
    person = {"name": "Alice", "age": 30}
    formatted_string_4 = "My name is {name} and I am {age} years old.".format(**person)
    print("Example 4:", formatted_string_4)


if __name__ == "__main__":
    main()
