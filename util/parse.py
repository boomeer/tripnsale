class ParsedWord:
    def __init__(self, word):
        self.word = word

    def isLink(self):
        return 0 in [self.word.find(pref) for pref in ["http://", "https://"]]


class ParsedLine:
    def __init__(self, line):
        self.words = [ParsedWord(word) for word in line.split(" ")]


class ParsedText:
    def __init__(self, content):
        self.lines = [ParsedLine(line) for line in content.split("\n")]
