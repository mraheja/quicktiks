import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type="pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")

def change_background(img_name, video_name, cropped_path, background_path, fps = 30):
    filename = f"{img_name}-{video_name}.mp4"
    output_path = f"./outputs/bg_changed/{filename}"
    change_bg.change_video_bg(cropped_path, background_path, frames_per_second = fps, output_video_name=output_path, detect = "person")
    return output_path