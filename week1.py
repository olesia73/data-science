# Problem 1
f1 = 1
f2 = 1
print(f1)
print(f2)
for i in range(4):
  f1 += f2
  print(f1)
  f2 += f1
  print(f2)

# Problem 2
for i in range(1, len(lst), 2):
  print(lst[i])

# Problem 3
print(len(string.split()))

# Problem 4
def count_vowels(word):
    count = 0
    for char in list(word):
        if char in list("AEIOUaeiou"):
            count += 1
    return count
  

# Problem 5
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
  print(animal.upper())

# Problem 6
for x in range(1, 21):
  print(x, end='')
  if x % 2: 
    print(" is odd")
  else:
    print(" is even")

# Problem 7
def sum_of_integers(a, b):
  return a + b



