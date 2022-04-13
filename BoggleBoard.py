
class BoggleBoard:

    def __init__(self, boardFilePath: str) -> None:
        #Generate the board from the lines in the passed file 
        boardFile = open(boardFilePath, "r")
        self.__board: list[list[str]] =  [char for line in boardFile.read() for char in line if char.isalpha()]
        if(len(self.__board) != 16):
            print("Invalid/Malformed board created ... ")
            raise ValueError
        boardFile.close()

    def __str__(self) -> str:
        return str(self.__board)
        