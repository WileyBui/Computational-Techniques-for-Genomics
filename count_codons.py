#!/usr/bin/python

import sys, os

def get_codon_counter(codon_dictionary, string):
  # iterates on every 3th term; remove remainder by: len(string) - len(string) % 3
  for i in range(0, len(string) - len(string) % 3, 3):
    codon = "{first}{second}{third}".format(first=string[i], second=string[i+1], third=string[i+2])
    if codon in codon_dictionary:
      codon_dictionary[codon] += 1
    else:
      codon_dictionary[codon] = 1
      
  # sorts the dictionary by the value
  return codon_dictionary

if __name__ == "__main__":
  arguments = sys.argv
  
  # checks for input command arguments: count_codons input.fna output.csv
  if (len(arguments) == 3):
    # checks if input file exists
    if (os.path.exists(arguments[1])):
      
      input_file = open(arguments[1], "r")
      codon_dictionary = {}
      for line in input_file.readlines():
        # removes the new line on every line
        line = line.replace("\n", '')
        if ((len(line) > 0) and (">" not in line)):
          output_file = open(arguments[2],"w+")
          codon_dictionary = get_codon_counter(codon_dictionary, line)
          
      # sorts & iterates the dictionary by the value from highest to lowest
      for key in sorted(codon_dictionary, key=codon_dictionary.get, reverse=True):
        output_file.write("{codon},{counter}\n".format(codon=key, counter=codon_dictionary[key]))
      output_file.close()
      
    else:
      print("Error: Could not find the `{file}` input file.".format(file=arguments[1]))
  else:
    print("Command error, use: <python file name> <input file> <output file>")