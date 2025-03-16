import csv

def find_and_transform_items_in_csv(file_path, list_to_transform):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        headers = csv_reader.fieldnames
        transformed_rows = []

        for row in csv_reader:
            # Replace values in the row if they match any in list_to_transform
            transformed_row = {key: ('' if value in list_to_transform else value) for key, value in row.items()}
            transformed_rows.append(transformed_row)
        
    return headers, transformed_rows

def write_transformed_csv(output_file_path='', headers='', transformed_rows=''):
    with open(output_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(transformed_rows)



def main():
    file_path = r'C:\Users\KLMembrano\OneDrive - PLDT\GENERATOR\data\MOCK_DATA.csv'
    list_to_transform = ['-1', '-1.00', 'NULL', 'null', '__EMPTY__', '__empty__']
    headers, transformed_rows = find_and_transform_items_in_csv(file_path, list_to_transform)
    output_file_path = 'transformed_v2.csv'
    write_transformed_csv(output_file_path=output_file_path, headers=headers, transformed_rows=transformed_rows)

    print("Transformation complete. Check the transformed CSV file.")

if __name__ == "__main__":
    main()


