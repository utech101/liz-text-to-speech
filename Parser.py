import spacy
from spacy import displacy
from nltk import Tree
from Chunking import Chunking
from FrequencyDistribution import FrequencyDistribution
from NamedEntityRecognition import NER
from SentimentAnalysis import SentimentAnalysis


class Parser:
    # Function that parses the text entered and provides it in a HTML that can be opened and view
    @staticmethod
    def parseText(text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        html = displacy.render(doc, style="dep")
        with open("data_vis.html", "w") as f:
            f.write(html)
        return [(token.i, token, token.dep_, token.head.i, token.head) for token in doc]

    # Used to format the parse tree
    @staticmethod
    def formatter(token):
        return ">>".join([token.orth_, token.tag_])

    # Used to retrieve the nodes of the parse tree
    def nltkTree(self, token):
        if token.n_lefts + token.n_rights > 0:
            return Tree(self.formatter(token), [self.nltkTree(child) for child in token.children])
        else:
            return self.formatter(token)

    # Used to display the parse tree
    def parseTree(self, text):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(text)
        return [self.nltkTree(sent.root).pretty_print() for sent in doc.sents]

    # Function used to display the relevant parsed information about the text
    @staticmethod
    def parsing(text):
        nounChunks = Chunking.nounChunking(text)
        verbChunks = Chunking.verbChunking(text)
        adjectiveChunks = Chunking.adjectiveChunking(text)
        pronounChunks = Chunking.pronounChunking(text)
        properNounChunks = Chunking.properNounChunking(text)
        numericChunks = Chunking.numericalChunking(text)
        prepositionChunks = Chunking.prepositionChunking(text)
        namedEntities = NER.ner(text)
        tokenDistribution = FrequencyDistribution.tokenDistribution(text)
        nounDistribution = FrequencyDistribution.nounDistribution(text)
        polarity = SentimentAnalysis.polarity(text)
        subjectivity = SentimentAnalysis.subjectivity(text)
        assessment = SentimentAnalysis.sentimentAssessment(text)
        ngrams = SentimentAnalysis.nGrams(text)
        parsedText = Parser.parseText(text)

        print("~~~~~~~~~~~~~~Parsing of the Text~~~~~~~~~~~~~~~~~~~~~~")
        print("The Noun Chunks of the Text")
        print("____________________________________")
        print(nounChunks)
        print("\n")

        print("The Verb Chunks in the Text")
        print("____________________________________")
        print(verbChunks)
        print("\n")

        print("The Adjective Chunks of the Text")
        print("____________________________________")
        print(adjectiveChunks)
        print("\n")

        print("The Pronoun Chunks of the Text")
        print("____________________________________")
        print(pronounChunks)
        print("\n")

        print("The Proper Nouns Chunks of the Text")
        print("____________________________________")
        print(properNounChunks)
        print("\n")

        print("The Numeric Chunks of the Text")
        print("____________________________________")
        print(numericChunks)
        print("\n")

        print("The Preposition Chunks of the Text")
        print("____________________________________")
        print(prepositionChunks)
        print("\n")

        print("Named Entities in the Text")
        print("____________________________________")
        print(namedEntities)
        print("\n")

        print("The Token Distribution of the Text")
        print("____________________________________")
        print(tokenDistribution)
        print("\n")

        print("The Noun Distribution of the Text")
        print("____________________________________")
        print(nounDistribution)
        print("\n")

        print("The Polarity of the Text")
        print("____________________________________")
        print(polarity)
        print("\n")

        print("The Subjectivity of the Text")
        print("____________________________________")
        print(subjectivity)
        print("\n")

        print("The Sentiment Assessment of the Text")
        print("____________________________________")
        print(assessment)
        print("\n")

        print("The NGrams of the Text")
        print("____________________________________")
        print(ngrams)
        print("\n")

        print("The Parsed Text")
        print("____________________________________")
        print(parsedText)
        print("\n")

        print("The Parse Tree of the Text")
        print("____________________________________")
        Parser().parseTree(text)
        print("\n")
