# 1
# crazy = "maniacal"
# uber = crazy.capitalize()
# print (uber)

# 2
# crazy = "maniacal"
# print (crazy.upper())

# 3
# crazy = "maniacal"
# uber = crazy [::-1]
# print (uber)

# 4
leet = (("a","4"), ("e" or "E","3"), ("g" or "G", "6"), ("o", "0"), ("s", "5"), ("t", "7"))
alpha =  """
Not terribly sure what I've been doing up until now, but I'll find a way
to make it work. I'm sure of it!
""" 
omega = alpha
for char, val in leet:
    omega = alpha.replace(char, val)
    
print (omega)