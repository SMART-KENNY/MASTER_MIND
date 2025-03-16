import pandas as pd

def transform_values(df, list_to_transform):
    # Replace specified values with empty strings
    for item in list_to_transform:
        df = df.replace(item, '')
    return df



def main():

    file_path =  r'C:\Users\KLMembrano\OneDrive - PLDT\GENERATOR\data\MOCK_DATA.csv'
    list_to_transform = ['-1', '-1.00', '-1.0', -1.0, 1.0, 'NULL', 'null', '__EMPTY__', '__empty__']
    chunk_size = 100000  # Number of rows per chunk
    
    # Reading and transforming the CSV file in chunks
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        transformed_chunk = transform_values(chunk, list_to_transform)
        chunks.append(transformed_chunk)

    # Concatenate all transformed chunks into a single DataFrame
    transformed_df = pd.concat(chunks)

    output_file_path = 'transformed_v3.csv'
    transformed_df.to_csv(output_file_path, index=False)

    print("Transformation complete. Check the transformed CSV file.")

if __name__ == "__main__":
    main()
