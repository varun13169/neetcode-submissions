class WordDictionary:

    def __init__(self):
        self.root = {}
        self.IS_THE_END = "IS_THE_END"
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if node.get(ch, None) == None:
                node[ch] = {}
            node = node[ch]
        node[self.IS_THE_END] = True

    def search(self, word: str) -> bool:
        lastNode = self.searchUtil(word, 0, self.root)
        if lastNode != None and lastNode.get(self.IS_THE_END, None) == True:
            return True
        else:
            return False
    
    def searchUtil(self, word, chIdx, root):
        if root == None:
            return None
        if chIdx == len(word):
            return root

        node = root
        ch = word[chIdx]
        if ch == '.':
            # iterate, because of wildcard
            for k in node.keys():
                if k == self.IS_THE_END:
                    # ignore
                    continue
                
                possibleNode = self.searchUtil(word, chIdx+1, node.get(k, None))
                if possibleNode != None and possibleNode.get(self.IS_THE_END, None) == True:
                    return possibleNode

        else:
            return self.searchUtil(word, chIdx+1, node.get(ch, None))


        
