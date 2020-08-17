print("CALCULATOR....")
 
print ("Operators Available : +, - ,÷ ,x,power / **")
op = input("Enter Operator : ")
n1 = input("Enter First Number : ")
n2 = input ("Enter Second Number : ")
print("\n")
if op== '+':
    print( "Solution of " ,n1,"+",n2,"is",int(n1)+ int(n2))
    
elif op== 'x':
    print( "Solution of " ,n1,"x",n2,"is",int(n1)* int(n2))
    
elif op== '÷':
    print( "Solution of " ,n1,"÷",n2,"is",int(n1)/ int(n2))
    

elif  op== '-':
    print( "Solution of " ,n1,"-",n2,"is",int(n1)- int(n2))
    
    
elif  op== 'power':
    print( "Solution of " ,n1,"raised to the power",n2,"is",int(n1)** int(n2))

elif  op== '**':
    print( "Solution of " ,n1,"raised to the power",n2,"is",int(n1)** int(n2))
    
    
else :
    print("................ERROR................")
    
