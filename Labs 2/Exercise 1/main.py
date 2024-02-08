# Finds the maximum value in an array
def max_n(array):
    current_max = array[0]
    for i in range(1, len(array)):
        if array[i] > current_max:
            current_max = array[i]
    return current_max

# Finds the sum of an array
def sum_array(array):
    total = 0
    for i in range(len(array)):
        total += array[i]
    return total

# Reverses a string
def reverse_string(string):
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

# Finds the unique values in an array
def unique(array):
    unique_values = []
    for i in range(len(array)):
        if array[i] not in unique_values:
            unique_values.append(array[i])
    return unique_values

# Combines unique, and sum_array
def unique_and_sum(array):
    return sum_array((unique(array)))

# Test the functions
test_array = []
for i in range(11):
    for _ in range(i):
        test_array.append(i)

test_string = 'Hello, World!'

print("test_array:", test_array)
print("test_string:", test_string)

print("max_n(test_array):", max_n(test_array))
print("sum_array(test_array):", sum_array(test_array))
print("reverse_string(test_string):", reverse_string(test_string))
print("unique(test_array):", unique(test_array))
print("unique_and_sum(test_array):", unique_and_sum(test_array))

