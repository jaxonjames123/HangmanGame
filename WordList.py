import random


def generate_word(word_min, word_max):
    words_processed = 0
    curr_word = None
    valid_word_list = []
    with open('words_alpha.txt', 'r') as f:
        for word in f:
            if word_min <= len(word) <= word_max:
                valid_word_list.append(word)
                words_processed += 1
                continue
        words = words_processed - 1
        random_num = random.randint(0, words)
        curr_word = valid_word_list[random_num]
        return curr_word
