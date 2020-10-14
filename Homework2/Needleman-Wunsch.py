import sys
import os
import numpy
import plt

class NW:
  
  def __init__(self, query, ref, is_print_all_info=True):
    # initialize scores
    self.MISMATCH_SCORE   = -3    # comes from the diagonal value && is mismatched
    self.MATCH_SCORE      = 1     # comes from the diagonal value && is matched
    self.GAP_SCORE        = -2    # comes from left/up value
    
    self.query            = query
    self.ref              = ref
    self.query_length     = len(self.query)
    self.ref_length       = len(self.ref)
    self.matrix           = []
    self.score            = None  # final score from the bottom right of matrix
    self.is_print_all_info= is_print_all_info
    self.initialize_matrix()
    self.calculate_nw_matrix()
    # self.print_matrix()
    self.backtrack_matrix()
    
  def print_matrix(self):
    '''
      This is only for testing purposes for the small sequence.
      Prints out the entire matrix.
      Also shows the first sequence on the first column & second sequence on the first row.
      
      @param  Nothing
      @return Nothing
    '''
    
    # prints out horizontal sequence
    print("\t\t", end="")
    for i in range(0, self.query_length):
      print("{}".format(self.query[i]), end="\t")
    print()
    
    for i in range(0, self.ref_length + 1):
      # prints out vertical sequence
      if (i == 0):
        print(end="\t")
      else:
        print(self.ref[i-1], end="\t")
      
      # prints out the entire matrix
      for j in range(0, self.query_length + 1):
        print("{}".format(self.matrix[i][j]), end="\t")
      print()
    

  def initialize_matrix(self):
    '''
      This function initialize the (ref x query) matrix
      to set all values as None (except the first row & first column for the GAP score).
      
      @param    Nothing
      @return   Nothing
    '''
    # sets all matrix values to None/null
    # ref = rows; query = columns
    for i in range(0, self.ref_length + 1):
      row = []
      for j in range(0, self.query_length + 1):
        row.append(None)
      self.matrix.append(row)
     
    # sets first row with GAP_SCORE
    for i in range(1, self.ref_length + 1):
      self.matrix[i][0] = i * self.GAP_SCORE
      
    # sets first column with GAP_SCORE 
    for j in range(1, self.query_length + 1):
      self.matrix[0][j] = j * self.GAP_SCORE
    
    # sets first row & first column to 0 for diagonal scoring purposes
    self.matrix[0][0] = 0
  
  def calculate_nw_matrix(self):
    '''
      This function calculates the matrix by the Needleman-Wunsch technique.
      The current row & column in the matrix is set to the max score of previous row, column, or row and column (diagonal),
      comebined with either a GAP_SCORE, MATCH_SCORE, or MISMATCH_SCORE.
      
      @param  Nothing
      @return Nothing
    '''
    for i in range(1, self.ref_length + 1):
      for j in range(1, self.query_length + 1):
        # diagonal score if match/mismatch
        if (self.query[j-1] == self.ref[i-1]):
          score = self.MATCH_SCORE
        else:
          score = self.MISMATCH_SCORE
          
        top       = self.matrix[i-1][j]   + self.GAP_SCORE
        left      = self.matrix[i][j-1]   + self.GAP_SCORE
        diagonal  = self.matrix[i-1][j-1] + score
        
        # sets the current row & column to max score between top, left, & diagonal
        self.matrix[i][j] = max(top, left, diagonal)  
    self.score = self.matrix[self.ref_length][self.query_length]    # score from the bottom right corner of the matrix
        
  def backtrack_matrix(self):
    '''
      Get back to the starting point (top left) from the end point (bottom right) by adding the
      GAP_SCORE/MATCH_SCORE/MISMATCH_SCORE to the current value and move up/left if they they match
      with the score from the up/left direction.
      
      @param  Nothing
      @return ( self.score,       The bottom right score of matrix
                ref_aligned,      Newly aligned ref
                query_aligned     Newly aligned query
              )
    '''
    ref_aligned   = ""
    query_aligned = ""
    
    i = self.ref_length   # row
    j = self.query_length # column
    
    while (i > 0 and j > 0):
      current_score   = self.matrix[i][j]
      diagonal_score  = self.matrix[i-1][j-1]
      left_score      = self.matrix[i][j-1]
      top_score       = self.matrix[i-1][j]
      
      if (self.ref[i-1] == self.query[j-1]):
        match_or_mismatch_score = self.MATCH_SCORE
      else:
        match_or_mismatch_score = self.MISMATCH_SCORE
        
      if (current_score == diagonal_score + match_or_mismatch_score): # matches with diagonal value
        i -= 1
        j -= 1
        ref_aligned   = self.ref[i] + ref_aligned
        query_aligned = self.query[j] + query_aligned
      elif (current_score == top_score + self.GAP_SCORE):             # matches with top value
        i -= 1
        ref_aligned   = self.ref[i] + ref_aligned
        query_aligned = "-" + query_aligned
      elif (current_score == left_score + self.GAP_SCORE):            # matches with left value
        j -= 1
        ref_aligned   = "-" + ref_aligned
        query_aligned = self.query[j] + query_aligned
    
    while (i > 0):  # fill the remaining i's with "-"
      i -= 1
      ref_aligned   = self.ref[i] + ref_aligned
      query_aligned = "-" + query_aligned
    
    while (j > 0):  # fill the remaining j's with "-"
      j -= 1
      ref_aligned   = "-" + ref_aligned
      query_aligned = self.query[j] + query_aligned
        
    if self.is_print_all_info:
      self.print_info(ref_aligned, query_aligned)
    return (self.score, ref_aligned, query_aligned)
      
  def print_info(self, ref_aligned, query_aligned):
    '''
      Prints out all necessary information, including ref, query, the aligned ref (ref_aligned), 
      and the aligned query (query_aligned).
      
      @param  ref_aligned         Aligned Needleman-Wunsch ref
      @param  query_aligned       Aligned Needleman-Wunsch query
      @return Nothing
    '''
    print("-----------------start--------------------")
    print("Ref:\t\t" + self.ref)
    print("\nQuery:\t\t" + self.query)
    print("\nAligned ref:\t" + ref_aligned)
    print("\nAligned query:\t" + query_aligned)
    print("\nScore:\t\t" + str(self.score))
    print(("------------------end---------------------"))


def get_matches(filename):
  '''
    Get all lines, except the first, and split each line by the tab, \t
    
    @param  ref_aligned         Aligned Needleman-Wunsch ref
    @param  query_aligned       Aligned Needleman-Wunsch query
    @return Nothing
  '''
  matches = []
  
  line_number = 0
  for line in open(filename, "r").readlines():
    if (line_number != 0):
      # convert all strings to int
      matches.append([int(i) for i in line.replace("\n", "").split("\t")])
    line_number += 1
  return matches
    
        
def anchored_nw(query, ref, matchfile):
  '''
    Iterates over the matches that were found by get_matches(), which uses the Needleman-Wunsch class
    based on the the starting and ending points in query and ref.
    
    @param query:     str query
    @param ref:       str ref
    @param matchfile: str existing matching file
    @return Nothing
  '''
  global_score = 0
  for each_match in get_matches(matchfile):
    cov1_start, cov1_end, cov2_start, cov2_end = each_match
    my_query = query[cov1_start-1:cov1_end]
    my_ref   = ref[cov2_start-1:cov2_end]
    
    nw = NW(my_query, my_ref)
    global_score += nw.score
  print("TOTAL GLOBAL SCORE:\t" + str(global_score))


def permute(query, ref, repeated_times):
  scores = []
  for x in range(repeated_times):
    permuted_query = ''.join(numpy.random.permutation(list(query)))
    permuted_ref   = ''.join(numpy.random.permutation(list(ref)))
    nw = NW(permuted_query, permuted_ref, is_print_all_info=False)
    scores.append(nw.score)
    print(nw.score)
  print("Total score: ", scores)
  
  return scores
  

def main(arguments):
  if ((len(arguments) == 3) or (len(arguments) == 4)):
    if (os.path.exists(arguments[1])):
      if (os.path.exists(arguments[2])):
        query  = open(arguments[1], "r").readlines()[1].replace("\n", '')
        ref    = open(arguments[2], "r").readlines()[1].replace("\n", '')
        if (len(arguments) == 3):
          # nw = NW(query, ref)
          permute(query, ref, 3)
        else:
          if (os.path.exists(arguments[3])):
            anw = anchored_nw(query, ref, arguments[3])
          else:
            print("Error: Unable to find `{file}` file.".format(file=arguments[3]))
      else:
        print("Error: Unable to find `{file}` file.".format(file=arguments[2]))
    else:
      print("Error: Unable to find `{file}` file.".format(file=arguments[1]))
  else:
    print("Error: use `Needleman_Wunsch <REQUIRED_file1> <REQUIRED_file2> <OPTIONAL_matches_file>`")
  
        
if __name__ == '__main__':
  main(sys.argv)
      