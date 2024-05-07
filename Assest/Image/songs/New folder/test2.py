import os
import random
import difflib

def closest_match(file_name, song_names):
    # Function to find the closest match of the file name in the list of song names
    matches = difflib.get_close_matches(file_name, song_names, n=1, cutoff=0.3)
    return matches[0] if matches else None

def generate_template(file_names, song_artists, include_duration):
    template = '''<div class="PlaylistItem">
            <div class="playlist-item-content">
              <!-- Song details -->
              <div class="song-thumb">
                <!-- Song thumbnail and details -->
                <p class="song-no">{serialNo}</p>
                <div class="song-img-container">
                  <img src="./Assest/LowResImg/songs/{filename}" class="song-img" />
                </div>
                <div class="song-detail-container">
                  <span class="song-title">{songName}</span>
                  <span class="song-subtitle">{artists_Name}</span>
                </div>
              </div>
            </div>
            {duration_line}
            <!-- Button container -->
            <div class="playlist-button-container">
              <!-- Like button -->
              <span class="song-like-button">
                <i class="far fa-heart"></i>
              </span>
            </div>
          </div>\n'''

    templates = []
    for index, song_artist in enumerate(song_artists, start=1):
        found = False
        for filename in file_names:
            match = closest_match(filename, [song_artist['song']])
            if match:
                duration_line = f'<span class="song-duration">{generate_random_duration()}</span>' if include_duration else '<!-- <span class="song-duration"></span> -->'
                templates.append(template.format(serialNo=str(index).zfill(2), filename=filename, songName=match, artists_Name=song_artist['artists'], duration_line=duration_line))
                found = True
                break  # Stop searching for this song once found
        if not found:
            print(f"Song '{song_artist['song']}' not found in files. Skipping...")
    return templates

def save_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.writelines(content)

def generate_random_duration():
    hours = random.randint(1, 8)
    minutes = random.randint(0, 59)
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"

def main():
    folder_path = r"C:\\Users\\kumar\\OneDrive\\Documents\\HTML\\CodingNinja-WebDevTest-2\\Assest\\Image\\songs"  # Update this with your folder path
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Update with your song and artist list
    song_artists = [
        {'song': 'A Thousand Years', 'artists': 'Christina Perri'},
    {'song': 'Afterdark', 'artists': 'Tito & Tarantula'},
    {'song': 'Afterlife (Deluxe)', 'artists': 'Avenged Sevenfold'},
    {'song': 'All The Little Lights (Deluxe)', 'artists': 'Passenger'},
    {'song': 'American Dream', 'artists': 'LCD Soundsystem'},
    {'song': 'Backslide', 'artists': 'Rascal Flatts'},
    {'song': 'Beautiful Things', 'artists': 'Ryan Corn'},
    {'song': 'Best of Hip Hop', 'artists': 'Various Artists'},
    {'song': 'Bling Bang Bang Born', 'artists': 'Mondo Grosso'},
    {'song': 'Born To Die (The Paradise Edition)', 'artists': 'Lana Del Rey'},
    {'song': 'Ckay: The First', 'artists': 'CKay'},
    {'song': 'Creatures In Heaven', 'artists': 'Craig Xen'},
    {'song': 'D Anum (Serbian)', 'artists': 'Dara Bubamara'},
    {'song': 'Dandelions', 'artists': 'Ruth B.'},
    {'song': 'Dark Matter', 'artists': 'Les Friction'},
    {'song': 'Decide', 'artists': 'Ckay'},
    {'song': 'Dreamland', 'artists': 'Glass Animals'},
    {'song': 'Everlasting Romance', 'artists': 'Lukas Graham'},
    {'song': 'Favorite', 'artists': 'Johnny Gill'},
    {'song': 'February Sky', 'artists': 'White Hart'},
    {'song': 'Feel Something', 'artists': 'Jaymes Young'},
    {'song': 'Fountain Baby', 'artists': 'Blue October'},
    {'song': 'Four (Deluxe)', 'artists': 'One Direction'},
    {'song': 'Happy Birthday Ronan Keating', 'artists': 'Ronan Keating'},
    {'song': 'Harleys In Hawaii', 'artists': 'Katy Perry'},
    {'song': 'Let Me Down Slowly', 'artists': 'Alec Benjamin'},
    {'song': "Let's Talk About Love", 'artists': 'Celine Dion'},
    {'song': "Let's Play", 'artists': 'Paul Hardcastle'},
    {'song': "Lovin' On Me", 'artists': 'Diddy - Dirty Money'},
    {'song': 'Way Down We Go', 'artists': 'Kaleo'},
    {'song': 'Perfect', 'artists': 'Ed Sheren'},
    {'song': 'Pink Venom', 'artists': 'Black Pink'},
    {'song': 'Until I Found You', 'artists': 'Stephen Sanchez'},
    {'song': 'Lover', 'artists': 'Taylor Shift'}
    ]
    
    include_duration = False  # Change this to False if you want to comment out the duration line

    templates = generate_template(file_names, song_artists, include_duration)
    output_file_path = os.path.join(folder_path, "output.txt")
    save_to_file(output_file_path, templates)
    print(f"Templates saved to {output_file_path}")

if __name__ == "__main__":
    main()
