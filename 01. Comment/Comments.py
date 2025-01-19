# COMMENTS
# Three types of comments: Single-line, Multi-line and Docstring  

# Single-line comment 
# 1. Comment only one line using #
# 2. Shortcut: ctrl+/
# 3. Doesn't affect statements written before it 
   
""" Multi-line comment 
1. (""" """) or (''' ''') triple quotes is use to comment multi-line 
2. Shortcut: shift+alt+A
3. Rarely use because it is hard to apply and remove
"""
def func(num1,num2):
    """Add 2 numbers(funcationality)
    Args:
        num1:number to add (Parameter details)
        num2:number to add
        Reutrns: sum of num1 and num2 (Return details)
        """
    
    """
    1. A strinmg used to document a python module,class,function 
       or method the declartion of function .
    2. It doesn't perform anything.
    3. Access by help function or __doc__ attribute.
    4. It is just used to explain the functionality of function. 
    5. Other comments inside the block are not accessable.
    """
    return num1+num2

print(func(4,5))      
print(func.__doc__)  
help(func)




