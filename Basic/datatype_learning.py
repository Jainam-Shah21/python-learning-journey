# if you assign data to a single variable twice than the older data is deleted and new is stored
# eg: a=1     here a=1 is stored but as soon as I enter another data 1 will vanish
# now i put a="abc" this is string data and now a is abc hence old "1 " is vanished

a=1 

b="abc" 

#a=b    # this will show error bcoz you will first have to assign the value to a temporary variable


c= a 
a=b
print (c)
print (a)

#----------------------------------------------------
a=10   #int
b=3.14   #float
c="HELLO"  #str
d='HI'   #str
e=True   #boolean  first char should be capital and the rest should be lower case i.e case sensitive datatype

f=False  #boolean 
g=None   #mostly used as temporary var and has no much importance in the prog but can store value of another var

#----------------------------------------------------

text="HI"
num=10

print(type(text))
print(type(num))

print(len(text))
#print(len(num)) this will show error as len would calculate the length of the string and not any number
print(text.upper())
#print(num.upper())  this will also show error bcoz upper is for string and int cannot be executed
print(num.bit_length())

#----------------------------------------------------
#CHALLENGE OF THE DAY
#To print the following output with their data type and their length

age=18
height=5.10
name="jash indias no. 1"
stu=True
noval=None

print("Age is",age,"Datatype=INT""  length=",age.bit_length())
#print("Height is",height,"Datatype=float""length=",{height_bit_length()})
print("Name is",name,"Datatype=String" "  length=",len(name))
