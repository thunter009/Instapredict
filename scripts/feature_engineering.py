'''
Collection of Feature engineering functions.
'''

from sklearn.preprocessing import LabelEncoder

def filter_encoder(df):
	le = LabelEncoder()
	df['filters'] = le.fit_transform(df['filters'])
	return df

def num_tags(df):
	df['hashtags'] = df.hashtags.apply(lambda x: len(x))
	df['caption_hashtags'] = df.caption_hashtags.apply(lambda x: len(x))
	return df

