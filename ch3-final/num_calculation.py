def calculator(operator,num1,num2,reverse): 
    if reverse == True:
        if operator in ('add','+'): 
            return float(num2 + num1) 
        elif operator in ('sub','-'): 
            return float(num2 - num1) 
        elif operator in ("mul",'*'): 
            return float(num2 * num1) 
        elif operator in('div','/'): 
            return float(num2 / num1) 

    if operator in ('add','+'): 
      return float(num1 + num2) 
    elif operator in ('sub','-'): 
        return float(num1 - num2) 
    elif operator in ("mul",'*'): 
        return float(num1 * num2) 
    elif operator in ('div','/'): 
        return float(num1 / num2) 
   