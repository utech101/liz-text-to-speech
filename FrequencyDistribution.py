import spacy
from collections import Counter


class FrequencyDistribution:
    # Function returns the frequency distribution of all tokens present in the text
    @staticmethod
    def tokenDistribution(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        token = [token.text for token in doc if not token.is_stop and not token.is_punct]
        return Counter(token).most_common(5)

    # Function returns the frequency distribution of all nouns present in the text
    @staticmethod
    def nounDistribution(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        nounToken = [token.text for token in doc if (not token.is_stop and not token.is_punct and token.pos_ == "NOUN")]
        return Counter(nounToken).most_common(5)
