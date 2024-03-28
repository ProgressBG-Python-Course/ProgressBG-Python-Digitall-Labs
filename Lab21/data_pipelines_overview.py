# Example Python code for a simple data integration task
import pandas as pd

def extract():
    # Load data from source
    df = pd.read_csv('source_data.csv')
    return df

def transform(df):
    # Data transformation
    df_transformed = df_source.dropna().drop_duplicates()
    return df_transformed

def load(df_transformed):
    # Load transformed data to destination
    df_transformed.to_csv('destination_data.csv', index=False)


def pipeline():
    # data = extract()
    # transformed_data = transform(data)
    # load(transformed_data)
    load(
        transform(
            extract()
        )
    )


