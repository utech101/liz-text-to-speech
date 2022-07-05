import spacy


class Tokenizer:

    # Function returns all the tokens present in the text
    @staticmethod
    def tokenizeText(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token.text for token in doc]

    # Function returns all the sentence tokens in the text
    @staticmethod
    def tokenizeSentence(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return list(doc.sents)

    # Function returns the n number of tokens grouped
    @staticmethod
    def tokenizeNGrams(text, n):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        tokens = [str(token) for token in doc]
        return [tokens[i:i + n] for i in range(len(tokens) - n + 1)]

    # Function removes all the stop words present in the text
    @staticmethod
    def removeStopWords(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        tokens = [token.text for token in doc]
        filtered_text = []

        for token in tokens:
            lexeme = nlp.vocab[token]
            if not lexeme.is_stop:
                filtered_text.append(token)
        return filtered_text

    # Function changes all the words present in the text to lowercase
    @staticmethod
    def toLower(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token.text.lower() for token in doc]
