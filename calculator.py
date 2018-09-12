class Calculator(object):
    def evaluate(self, string):
        string = string.replace(' - ', ' @ ')
        string = do_operations(string, '*', '/')
        string = do_operations(string, '+', '@')
            
        if len(string)>2 and string[-2:]=='.0':
            string = string[:-2]
        
        if string.find('.')!=-1:
            output = float(string)
        else:
            output = int(string)
        
        return output
        
def do_operations(string, oper1, oper2):
    while(string.find(oper1)!=-1 or string.find(oper2)!=-1):
        if string.find(oper1)>string.find(oper2):
            string = combine(string, oper1)
        elif string.find(oper2)>string.find(oper1):
            string = combine(string, oper2)
    return string
        
def combine(string, oper):
    l = string.split(' ')
    i = l.index(oper)
    x = float(l[i-1])
    y = float(l[i+1])
        
    if oper=='*':
        z = x * y
    elif oper=='/':
        z = x / y
    elif oper=='+':
        z = x + y
    elif oper=='@':
        z = x - y
            
    l[i]=str(z)
    del l[i+1]
    del l[i-1]
        
    return ' '.join(l)
