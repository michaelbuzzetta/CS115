#name: Michael Buzzetta
#Pledge: I pledge my honor that I have abided by
#the stevens honor system.

r = int(input("Please enter r value: "))
g = int(input("Please enter g value: "))
b = int(input("Please enter b value: "))

w = max(r/255, g/255, b/255)
c=(w-r/255)/w
m=(w-g/255)/w
y=(w-b/255)/w
k=1-w

print(c)
print(m)
print(y)
print(k)
