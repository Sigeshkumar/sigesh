#Argument
'''def my_func(lname):
    print("This is",lname)
my_func("sigesh")'''

#Multiple Argument
'''def my_func(fname,lname):
    print(fname,lname)
my_func("sigesh","R")'''

#Keyword Argument
'''def my_func(fname,lname):
    print("Hi",fname,lname)
my_func(lname="R",fname="Sigesh")'''

#Arbitrary Arguments
'''def my_func(*teams):
    print("my",teams)
my_func("CSK","MI","RCB","GT")'''

#Arbitrary Keyword Argument
'''def my_func(**teams):
    print("my",teams["key1"])
my_func(key1="CSK",key2="MI",key3="RCB",key4="GT")'''

'''#Default Argument
def my_func(team="CSK"):
    print(team)
my_func("MI")
my_func("RCB")
my_func("GT")
my_func()'''

'''def fun_ret(x=10):
    pass
(fun_ret()'''

'''def fun_ret(x=10):
    return 5*x
print(fun_ret())'''

'''def fun_ret(x):
    return x*x
print(fun_ret(20))'''

def func_recur(x):
    if(x==1):
        return 1
    else:
        return(x*func_recur(x-1))
print(func_recur(4))








