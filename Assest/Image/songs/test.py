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


import os
import difflib

# List of song names
song_names = [
    "A Thousand Years", "Afterdark", "Afterlife (Deluxe)", "All The Little Lights (Deluxe)",
    "American Dream", "Backslide", "Beautiful Things", "Best of Hip Hop", "Bling Bang Bang Born",
    "Born To Die (The Paradise Edition)", "Ckay: The First", "Creatures In Heaven", "D Anum (Serbian)",
    "Dandelions", "Dark Matter", "Decide", "Dreamland", "Everlasting Romance", "Favorite",
    "February Sky", "Feel Something", "Fountain Baby", "Four (Deluxe)", "Future Hits",
    "Happy Birthday Ronan Keating", "Harleys In Hawaii", "I Like The Way You Kiss Me",
    "Indigo (Extended)", "Lady Lady", "Let Me Down Slowly", "Let's Talk About Love", "Let's Play",
    "Lovin' On Me", "Middle Of The Night", "My Own Way", "My World 2.0", "Orgy Of The Damned",
    "Pedro", "People", "Seven Inches Of Satanic Panic", "Stray", "Tarantula Heart", "Test",
    "The Piper's Call", "Treadmill Pop", "Unheard", "Utopia", "Vol. 1: Music From The HBO Original Series",
    "Wasteland Baby (Special Edition)", "Way Down We Go", "Wmg"
]

def closest_match(file_name):
    # Function to find the closest match of the file name in the list of song names
    return difflib.get_close_matches(file_name, song_names, n=1, cutoff=0.3)

def generate_template(file_names):
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
                                    <span class="song-subtitle">19/20/20</span>
                                </div>
                            </div>
                        </div>
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
        song_name = closest_match(filename)[0] if closest_match(filename) else "Unknown"
        templates.append(template.format(serialNo=str(index).zfill(2), filename=filename, songName=song_name))
    return templates

def save_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.writelines(content)

def main():
    folder_path = "./"  # Update this with your folder path
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    templates = generate_template(file_names)
    output_file_path = os.path.join(folder_path, "output.txt")
    save_to_file(output_file_path, templates)
    print(f"Templates saved to {output_file_path}")

if __name__ == "__main__":
    main()
