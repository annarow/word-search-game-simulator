"""
File: word_search.py
Author: Anna Rowena Waldron
Purpose: The purpose of this program is to read a grid of letters and determine
if there are any real words.
Section: Section 1G, CSC 120 Spring 2018

"""

"""
Function main takes all other functions with their parameters and returned
values in one concise summary. Takes function read_files with a file parameter,
horizontal_search twice with the large wordlist and lis of lists parameters and
real_words list as its' return.
Function occurs_in twice with real_words list and words_list as its parameter
with occured string as its returned.
"""
def main():
    word_list, G = read_files(file)
    real_words = horizontal_search(G)
    occured = occurs_in(real_words, word_list)
    D = reverse_horizontal(G)
    real_words = horizontal_search(D)
    occured = occurs_in(real_words, word_list)

"""
Function reverse_horizontal taking parameter G, list of lists with letters,
that makes a new list of lists but in reverse order and then returns said list.
"""
def reverse_horizontal(G):
    D = []
    for i in range(len(G)):
        lis = []
        for j in range(1, len(G) + 1):
            if j == 0:
                lis.append(G[i][-1])
            else:
                lis.append(G[i][-j])
        D.append(lis)            
    return D    

"""
Function read_files takes the parameter file and creates two lists: one list
using the files WORDS.txt for all real words and then creates another list
of lists for letters in the grid that is passed by the parameter. returns
both lists word_list and G.
"""
def read_files(file):
    word_list = open("WORDS.txt").readlines()
    for e in range(len(word_list)):
        word_list[e] = word_list[e].strip().lower()
    grid_of_letters = open(file).readlines()
    G = []
    for i in range(len(grid_of_letters)):
        grid_of_letters[i] = grid_of_letters[i].strip()
        s = []
        for j in range(len(grid_of_letters[i])):
            if grid_of_letters[i][j] != " ":
                s.append(grid_of_letters[i][j])
        G.append(s)
    return word_list, G

"""
Function horizontal_search takes parameter G which is a list of lists and
creates a new list to store strings of lengths 3  until the length of the list.
then returns real_words. 
"""
def horizontal_search(G):
    real_words = []
    for i in range(len(G)):
        start = 0
        stop = 3
        while start != (len(G) - 2):
            while stop != len(G) + 1:
                string = ''
                for j in range(start, stop):
                    string += G[i][j]
                
                real_words.append(string)
                stop += 1
            start += 1
            stop = start + 3
    return real_words
        
"""
Function occurs_in takes in parameters S, a list of strings created from
the previous function horizontal_search and the word list L and creates
a new string of words in S that are found in L using a for loop. Returns
the string occured.
"""

def occurs_in(S, L):
    occured = ""
    for e in L:
        for string in S:
            if string == e:
                occured += string
    return occured
"""
Calls function main.
"""
main()
