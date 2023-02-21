def func1():
    return 'Olá mundo!'
def func2(funcao):
    return funcao()
executando = func2(func1)
print(executando)

def func1(*args):
    print (args)
def func2(args):
    args = '30'
    return args
def func3(args):
    args = '40'
    return args
var = func2(func1)
var2 = func3(func1)
func1(var, var2)