# Inbuilt functions
y = max(67, 56, 34, 23, 89)
print(y)

x = min(12, 21, 54, 74, 2)
print(x)
# power of a number
z = pow(2, 3)
print(z)


# User-defined functions
def details():
    print("Natasha")


details()  # Calling a function

# Parameters and arguments
def students(name, course, age):
    print(name, course,age)

students("Ashely","MIT",17)
students("Goretti","Cyber Security",19)

def employee(fullname, idnum, salary, position, age):
    print(fullname,idnum, salary, position, age)

employee("Natasha Wambui", 9874854, 100000, "Manager", 24)
employee("Grace Ndegwa", 8574214, 50000, "Director", 21)
employee("Mark Mwangi", 9785854, 60000, "Manager", 22)
employee("Mike Njenga", 987289, 100000, "Director", 34)
employee("Cliff Anyanzo", 1537927, 100000, "Manager", 35)

