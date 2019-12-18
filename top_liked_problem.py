import pandas as pd

def sort_liked():
    df = pd.read_csv('./info.csv')
    print(df)
    df[['liked']] = df[['liked']].astype(int)
    df.sort_values(by=['liked'], ascending=False)
    print(df.head())
    print(df)

sort_liked()