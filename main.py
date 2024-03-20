stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code 
mantissa = stdform[0: stdform.index("x")] 
exponent = stdform[stdform.index("^") + 1:]
print(f"This number in E notation is {mantissa}E{exponent}.")
