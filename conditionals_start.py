#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini modified by CE for learning purposes only!
#

# Why is this code below often added to a Python program file?

# if __name__ == "__main__":
#     main()


# It allows us to skip calling the main() function by defining an environment variable.
# It executes the main() function only if this file is executed as the main program.



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    # if x < y:
    #     result = 'x is less than y'
    # elif x == y:
    #     result = 'x is equal to y'
    # else:
    #     result = 'x is greater than y'
    
    # print(result)

    # conditional statements let you use "a if C else b"
    # result = 'x is less than y' if x < y else 'x is greater than or equal to y'
    # print(result)

    # match-case makes it easy to compare multiple values
    value = "eighty five"

    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three":
            result = 3
        case "four" | "five":
            result = (4, 5)
        case _:
            result = -99
    print(result)

if __name__ == "__main__":
    main()
