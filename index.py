print("      WELCOME TO")
print("   MATH MAGIC  GAME   ")
print("1.magic of math ")
print("2.maths trick MCQ")
game= int(input("enter your game no: "))
if game == 1 :
    import random

    x =print("guess a number in your mind   ")
    set = {10,100,200,500,1000}
    random_element = random.choice(list(set))
    t = random_element/2
    y = int(input("please press 2 continue"))
    print("now  add same no. of your friend in it  ")
    a= int(input("please press 2 continue"))
    print("Now add my no.", random_element, "in your no")
    b= int(input("please press 2 continue"))
    print("divide  it by 2  ")
    c= int(input("please press 2 continue"))
    print("now  subtract your friend no. from it")
    g= int(input("please press 2 continue"))
    print("your number is ",t)
elif game == 2:
    print("welcome to ")
    print("maths trick MCQ")
    print("1.if on tree there are 11 birds and if hunter fire on 1 bird add kill it then how many bird on that tree are present after fire")
    ans_1= int(input("enter your ans in int"))
    if ans_1==0:
        print("your ans is correct ")
    else :
        print("your ans is wrong")
        print("after fire no bird on tree because all of them fly away .by sound of gun")
    print("2")
else:
    print("error")


