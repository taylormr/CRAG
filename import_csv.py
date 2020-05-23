import pandas as pd

df = 0


def load_csv():
    csv_path = 'metadata.csv'
    global df
    df = pd.read_csv(csv_path, sep=',', header=0, usecols=[
        'cord_uid', 'source_x', 'title', 'doi', 'abstract', 'publish_time', 'authors', 'journal', 'pdf_json_files', 'pmc_json_files', 'url'])
    return df
    # print(df[df.cord_uid == 'ug7v899j'])  -- Example search by exact


def search(search_type, query_str):
    return df[df[search_type].str.contains(query_str, na=False, case=False)]


if __name__ == "__main__":
    df = load_csv()
    # Search by Title
    title_q = 'Clinical features of culture-proven Mycoplasma'
    print(df[df['title'].str.contains(title_q, na=False)])
    print(df[df['title'].str.contains('disease', na=False)])
