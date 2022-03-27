print('Hello, World!')
print(1+2)
print(7*6)
print()
print("The end", "or is it?", "keep watching to learn more about python", 3)
#################
print("today is a good day to learn python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quote" in strings')
print("hello"+"world")
#################

#greeting = "Hello"
#name = str(input("Please enter your name: "))
#print(greeting + name)
#if we want a space, we can add that too
#print(greeting + ' ' + name)
#####################

splitString = "This String has been \nsplit over\nseveral\nlines"
print(splitString)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No,no, \'e\'s uh,... he\'s resting".')
print("""The pet shop owner said "No, no,'e's uh,... he's resting".""")

anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)
#######################
print(r"C:\Users\amritmurali\notes.txt")
print("C:\\Users\\amritmurali\\notes.txt")
#######################
age = str(20)
print(age)

#print(type(greeting))
print(type(age))

age_in_words ="2 years"
#print(name + " is " + age + " years old ")
print(type(age_in_words))
########################
a = 12
b = 3

print(a+b) #15
print(a-b) #9
print(a*b) #36
print(a/b) #4.0
print(a//b) #4 integer division, rounded down towards minus infinity
print(a % b) #0 modulo: the remainder after integer division
#######################

print((((a+b)/3)-4)*12)

c = a+b
d = c/3
e = d-4
print(e*12)

print(a/(b*a)/b)
######################

parrot = "Norwegian Blue"
print(parrot)

#mini challenge - print out we win from the string assigned to parrot variable using indexing

print(parrot[3]+"\n"+parrot[4]+"\n"+"\n"+parrot[3]+ "\n"+parrot[6]+"\n"+parrot[8])
print()
print(parrot[-11]+"\n"+parrot[-1]+"\n"+"\n"+parrot[-11]+ "\n"+parrot[-8]+"\n"+parrot[-6])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[10:14])

print(parrot[-4:-2])
print(parrot[-4:12])

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " "for char in number).split()
print([int(val) for val in values])
##############################################

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[25:17:-1])

##############################################

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "

print(string1 + string2 + string3 + string4 + string5)
print("Hello "*5)

today = "friday"
print("day" in today) #true
print("fri" in today) #true
print("thur" in today) #false
print("parrot" in "fjord") #false

#############################################

age = 24
print("my age is {0} years" .format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

##############################################

for i in range(1,13):
    print("No.{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:<52.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

print(f"Pi is approximately {22 / 7 :12.50f} ")
