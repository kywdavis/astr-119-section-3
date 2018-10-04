#string

s = "I am a string."
print(type(s)) # will say str

#BOOLean

yes = True #Boolean True
print(type(yes))

no = False
print(type(no))

#List -- ordered and changeable

alpha_list = ["a", "b", "c"]
print(type(alpha_list)) #will say list
print(type(alpha_list[0])) #will say string
alpha_list.append("d") 
print(alpha_list)

#tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple)) #will say tuple

try:
	alpha_tuple[2] = "d" #won't work because cant change tuple
except TypeError:
	print ("We can't add elements to tuples!")

print(alpha_tuple)