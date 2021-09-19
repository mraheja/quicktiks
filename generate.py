import os
import os.path as osp
import platform
import argparse
import time
import sys
import subprocess
from base64 import b64encode


#SET-UP CODE
gpu_ids = "0"
image_size = 512
num_source = 2
assets_dir = "./iPERCore/assets"
output_dir = "./results"
work_asserts_dir = os.path.join("./assets")
if not os.path.exists(work_asserts_dir):
    os.symlink(osp.abspath(assets_dir), osp.abspath(work_asserts_dir),
               target_is_directory=(platform.system() == "Windows"))

cfg_path = osp.join(work_asserts_dir, "configs", "deploy.toml")


#RUN MODEL
def run_model(model_id, img_path, img_name, video_path, video_name, fps = 30):
  src_path = f"\"path?={img_path},name?={img_name}\""
  ref_path = f"\"path?={video_path}," \
              f"name?={video_name}," \
              "pose_fc?=400," \
              f"fps?={fps}\""

  cmd = f"python3 -m iPERCore.services.run_imitator  \
    --gpu_ids     {gpu_ids}       \
    --num_source  {num_source}    \
    --image_size  {image_size}    \
    --output_dir  {output_dir}    \
    --model_id    {model_id}      \
    --cfg_path    {cfg_path}      \
    --src_path    {src_path}      \
    --ref_path    {ref_path}"

  os.system(cmd)