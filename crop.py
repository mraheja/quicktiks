

import os

def crop_video(img_name, video_name):
    filename = f"{img_name}-{video_name}.mp4"
    path = f"./results/primitives/{img_name}/synthesis/imitations/{filename}"
    output_path = f"./outputs/cropped/{filename}"
    os.system(f"ffmpeg -i {path} -filter:v \"crop=in_w/3:in_h:2*in_w/3:0\" {output_path}")
    return output_path

