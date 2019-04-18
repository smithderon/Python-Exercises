#1
# agonize = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(sum(agonize))

#2

# agonize = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(max(agonize))

#3

# agonize = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(min(agonize))

#4
# agonize = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for numbers in range(2, 9, 2):
#     print (numbers)

#5
# agonize = [1, -2, 3, 4, -5, -6, 7, 8, 9]

# for numbers in range(1, 10):
#     if numbers >= 0:
#         print (numbers)

#6

# agonize = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# annoying = [agonize for agonize in agonize if agonize >= 0 ]
# print(annoying)

#7
# agonize = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# annoying = [numb * 3 for numb in agonize]
# print(annoying)

#8

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 4, 6, 8, 10, 12, 14, 16]
why = [a*b for a,b in zip(a,b)]
print(why)