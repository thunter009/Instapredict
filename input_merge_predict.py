import numpy as np
from image_extractor import *
from likes import likes
import pickle


# set constant variables

num_hashtags = 257.598390
hashtag_polarity = 0.0
hashtag_subjectivity = 0.350207
filters = 27

# get image directory

im_fname
image_df = image_extract(im_fname)

# read in scrape data
scrape_df = blank

scrape_df = likes(scrape_df)

# combine and scrub
input_array = np.array([
						image_df['B_max'].iloc[0],
						 image_df['B_mean'].iloc[0],
						 image_df['B_median'].iloc[0],
						 image_df['B_rms'].iloc[0],
						 image_df['B_stddev'].iloc[0],
						 image_df['B_sum'].iloc[0],
						 image_df['B_sum2'].iloc[0],
						 image_df['B_var'].iloc[0],
						 image_df['G_max'].iloc[0],
						 image_df['G_mean'].iloc[0],
						 image_df['G_median'].iloc[0],
						 image_df['G_rms'].iloc[0],
						 image_df['G_stddev'].iloc[0],
						 image_df['G_sum'].iloc[0],
						 image_df['G_sum2'].iloc[0],
						 image_df['G_var'].iloc[0],
						 image_df['R_max'].iloc[0],
						 image_df['R_mean'].iloc[0],
						 image_df['R_median'].iloc[0],
						 image_df['R_rms'].iloc[0],
						 image_df['R_stddev'].iloc[0],
						 image_df['R_sum'].iloc[0],
						 image_df['R_sum2'].iloc[0],
						 image_df['R_var'].iloc[0],
						 image_df['blur'].iloc[0],
						 filters,
						 image_df['image_height'].iloc[0],
						 image_df['image_width'].iloc[0],
						 image_df['luminance'].iloc[0],
						 image_df['num_faces'].iloc[0],
						 image_df['percieved_luminance'].iloc[0],
						 scrape_df['Followers'].iloc[0],
						 scrape_df['Following'].iloc[0],
						 scrape_df['Posts'].iloc[0],
						 scrape_df['max_likes'].iloc[0],
						 scrape_df['mean_likes'].iloc[0],
						 scrape_df['median_likes'].iloc[0],
						 scrape_df['min_likes'].iloc[0],
						 num_hashtags,
						 hashtag_polarity,
						 hashtag_subjectivity
						 ])

# load the model
gb_regressor = pickle.load(open('gbr_model.sav', 'rb'))


# call model on input array to obtain result
predicted_likes = gb_regressor.predict(input_array)

# print result
print predicted_likes










