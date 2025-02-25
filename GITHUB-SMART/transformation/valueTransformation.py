import csv




def readFile(file_path="", item_list=""):

    try:
        with open(file_path, 'r') as f:
            content = csv.DictReader(f)
            rows_match_items: list(str) = []

            for row in content:
                for key, value in row.items():
                    if value in item_list:
                        rows_match_items.append(row)
    except FileNotFoundError:
        print(f"ERROR: File not found for the source path!!! ")

    return rows_match_items

def main():
    list_to_transform = ['-1', '-1.00', 'NULL', 'null', '__EMPTY__', '__empty__']
    source_file_path = r'C:\Users\KLMembrano\OneDrive - PLDT\GENERATOR\data\MOCK_DATA.csv'
    foundItems = readFile(file_path=source_file_path, item_list=list_to_transform)
    print(list(foundItems))

if __name__ == "__main__":
    main()