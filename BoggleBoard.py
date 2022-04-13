from WordCache import WordCache
from wordTree import wordTree


class BoggleBoard:

    #Creates a board instance with WordCache of valid words and a list of letters representing the board in a 1d list.
    def __init__(self, boardFilePath: str, validWords: wordTree) -> None:
        self.__dict: wordTree = validWords
        self.__containedWords: wordTree = WordCache()
        #Generate the board from the lines in the passed file 
        boardFile = open(boardFilePath, "r")
        self.__board: list[list[str]] =  [char for line in boardFile.read() for char in line if char.isalpha()]
        if(len(self.__board) != 16):
            print("Invalid/Malformed board created ... ")
            raise ValueError
        boardFile.close()

    #checks if a given x, y pair are a valid coordinate
    def isValidLocation(self, x: int, y: int) -> bool:
        if not 0 <= x < 4 or not 0 <= y < 4: return False
        desiredIndex: int = x + (y * 4)
        if (desiredIndex < 0) or desiredIndex > (len(self.__board) - 1): return False
        return True

    #gets the character on the board at a given x,y location. Returns None if invalid location. Accounts for Q = QU 
    def getCharAt(self, x: int, y:int) -> str:
        if not self.isValidLocation(x, y):
            return None
        char: str = self.__board[x+ (y * 4)]
        #If the character is a Q, then return QU per the rules
        if char == "q":
            char += "u"
        return char
    
    #sets the character at a given x,y position to a new character if the coordinates are valid
    def setCharAt(self, x: int, y:int, newChar: str) -> None:
        if self.isValidLocation(x, y):
            self.__board[x + (y * 4)] = newChar

    #go down until the sequence is no longer in the tree, as you go back up check if the sequence is a word at each step 
    def dfs(self, x: int, y:int, sequence: str) -> None:
        #If the tree contains no sequences with this char string, then return as there are no further words down this path
        #If this is not a valid x,y location, then return as there is nothing here
        if not self.__dict.containsSequence(sequence) or not self.isValidLocation(x, y):
            return
        #The tree does contain this sequence replace this char with an invalid one (prevent repeat use) and continue DFS on all surrounding cells
        else:
            actualCharacter: str = self.getCharAt(x, y)
            self.setCharAt(x, y, "!")
            #iterate over the immeadiate surrounding cells
            for xOffset in range(-1, 2):
                for yOffset in range(-1, 2):
                    nextX: int = x + xOffset
                    nextY: int = y + yOffset
                    nextChar: str = self.getCharAt(nextX, nextY)
                    #If there is a valid character present at that location then continue DFS there
                    if(nextChar is not None and nextChar.isalpha()): self.dfs(x + xOffset, y + yOffset, sequence + nextChar)

            #Now we are on the way up, returning from the recursive calls. 
            #restore the character
            self.setCharAt(x, y, actualCharacter)
            # Add any valid words to the cache and then return
            if self.__dict.containsWord(sequence): self.__containedWords.add(sequence)
            return

    #triggers simulation and generates all valid strings. Kicks off a DFS on each starting tile on the board.
    def play(self) -> WordCache:
        for y in range(4):
            for x in range (4):
                self.dfs(x, y, self.getCharAt(x, y))
        return self.__containedWords

