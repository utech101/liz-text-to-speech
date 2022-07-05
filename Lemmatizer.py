import spacy


class Lemmatizer:
    # Function used to find and return the lemmatizer of the tokens present in the text
    @staticmethod
    def lemmatize(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [f"{token} ==> {token.lemma_}" for token in doc]
