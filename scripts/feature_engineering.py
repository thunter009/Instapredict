'''
Collection of Feature engineering functions.
'''

from sklearn.preprocessing import LabelEncoder
from textblob import TextBlob


def filter_encoder(df):
    le = LabelEncoder()
    df['filters'] = le.fit_transform(df['filters'])
    return df


def num_tags(df):
    df['hashtags'] = df.hashtags.apply(lambda x: len(x))
    df['caption_hashtags'] = df.caption_hashtags.apply(lambda x: len(x))
    return df


def sentiment_encoder(df):

    # list fields to apply sentiment analysis
    sent_fields = []

    # apply sentiment analysis for each field of text data, obtaining polarity
    # (neg < neutral < pos: range [-1,1]) and subjectivity (object <
    # subjective: range [0,1])
    for field in sent_fields:
        df[str(field_) + 'polarity'] = df.apply(lambda x: TextBlob(x[field]
                                                                   ).sentiment.polarity, axis=1)
        df[str(field_) + 'subjectivity'] = df.apply(lambda x: TextBlob(x[field]
                                                                       ).sentiment.subjectivity, axis=1)
    return df
