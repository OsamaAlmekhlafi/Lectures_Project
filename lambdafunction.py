
# *BY Osama Abdo Modhish*

def say_hello(name,age ):
    return f"Hello {name} your age is: {age}"

hello = lambda name, age :f"Hello {name} your age is {age}"

print(say_hello("osama",22 ))
print(hello("osama",22 ))

print(say_hello.__name__)
print(hello.__name__)
