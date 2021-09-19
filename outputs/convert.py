import os

for file in os.listdir("./final"):
	path = "./final/" + file
	new_file = file.replace(".mp4",".gif")
	os.system(f"ffmpeg -i {path} ./gifs/{new_file}")
