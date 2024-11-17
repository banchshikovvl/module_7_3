class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        not_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            line_split = []
            with open(i, encoding='utf - 8') as file:
                for j in file:
                    lower_line = j.lower()
                    line_join = ''.join([c for c in lower_line if c not in not_list])
                    line_split.extend(line_join.split())
                all_words[str(i)] = line_split
        return all_words

    def find(self, word):
        self.word = word.lower()
        tuple_ = {}
        a = self.get_all_words()
        for key, value in a.items():
            if self.word in value:
                tuple_[key] = value.index(self.word) + 1
        return print(tuple_)

    def count(self, word):
        self.word = word.lower()
        tuple_ = {}
        a = self.get_all_words()
        for key, value in a.items():
            if self.word in value:
                tuple_[key] = value.count(self.word)
        return print(tuple_)


finder2 = WordsFinder('test.txt', 'test2.txt')
finder2.get_all_words()
print(finder2.get_all_words())
finder2.find('teXt')
finder2.count('Text')
finder2.find('Осень')
finder2.count('Осень')
