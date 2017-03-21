import pandas as pd
import re


def scrub_caption_text(df, col='caption'):
    # scrub caption for text only
    df[col] = df[col].apply(lambda x: x.strip().replace('\n', ' '))
    return df


def scrub_caption_emoji(df, col='caption'):
    # scrub caption column for emoji
    df = scrub_caption_text(df)
    return df


def scrub_caption_hashtags(df, col='caption'):
    # add tages to hashtags column
    df = scrub_caption_text(df)
    pat = re.compile(r'[#]\w+')
    df['caption_hashtags'] = df[col].apply(
        lambda x: [y.replace('#', '') for y in pat.findall(x)])
    return df


def scrub_caption_text_only(df, col='caption'):
    # TBD
    #     ([^#a-z0-9]*|[^@a-z0-9]+)\w+
    return df


def scrub_shoutouts(df, col='caption'):
    df = scrub_caption_text(df)
    pat = re.compile(r'[@]\w+')
    df['shoutouts'] = df[col].apply(
        lambda x: [y.replace('@', '') for y in pat.findall(x)])
    return df


def scrub_user(df, col='user'):
    df[col] = df[col].apply(lambda x: x.lstrip('@'))
    return df


def scrub_filter(df, col='filters'):
    # drop 'Filter' from filters columns
    df[col] = df[col].apply(lambda x: x.replace('Filter', ''))
    return df


def scrub_hashtags(df, col='hashtags'):
    df[col] = df[col].apply(lambda x: [y.replace('#', '')
                                       for y in str(x).split()])
    return df


def scrub_scrape_time(df, col='scrape_time'):
    df[col] = pd.to_datetime(df[col])
    return df


def deduplicate(df, sub=['caption',
                         'comments',
                         'filters',
                         'image',
                         'likes',
                         'time',
                         'user']):
    return df.drop_duplicates(subset=sub)


def scrub(df):
    """
    scrub runs all scrubbing functions on an input dataframe and returns a 
    dataframe with scrubbed data
    """

    scrub = [
        deduplicate,
        scrub_caption_emoji,
        scrub_caption_hashtags,
        scrub_shoutouts,
        scrub_caption_text_only,
        scrub_user,
        scrub_filter,
        scrub_hashtags,
        scrub_scrape_time,
    ]

    for func in scrub:
        try:
            df = func(df)
        except Exception as e:
            print("error in {} \n{}".format(func, e))
            continue
