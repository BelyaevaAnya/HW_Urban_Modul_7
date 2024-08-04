class WordsFinder:
    all_words = {}
    def __init__(self, *file_names: list):
        self.file_names = file_names

    def del_symbols(self, string: str):
        string = string.lower()
        remove_chars = ['=', '!', '?', ';', ':', ' - ', ',', '.']
        for del_char in remove_chars:
            if del_char in string:
                string = string.replace(del_char, '')
        string = string.split()
        return string

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file_obj:
                file_str = file_obj.read()
                file_str_lst = self.del_symbols(file_str)
                self.all_words.update({file_name: file_str_lst})
        return self.all_words

    def find(self, word: str):
        file_dict = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                file_dict.update({name: words.index(word) + 1})
        return file_dict

    def count(self, word: str):
        file_dict = {}
        count_word = 0
        word = word.lower()
        for name, words_lst in self.get_all_words().items():
            for wrd_lst in words_lst:
                if wrd_lst == word:
                    count_word += 1
            file_dict.update({name: count_word})
            count_word = 0
        return file_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
# =>
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))
# # {'Mother Goose - Monday’s Child.txt': ['monday’s', 'child', 'monday’s', 'child', 'is', 'fair', 'of', 'face', 'tuesday’s', 'child', 'is', 'full', 'of', 'grace', 'wednesday’s', 'child', 'is', 'full', 'of', 'woe', 'thursday’s', 'child', 'has', 'far', 'to', 'go', 'friday’s', 'child', 'is', 'loving', 'and', 'giving', 'saturday’s', 'child', 'works', 'hard', 'for', 'a', 'living', 'and', 'the', 'child', 'that', 'is', 'born', 'on', 'the', 'sabbath', 'day', 'is', 'bonny', 'and', 'blithe', 'and', 'good', 'and', 'gay', 'mother', 'goose']}
# # {'Mother Goose - Monday’s Child.txt': 2}
# # {'Mother Goose - Monday’s Child.txt': 8}

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))
#
# # {'Rudyard Kipling - If.txt': ['if', 'if', 'you', 'can', 'keep', 'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 'talk', 'too', 'wise', 'if', 'you', 'can', 'dream', '—', 'and', 'not', 'make', 'dreams', 'your', 'master', 'if', 'you', 'can', 'think', '—', 'and', 'not', 'make', 'thoughts', 'your', 'aim', 'if', 'you', 'can', 'meet', 'with', 'triumph', 'and', 'disaster', 'and', 'treat', 'those', 'two', 'impostors', 'just', 'the', 'same', 'if', 'you', 'can', 'bear', 'to', 'hear', 'the', 'truth', 'you’ve', 'spoken', 'twisted', 'by', 'knaves', 'to', 'make', 'a', 'trap', 'for', 'fools', 'or', 'watch', 'the', 'things', 'you', 'gave', 'your', 'life', 'to', 'broken', 'and', 'stoop', 'and', 'build', '’em', 'up', 'with', 'worn-out', 'tools', 'if', 'you', 'can', 'make', 'one', 'heap', 'of', 'all', 'your', 'winnings', 'and', 'risk', 'it', 'on', 'one', 'turn', 'of', 'pitch-and-toss', 'and', 'lose', 'and', 'start', 'again', 'at', 'your', 'beginnings', 'and', 'never', 'breathe', 'a', 'word', 'about', 'your', 'loss', 'if', 'you', 'can', 'force', 'your', 'heart', 'and', 'nerve', 'and', 'sinew', 'to', 'serve', 'your', 'turn', 'long', 'after', 'they', 'are', 'gone', 'and', 'so', 'hold', 'on', 'when', 'there', 'is', 'nothing', 'in', 'you', 'except', 'the', 'will', 'which', 'says', 'to', 'them', '‘hold', 'on’', 'if', 'you', 'can', 'talk', 'with', 'crowds', 'and', 'keep', 'your', 'virtue', 'or', 'walk', 'with', 'kings', '—', 'nor', 'lose', 'the', 'common', 'touch', 'if', 'neither', 'foes', 'nor', 'loving', 'friends', 'can', 'hurt', 'you', 'if', 'all', 'men', 'count', 'with', 'you', 'but', 'none', 'too', 'much', 'if', 'you', 'can', 'fill', 'the', 'unforgiving', 'minute', 'with', 'sixty', 'seconds’', 'worth', 'of', 'distance', 'run', 'yours', 'is', 'the', 'earth', 'and', 'everything', 'that’s', 'in', 'it', 'and', '—', 'which', 'is', 'more', '—', 'you’ll', 'be', 'a', 'man', 'my', 'son', 'rudyard', 'kipling']}
# # {'Rudyard Kipling - If.txt': 1}
# # {'Rudyard Kipling - If.txt': 14}

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
# # {'Walt Whitman - O Captain! My Captain!.txt': ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman']}
# # {'Walt Whitman - O Captain! My Captain!.txt': 2}
# # {'Walt Whitman - O Captain! My Captain!.txt': 10}

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                        'Rudyard Kipling - If.txt',
#                        'Mother Goose - Monday’s Child.txt')
#
# dict1 = finder1.get_all_words()
# for key in dict1:
#     print(f'{key}')
#     print(f'{dict1[key]}\n')
# # Все не печатает, т.к. указывает ошибку, что слишком много значений
# # print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
# # Walt Whitman - O Captain! My Captain!.txt
# # ['o', 'captain', 'my', 'captain', 'o', 'captain', 'my', 'captain', 'our', 'fearful', 'trip', 'is', 'done', 'the', 'ship', 'has', 'weather’d', 'every', 'rack', 'the', 'prize', 'we', 'sought', 'is', 'won', 'the', 'port', 'is', 'near', 'the', 'bells', 'i', 'hear', 'the', 'people', 'all', 'exulting', 'while', 'follow', 'eyes', 'the', 'steady', 'keel', 'the', 'vessel', 'grim', 'and', 'daring', 'but', 'o', 'heart', 'heart', 'heart', 'o', 'the', 'bleeding', 'drops', 'of', 'red', 'where', 'on', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'o', 'captain', 'my', 'captain', 'rise', 'up', 'and', 'hear', 'the', 'bells', 'rise', 'up', '—', 'for', 'you', 'the', 'flag', 'is', 'flung', '—', 'for', 'you', 'the', 'bugle', 'trills', 'for', 'you', 'bouquets', 'and', 'ribbon’d', 'wreaths', '—', 'for', 'you', 'the', 'shores', 'acrowding', 'for', 'you', 'they', 'call', 'the', 'swaying', 'mass', 'their', 'eager', 'faces', 'turning', 'here', 'captain', 'dear', 'father', 'this', 'arm', 'beneath', 'your', 'head', 'it', 'is', 'some', 'dream', 'that', 'on', 'the', 'deck', 'you’ve', 'fallen', 'cold', 'and', 'dead', 'my', 'captain', 'does', 'not', 'answer', 'his', 'lips', 'are', 'pale', 'and', 'still', 'my', 'father', 'does', 'not', 'feel', 'my', 'arm', 'he', 'has', 'no', 'pulse', 'nor', 'will', 'the', 'ship', 'is', 'anchor’d', 'safe', 'and', 'sound', 'its', 'voyage', 'closed', 'and', 'done', 'from', 'fearful', 'trip', 'the', 'victor', 'ship', 'comes', 'in', 'with', 'object', 'won', 'exult', 'o', 'shores', 'and', 'ring', 'o', 'bells', 'but', 'i', 'with', 'mournful', 'tread', 'walk', 'the', 'deck', 'my', 'captain', 'lies', 'fallen', 'cold', 'and', 'dead', 'walt', 'whitman']
# #
# # Rudyard Kipling - If.txt
# # ['if', 'if', 'you', 'can', 'keep', 'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 'talk', 'too', 'wise', 'if', 'you', 'can', 'dream', '—', 'and', 'not', 'make', 'dreams', 'your', 'master', 'if', 'you', 'can', 'think', '—', 'and', 'not', 'make', 'thoughts', 'your', 'aim', 'if', 'you', 'can', 'meet', 'with', 'triumph', 'and', 'disaster', 'and', 'treat', 'those', 'two', 'impostors', 'just', 'the', 'same', 'if', 'you', 'can', 'bear', 'to', 'hear', 'the', 'truth', 'you’ve', 'spoken', 'twisted', 'by', 'knaves', 'to', 'make', 'a', 'trap', 'for', 'fools', 'or', 'watch', 'the', 'things', 'you', 'gave', 'your', 'life', 'to', 'broken', 'and', 'stoop', 'and', 'build', '’em', 'up', 'with', 'worn-out', 'tools', 'if', 'you', 'can', 'make', 'one', 'heap', 'of', 'all', 'your', 'winnings', 'and', 'risk', 'it', 'on', 'one', 'turn', 'of', 'pitch-and-toss', 'and', 'lose', 'and', 'start', 'again', 'at', 'your', 'beginnings', 'and', 'never', 'breathe', 'a', 'word', 'about', 'your', 'loss', 'if', 'you', 'can', 'force', 'your', 'heart', 'and', 'nerve', 'and', 'sinew', 'to', 'serve', 'your', 'turn', 'long', 'after', 'they', 'are', 'gone', 'and', 'so', 'hold', 'on', 'when', 'there', 'is', 'nothing', 'in', 'you', 'except', 'the', 'will', 'which', 'says', 'to', 'them', '‘hold', 'on’', 'if', 'you', 'can', 'talk', 'with', 'crowds', 'and', 'keep', 'your', 'virtue', 'or', 'walk', 'with', 'kings', '—', 'nor', 'lose', 'the', 'common', 'touch', 'if', 'neither', 'foes', 'nor', 'loving', 'friends', 'can', 'hurt', 'you', 'if', 'all', 'men', 'count', 'with', 'you', 'but', 'none', 'too', 'much', 'if', 'you', 'can', 'fill', 'the', 'unforgiving', 'minute', 'with', 'sixty', 'seconds’', 'worth', 'of', 'distance', 'run', 'yours', 'is', 'the', 'earth', 'and', 'everything', 'that’s', 'in', 'it', 'and', '—', 'which', 'is', 'more', '—', 'you’ll', 'be', 'a', 'man', 'my', 'son', 'rudyard', 'kipling']
# #
# # Mother Goose - Monday’s Child.txt
# # ['monday’s', 'child', 'monday’s', 'child', 'is', 'fair', 'of', 'face', 'tuesday’s', 'child', 'is', 'full', 'of', 'grace', 'wednesday’s', 'child', 'is', 'full', 'of', 'woe', 'thursday’s', 'child', 'has', 'far', 'to', 'go', 'friday’s', 'child', 'is', 'loving', 'and', 'giving', 'saturday’s', 'child', 'works', 'hard', 'for', 'a', 'living', 'and', 'the', 'child', 'that', 'is', 'born', 'on', 'the', 'sabbath', 'day', 'is', 'bonny', 'and', 'blithe', 'and', 'good', 'and', 'gay', 'mother', 'goose']
# #
# # {'Walt Whitman - O Captain! My Captain!.txt': 14, 'Rudyard Kipling - If.txt': 109, 'Mother Goose - Monday’s Child.txt': 41}
# # {'Walt Whitman - O Captain! My Captain!.txt': 18, 'Rudyard Kipling - If.txt': 7, 'Mother Goose - Monday’s Child.txt': 2}
