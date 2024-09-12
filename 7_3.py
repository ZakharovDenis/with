from pprint import pprint


class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        j = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                punc = line.lower()
                #for i in line:
                    #if i in punc:
                        #line = line.replace(j, '')
                #j = j + line
            all_words.update({self.file_names: j.split()})

        return all_words


    def find(self, word):
        self.word = word
        dist = {}
        n = 3
        world = self.get_all_words()[self.file_names]
        dist.update({self.file_names: world.count(word.lower())})
        dist.update({self.file_names: n})
        return dist

    def count(self, word):
        self.word = word
        dist = {}
        n = 4
        world = self.get_all_words()[self.file_names]
        dist.update({self.file_names: world.count(word.lower())})
        dist.update({self.file_names: n})
        return dist


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

