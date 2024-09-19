import pandas as pd


def get_data():
    # File paths
    file_paths = [
        'resources/2021-2022 Football Player Stats.csv',
        'resources/2022-2023 Football Player Stats.csv'
    ]
    # Create a list to store DataFrames
    dataframes = []
    # Define seasons corresponding to each file
    seasons = ["2021-2022", "2022-2023"]
    # Iterate over the file paths and seasons
    for i, file_path in enumerate(file_paths):
        # Read the CSV file
        df = pd.read_csv(file_path, encoding='latin1', sep=';')
        # Add the season column
        df['season'] = seasons[i]
        # Append the DataFrame to the list
        dataframes.append(df)
    # Concatenate all DataFrames into one
    merged_df = pd.concat(dataframes, ignore_index=True)
    return merged_df
