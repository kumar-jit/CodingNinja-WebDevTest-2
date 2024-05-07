# import os


# def generate_template(file_names):
#     template = '''<div class="PlaylistItem">
#                         <div class="playlist-item-content">
#                             <!-- Song details -->
#                             <div class="song-thumb">
#                                 <!-- Song thumbnail and details -->
#                                 <p class="song-no">{serialNo}</p>
#                                 <div class="song-img-container">
#                                     <img src="./Assest/Image/songs/{filename}" class="song-img">
#                                 </div>
#                                 <div class="song-detail-container">
#                                     <span class="song-title">{songName}</span>
#                                     <span class="song-subtitle">19/20/20</span>
#                                 </div>
#                             </div>
#                         </div>
#                         <!-- Button container -->
#                         <div class="playlist-button-container">
#                             <!-- Like button -->
#                             <span class="song-like-button">
#                                 <i class="fas fa-heart"></i>
#                             </span>
#                         </div>
#                     </div>\n'''

#     templates = []
#     for index, filename in enumerate(file_names, start=1):
#         song_name = get_song_name(filename)
#         templates.append(template.format(serialNo=str(index).zfill(2), filename=filename, songName=song_name))
#     return templates

# def get_song_name(filename):
#     # You can replace this function with any AI or online service to get the song name
#     # For simplicity, let's just remove the file extension and capitalize the words
#     nameFile.append(os.path.splitext(filename)[0].replace("_", " ").title())
#     return os.path.splitext(filename)[0].replace("_", " ").title()

# def main():
#     folder_path = "./"  # Update this with your folder path
#     file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
#     templates = generate_template(file_names)
#     for template in templates:
#         print(template)
#     print(nameFile)

# nameFile = []
# if __name__ == "__main__":
#     main()


# ---------------------------------------------------------------------------- #
#                                    type 2                                    #
# ---------------------------------------------------------------------------- #

# import os
# import difflib

# # List of song names
# song_names = [
#     "A Thousand Years", "Afterdark", "Afterlife (Deluxe)", "All The Little Lights (Deluxe)",
#     "American Dream", "Backslide", "Beautiful Things", "Best of Hip Hop", "Bling Bang Bang Born",
#     "Born To Die (The Paradise Edition)", "Ckay: The First", "Creatures In Heaven", "D Anum (Serbian)",
#     "Dandelions", "Dark Matter", "Decide", "Dreamland", "Everlasting Romance", "Favorite",
#     "February Sky", "Feel Something", "Fountain Baby", "Four (Deluxe)", "Future Hits",
#     "Happy Birthday Ronan Keating", "Harleys In Hawaii", "I Like The Way You Kiss Me",
#     "Indigo (Extended)", "Lady Lady", "Let Me Down Slowly", "Let's Talk About Love", "Let's Play",
#     "Lovin' On Me", "Middle Of The Night", "My Own Way", "My World 2.0", "Orgy Of The Damned",
#     "Pedro", "People", "Seven Inches Of Satanic Panic", "Stray", "Tarantula Heart", "Test",
#     "The Piper's Call", "Treadmill Pop", "Unheard", "Utopia", "Vol. 1: Music From The HBO Original Series",
#     "Wasteland Baby (Special Edition)", "Way Down We Go", "Wmg"
# ]

# def closest_match(file_name):
#     # Function to find the closest match of the file name in the list of song names
#     return difflib.get_close_matches(file_name, song_names, n=1, cutoff=0.3)

# def generate_template(file_names):
#     template = '''<div class="PlaylistItem">
#                         <div class="playlist-item-content">
#                             <!-- Song details -->
#                             <div class="song-thumb">
#                                 <!-- Song thumbnail and details -->
#                                 <p class="song-no">{serialNo}</p>
#                                 <div class="song-img-container">
#                                     <img src="./Assest/Image/songs/{filename}" class="song-img">
#                                 </div>
#                                 <div class="song-detail-container">
#                                     <span class="song-title">{songName}</span>
#                                     <span class="song-subtitle">19/20/20</span>
#                                 </div>
#                             </div>
#                         </div>
#                         <!-- Button container -->
#                         <div class="playlist-button-container">
#                             <!-- Like button -->
#                             <span class="song-like-button">
#                                 <i class="fas fa-heart"></i>
#                             </span>
#                         </div>
#                     </div>\n'''

#     templates = []
#     for index, filename in enumerate(file_names, start=1):
#         song_name = closest_match(filename)[0] if closest_match(filename) else "Unknown"
#         templates.append(template.format(serialNo=str(index).zfill(2), filename=filename, songName=song_name))
#     return templates

# def save_to_file(file_path, content):
#     with open(file_path, "w") as file:
#         file.writelines(content)

# def main():
#     folder_path = "./"  # Update this with your folder path
#     file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
#     templates = generate_template(file_names)
#     output_file_path = os.path.join(folder_path, "output.txt")
#     save_to_file(output_file_path, templates)
#     print(f"Templates saved to {output_file_path}")

# if __name__ == "__main__":
#     main()


# List of song names and artists
# song_artists = [
#     {'song': 'A Thousand Years', 'artists': 'Christina Perri'},
#     {'song': 'Afterdark', 'artists': 'Tito & Tarantula'},
#     {'song': 'Afterlife (Deluxe)', 'artists': 'Avenged Sevenfold'},
#     {'song': 'All The Little Lights (Deluxe)', 'artists': 'Passenger'},
#     {'song': 'American Dream', 'artists': 'LCD Soundsystem'},
#     {'song': 'Backslide', 'artists': 'Rascal Flatts'},
#     {'song': 'Beautiful Things', 'artists': 'Ryan Corn'},
#     {'song': 'Best of Hip Hop', 'artists': 'Various Artists'},
#     {'song': 'Bling Bang Bang Born', 'artists': 'Mondo Grosso'},
#     {'song': 'Born To Die (The Paradise Edition)', 'artists': 'Lana Del Rey'},
#     {'song': 'Ckay: The First', 'artists': 'CKay'},
#     {'song': 'Creatures In Heaven', 'artists': 'Craig Xen'},
#     {'song': 'D Anum (Serbian)', 'artists': 'Dara Bubamara'},
#     {'song': 'Dandelions', 'artists': 'Ruth B.'},
#     {'song': 'Dark Matter', 'artists': 'Les Friction'},
#     {'song': 'Decide', 'artists': 'Ckay'},
#     {'song': 'Dreamland', 'artists': 'Glass Animals'},
#     {'song': 'Everlasting Romance', 'artists': 'Lukas Graham'},
#     {'song': 'Favorite', 'artists': 'Johnny Gill'},
#     {'song': 'February Sky', 'artists': 'White Hart'},
#     {'song': 'Feel Something', 'artists': 'Jaymes Young'},
#     {'song': 'Fountain Baby', 'artists': 'Blue October'},
#     {'song': 'Four (Deluxe)', 'artists': 'One Direction'},
#     {'song': 'Happy Birthday Ronan Keating', 'artists': 'Ronan Keating'},
#     {'song': 'Harleys In Hawaii', 'artists': 'Katy Perry'},
#     {'song': 'I Like The Way You Kiss Me', 'artists': 'Elvis Presley'},
#     {'song': 'Indigo (Extended)', 'artists': 'Chris Brown'},
#     {'song': 'Lady Lady', 'artists': 'Masego'},
#     {'song': 'Let Me Down Slowly', 'artists': 'Alec Benjamin'},
#     {'song': "Let's Talk About Love", 'artists': 'Celine Dion'},
#     {'song': "Let's Play", 'artists': 'Paul Hardcastle'},
#     {'song': "Lovin' On Me", 'artists': 'Diddy - Dirty Money'},
#     {'song': 'Middle Of The Night', 'artists': 'Monarchy'},
#     {'song': 'My Own Way', 'artists': 'KSI'},
#     {'song': 'My World 2.0', 'artists': 'Justin Bieber'},
#     {'song': 'Orgy Of The Damned', 'artists': 'Midnight Syndicate'},
#     {'song': 'Pedro', 'artists': 'Skusta Clee'},
#     {'song': 'People', 'artists': 'Hillsong UNITED'},
#     {'song': 'Seven Inches Of Satanic Panic', 'artists': 'Ghost'},
#     {'song': 'Stray', 'artists': 'Grace VanderWaal'},
#     {'song': 'Tarantula Heart', 'artists': 'Herbie Hancock'},
#     {'song': 'Test', 'artists': 'Alan Walker'},
#     {'song': "The Piper's Call", 'artists': 'Alphaville'},
#     {'song': 'Treadmill Pop', 'artists': 'Daniel Pemberton'},
#     {'song': 'Utopia', 'artists': 'Björk'},
#     {'song': 'Wasteland Baby (Special Edition)', 'artists': 'Hozier'},
#     {'song': 'Way Down We Go', 'artists': 'Kaleo'},
#     {'song': 'Perfect', 'artists': 'Ed Sheren'},
#     {'song': 'Pink Venom', 'artists': 'Black Pink'},
#     {'song': 'Until I Found You', 'artists': 'Stephen Sanchez'},
#     {'song': 'Lover', 'artists': 'Taylor Shift'}
# ]



import os
import difflib
import random

# List of song names and artists
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

def closest_match(file_name):
    # Function to find the closest match of the file name in the list of song names
    matches = difflib.get_close_matches(file_name, [song_artist['song'] for song_artist in song_artists], n=1, cutoff=0.3)
    return matches[0] if matches else None

def get_artist_name(song_name):
    for song_artist in song_artists:
        if song_artist['song'] == song_name:
            return song_artist['artists']
    return "Unknown"

def generate_template(file_names, include_duration):
    template = '''<div class="PlaylistItem">
                        <div class="playlist-item-content">
                            <!-- Song details -->
                            <div class="song-thumb">
                                <!-- Song thumbnail and details -->
                                <p class="song-no">{serialNo}</p>
                                <div class="song-img-container">
                                    <img src="./Assest/Image/songs/{filename}" class="song-img">
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
                                <i class="fas fa-heart"></i>
                            </span>
                        </div>
                    </div>\n'''

    templates = []
    for index, filename in enumerate(file_names, start=1):
        song_name = closest_match(filename) or os.path.splitext(filename)[0].replace("_", " ").title()
        artist_name = get_artist_name(song_name)
        duration_line = f'<span class="song-duration">{generate_random_duration()}</span>' if include_duration else '<!-- <span class="song-duration"></span> -->'
        templates.append(template.format(serialNo=str(index).zfill(2), filename=filename, songName=song_name, artists_Name=artist_name, duration_line=duration_line))
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
    include_duration = True  # Change this to False if you want to comment out the duration line
    templates = generate_template(file_names, include_duration)
    output_file_path = os.path.join(folder_path, "output.txt")
    save_to_file(output_file_path, templates)
    print(f"Templates saved to {output_file_path}")

if __name__ == "__main__":
    main()