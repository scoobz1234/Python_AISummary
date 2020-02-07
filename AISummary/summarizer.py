import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq


def nltk_summarizer(text):
    # Set our stop words to the english dictionary stopwords
    stop_words = set(stopwords.words("english"))
    # Initialize our word frequency array
    word_freq = {}
    # Loop through each word in the text after its tokenized
    for word in nltk.word_tokenize(text):
        # If the word is NOT in stopwords
        if word not in stop_words:
            # and if the word is NOT in the word frequency array
            if word not in word_freq.keys():
                # then we set the word frequency of that word to 1
                word_freq[word] = 1
            else:
                # else, we have multiple occurrences and we add 1 to the frequency
                word_freq[word] += 1
    # After we get the frequencies, we set a variable to the word that is found the MOST
    max_freq = max(word_freq.values())

    # For each word in the word frequency array, we set the word to its occurrence divided by the max occurrence
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word] / max_freq)

    # Now we create a sentence list and set it to the tokenized sentence
    sentence_list = nltk.sent_tokenize(text)
    # Initialize the sentence scores array
    sentence_scores = {}
    # For each sentence in the sentence list
    for sent in sentence_list:
        # and for each word in the tokenized sentence
        for word in nltk.word_tokenize(sent.lower()):
            # if the word is present in word frequency list
            if word in word_freq.keys():
                # and if the length of the sentence split is less than 30
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        # the score = the word frequency
                        sentence_scores[sent] = word_freq[word]
                    else:
                        # else the score adds the word frequency
                        sentence_scores[sent] += word_freq[word]

    # create the summary sentences
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    # Add all the sentences together and make a paragraph.
    summary = ' '.join(summary_sentences)
    return summary
