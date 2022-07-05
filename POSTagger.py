import spacy


class POSTagger:
    # Function used to tag each token present in the text with its Part of Speech
    @staticmethod
    def tagger(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [f"{token} ==> {token.pos_}" for token in doc]
