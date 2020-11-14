#!/usr/bin/env python3
import sys
import os
from Node import * 

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

# Get the dissimilarity percentage between 2 sequences.
def get_dissimilarity_between_2_sequences(sequence1, sequence2):
  dissimilarity   = 0
  sequence_length = len(sequence1)
  
  if (sequence_length != len(sequence2)):
    print("Error: Sequence 1's length ({}) doesn't match with Sequence 2's ({}).".format(len(sequence1), len(sequence2)))
    return
  
  for i in range(sequence_length):
    if (sequence1[i] != sequence2[i]):
      dissimilarity += 1
  
  if (dissimilarity == 0):
    return 0
  return (dissimilarity / (0.0 + sequence_length))

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
  distance_matrix = initialize_matrix(0, length)
  
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

def initialize_matrix(start_at, length):
  matrix = []
  for i in range(start_at, length):
    row = []
    for j in range(start_at, length):
      row.append(0)
    matrix.append(row)
  matrix[0][0] = ""
  return matrix

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
  
  @return min_val         minimal value
  @return min_location    i, j location of minimal value
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
  
def generate_q_matrix(distance_matrix):
  '''
  Generating a Q-matrix from the distance matrix
  '''
  matrix_length = len(distance_matrix)
  
  q_matrix = []
  for i in range(1, matrix_length):
    row = []
    for j in range(1, matrix_length):
      if (i != j):
        row.append(((matrix_length - 2 - 1) * distance_matrix[i][j] - get_row_sum(distance_matrix, i) - get_col_sum(distance_matrix, j)))
        # -1 due to the first row/column indicators
      else:
        row.append(0)
    q_matrix.append(row)
  return q_matrix
  
def neighbor_joining(distance_matrix):
  q_matrix = generate_q_matrix(distance_matrix)
  min_val, min_location = get_min_val_and_location(q_matrix)
  x = 120
  nodes = list(range(len(q_matrix))) # -1 due to indicator
  edges = []
  
  # Calculating the distance to the new node
  # See: https://wikimedia.org/api/rest_v1/media/math/render/svg/fbb5a4b2a6fbec48a4bbc6d6fc1e351e5eb851e0
  #      https://en.wikipedia.org/wiki/Neighbor_joining
  # branch distance a & b to u
  distance_a =  (distance_matrix[min_location[0] + 1][min_location[1] + 1] / 2.0) + \
                ((get_row_sum(distance_matrix, min_location[0] + 1) - get_col_sum(distance_matrix, min_location[1] + 1)) / \
                (2 * (len(distance_matrix) - 2 - 1)))
  distance_b =  (distance_matrix[min_location[0] + 1][min_location[1] + 1]) - distance_a
  
  # sets all new_distance_matrix values to 0
  new_distance_matrix = initialize_matrix(1, len(q_matrix))
  new_distance_matrix[min_location[0]][x] = distance_a
  new_distance_matrix[min_location[1]][x] = distance_b
  
  edges.append((x, min_location[0], distance_a))
  edges.append((x, min_location[1], distance_b))
  
  print(len(new_distance_matrix))
  return
  # for node in nodes:
  #   if not ((node == min_location[0]) or (node == min_location[1])):
  #     distance_matrix[x + 1][]
  
  
  for i in range(0, (len(q_matrix))):
    row = []
    for j in range(0, len(q_matrix)):
      row.append(q_matrix[i][j])
    print(row)
  # print(distance_difference)
  
  
def main(arguments):
  if (len(arguments) == 2):
    if (os.path.exists(arguments[1])):
      ids, sequences = get_ids_and_sequences_from_file(arguments[1])
      
      distance_matrix = generate_genetic_distance_matrix(ids, sequences)
      # distance_matrix = generate_fake_matrix()
      
      neighbor_joining(distance_matrix)
    else:
      print("Error: Unable to find `{file}` file.".format(file=arguments[1]))
  else:
    print("Error: requires an <input_file.fna> argument only`")
  
        
if __name__ == '__main__':
  main(sys.argv)