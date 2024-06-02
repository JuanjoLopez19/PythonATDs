
from ATD.stack.Stack import Stack
from ATD.qeue.queue import Queue

def symbol_balance(exp: str = None) -> bool:
    """
        @param exp: str --> The expression to check if it pair of symbols is balance
        @return bool --> True if its balanced and False if itsn't 
        
        The function will check if the expression given as parameter is
        valid, being valid as each pair of symbols are closed correct
        This might be done with a regex but just for practising
    """

    aux: Stack = Stack()

    if exp is None or len(exp) == 0 or exp == "":
        return False

    for char in exp:
        if char == '{' or char == '[' or char == '(':
            aux.push(ord(char))
        else:
            if aux.isEmpty():
                return True
            else:
                temp: str = chr(aux.pop())
                if temp == '{':
                    if char != '}':
                        return True
                elif temp == '(':
                    if char != ')':
                        return True
                elif temp == '[':
                    if char != ']':
                        return True
    if aux.isEmpty():
        return True
    else:
        return False
    
def check_palyndrome(exp: str = None) -> bool:
    """
        @param exp: str --> The expression to check if its a palyndrome
        @return bool --> True if its and False if itsn't 
        
        The function will check if the expression given as parameter is
        valid, being valid as the expression is a palyndrome
    """
    
    if exp is None or len(exp) == 0:
        return False
    
    s = Stack()
    q = Queue()
    
    for char in exp:
        if char == ' ':
            pass
        else:
            s.push(ord(char))
            q.push(ord(char))

    while not s.isEmpty() and not q.isEmpty():
        temp1 = chr(s.pop())
        temp2: str = chr(q.pop())
        if temp1 != temp2:
            return False
        
    if s.isEmpty() and q.isEmpty():
        return True
    else:
        while not s.isEmpty() and not q.isEmpty():
            s.pop()
            q.pop()
        return False
        
if __name__ == '__main__':
    temp: str = "{([[[]]]})}"
    aux: bool = symbol_balance(temp)
    if aux:
        print(f"The expression {temp} is balanced")
    else:
        print(f"The expression {temp} is not balanced")

    temp: str = "amad a la dama"
    aux = check_palyndrome(temp)
    if aux:
        print(f"The expression {temp} is a palyndrome")
    else:
        print(f"The expression {temp} is not a palydrome")