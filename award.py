#three variables to get the value in input
swim = int(input("Swim : "))
cycle = int(input("Cycle : " ))
run = int(input("Run : "))

#making sum of that collected value
total = (swim + cycle + run)
print(total)

#checking condition from the value by logical operators
if(total<=100):
    print("Provincial colors")
elif(total>=101 and total<=105):
    print("Provincial Half Colours")
elif(total>=106 and total<110):
    print("Provicial Scroll")
elif(total>=111):
    print("No award")