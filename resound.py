import os

def apply_original_sound(img_name, video_name, cropped_path, changed_background_path):
    filename = f"{img_name}-{video_name}.mp4"
    output_path = f"./outputs/final/{filename}"
    os.system(f"ffmpeg -i {cropped_path} temp.mp3 -y")
    os.system(f"ffmpeg -i {changed_background_path} -i temp.mp3 -c copy -map 0:v:0 -map 1:a:0 {output_path}")