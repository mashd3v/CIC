# Required instalations
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SA
import spacy
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import math
import operator
import nltk
import subprocess

subprocess.run(["python3", "-m", "pip", "install", "spacy-3.5.2"])
subprocess.run(["python3", "-m", "pip", "install", "vaderSentiment==3.3.2"])

"""Imports"""

# Remover stopwords

# Descargar las stopwords
nltk.download("stopwords")

# NLP library
subprocess.run(["python3", "-m", "spacy", "download", "en_core_web_sm"])
subprocess.run(["python3", "-m", "spacy", "download", "es_core_news_sm"])

# Sentiment analysis


class FeatureExtraction:
    def __init__(
        self,
        data,
        text_column,
        lemma,
        pos,
        tag,
        other_features,
        oth_feats_vectorizer,
        vectorizer,
        language,
    ):
        self.data = data
        self.text_column = text_column
        self.lemma = lemma
        self.pos = pos
        self.tag = tag
        self.other_features = other_features
        self.vectorizer = vectorizer
        self.oth_feats_vectorizer = oth_feats_vectorizer
        self.language = language
        if self.language == "en":
            self.nlp = spacy.load("en_core_web_sm")
        elif self.language == "es":
            self.nlp = spacy.load("es_core_news_sm")

    def features(self):
        sentiment_analyzer = SA()
        if self.language == "en":
            stop_words = set(stopwords.words("english"))
        elif self.language == "es":
            stop_words = set(stopwords.words("spanish"))
        final_feature_list, feats_list, features_names = [], [], []
        text2lemma, text2pos, text2tag = [], [], []

        for i, row in self.data.iterrows():
            doc = self.nlp(row[self.text_column])
            final_volcabulary, feature_list, lemma, pos, tag = [], [], [], [], []

            # Obtaining lemma, pos and tag vectors
            if self.lemma or self.pos or self.tag:
                for token in doc:
                    # Creating lemma vector
                    if self.lemma:
                        lemma.append(token.lemma_)
                        lemma_text = " ".join(lemma)

                    # Creating POS tagging vector
                    if self.pos:
                        pos.append(token.pos_)
                        pos_text = " ".join(pos)

                    # Creating TAG vector
                    if self.tag:
                        if token.tag_ == "SYM":
                            continue
                        else:
                            tag.append(token.tag_)
                            tag_text = " ".join(tag)

                if self.lemma:
                    text2lemma.append(lemma_text)
                if self.pos:
                    text2pos.append(pos_text)
                if self.tag:
                    text2tag.append(tag_text)

            # Obtaining other features vector
            if self.oth_feats_vectorizer:
                # Syllables
                syllables_ = 0
                for w in doc.text:
                    if w == "a" or w == "e" or w == "i" or w == "o" or w == "u":
                        syllables_ += 1
                feature_list.append(f"SYL_{syllables_}")
                features_names.append("syllables")

                # Number of characters
                num_characters_ = sum(len(w) for w in doc.text)
                feature_list.append(f"NUM_CHAR_{num_characters_}")
                features_names.append("num_characters")

                # Number of words
                num_words_ = len(doc.text.split())
                feature_list.append(f"NUM_WORDS_{num_words_}")
                features_names.append("num_words")

                # Average of syllables
                avg_syllables_ = round((syllables_ / num_words_), 1)
                feature_list.append(f"AVG_SYL_{avg_syllables_}")
                features_names.append("avg_syllables")

                # Number of unique words
                num_unique_words_ = len(set(doc.text.split()))
                feature_list.append(f"UNIQUE_WORDS_{num_unique_words_}")
                features_names.append("num_unique_words")

                # Count stopwords
                stopwords_x = [w for w in doc.text.split() if w in stop_words]
                feature_list.append(f"NUM_STOPWORDS_{len(stopwords_x)}")
                features_names.append("num_stopwords")

                # Flesch Reading Ease
                fre = round(
                    206.835 - 1.015 * (num_words_ / 1) - (84.6 * avg_syllables_), 2
                )
                if fre > 90.0:
                    feature_list.append(f"FRE_5_GRADE")

                elif fre <= 90.0 and fre > 80.0:
                    feature_list.append(f"FRE_6_GRADE")

                elif fre <= 80.0 and fre > 70.0:
                    feature_list.append(f"FRE_7_GRADE")

                elif fre <= 70.0 and fre > 60.0:
                    feature_list.append(f"FRE_8-9_GRADE")

                elif fre <= 60.0 and fre > 50.0:
                    feature_list.append(f"FRE_10-12_GRADE")

                elif fre <= 50.0 and fre > 30.0:
                    feature_list.append(f"FRE_COLLEGE")

                elif fre <= 30.0 and fre > 10.0:
                    feature_list.append(f"FRE_COLLEGE_GRADUATE")

                elif fre <= 10.0:
                    feature_list.append(f"FRE_PROFESSIONAL")

                features_names.append("fre")

                # Flesch-Kincaid grade level
                fk = math.trunc(
                    round((0.39 * num_words_ / 1) + (11.8 * avg_syllables_) - 15.59, 1)
                )
                feature_list.append(f"FK_{fk}_YEARS")
                features_names.append("fk")

            final_feature_list.append(feature_list)

        for feats in final_feature_list:
            feats2text = feats_list.append(" ".join(feats))

        # Lemma to vector
        if self.lemma:
            lemma_vectorizer = self.vectorizer.fit_transform(
                pd.Series(text2lemma)
            ).toarray()
            lemma_vocab = self.vectorizer.get_feature_names_out().tolist()
            final_volcabulary += lemma_vocab

        # POS to vector
        if self.pos:
            pos_vectorizer = self.vectorizer.fit_transform(
                pd.Series(text2pos)
            ).toarray()
            pos_vocab = self.vectorizer.get_feature_names_out().tolist()
            final_volcabulary += pos_vocab

        # TAG to vector
        if self.tag:
            tag_vectorizer = self.vectorizer.fit_transform(
                pd.Series(text2tag)
            ).toarray()
            tag_vocab = self.vectorizer.get_feature_names_out().tolist()
            final_volcabulary += tag_vocab

        # OTHER FEATURES to vector
        if self.other_features:
            oth_feats_vectorizer = self.oth_feats_vectorizer.fit_transform(
                pd.Series(feats_list)
            ).toarray()
            oth_feats_vocab = self.oth_feats_vectorizer.get_feature_names_out().tolist()
            final_volcabulary += oth_feats_vocab

        final_dataframes = [
            pd.Series(text2lemma),
            pd.Series(text2pos),
            pd.Series(text2tag),
            pd.Series(feats_list),
        ]

        # # Correcting the duplicated vocabulary
        # seen = set()
        # unique, index = [], []
        # for i, x in enumerate(final_volcabulary):
        #     if x not in seen:
        #         unique.append(x)
        #         seen.add(x)
        #     else:
        #         index.append(i)

        # Join the text, pos and tag matrices into a single one
        final_vector = np.concatenate(
            [lemma_vectorizer, pos_vectorizer, tag_vectorizer, oth_feats_vectorizer],
            axis=1,
        )

        # flag = 0
        # for i, x in enumerate(index):
        #     if i == 0:
        #         a.pop(x)
        #     else:
        #         flag -= 1
        #         print(flag)
        #         a.pop(x + flag)

        # print(a)

        print(f"Lemma: {lemma_vectorizer.shape}")
        print(f"POS: {pos_vectorizer.shape}")
        print(f"TAG: {tag_vectorizer.shape}")
        print(f"Other features: {oth_feats_vectorizer.shape}")
        print(f"Final vector shape: {final_vector.shape}")

        return final_vector, final_volcabulary, final_dataframes

    def add_features(self):
        data_ = self.data.copy()
        sentiment_analyzer = SA()
        if self.language == "en":
            stop_words = set(stopwords.words("english"))
        elif self.language == "es":
            stop_words = set(stopwords.words("spanish"))

        for i, row in data_.iterrows():
            doc = self.nlp(row[self.text_column])
            lemma, pos, tag, other_features = [], [], [], []

            # Obtaining lemma, pos and tag values
            if self.lemma or self.pos or self.tag:
                for token in doc:
                    if self.lemma:
                        lemma.append(token.lemma_)

                    if self.pos:
                        pos.append(token.pos_)

                    if self.tag:
                        if token.tag_ == "SYM":
                            continue
                        else:
                            tag.append(token.tag_)

                if self.lemma:
                    data_.at[i, self.text_column] = " ".join(lemma)
                if self.pos:
                    data_.at[i, self.text_column] = (
                        data_[self.text_column][i] + " " + " ".join(pos)
                    )
                if self.tag:
                    data_.at[i, self.text_column] = (
                        data_[self.text_column][i] + " " + " ".join(tag)
                    )

            if self.other_features:
                # Syllables
                syllables_ = 0
                for w in doc.text:
                    if w == "a" or w == "e" or w == "i" or w == "o" or w == "u":
                        syllables_ += 1
                other_features.append(f"SYL_{syllables_}")

                # Number of characters
                num_characters_ = sum(len(w) for w in doc.text)
                other_features.append(f"NUM_CHAR_{num_characters_}")

                # Number of words
                num_words_ = len(doc.text.split())
                other_features.append(f"NUM_WORDS_{num_words_}")

                # Average of syllables
                avg_syllables_ = round((syllables_ / num_words_), 1)
                other_features.append(f"AVG_SYL_{avg_syllables_}")

                # Number of unique words
                num_unique_words_ = len(set(doc.text.split()))
                other_features.append(f"UNIQUE_WORDS_{num_unique_words_}")

                # Count stopwords
                stopwords_x = [w for w in doc.text.split() if w in stop_words]
                other_features.append(f"NUM_STOPWORDS_{len(stopwords_x)}")

                # Flesch Reading Ease
                fre = round(
                    206.835 - 1.015 * (num_words_ / 1) - (84.6 * avg_syllables_), 2
                )
                if fre > 90.0:
                    other_features.append(f"FRE_5_GRADE")

                elif fre <= 90.0 and fre > 80.0:
                    other_features.append(f"FRE_6_GRADE")

                elif fre <= 80.0 and fre > 70.0:
                    other_features.append(f"FRE_7_GRADE")

                elif fre <= 70.0 and fre > 60.0:
                    other_features.append(f"FRE_8-9_GRADE")

                elif fre <= 60.0 and fre > 50.0:
                    other_features.append(f"FRE_10-12_GRADE")

                elif fre <= 50.0 and fre > 30.0:
                    other_features.append(f"FRE_COLLEGE")

                elif fre <= 30.0 and fre > 10.0:
                    other_features.append(f"FRE_COLLEGE_GRADUATE")

                elif fre <= 10.0:
                    other_features.append(f"FRE_PROFESSIONAL")

                # Flesch-Kincaid grade level
                fk = math.trunc(
                    round((0.39 * num_words_ / 1) + (11.8 * avg_syllables_) - 15.59, 1)
                )
                other_features.append(f"FK_{fk}_YEARS")

                data_.at[i, self.text_column] = (
                    data_[self.text_column][i] + " " + " ".join(other_features)
                )

        return data_
