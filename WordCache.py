class WordCache: 

    #Start with empty __containedWords
    def __init__(self) -> None:
        pass

    #Constructed from existing set of words
    def __init__(self, PathToWordList: str) -> None:
        #Generate word list from the passed file 
        wordFile = open(PathToWordList, "r")
        self.__containedWords : set = {word.strip() for word in wordFile.readlines()}
        wordFile.close()

    def __str__(self) -> str:
        return str(self.__containedWords)

    def contains(self, word: str) -> bool:
        return word in self.__containedWords

    def add(self, newWord: str) -> None:
        self.__containedWords.add(newWord)