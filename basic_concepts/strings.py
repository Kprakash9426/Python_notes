name= "vnekata guna govind"

# v=[0]
# e--[1]
print(len(name))
print("#positive  indexing the first character")

print(name[0])  
print(name[18])

num=[1,2,3,45,6,7,8]
print([num[0]])

print("-------Negative indexing------")
print(name[-1])

# slicing--to retrieve particular the range of data
print("start","end","interval")
print(name[::3])
#positive  indexing the first character
print(name[1:4])

"""
What is strip() in Python? (Easy Story)

Imagine you have a chocolate bar, but it is wrapped with paper on the left and right sides.

Before eating, you remove the wrapper.

In Python, strings also sometimes come with extra spaces, newlines, or unwanted characters on the left and right.
To clean them, we use:

✅ strip() → Removes unwanted characters from both sides
✅ lstrip() → Removes from left
✅ rstrip() → Removes from right

⭐ Default Behavior

If you DO NOT specify characters, it removes:

spaces " "

newline \n

tab \t"""

# Strips in python--remove beining and ending charcter or words etc...
college=" Engineering  "
print(college.strip())


# Strip will remove the middel character or value
print(college.strip('e'))

ins="Trishna tech"
print(ins.lstrip('T'))

print(ins.rstrip('t'))


# Real Use Case (clean user input)
username = input("Enter name: ").strip()
print("Welcome,", username)
