import sys

if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("Hello, my name is" , sys.argv[1])

# Alternative way
if len(sys.argv)<2:
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")

print("Hello, my name is" , sys.argv[1])

# Giving many names in cmd line arg and using slicing method 
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for argv in sys.argv[1:]:
    print("Hello, my name is " , argv)