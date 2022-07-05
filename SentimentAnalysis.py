import spacy
from spacytextblob.spacytextblob import SpacyTextBlob


class SentimentAnalysis:
    # Function returns the polarity of the text
    @staticmethod
    def polarity(text):
        nlp = spacy.load("en_core_web_md")
        nlp.add_pipe('spacytextblob')
        doc = nlp(text)
        return doc._.blob.polarity

    # Function returns the subjectivity of the text
    @staticmethod
    def subjectivity(text):
        nlp = spacy.load("en_core_web_md")
        nlp.add_pipe('spacytextblob')
        doc = nlp(text)
        return doc._.blob.subjectivity

    # Function returns the sentiment assessment of the text
    @staticmethod
    def sentimentAssessment(text):
        nlp = spacy.load("en_core_web_md")
        nlp.add_pipe('spacytextblob')
        doc = nlp(text)
        return doc._.blob.sentiment_assessments.assessments

    # Function returns the ngrams of the text
    @staticmethod
    def nGrams(text):
        nlp = spacy.load("en_core_web_md")
        nlp.add_pipe('spacytextblob')
        doc = nlp(text)
        return doc._.blob.ngrams()
