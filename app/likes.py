import numpy as np
import ast


def likes(df):

    df['list_likes'] = [x['likes'] for x in df['top_N_photos']]
    df['mean_likes'] = [np.mean(x) if len(
        x) > 0 else 0 for x in df['list_likes']]
    df['median_likes'] = [np.median(x) if len(
        x) > 0 else 0 for x in df['list_likes']]
    df['max_likes'] = [np.max(x) if len(
        x) > 0 else 0 for x in df['list_likes']]
    df['min_likes'] = [np.min(x) if len(
        x) > 0 else 0 for x in df['list_likes']]
    return df
