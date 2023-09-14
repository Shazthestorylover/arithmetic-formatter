'''
    Author: Shazzam Austin
    Course: Scientific Computing with Python
    Project: Arithmetic Formatter
    Website: FreeCodeCamp.org
    
    Date (Start): March 13, 2023
    Date (End): March 24, 2023
'''

# https://stackoverflow.com/questions/1740726/turn-string-into-operator
import operator
ops = { "+": operator.add, "-": operator.sub } # etc.

DEBUG = False

def arithmetic_arranger(problems, give_ans=False):
    arranged_problems = '' # Used to hold the collection of problems
                        # after they have been joined.

    row_1 = [] # Used to store an array of the first numbers.
    row_2 = [] # Used to store an array of the second numbers.
    row_dashes = [] # Used to store an array of dashes for each equation.
    row_3 = [] # Used to store an array of the answers

    str_1 = '' # Used to store the 1st numbers with 4 spaces between them.
    str_2 = '' # Used to store the 2nd numbers with 4 spaces between them.
    str_dashes = '' # Used to store the dashes for each problem with 4 spaces between them.
    str_3 = '' # Used to store the answers with 4 spaces between them.

    # if the number of problems exceeds 5:
    if len(problems) > 5:
        print('Error: Too many problems')
    
    # For each problem in the list of problems
    for prob in problems:
        # Find the operator in the math problem.
        if "+" in prob:
            op_pos = prob.find("+")
        elif "-" in prob:
            op_pos = prob.find("-")
        elif "*" in prob or "/" in prob:
            print("Error: Operator must be '+' or '-'.")

        #DEBUG
        if DEBUG == True: print(f'\n\nFound operator (+/-) at position: {op_pos} \n')

        # Store the operator for later use.
        op = prob[op_pos]

        # Get both numbers and store them
        num1 = prob[ : op_pos-1]
        num2 = prob[op_pos+2 : ]

        # Check if the numbers are only digits.
        if not num1.isnumeric() or not num2.isnumeric():
            print("Error: Numbers must only contain digits.")
            
        # Remove any whitespaces that the numbers have    
        num1 = num1.rstrip()

        #DEBUG
        if DEBUG == True: 
            print(f'num1: {num1} \n')
            print(f'operator: {op} \n')
            print(f'num2: {num2} \n')

        # Check for the number with the most digits.
        # If the 1st digit is larger than the 2nd digit:
        if len(num1) > len(num2):
            # DEBUG
            if DEBUG == True: print(f'length of num1 > length of num2: {num1} > {num2} \n')

            # Re-formatting numbers into the specified format

            dashed_line = '' # Used to help create the dashed line under each problem.
            len_of_dashes = len(num1)+2 # Used to calculate how long the dashed line should be. 

            length = len(num1)+2 # Used to determine how many spaces the numbers should be right justified by.
                                 # i.e. Same the length of dashes.
            fillchar_1 = f'{op}' # Stores the actual operator.
            fillchar_2 = '-' # Used to create the dashed border under the re-formmatted
                             # equation.
            fillchar_3 = ' ' # Used as padding to right justify the numbers.

            # Do the calculation 
            ans = ops[op]( int(num1),int(num2) )

            row_1.append(num1.rjust(length, fillchar_3))
            row_2.append(fillchar_1+' '+num2.rjust(length-2, fillchar_3))
            row_dashes.append(dashed_line.rjust(len_of_dashes, fillchar_2))
            row_3.append(str(ans).rjust(length, fillchar_3))

            # DEBUG
            if DEBUG == True: print(f'Var type of ans: {type(ans)}')
#------------------------------------------------------------------------------------------------------
        # Otherwise, the 2nd number has more digits than the 1st number.
        else:
            # DEBUG
            if DEBUG == True: print(f'length of num2 > length of num1: {num2} > {num1} \n')

            # Re-formatting numbers into the specified format.

            dashed_line = '' # Used to help create the dashed line under each problem.
            len_of_dashes = len(num2)+2 # Used to calculate how long the dashed line should be.

            length = len(num2)+2 # Used to determine how many spaces the equation should take.
                                 # i.e. Same the length of dashes.
            fillchar_1 = f'{op}' # Stores the actual operator.
            fillchar_2 = '-' # Used to create the dashed border under the re-formmatted
                             # equation.
            fillchar_3 = ' ' # Used as padding to right justify the numbers.

            # Then, do the calculation, and output
            # the answer under the dashed line.
            ans = ops[op]( int(num1),int(num2) )

            row_1.append(num1.rjust(length, fillchar_3))
            row_2.append(fillchar_1+' '+num2.rjust(length-2, fillchar_3))
            row_dashes.append(dashed_line.rjust(len_of_dashes, fillchar_2))
            row_3.append(str(ans).rjust(length, fillchar_3))

            # DEBUG
            if DEBUG == True: print(f'Var type of ans: {type(ans)}')

    # For loops are used to take each number within each array and
    # store them in string variables with 4 spaces between them.
    for el in row_1:
        str_1 += el + '    '
        
    for el in row_2:
        str_2 += el + '    '
        
    for el in row_dashes:
        str_dashes += el + '    '
        
    for el in row_3:
        str_3 += el + '    '

    # If the user asks for an answer:
    if give_ans == True:  
        # Reformat the problem with the answer vertically, and output
        # the answer under the dashed line.
        arranged_problems = str_1 +'\n'+ str_2 +'\n'+ str_dashes +'\n'+ str_3 
    else:
        # Simply display the problem vertically.
        arranged_problems = str_1 +'\n'+ str_2 +'\n'+ str_dashes

     # DEBUG
    if DEBUG == True: print(f'Var type of arranged_problems: {type(arranged_problems)}\n')

    return arranged_problems