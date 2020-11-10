#!/usr/bin/env python3
import sys
import os

def get_ids_and_sequences_from_file(filename):
  ids        = []
  sequences  = []
  
  for line in open(filename, "r").readlines():
    line = line.rstrip()    # removing unnecessary characters: \n
    
    if (line[0] == ">"):
      ids.append(line[1:])
    elif (len(line) > 0):
      sequences.append(line)
  return ids, sequences

def get_dissimilarity_between_2_sequences(sequence1, sequence2):
  '''
    Get the dissimilarity percentage between 2 sequences.
    
    @param sequence1:  str sequence
    @param sequence2:  str sequence
    @return dissimilarity percentage
  '''
  dissimilarity   = 0
  sequence_length = len(sequence1)
  
  if (sequence_length != len(sequence2)):
    print("Error: Sequence 1's length ({}) doesn't match with Sequence 2's ({}).".format(len(sequence1), len(sequence2)))
    return
  
  for i in range(len(sequence1)):
    if (sequence1[i] != sequence2[i]):
      dissimilarity += 1
  
  if (dissimilarity == 0): # return 0 instead of 0.0
    return 0
  return (dissimilarity / len(sequence1))

def save_matrix(matrix):
  length = len(matrix)
  
  # for i in range(0, length):
  #   row = []
  #   for j in range(0, length):
  #     row.append(matrix[i][j])
  #   print(row)
    
  output_file = open("genetic-distances.txt", "w+")
  for i in range(0, length):
    row = ""
    for j in range(0, length):
      row += str(matrix[i][j]) + "\t"
    output_file.write("{}\n".format(row))
  output_file.close()

def generate_genetic_distance_matrix(ids, sequences):
  length = len(ids) + 1     # +1 due to exclusive element at the end
  distance_matrix = []
  
  # sets all distance_matrix values to None/null
  for i in range(0, length):
    row = []
    for j in range(0, length):
      row.append(None)
    distance_matrix.append(row)
  distance_matrix[0][0] = ""
    
  # First row indicators
  for i in range(1, length):
    distance_matrix[0][i] = ids[i-1]

  # First column indicator
  for j in range(1, length):
    distance_matrix[j][0] = ids[j-1]

  # Calculate the distance_matrix
  for i in range(1, length):
    for j in range(1, length):
      distance_matrix[i][j] = get_dissimilarity_between_2_sequences(sequences[i-1], sequences[j-1])

  # save_matrix(distance_matrix)
  return distance_matrix

def get_row_sum(matrix, row_num):
  row_sum = 0
  for i in range(1, len(matrix)):
    row_sum += matrix[row_num][i]
  return row_sum

def get_col_sum(matrix, col_num):
  col_sum = 0
  for i in range(1, len(matrix)):
    col_sum += matrix[i][col_num]
  return col_sum
  
def generate_q_matrix(matrix):
  '''
  Generating a Q-matrix from the distance matrix
  '''
  matrix_length = len(matrix)
  
  q_matrix = []
  # sets all q_matrix values to None/null
  for i in range(1, matrix_length):
    row = []
    for j in range(1, matrix_length):
      if (i != j):
        row.append(((matrix_length - 2 - 1) * matrix[i][j] - get_row_sum(matrix, i) - get_col_sum(matrix, j)))
        # -1 due to the first row/column indicators
      else:
        row.append(0)
    q_matrix.append(row)
  return q_matrix
  
def generate_fake_matrix():
  length = 6
  distance_matrix = []
    # sets all distance_matrix values to None/null
  for i in range(0, length):
    row = []
    for j in range(0, length):
      row.append(None)
    distance_matrix.append(row)
  distance_matrix[0][0] = ""
    
  ids = ["a", "b", "c", "d", "e"]
  # First row indicators
  for i in range(1, length):
    distance_matrix[0][i] = ids[i-1]

  # First column indicator
  for j in range(1, length):
    distance_matrix[j][0] = ids[j-1]
  
  lst = [[0,5,9,9,8],
   [5,0,10,10,9],
   [9,10,0,8,7],
   [9,10,8,0,3,],
   [8,9,7,3,0]
   ]

  # # Calculate the distance_matrix
  for i in range(1, length):
    for j in range(1, length):
      distance_matrix[i][j] = lst[i-1][j-1]
      
  # for i in range(0, length):
  #   row = []
  #   for j in range(0, length):
  #     row.append(distance_matrix[i][j])
  #   print(row)
  return distance_matrix

def fake_print_matrix(matrix):
  length = len(matrix)
  for i in range(0, length):
    row = []
    for j in range(0, length):
      row.append(matrix[i][j])
    print(row)
  
def get_min_val_and_location(matrix):
  '''
  Get the min values and locations of the matrix
  '''
  min_val      = 0
  min_location = (0, 0)
  matrix_length = len(matrix)
  
  for i in range(matrix_length):
    for j in range(matrix_length):
      if (min_val > matrix[i][j]):
        min_val = matrix[i][j]
        min_location = list(min_location)
        min_location[0] = i
        min_location[1] = j
  return min_val, min_location
  
def main(arguments):
  if (len(arguments) == 2):
    if (os.path.exists(arguments[1])):
      ids, sequences = get_ids_and_sequences_from_file(arguments[1])
      
      # distance_matrix = generate_genetic_distance_matrix(ids, sequences)
      distance_matrix = generate_fake_matrix()
      
      q_matrix = generate_q_matrix(distance_matrix)
      min_val, min_location = get_min_val_and_location(q_matrix)
      
      # Calculating the distance to the new node
      # See: https://wikimedia.org/api/rest_v1/media/math/render/svg/fbb5a4b2a6fbec48a4bbc6d6fc1e351e5eb851e0
      #      https://en.wikipedia.org/wiki/Neighbor_joining
      distance_to_new_node =  (distance_matrix[min_location[0] + 1][min_location[1] + 1] / 2) + \
                              ((get_row_sum(distance_matrix, min_location[0] + 1) - get_col_sum(distance_matrix, min_location[1] + 1)) / \
                              (2 * (len(distance_matrix) - 2 - 1)))
      
      distance_difference  =  (distance_matrix[min_location[0] + 1][min_location[1] + 1]) - distance_to_new_node
      print(distance_difference)
    else:
      print("Error: Unable to find `{file}` file.".format(file=arguments[1]))
  else:
    print("Error: requires an <input_file.fna> argument only`")
  
        
if __name__ == '__main__':
  main(sys.argv)