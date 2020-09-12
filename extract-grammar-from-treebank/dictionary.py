
class Dictionary:
    
    """POS TAG: {word}"""

    def __init__(self, tag):

        self.upostag = tag
        self.words = []

    @staticmethod
    def mkTagList(trees):

        taglist = []
        for tree in trees:

            for node in tree.sentence:

                if node.UPOSTAG not in taglist:
                    tag = Dictionary(node.UPOSTAG)
                    taglist.append(tag)

        return taglist

        return taglist