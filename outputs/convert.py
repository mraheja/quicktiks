import os

for file in os.listdir("./final"):
	path = "./final/" + file
	new_file = file.replace(".mp4",".gif")
	new_path = f"./gifs/{new_file}"
	if(os.path.exists(new_path)):
		continue
	os.system(f"ffmpeg -i {path} {new_path}")
