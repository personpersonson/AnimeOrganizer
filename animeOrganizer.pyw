import glob
import os
import shutil
import time


anime_folder = r'C:/Users/korisnik/Downloads/Anime'
uncat_folder = r'C:/Users/korisnik/Downloads/Anime/Uncategorized'

if not os.path.exists(anime_folder):
    os.makedirs(anime_folder)

while True:
    good_path_mp4 = r'C:/Users/korisnik/Downloads/anime-*-*-*.mp4'
    bad_path_mp4 = r'C:/Users/korisnik/Downloads/anime-*.mp4'

    good_anime_list = glob.glob(good_path_mp4)

    for file in good_anime_list:
        filename_arr = os.path.basename(file).split("-")
        if not os.path.exists("C:/Users/korisnik/Downloads/Anime/" + str(filename_arr[1]) + "/" + str(filename_arr[2])):
            os.makedirs("C:/Users/korisnik/Downloads/Anime/" + str(filename_arr[1]) + "/" + "Season " + str(filename_arr[2]))
        shutil.move("C:/Users/korisnik/Downloads/" + os.path.basename(file), "C:/Users/korisnik/Downloads/Anime/" + str(filename_arr[1]) + "/" + "Season " + str(filename_arr[2]) + "/" + "episode " + str(filename_arr[3]))

    bad_anime_list = glob.glob(bad_path_mp4)

    for file in bad_anime_list:
        if not os.path.exists(uncat_folder):
            os.makedirs(uncat_folder)
        shutil.move("C:/Users/korisnik/Downloads/" + str(os.path.basename(file)), uncat_folder + "/" + str(os.path.basename(file)))

    time.sleep(1)


