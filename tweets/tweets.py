import os
import pandas as pd


def tweets_analysis(path, tags=[], bin_frequency="600s"):
    """
    Method to analyse correlation between Twitter tags
        :param path: path to json file with tweets
        :param tags: list of tags to perform analysis on
        :param bin_frequency: frequence of bins 
        :type path: str
        :type tags: list
        :type bin_frequency: str
        :returns: Pandas DataFrame | float
        :rtype: class 'pandas.DataFrame' | float
        :Example:
            >>> from tweets.tweets import tweets_analysis as ta
            >>> res = ta('./tweets/tweets.json', tags=['#ai', '#bigdata'], bin_frequency="600s")
            >>> res
                0.5603877123165414
    """
    path = os.path.expanduser(path)

    if not os.path.isfile(path):
        raise OSError(f'File {path} not found')

    df = pd.read_json(path)
    unique_tags = df.tag.unique()
    missing_tags = [tag for tag in tags if tag not in unique_tags]
    if missing_tags:
        if len(missing_tags) > 1:
            raise ValueError(
                f'Tags {", ".join(missing_tags)} do not exist in a dataset')
        else:
            raise ValueError(
                f'Tag {missing_tags[0]} does not exist in a dataset')

    # filter by provided tags
    if tags:
        df = df[df.tag.isin(tags)]

    # bin, group, sort data and fill missing values with zeros
    df = df.groupby(
        [
            pd.Grouper(key='created_at', freq=bin_frequency),
            'tag'
        ]
    ).size().unstack().sort_index(ascending=False).fillna(0)

    # return correlation between particular tags if there are 2 of them
    if len(tags) == 2:
        return df[tags[0]].corr(df[tags[1]], method='spearman')
    else:
        return df.corr(method='spearman')
