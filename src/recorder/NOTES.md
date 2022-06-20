# Notes:

working 'title' must be in ""     -->     name = f'"{name}"'
working desktop rec               -->     ffmpeg -f dshow -f gdigrab -video_size 1920x1080 -framerate 30 -i desktop -vcodec libx264 -preset ultrafast -qp 0 -pix_fmt yuv444p video.mkv
overwrite output file if exists   -->     ffmpeg -y ...
in case .mp4 broke                -->     ffmpeg -i foo.mp4.part -c copy -f mp4 foo.mp4
in case .mkv -> .mp4              -->     ffmpeg -i inputVideoName.mkv -c:v copy -c:a copy outputVideoName.mp4
video to frames                   -->     ffmpeg -i 0.mp4 %04dout.png
kill ffmpeg process               -->     taskkill /im ffmpeg.exe /t /f
force PathLib to create folder    -->     .mkdir(parents=True, exist_ok=True)

can save 'subprocess.Popen' to variable       # but need to return object to kill outside function
rec_out.stdin.write(bytes("q",'UTF-8'))       # pass 'q' for ffmpeg, sometimes cant kill process