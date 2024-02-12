# 5 examples of floating point arithmetic errors
print("")
print("5 Examples of Floating Point Arithmetic Errors")
print("")

# Subtraction of nearly equal numbers (Loss of Significance)
print("Example 1: Subtraction of nearly equal numbers (Loss of Significance)")
x1 = 1.2
x2 = 1.2000000000001
print(f"x1: {x1}, x2: {x2}")
print(f"{x2} - {x1} = ???")
print("Expected value: 0.0000000000001")
print(f"Actual value: {x2-x1}")
print("")

# Addition of a small number to a large number
print("Example 2: Addition of a small number to a large number")
x1 = 1e16
x2 = 1
print(f"x1: {x1}, x2: {x2}")
print(f"{x1} + {x2} = ???")
print("Expected value: 10000000000000001")
print(f"Actual value: {x1+x2}")
print("")

# Accumulation of Errors
print("Example 3: Accumulation of Errors")
x = 0.1
sum = 0
for i in range(10000000):
    sum += x
print(f"Summing over {x} {10000000} times.")
print("Expected value: 1000000.0")
print(f"Actual value: {sum}")
print("")

# Division that results in a number smaller than the minimum representable positive number (Underflow)
print("Example 4: Division that results in a number smaller than the minimum representable positive number (Underflow)")
x1 = 1e-345
x2 = 10
print(f"x1: {x1}, x2: {x2}")
print(f"{x1} / {x2} = ???")
print("Expected value: 1e-236")
print(f"Actual value: {x1/x2}")
print("")

# Inaccurate representation of decimal fractions
print("Example 5: Inaccurate representation of decimal fractions")
x1 = 0.1
x2 = 0.2
print(f"x1: {x1}, x2: {x2}")
print(f"{x1} + {x2} = ???")
print("Expected value: 0.3")
print(f"Actual value: {x1+x2}")



