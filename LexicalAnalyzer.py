from Lemmatizer import Lemmatizer
from POSTagger import POSTagger
from Tokenizer import Tokenizer


class LexicalAnalyzer:
    # Function used to display the relevant lexical information about the text
    @staticmethod
    def lexicalanalyzer(text):
        sentences = Tokenizer.tokenizeSentence(text)
        tokens = Tokenizer.tokenizeText(text)
        biGramTokens = Tokenizer.tokenizeNGrams(text, 2)
        triGramTokens = Tokenizer.tokenizeNGrams(text, 3)
        withoutStopWords = Tokenizer.removeStopWords(text)
        lowerCase = Tokenizer.toLower(text)
        lemmatizedText = Lemmatizer.lemmatize(text)
        POS = POSTagger.tagger(text)

        print("~~~~~~~~~~~~~~Lexical Analysis of the text~~~~~~~~~~~~~~~~~~~~~~")
        print("The Sentences of the Text")
        print("____________________________________")
        print(sentences)
        print("\n")

        print("The Tokens of the Text")
        print("____________________________________")
        print(tokens)
        print("\n")

        print("The Text without Stop Words")
        print("____________________________________")
        print(withoutStopWords)
        print("\n")

        print("The Lowercase Text")
        print("____________________________________")
        print(lowerCase)
        print("\n")

        print("The Lemmatized Text")
        print("____________________________________")
        print(lemmatizedText)
        print("\n")

        print("The Parts of Speech of the Tokens in the Text")
        print("____________________________________")
        print(POS)
        print("\n")

        print("The Bi-gram of the Text")
        print("____________________________________")
        print(biGramTokens)
        print("\n")

        print("The Tri-gram of the Text")
        print("____________________________________")
        print(triGramTokens)
        print("\n")
