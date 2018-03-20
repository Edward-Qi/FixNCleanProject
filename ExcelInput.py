import os.path
def callfile():
    print("What file would you lke to sort?")
    callfile_run = True    # Variable Controlling the input check loop

    # This loop runs if the user's input is invalid
    while callfile_run == True:

        callfile_choice = input()

        if: callfile_choice.endswith('.xslx') & os.path.exists(callfile_choice)
            callfile_run = False
        else: callfile_run = True
            print('Please try again')


    return callfile_choice
