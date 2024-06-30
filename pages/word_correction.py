import streamlit as st
from levelshtein_distance import levenshtein_distance


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab('data/vocab.txt')


def main():
    st.title(" Word Correction using Levenshtein Distance ")
    word = st.text_input('Word: ')
    # press the button to compute the levenshtein distance

    if st.button("Compute"):
        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(),
                                       key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word:', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary: ')
        col1.write(vocabs)
        col2.write('Distances: ')
        col2.write(sorted_distences)


if __name__ == "__main__":
    main()
