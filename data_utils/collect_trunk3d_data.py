import os
import sys
from trunk3d_util import DATA_PATH, collect_point_label

BASE_DIR = os.path.dirname(os.path.abspath(__file__))# data_utils
print(f"BASE_DIR = {BASE_DIR}")
ROOT_DIR = os.path.dirname(BASE_DIR)#..
print(f"ROOT_DIR = {ROOT_DIR}")
sys.path.append(BASE_DIR)

trunk_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/trunk_path.txt'))]
trunk_paths = [os.path.join(DATA_PATH, p) for p in trunk_paths]
print(trunk_paths)
# exit()
output_folder = ROOT_DIR
# if not os.path.exists(output_folder):
#     os.mkdir(output_folder)

# Note: there is an extra character in the v1.2 data in Area_5/hallway_6. It's fixed manually.
trunk_pre = trunk_paths[0]
trunk_post = trunk_paths[1]

pre_filelist = os.listdir(trunk_pre)
post_filellst = os.listdir(trunk_post)
# print(pre_filelist)
out_filename = os.path.join(output_folder, "Data.npy")
# print(out_filename)
if not os.path.exists(out_filename):
    fout = open(out_filename, "w")
    fout.close()

# for prefile in pre_filelist:
    # print(prefile)
    # tks = prefile.split('_')
    # postfile = f"{tks[0]}_{tks[1]}_Postop_Analyse_rgb_gt.obj"
    # prefilepath = os.path.join(trunk_pre, prefile)
    # postfilepath = os.path.join(trunk_post, postfile)
    
collect_point_label(trunk_pre, trunk_post, out_filename, 'numpy')
# for trunk_path in trunk_paths:
#     print(trunk_path)
#     try:
#         elements = trunk_path.split('/')
#         out_filename = elements[-3]+'_'+elements[-2]+'.npy' # Area_1_hallway_1.npy
#         collect_point_label(anno_path, os.path.join(output_folder, out_filename), 'numpy')
#     except Exception:
#         print(anno_path, 'ERROR!!')
