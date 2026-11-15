# Multiple parameters
def add(a, b):
    return a + b
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# No parameters
def greet():
    return "Hello"
greet = lambda: "Hello"
print(greet())  # Output: Hello

# Default values
def power(x, n=2):
    return x ** n
power = lambda x, n=2: x ** n
print(power(3))  # Output: 9
# if/else becomes a conditional expression
def check(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
check = lambda n: "even" if n % 2 == 0 else "odd"
print(check(4))  # Output: even
print(check(5))  # Output: odd