import random
q = 353
a = 3
print(f"Prime number is: {q}")
print(f"Primitiveroot  number is: {a}")
X = int(input("Enter the private key Xa: "))
x = int(input("Enter the private key Xb: "))
Y = pow(a,X,q)
y = pow(a,x,q)
print(f"Public key Ya is: {Y}")
print(f"Public key Yb is: {y}")
k1 = pow(y,X,q)
k2 = pow(Y,x,q)
print(f"The key generated are: K1-{k1} and K2-{k2}")
if(k1==k2):
    print("The keys are same, the code is correct!")
