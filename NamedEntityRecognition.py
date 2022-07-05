import spacy


class NER:
    # Function returns all the tokens alongside the entities they belong to if any
    @staticmethod
    def ner(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [f"{token} ==> {token.label_}" for token in doc.ents]
