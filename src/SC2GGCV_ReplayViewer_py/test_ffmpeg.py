import os
import glob
import pyautogui



for x in pyautogui.getAllWindows():  
    print(x)


x = 0

def record_vid(name):

    global x
    folder_path = ""

    if not (folder_path + str(x) + ".mp4") in glob.glob(folder_path + "*.mp4"):
        filename = folder_path + str(x) + ".mp4"
    else:
        x += 1
        record_vid(name)

    video_size = "1366x768"

    # os.system(f"""ffmpeg -rtbufsize 1500M -f dshow -f gdigrab -framerate 30 -draw_mouse 1 -video_size {video_size} -i title={name} -pix_fmt yuv420p -profile:v baseline -y Huangbaohua.mp4""")
    os.system(f"""ffmpeg -rtbufsize 1500M -f dshow -f gdigrab -framerate 30 -draw_mouse 1 -i title={name} -pix_fmt yuv420p -profile:v baseline -y {filename}""")



# record_vid("Steam")







# Dzialajaca linijka FFMPEG
# ffmpeg -rtbufsize 1500M -f dshow -f gdigrab -framerate 30 -draw_mouse 1 -i title=Steam -pix_fmt yuv420p -profile:v baseline -y Huangbaohua.mp4
# Video do Klatek -> ffmpeg -i 0.mp4 %04dout.png