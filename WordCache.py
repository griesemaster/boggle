from wordTree import wordTree


class WordCache: 

    #Constructed from existing set of words
    def __init__(self) -> None:
        self.__words = set()
   
    #returns true if the item is contained in the set of all words
    def contains(self, item: str) -> bool:
        return item in self.__words

    #adds the passed item to the set
    def add(self, item: str) -> None:
        self.__words.add(item)

    #sorts the held words into alphabetical order and then writes them to file
    def dumpWords(self, dumpPath: str) -> None:
        outFile = open(dumpPath, "w")
        for word in sorted(self.__words): outFile.write(word.lower() + "\n")
        outFile.close()