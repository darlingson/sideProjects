def convert_to_csv(json_data, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=json_data["Songs"][0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(json_data["Songs"])

# Example usage:
if __name__ == "__main__":
    # Assuming your JSON data is stored in a file named "songs.json"
    json_file_path = "songs.json"
    csv_file_path = "songs.csv"
    with open(json_file_path, "r") as file:
      data = json.load(file)
    convert_to_csv(data, csv_file_path)
