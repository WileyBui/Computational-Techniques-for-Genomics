#!/usr/bin/env python3

import sys
import os

def get_codon_dictionary(codon_dictionary, string):
    """ Returns a dictionary with codon as key and its frequency as value """
    
    # iterates on every 3th item; remove remainders by: len(string) - len(string) % 3
    for i in range(0, len(string) - len(string) % 3, 3):
        codon = "{first}{second}{third}".format(first=string[i], second=string[i+1], third=string[i+2])
        
        if codon in codon_dictionary:
            codon_dictionary[codon] += 1
        else:
            codon_dictionary[codon] = 1
    return codon_dictionary


if __name__ == "__main__":
    arguments = sys.argv

    # checks for input command arguments: count_codons input.fna output.csv
    if (len(arguments) == 3):
        # checks if input file exists
        if (os.path.exists(arguments[1])):
            codon_dictionary    = {}
            input_file          = open(arguments[1], "r")
            output_file         = open(arguments[2], "w+")
            
            # iterates through each line in input file
            for line in input_file.readlines():
                line = line.replace("\n", '')
                
                # ignores lines that are empty or starts with ">"
                if ((len(line) > 0) and (">" not in line)):
                    codon_dictionary = get_codon_dictionary(codon_dictionary, line)

            # sorts & iterates the dictionary by values from highest to lowest
            # then write them to the output file
            for key in sorted(codon_dictionary, key=codon_dictionary.get, reverse=True):
                output_file.write("{codon},{counter}\n".format(codon=key, counter=codon_dictionary[key]))
            output_file.close()

        else:
            print("Error: Could not find the `{file}` input file.".format(file=arguments[1]))
    else:
        print("Command error, use: count_codons <input file> <output file>")
