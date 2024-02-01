
def count(number):
    ''' the count function converts integer to string
        and count the number of string to determine legth
        of the string
        Return: it returns the total length of the string
    '''
    string = str(number)
    counter = 0
    for item in string:
        counter = counter + 1
        
    return counter


def printstr(string):
    for item in string:
        print(item)
    


def fmtNumber(number):
    '''
        this function will formart integers to financial formart
        parameters: it accepts Integer as parameter
        Returns: it return the string formart of the numbers
    '''    
    if count(number) < 4 :
        return number
    elif count(number) < 7:
        a = str(number)[:-3]
        b = str(number)[-3:]
        return f"{a},{b}"
    elif count(number) < 10:
        a = str(number)[:-6]
        b = str(number)[-6:-3]
        c = str(number)[-3:]
        return f"{a},{b},{c}"
    elif count(number) < 13:    
        a = str(number)[:-9]
        b = str(number)[-9:-6]
        c = str(number)[-6:-3]
        d = str(number)[-3:]
        return f"{a},{b},{c},{d}"
    elif count(number) < 16:    
        a = str(number)[:-12]
        b = str(number)[-12:-9]
        c = str(number)[-9:-6]
        d = str(number)[-6:-3]
        e = str(number)[-3:]
        return f"{a},{b},{c},{d},{e}" 
