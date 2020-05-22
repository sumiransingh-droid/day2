1
name=input("name")
branch=input("branch")
gender=input("gender")
collegename=input("college name")
age=input("age")
print("name:",name)
print("branch:",branch) 
print("gender:",gender) 
print("collegename:",collegename) 
print("age:",age) 

2
number=float(input("enter a number"))
sqroot= number ** 0.5
print("square root of a ",number,"is",sqroot) 


3
a=int(input("let a="))
b=int(input("let b="))
a=a+b
b=a-b
a=a-b
print("after swap")
print("value of a",a) 
print("value of b",b) 


4
sellingprice=float(input("enter selling price "))
costprice=float(input("enter cost price"))
profit=sellingprice-costprice
newsellingprice= 1.05 + profit + costprice
print("profit=",profit) 
print("new selling price=",newsellingprice)


5
player1=int(input("run of player 1 in 60 balls"))
player2=int(input("run of player 2 in 60 balls"))
player3=int(input("run of player 3 in 60 balls"))
strikerate1=player1*100/60
strikerate2=player2*100/60
strikerate3=player3*100/60
print("run score player 1=",player1*2)
print("run score player 2=",player2*2)
print("run score player 3=",player3*2)
print("max no of sixes player 1=",player1//6)
print("max no of sixes player 2=",player2//6)
print("max no of sixes player 3=",player3//6)

