# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Students")


for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
 
print('Current Letter :', letter)


# Python program to illustrate
# Iterating over range 0 to n-1
 
n = 4
for i in range(0, n):
    print(i)

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

