# created on gitHub.

# import os
# clear = lambda: os.system('cls')
# clear()

print(chr(27)+'[2j')
print('\033c')
print('\x1bc')



user_input = 55

x = 0
y = 1
total_x_y = 0

fibonacci = [x, y]



while total_x_y < user_input:
    total_x_y = x + y
    fibonacci.append(total_x_y)
    x = y
    y = total_x_y




print(fibonacci)


# TASK

# Create a list consisting of Fibonacci numbers from 1 to 55. 

# The desired output is like :

# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
# Fibonacci Dizisi, her sayının kendisinden bir önceki sayı ile toplanması ile elde edilen sayılar serisidir.

# ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 3, 5, 8, 13, 21

# start_val = 1
# end_val = 11

# incremented_list = list(range(start_val, end_val, 2))         #; print(fibonacci)
# fibonacci = list()
# for i in range(end_val - 1): fibonacci.append(0)
# ordered_list = list(range(start_val, end_val))
# print("initial fibonacci:    ", incremented_list)
# print("initial ordered list: ", ordered_list)
# print("initial fibonacci:    ", fibonacci)

# for i in range(end_val-2):

#     sum_of_two = ordered_list[i] + ordered_list[i + 1] 

#     sum_of_three = ordered_list[i] + sum_of_two             ; print("sum_of_two: ", sum_of_two, "     sum_of_three: ", sum_of_three)
    
#     ordered_list[i] = ordered_list[i] + sum_of_three
    
# for i in range(5):


#     sum_of_three = sum_of_two + incremented_list[i]             ; print("sum_of_two: ", sum_of_two, "     sum_of_three: ", sum_of_three)

#     fibonacci.append(sum_of_three)



    


#     fibonacci.append(i + temp_val)





# print("fibonacci: ", fibonacci)
# print("ordered list: ", ordered_list)
