# The goal of this exercise is to implement the game of Boggle.
# Game Rules:
# 1) The game board is 4 x 4 board of the letters A - Z.
# 2) The same letter may appear on the board more than once.
# 3) A player tries to make as many words as possible from the letters on the board.
# 4) Words are formed by sequencing together adjacent letters horizontally, vertically, and diagonally.
# 5) Each letter on the board may only be used once in each word.
# 6) Words must be at least 3 letters long.
# 7) On the board, the letter Q is always treated as QU.
# 8) A word, even if formed multiple ways on the board, only counts once.
#
# Programming exercise:
# 1) Your program will be passed 3 arguments: input board file name; input dictionary file name; output result file name.
# 2) The board file is a text file.  Each line in the text file is a row on the board.  Each letter on a row corresponds
#    to a column on the board.  Whitespace may or may not 1be used to separate letters.
# 3) The dictionary file is a text file with one word per line.
# 4) The output file should be written by your program.  This file should contain each dictionary word that your program
#    can find on the board, and write that word in lowercase, one word per line.  The words should be written in alphabetical
#    order.
#
# Your code should be suitable for production.  When returning your solution, please include all source code and information
# regarding the intepreter and platform you used for development (for example: Windows 10, Python 3.7.8 64-bit).
# DO NOT send compiled executables.
#
# Please don't distribute this exercise or your solution publicly.  If you decide to develop this in your github, for example,
# please keep it private.

import sys

from BoggleBoard import BoggleBoard
from wordTree import wordTree

def main():
    args = sys.argv[1:]
    
    args = ["board-sample-1.txt", "dictionary.txt", "myOut.txt"]

    if len(args) < 3:
        sys.exit("Usage: Boggle.py <board file> <dictionary file> <output file>")

    boardFile: str = args[0]
    dictFile: str = args[1]
    outFile: str = args[2]

    #Create the game board and the valid words
    ValidWords: wordTree = wordTree(dictFile)
    GameBoard: BoggleBoard = BoggleBoard(boardFile, ValidWords)
    GameBoard.play().dumpWords(outFile)

if __name__ == '__main__':
    main()
