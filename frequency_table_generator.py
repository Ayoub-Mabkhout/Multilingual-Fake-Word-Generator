import numpy as np
import pandas as pd


def count_frequencies(language):

    file_path = f'./base words/words-{language}.txt'

    alphabet = []
    with open(file_path, encoding='utf-8') as words:
        for word in words:
            word = word.lower()
            for c in word:
                if c not in alphabet:
                    alphabet.append(c)
        alphabet.append(' ')
    alphabet.sort()
    print(alphabet)

    DIM = len(alphabet)
    count = np.zeros((DIM, DIM), dtype='int32')

    with open(file_path, encoding='utf-8') as words:
        for word in words:
            word = ' ' + word.lower()
            for c1, c2 in zip([alphabet.index(c) for c in word],
                              [alphabet.index(c) for c in word[1:]]):
                count[c1, c2] += 1
                # print(f'count[{alphabet[c1]},{alphabet[c2]}]={count[c1,c2]}')

    frequency_table = np.zeros((DIM, DIM), dtype='float64')
    for i in range(DIM):
        sum = 0

        for j in range(DIM):
            sum += count[i, j]

        if sum == 0:
            continue

        for j in range(DIM):
            frequency_table[i, j] = count[i, j] / sum

    df = pd.DataFrame(frequency_table, index=alphabet, columns=alphabet)
    out_path = f'./counts/table-{language}.xlsx'
    df.to_excel(out_path)


if __name__ == '__main__':
    language = 'german'
    count_frequencies(language)
