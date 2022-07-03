import numpy as np
import pandas as pd


def generate_word(language, min_len=4, max_len=11, start_letter=None):

    try:
        language = language.lower()
        # loading frequency table and corresponding alphabet
        # from excel file in './count' directory
        file_path = f'./counts/table-{language}.xlsx'
        df = pd.read_excel(file_path, index_col=0)
        alphabet = df.index.to_list()
        print(alphabet)
        frequency_table = df.to_numpy()

        # loading a dictionary of all existing words
        # for generated words to be compared with
        dictionary = []
        with open(f'./base words/words-{language}.txt', encoding='utf-8') as f:
            dictionary = [word.rstrip() for word in f]
    except (Exception):
        raise Exception('Invalid argument: language')

    if max_len < min_len:
        raise Exception(f'Invalid arguments: min_len ({min_len}) is ' +
                        f'greater than max_len ({max_len}).')

    MAX_ATTEMPTS = 500

    # limited number of attemps to generate
    # a word with the specified parameters
    for i in range(MAX_ATTEMPTS):
        # if a user specified a starting letter as a parameter,
        # then that would be the starting letter for our fake word
        # otherwise pick a starting letter at random
        # following frequency probabilities
        if start_letter:
            next_letter = start_letter
        else:
            next_letter = np.random.choice(
                alphabet, p=frequency_table[alphabet.index(' ')])
        if next_letter not in alphabet:
            raise Exception(
                f'Error: \'{next_letter}\' is not a valid character')
        word = ''
        # generating a word by generating random letters
        # until the '\n' character is generated
        while (next_letter != '\n'):
            word = word + next_letter
            next_letter = np.random.choice(
                alphabet, p=frequency_table[alphabet.index(next_letter)])
        # if word meets specified criteria, return it.
        # otherwise repeat until a word that meets
        # the specified criteria is generated
        if len(word) >= min_len and len(
                word) <= max_len and word not in dictionary:
            return word.capitalize()

    raise Exception(
        'Failure: Could not generate a word with the specified criteria.')


if __name__ == '__main__':
    generate_word('french', min_len=8, max_len=11, start_letter='m')
