#basic if single
score=100
if(score>=90):
    print("A")

#if with else statement 
score=34

if(score>=90):
    print("A")
else:
    print("F")

    #with 1 elif

score=80

if(score>=90):
    print("A")
elif(score>=80):
    print("B")
else:
    print("F")

    #with 2 elif

score=75

if(score>=90):
    print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
else:
    print("F")

# if is nested

score=96
project_sub=True

if(score>=90):
    print("A")
    if(project_sub):  #avoid this ==true python analyzes by itself whether it is true or false
        print("A+")
    else:
        print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
else:
    print("F")

#modification of nested if using logical op

score=98
project_sub=True

if(score>=90 and project_sub):
    print("A++")
elif(score>=90 ):
    print("A")
elif(score>=80):
    print("B")
elif(score>=70):
    print("C")
else:
    print("F")

    #independent if else

sco=98

proj=True

if(sco>=90):
    print("high score")
else:
    print("low score")
if(proj):
    print("proj sub")
else:
    print("proj not")
