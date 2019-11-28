import pkgutil
import importlib
from inspect import getmembers, isfunction, isclass, ismethod
import sys



while True:
    try: 
        filename = input("Enter filename: ")

        if (filename[-3:] == ".py"):
            filename = filename[:-3]


        my_module = importlib.import_module(filename)
        break
    except:
        print("\nFile does not exist. Try again.")
        continue



functions_list = [o[0] for o in getmembers(my_module) if isfunction(o[1])]

class_list = [o[0] for o in getmembers(my_module) if isclass(o[1],)]


while True:

    while True:

        try:
            import_name = input(
                    "\n\nTo start the test, type your function or class name from the lists below (to end the program type exit): \n \n ****** \n \nFunctions: {} \n Classes: {} \n \n ****** \n \nName the function or class: ".format(functions_list,class_list)
            )

            if (import_name == "exit"):
                sys.exit(0)

            method_to_call = getattr(my_module, import_name)
            break

        except Exception as error:
            print("Invalid function. Try again.")
            continue



    f_input_split = None
    f_input_eval = None


    if (isclass(method_to_call)):



        while True:

            try:
                c_input = input(
                    "\n \nInsert inputs for the instance of your class separated by semicolon as a1;a2;...;an e.g. for f = foo(1,\"hello\") insert 1;\"hello\": ")

                c_input_split = c_input.split(";")
                c_input_eval = [eval(i) for i in c_input_split]


                printed_input= str(c_input_eval)[1:-1]

                check_input = input("\n \nIs the following input correct?  \n \n ****** \n \n f = {}({})  \n \n ****** \n \ny o n: ".format(import_name,
                    printed_input))
                if (check_input == "y" or check_input == "yes"):
                    try:

                        test_instance = method_to_call(*c_input_eval)
                        break

                    except: 
            
                    print("\n\nERROR: Possibly wrong number of inputs or input types. Retry.")
                    continue

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
                list_of_methods = [o[0] for o in getmembers(test_instance) if ismethod(o[1],)]
                submethod_name = input("\n \nInsert the name of the method to test. \n\n****\n\nList of methods: {}\n\nName of the method:".format(list_of_methods))

                if submethod_name not in list_of_methods:
                    print("\nMethod not exists. Try again.")
                    continue

                else: 

                    submethod = getattr(test_instance, submethod_name)

                break
                    
            except ValueError:
                print("\nInvalid name. Try again.")
                continue


        while True:

            try:
                f_input = input(
                    "\n \nInsert inputs for the method of your class separated by semicolon as a1;a2;...;an e.g. for f.{}(1,\"hello\") insert 1;\"hello\". If there is no input press enter: ".format(submethod_name))

                if len(f_input) != 0:


                    f_input_split = c_input.split(";")
                    f_input_eval = [eval(i) for i in f_input_split]


                    printed_input= str(f_input_eval)[1:-1]
                else:

                    printed_input = ""
                    f_input_eval = []


                check_input = input("\n \nIs the following input correct?  \n \n ****** \n \n f.{}({})  \n \n ****** \n \ny o n: ".format(submethod_name,
                    printed_input))
                if (check_input == "y" or check_input == "yes"):

                    if (len(f_input) == 0):
                        result = submethod()
                        break
                    elif (len(f_input) > 0):
                        result = submethod(*f_input_eval)
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
                f_output = eval(input("\n \nInsert your expected output. If the function is not returning anything insert None: "))
                break
            except:
                print("\nInvalid output. Try again.")
                continue


        print("\nClass instance internal variables: ")
        print(vars(test_instance))


        if (result == f_output):
            print("\n \n******* Success!. Your function output: " + str(result))

        else:
            print("\n \n******* Failed. Your function output: " + str(result))

        reset = input("\nTest again? y or n: ")
        if (reset== 'y' or reset == 'yes'):
            continue
        else:
            break


    elif (isfunction(method_to_call)):
        while True:
            
            f_input = input(
                "\n \nInsert your inputs in separated by semicolon as a1;a2;...;an : ")


            if len(f_input) != 0:


                f_input_split = f_input.split(";")
                f_input_eval = [eval(i) for i in f_input_split]


                printed_input= str(f_input_eval)[1:-1]
            else:

                printed_input = ""
                f_input_eval = []

            check_input = input("\n \nIs the following input correct?  \n \n ****** \n \n {}({})  \n \n ****** \n \n y o n: ".format(import_name,
                printed_input))
            if (check_input == "y" or check_input == "yes"):

                try:

                    if len(f_input) == 0:

                        test_output = method_to_call()

                    else:

                        test_output = method_to_call(*f_input_eval)
                        break

                except: 
        
                    print("\n\nERROR: Possibly wrong number of inputs or input types. Retry.")
                    continue


        while True:
            try:
                f_output = eval(input("\n \nInsert your expected output. If the function is not returning anything insert None: "))
                break
            except:
                print("\nInvalid output. Try again.")
                continue



        if (test_output == f_output):
            print("\n \n******* Success!. Your function output: " + str(test_output))

        else:
            print("\n \n******* Failed. Your function output: " + str(test_output))

        reset = input("\nTest again? y or n: ")
        if (reset== 'y' or reset == 'yes'):
            continue
        else:
            break

print("Test finished.")