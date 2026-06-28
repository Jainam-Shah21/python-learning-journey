import math
x = 5
y = 5.3
z = 2+3j
print(type(x))
print(type(y))
print(type(z))

# How to convert a datatype to numeric datatype
x = "24"
print(type(x))
x = int(x)  # converts any datatype to int

print(x*3)
print(float(x))  # converts any datatype to float
print(complex(x, y))  # converts any datatype to complex
# just remember to add 2 num

# ==============================================
# MATHEMATICAL OPERATORS
print(2+3)
print(5-3)
print(7*4)
print(7/2)
print(7//2) #this is called floor division which would always give a whole no. but in lower value
print(7%2)
print(2**3)# Exponents 1st no. is the base and the second number is the power
o=3
o+=2
print(o)#similar to java

#==================================================\
#Rounding
#to measure the dist we always need a +ve numbver hence use abs
#eg:
x=2-9
print(x)
print(abs(x))

#round off
price=233.04594958
print(math.ceil(price))
print(math.floor(price))
print(round(price,2))  #after 2nd decimal nothing would print and till 2nd decimal print with round off value

print(math.trunc(price))  #this would only print the integer similar to floor

#================================================
