# TYPES OF STRINGS

name = "jash"
# type(data) WILL provide you which datatype is used in the variable "data"
print(type(name))

age = 18
print(type(age))  # int

# print("your age is:" + age)  #this will show an error as the quoted text is a string and the word "age is an integer


# so if we have any value to convert it to string we just have to put str() datatype

print("Your age is:" + str(age))

# ----------------------------------------------------
# 1. MATHS

password = "123a"
print(len(password))  # len() will also count spaces in the string


if len(password) < 8:  # cases can prevent too short or too long things
    print("Pass to short!")

    textt = """
Python is too powerful
python is easy to learn
many ppl love python
"""
# in this "textt" we will use count(substring) which will provide us with the result of number of times the word has been repeated
# this is case sensitive hence only a particular ans will be provided
print(textt.count("python"))
# this can also be used to elem spcl character in string

# ----------------------------------------------------

# 2. TRANSFORMATION
price = "1234,56"
price = price.replace(",", ".")
print(price)

# 3. JOINING STRING
fir = "MIC"
las = "JACK"
print(fir, " ", las)

# THE F-STRING--- makes the classical print system nerfed and acts as short and time saver

name = "jash"
age = 18
is_stud = True
print(f"y name is {name} age is {age} I am a student?{is_stud}")

# 4. split()
stamp = "2026-09-02 14:24"
# print(stamp.split(" ").split("-")) 2 bar split nai krr skkte

print(stamp.split(" "))
stammp = "2191-23-3"
print(stammp.split("-"))

# 5. MULTIPLIER
# "string"* number

print("ha"*5)

# ----------------------------------------------

# 6. indexing and slicing

text = "python"

# to extrcat the first char
print(text[0])
# to extrcat the last char
print(text[5])

# extract H
print(text[3])

# 7. Slicing

date = "2026-03-26"
# to extract the year

# If we also leave the start empty its auto feature would be 0 egdate[: 4] will give same o/p
print(date[0:4])

# Print the month

print(date[5:7])

# extract the date

print(date[8:])
# If we have to use the no. from the right then use negative numbers

#8. Cleaning

#i]  Clean whitespace

name=" eng ".strip()
print(name)#this will not remove the space in the middle of 2 words
# if we specify the character to be removed , it will remove that character if nothing is mentioned then it will remove only the white space at the front and the back
#eg:
text="###ABC###".strip("#")
print(text)
text="###ABC###".lstrip("#")
print(text)

#can be used to detect whitespace
#eg:
text=" eng"
print(len(text))
print(len(text.strip()))

#ii] Clean cases
tex="python PROGRMMING"
print(tex.lower())
print(tex.upper())

#Clean data is used for searching the users choices
#Eg:
search=" EMAIL"
data=" email"
search= search.lower().strip()
data=data.strip()
print(search==data)

#9. Search
date="2026-feb-29"
email="bulky@gmail.com"
print(email.find('@'))
print("@" in email )


#=============================================
phone1="+49-65986-9632"
phone2="649-65986-9632"
phone3="0049-65986-9632"
Num1=phone1.find('-')+1
Num2=phone2.find('-')+1
print("the extracted number is:"+phone1[Num1:])
print("the extracted number is:"+phone2[Num2:])

#=============================================

#VALIDATION
country="USA"
print(country.isalpha())# to detect the presence of only characters that are letters

phone="03945209"
print(phone.isnumeric())
