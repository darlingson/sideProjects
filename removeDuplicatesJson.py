import json

def removeDuplicates(songs):
    seen_titles = set()
    unique_songs = []

    for song in songs:
        title = song["title"]

        if title not in seen_titles:
            unique_songs.append(song)
            seen_titles.add(title)

    return unique_songs

if __name__ == '__main__':
    input_file_path = "songs.json"
    output_file_path = "unique_songs.json"
    # removeDuplicates("json")

    with open(input_file_path, "r") as file:
        songs_data = json.load(file)

    unique_songs_data = removeDuplicates(songs_data["Songs"])

    with open(output_file_path, "w") as file:
        json.dump({"Songs": unique_songs_data}, file, indent=2)
