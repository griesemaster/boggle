class wordTree:

    class node:
        def __init__(self, wordEnd: bool = False) -> None:
            self.isWord: bool = False
            self.children: list[str] = [None] * 26

    #Changes a character to a number based on the offset from 'a'. Allows 0-25 indexing of letters.
    def ordinal(self, char: str) -> int:
        return ord(char) - ord('a')

    #create a root node with empty values and then insert all words from file into tree
    def __init__(self, pathToDict: str) -> None:
        self.root = self.node()
        if pathToDict is not None:
            wordFile = open(pathToDict, "r")
            for word in wordFile.readlines(): self.insert(word.strip())
            wordFile.close()
   

    #insert the word into the tree, creating any new nodes as needed
    def insert(self, newWord: str) -> None:
        newWord = newWord.lower()
        currentNode : self.node = self.root
        for charIndex in range(len(newWord)):
            #if no node is present for this letter then add a new node
            if not currentNode.children[self.ordinal(newWord[charIndex])]:
                currentNode.children[self.ordinal(newWord[charIndex])] = self.node()
            currentNode = currentNode.children[self.ordinal(newWord[charIndex])]
        #once all nodes are in place, label the node as valid word and insert the word for easy access
        currentNode.isWord = True

    def getNode(self, sequence: str) -> node:
        currentNode: self.node = self.root
        for char in sequence:
            #if the node is not present, the word is not in the tree
            if not currentNode.children[self.ordinal(char)]:
                return None
            currentNode = currentNode.children[self.ordinal(char)]
        return currentNode

    #determines if a word is in the tree or not, must be a valid word per the dictionary (and longer than len 3)
    def containsWord(self, word: str) -> bool:
        #short circuit to prevent un-needed tree traversal (all valid words are 3 char or longer)
        if(len(word) < 3): return False
        return self.getNode(word) is not None and self.getNode(word).isWord 
    
    #Determines if a char sequence is in the tree or not, does not need to be a terminated word
    def containsSequence(self, sequence: str) -> bool:
        return self.getNode(sequence) is not None