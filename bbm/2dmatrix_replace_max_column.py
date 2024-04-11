import copy

#MXN matrix, has -1 in certain cells, make copy of matrix, 
#replace -1 with max value in column,
#return copy of matrix in your function
#matrix = 
#[[1,2,3],
# [4,5,6],
# [-1,7,8]] 
#equals 
#[[1,2,3] 
# [4,5,6] 
# [4,7,8]]

# matrix = [[1,2,3],[4,5,6],[-1,7,8]]
# copied_list = None

# def change_matrix(matrix):
# 	copied_list = copy.deepcopy(matrix)
	

# 	for j in range(len(copied_list[0])):
# 		max_val = float('-inf')
# 		for i in range(len(copied_list)):
# 			if copied_list[i][j] != -1 and copied_list[i][j] > max_val:
# 				max_val = copied_list[i][j]
				

# 		for i in range(len(copied_list)):
# 			if copied_list[i][j] == -1:
# 			    copied_list[i][j] = max_val
    

#     return copied_list

		
# new_matrix = change_matrix(matrix)
# for row in new_matrix:
#     print(row)
# print(change_matrix(matrix))
#--------------------------------------------------------
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [-1, 7, 8]
# ]

# # Initialize a list to store maximum values for each column
# max_values = []

# # Iterate over each column
# for j in range(len(matrix[0])):
#     # Initialize the maximum value for the current column
#     max_val = float('-inf')
#     # Iterate over each row in the current column
#     for i in range(len(matrix)):
#         # Update the maximum value if the current element is greater
#         if matrix[i][j] > max_val:
#             max_val = matrix[i][j]
#     # Append the maximum value for the current column to the list
#     max_values.append(max_val)

# print("Maximum values for each column:", max_values)
#----------------------------------------------------------

# def replace_negatives(matrix):
#     # Find the maximum value for each column
#     max_values = [max(col) for col in zip(*matrix)]
    
#     # Create a copy of the matrix
#     # new_matrix = [row[:] for row in matrix]
#     new_matrix = copy.deepcopy(matrix)
    
#     # Iterate over each element in the matrix
#     for i in range(len(new_matrix)):
#         for j in range(len(new_matrix[0])):
#             # If the element is -1, replace it with the maximum value of its column
#             if new_matrix[i][j] == -1:
#                 new_matrix[i][j] = max_values[j]
    
#     return new_matrix

# # Example matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [-1, 7, 8]
# ]

# print(replace_negatives(matrix))
#-----------------------------------------------
# bbm dsa

# Neka
#MXN matrix, has -1 in certain cells, make copy of matrix, 
#replace -1 with max value in column,
#return copy of matrix in your function
#matrix = 
#[[1,2,3],
# [4,5,6],
# [-1,7,8]] 
#equals 
#[[1,2,3] 
# [4,5,6] 
# [4,7,8]]

import copy

# matrix = 
# [[1,2,3],
# [4,5,6],
# [-1,7,8]]
matrix = [[1,2,3],[4,5,6],[-1,7,8]]

def change_matrix(matrix):

	max_values = [max(col) for col in zip(*matrix)]
	
	new_matrix = copy.deepcopy(matrix)
	
	for i in range(len(new_matrix)):
		for j in range(len(new_matrix[0])):
			if new_matrix[i][j] == -1:
				new_matrix[i][j] = max_values[j]
				
	return new_matrix
	

print(change_matrix(matrix))
