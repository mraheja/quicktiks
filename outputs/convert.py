import os

for file in os.listdir("./final"):
	path = "./final/" + file
	new_file = file.replace(".mp4",".gif")
	new_path = f"./gifs/{new_file}"
	new_file2 = file.replace(".mp4",".mp3")
	new_path2 = f"./audios/{new_file2}"
	if(not os.path.exists(new_path)):
		os.system(f"ffmpeg -i {path} {new_path}")
	if(not os.path.exists(new_path2)):
		os.system(f"ffmpeg -i {path} {new_path2}")
