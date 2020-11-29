import sys
import os
import numpy as np
import matplotlib.pyplot as plt

def get_sequences_from_file(filename):
  sequences = []
  
  line_number = 0
  for line in open(filename, "r").readlines():
    if (line_number % 2 == 1):
      sequences.append(line.strip())
    line_number += 1
  return sequences

def calculate_conservation_rate(sequences):
  """
  Calculates the average identity (or fraction of most common base) at each position in the
    gapped alignment.
  """
  positions = {}
  for sequence in sequences:
    for i in range(len(sequence)):
      sequence = sequence.upper()
      if i not in positions:
        positions[i] = [0, 0, 0, 0]  # initializes the counts for A, C, G, and T
      
      # increments the conserved character from the non-gap character (A, C, G, or T)
      #   "-" and other ambiguous bases (B, D, H, K, ...) are considered as gaps
      if sequence[i]    == "A":
        positions[i][0] += 1
      elif sequence[i]  == "C":
        positions[i][1] += 1
      elif sequence[i]  == "G":
        positions[i][2] += 1
      elif sequence[i]  == "T":
        positions[i][3] += 1
        
  total_length = len(sequences)
  sequence_identity_percentages = []
  output_file = open("solution-problem-1.txt", "w+")
  
  for i in positions:
    max_value = max(positions[i])                                   # gets max value from [A, C, G, T]
    value_to_be_saved = (max_value / (total_length + 0.0)) * 100    # 0.0 for float rounding purposes
    sequence_identity_percentages.append(value_to_be_saved)         # gets percentages of sequence identity
    output_file.write(str(value_to_be_saved) + "\n")                # writes sequence identity to file
    
  output_file.close()
  return sequence_identity_percentages

def smooth(y, box_pts):
  """
  This function is from https://stackoverflow.com/a/26337730,
    which smooths out the data by the sliding window average method.
  """
  box = np.ones(box_pts)/box_pts
  y_smooth = np.convolve(y, box, mode='same')
  return y_smooth
  
def cluster(data, maxgap):
  """
  This function is from https://stackoverflow.com/a/14783998,
    which arranges data into groups where successive elements
    differ by no more than *maxgap*.
  """
  data.sort()
  groups = [[data[0]]]
  for x in data[1:]:
      if abs(x - groups[-1][-1]) <= maxgap:
          groups[-1].append(x)
      else:
          groups.append([x])
  return groups
  
def plot_rate(sequence_identity_percentages, percent_separator = -1):
  """
  Plots out the variability (% sequence identity) against the position in the
    gapped alignment by first calling smooth() to smoothing out the data. Then
    plots and saves it to a pdf file.
  If the 2nd argument is passed in, we form clusters of data for the variable regions
    by filtering the confidence value first then call the cluster() function to group
    data together.
  """
  x = [x for x in range(len(sequence_identity_percentages))]  # position in the gapped alignment
  y = sequence_identity_percentages                           # variablity

  plt.rcParams['axes.xmargin'] = 0        # removes margin
  plt.figure(figsize=(20, 5))             # expands graph
  plt.plot(x, smooth(y, 30), 'b-', lw=1)  # plots out the smoothed data

  # Adds title & labels
  plt.title("Percent Conserved vs Gene Position", fontsize=23)
  plt.xlabel("Gene Position", fontsize=17)
  plt.ylabel("Percent Conserved", fontsize=17)
  
  if (percent_separator != -1):           # plots the selected variable regions
    data_below_x_sequence_identity = []
    output_file = open("solution-problem-3.txt", "w+")
    
    # filters all the positions that are less than the sequence identity's percent_separator
    #   meaning values that are below the confidence value (percent_separator), then it's 
    #   part of a variable region.
    data_below_x_sequence_identity = [index for index in x if y[index] < percent_separator]
    
    groups = cluster(data_below_x_sequence_identity, 8) # groups the data together
    
    for group in groups:
      if len(group) > 15:     # picks groups that have more than 15 plots in a group
        starting = group[0]   # 1st element in a group
        ending   = group[-1]  # last element
        
        plt.plot([starting, ending], [50, 50], 'r-', lw=3)
        output_file.write("{}\t{}\n".format(str(starting), str(ending)))
  
    output_file.close()
  
    # adds chart legend & saves it to a pdf file
    legend1 = plt.plot([0], 'b-', label='Sliding window average')
    legend2 = plt.plot([0], 'r-', label='Variable region', lw=3)
    plt.legend([legend1[0], legend2[0]], ['Sliding window average', 'Variable region'], loc="lower left")
    plt.savefig('solution-problem-4.pdf')
  else:
    plt.savefig('solution-problem-2.pdf')
  return
  
def main(arguments):
  if (len(arguments) == 2):
    if (os.path.exists(arguments[1])):
      # read the sequences from a file, then 
      sequences = get_sequences_from_file(arguments[1])
      sequence_identity_percentages = calculate_conservation_rate(sequences)
      plot_rate(sequence_identity_percentages)
      plot_rate(sequence_identity_percentages, percent_separator=70)
    else:
      print("Error: Unable to find `{}` file.".format(file=arguments[1]))
  else:
    print("Error: use `python3 Variable_Genomic_Regions.py <REQUIRED_INPUT_FILE.fna>`")
  
if __name__ == '__main__':
  main(sys.argv)