import pkgutil
import importlib
from inspect import getmembers, isfunction
import sys
filename = input("Enter filename: ")

if (filename[-2:] == ".py"):
    filename = filename[:-2]

my_module = importlib.import_module(filename)

modualList = []
functions_list = [o[0] for o in getmembers(my_module) if isfunction(o[1])]


while True:

    while True:

        try:
            f_name = input(
                    "\n\nTo start the test, type your function name from the list of available functions (to end the program type exit): \n \n ****** \n \n {}  \n \n ****** \n \n Name the function: ".format(functions_list)
            )

            if (f_name == "exit"):
                sys.exit(0)

            method_to_call = getattr(my_module, f_name)
            break

        except Exception as error:
            print("Invalid function. Try again.")
            continue



    f_input_split = None
    f_input_eval = None

    while True:

        try:
            f_input = input(
                "\n \nInsert your inputs in separated by semicolon as a1;a2;...;an : ")

            f_input_split = f_input.split(";")
            f_input_eval = [eval(i) for i in f_input_split]


            printed_input= str(f_input_eval)[1:-1]

            check_input = input("\n \nIs the following input correct?  \n \n ****** \n \n {}({})  \n \n ****** \n \n y o n: ".format(f_name,
                printed_input))
            if (check_input == "y" or check_input == "yes"):
                break
            else:
                print("Retry")
                continue

        except ValueError:
            print(
                "\nInvalid format. Separate each variable by semicolon character -> ; e.g. 3;4;5;6"
            )
            continue

    while True:

        try:
            f_output = eval(input("\n \nInsert your expected output:"))
            break
        except ValueError:
            print("\nInvalid output. Try again.")
            continue

    test_output = method_to_call(*f_input_eval)

    if (test_output == f_output):
        print("\n \n******* Success!. Your function output: " + str(test_output))

    else:
        print("\n \n******* Failed. Your function output: " + str(test_output))

    reset = input("\nTest another function? y or n: ")
    if (reset== 'y' or reset == 'yes'):
        continue
    else:
        break

print("Test finished.")
