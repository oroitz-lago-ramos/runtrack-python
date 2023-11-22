def calcule(num1, operator, num2):
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
        }
    if operator in op:
        return op[operator](num1,num2)
    else:
        return "Nous sommes désolés, l'opérateur rentré n'est pas valide"
        
print(calcule(17,"+",3))
print(calcule(1,"f",3))
print(calcule(2,"*",3))
print(calcule(9,"/",3))
print(calcule(3,"%",3))
print(calcule(9,"-",3))
