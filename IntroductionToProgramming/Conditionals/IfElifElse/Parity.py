num = int(input("Write the number to check the parity: "))

if(num%2==0):
    print("The given number is an even number")
else:
    print("The given number is an odd number")


# Checking the parity by creating function (Alternative way)
def main():
    num = int(input("Write the number to check the parity: "))
    if(is_evenNumber(num)):
        print("The given number is an Even number")
    else:
        print("The given number is an odd number")

def is_evenNumber(num):
    #Way 1 
    # -----------------------------
    # if(num%2==0):
    #     return True
    # else:
    #     return False

    # ----------------------------- 
    
    #Another way to write the if else is:
    #return True if num%2==0 else False

    #-------------------------------

    # There is still a better way to optimize this:
    return (num%2==0)  # Here it will already return true or false then why use if else 

main()
    