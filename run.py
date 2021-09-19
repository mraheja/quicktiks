import generate
import crop
import change_background
import resound
import sys

img, img_ext, video, video_ext, background, background_ext = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]

model_id = img

img_path = f"./inputs/images/{img}.{img_ext}"
img_name = img

video_path = f"./inputs/videos/{video}.{video_ext}"
video_name = video

background_path = f"inputs/backgrounds/{background}.{background_ext}"

generate.run_model(model_id,img_path, img_name, video_path, video_name)

cropped_video_path = crop.crop_video(img_name, video_name)

changed_background_path = change_background.change_background(img_name,video_name,cropped_video_path,background_path)

final_path = resound.apply_original_sound(img_name, video_name, cropped_video_path, changed_background_path)

