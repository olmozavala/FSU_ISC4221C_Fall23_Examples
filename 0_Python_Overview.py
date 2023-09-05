# %%

# ints, floats, strings, booleans
xint = 5
xfloat = 5.0
xstring = "5"
xbool = True

print(type(xint))
print(type(xfloat))
print(type(xstring))
print(type(xbool))
# %% Arrays and tuples
mytuple = (1, 2, 3)
myarray = [1, 2, 3]

myarray[0] = 5
print(myarray)
# %% Dictionaries
mydict = {"a": 1, "b": [3,4,43], "c": False}
print(mydict["b"])

# %%
x = True
y = False
if not x or y:
    print("true")
else:
    print("false")

# %%
if y:
    print("true")
elif x and not y:
    print("false")
else:
    print("Here")

# %%
for i in [1, 2, 3, 4, 5]:
    print(i)
# %%
for i in range(10):
    print(i)
# %%
for idx, value in enumerate([2,4,6,8]):
    print(f"index: {idx}, value: {value}")
    if idx == 2:
        break

# %%
i = 0
while i < 10:
    print(i)
    i += 1

# %%
def name_func(name):
    print(f"Hello {name}")

name_func("John")

# %%
def add_func(x, y = 5, z = 20):
    return print(x + y + z)
# add_func(10)
# add_func(10, 20)
add_func(10, z = 20)

# %% 
def add_func(*args):
    print(type(args))
    print(args)
    print(sum(args))

add_func(1,2,'a')

# %% Comprehenstions
x = [i*2 + 5 for i in range(2)]
print(x)
# %% Comprehenstions
x = [i*2 + 5 for i in range(10) if i*3 < 10]
print(x)
# %% Comprehenstions
x = [i*2 + 5 for i in range(10name = "Fido")
# Documentation here
x = [1 if x > 5 else 0 for x in range(10)]
print(x)

# %%
class Dogname = "Fido"):
    name = ""
    def __init__(self, name = "Fido"):
        self.name = name

    def printName(self):
        print(self.name)

mydog = Dog("Hiro")
mydog.printName()
# %%
# mydog2 = Dog()
# mydog2.printName()

# %% 
# Factorial n! = n * (n-1) * (n-2) * ... * 1
def myrec(x):
    if x == 0:
        return 1
    else:
        return x * myrec(x-1)

print(myrec(5))
    


# %%
