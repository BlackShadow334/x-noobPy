
print("input 'sum' for addition")
print("input 'sub' for subtraction")
print("input 'mul' for multiplication")
print("input 'div' for division")
print("input 'rem' for remainder")
print("input 'quit' for exit")
while 1==1:    
    try:
        inp = input("input : ")
        if inp=="sum":
            a=float(input("1st no : "))
            b=float(input("2nd no : "))
            print("addition : ", float(a+b) )
        elif inp=="sub":
            a=float(input("1st no : "))
            b=float(input("2nd no : "))
            print("subtraction",float(a-b))
        elif inp=="mul":
            a=float(input("1st no : "))
            b=float(input("2nd no : "))
            print("multiplication", float(a*b))
        elif inp=="div":
            a=float(input("1st no : "))
            b=float(input("2nd no : "))
            print("division :" ,float(a/b))
        elif inp=="rem":
            a=float(input("1st no : "))
            b=float(input("2nd no : "))
            print("remainder",float(a%b))
        elif inp=="quit":
            break
    except ZeroDivisionError:
        print("""error occoured......
cant divide by zero......
        """)
    except :
        print("""error occoured......
please provide right input......
        """)
print("...PROGRAM FINISHED...") 
