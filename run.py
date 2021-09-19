import generate
import crop
import change_background
import resound

model_id = "obama"

img_path = "./inputs/images/obama.jpg"
img_name = "obama"

video_path = "./inputs/videos/fortnite.mp4"
video_name = "fortnite"

background_path = "inputs/backgrounds/rushmore.jpg"

#generate.run_model(model_id,img_path, img_name, video_path, video_name)

#cropped_video_path = crop.crop_video(img_name, video_name)
cropped_video_path = "./outputs/cropped/obama-fortnite.mp4"

#changed_background_path = change_background.change_background(img_name,video_name,cropped_video_path,background_path)
changed_background_path = "./outputs/bg_changed/obama-fortnite.mp4"

final_path = resound.apply_original_sound(img_name, video_name, cropped_video_path, changed_background_path)

