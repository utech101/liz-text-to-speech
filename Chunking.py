import spacy


class Chunking:
    # Function returns all the noun tokens present in the text
    @staticmethod
    def nounChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [f"{token} ==> {token.label_}" for token in doc.noun_chunks]

    # Function returns all the verb tokens present in the text
    @staticmethod
    def verbChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token for token in doc if token.pos_ == "VERB"]

    # Function returns all the adjective tokens present in the text
    @staticmethod
    def adjectiveChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token for token in doc if token.pos_ == "ADJ"]

    # Function returns all the pronoun tokens present in the text
    @staticmethod
    def pronounChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token for token in doc if token.pos_ == "PRON"]

    # Function returns all the proper noun tokens present in the text
    @staticmethod
    def properNounChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token for token in doc if token.pos_ == "PROPN"]

    # Function returns all the numerical value tokens present in the text
    @staticmethod
    def numericalChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token for token in doc if token.pos_ == "NUM"]

    # Function returns all the prepositional tokens present in the text
    @staticmethod
    def prepositionChunking(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [token for token in doc if token.pos_ == "ADP"]
