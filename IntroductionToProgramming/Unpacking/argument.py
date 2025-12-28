# printing positonal args 

# def f(*args,**kwargs):
#     print("Positonal:",args)

# f(100)

# printing keyword arguments 

def f(*args,**kwarg):
    print("Named: ", kwarg)

f(galleons=100,sickles=50,knuts=25)