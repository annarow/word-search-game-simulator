"""
File: word_grid.py
Author: Anna Rowena Waldron
Purpose: The purpose of this program is to create a word grid of an inputed
length with random letters. 
Section: Section 1G, CSC 120 Spring 2018

"""
"""
Function main calls all other functions inint, with called returned value N,
make_grid, with called return value G and print_grid. Imports random functions.
"""

import random
def main():
    N = inint()
    G = make_grid(N)
    print_grid(G)
"""
Function inint uses user input to determine the random seed S and the N integer
of the length of the grid. initiates the random seed S and returns the integer
N.
"""
def inint():
    N = int(input())
    S = input()
    random.seed(S)
    return N

"""
Function make_grid takes in parameter integer N and creates a string of the
alaphabet to then create a list of letters corresponding to integers from
0 to 25. returns the list of random letters G.
"""
def make_grid(N):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    z = []
    for e in alpha:
       z.append(e)
    G = []
    for i in range(N):
        lis = []
        for j in range(N):
            x = random.randint(0, 25)
            lis.append(z[x])
        G.append(lis)
    return G
"""
Function print_grid takes parameter G list of list of letters and prints
the letters in a grid with commas using a fencepost function.
"""
def print_grid(G):
    for i in range(len(G)):
        print(G[i][0], end='')
        for j in range(1, len(G[i])):
            print("," + G[i][j], end='')
        print()
"""
Calls main.
"""
main()
