# List, List function and Tuple in python


# product = ['Vim bar', "Detergent", "Potato", 'Tomato', 210]
# product.sort()
# print(product)

# numbers = [43, 12, 4, 20, 14]
# numbers.sort()
# numbers.reverse()
# print(numbers[::-1])
# print(len(numbers))
# print(max(numbers))
# numbers.append((82))   # For enter at the end
# numbers.insert(3, 27)
# numbers.remove(20)
# numbers.pop()
# numbers[1]=100
# print(numbers)

# Mutable "[]" - can change
# Immutable "()" - can not change  (Tuple)

# tp = (3, 92, 25, 'Mango')
# tp[1] = 8  -> it is wrong
# print(type(tp))
# print(tp)

a = 3
b = 7
# temp = a
# a = b
# b=temp
a, b = b, a
print(a, b)