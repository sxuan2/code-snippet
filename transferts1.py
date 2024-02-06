import os
import ffmpeg
import time

output_path = r'C:\Users\sijian\Downloads\Video'
height = 1080

input_path = r'C:\Users\sijian\Downloads\Video'
filels = os.listdir(input_path)

for file in filels:
    filename = '-'.join(file.split('.')[:-1])
    filetype = file.split('.')[-1]

    if filetype == 'ts':
        print("Processing: {}".format(file))
        outfile = filename + '.mp4'
        a = time.time()

        stream = ffmpeg.input(os.path.join(input_path, file))
        audio = stream.audio
        video = stream.video.filter('scale', width=1920, height=-1).h264_nvenc()  # Using NVENC for H.264 encoding
        stream = ffmpeg.output(audio, video, os.path.join(output_path, outfile), vf=f'scale=1920:{height}', threads=4)
        
        try:
            ffmpeg.run(stream)
        except ffmpeg.Error as e:
            print(f"An error occurred: {e.stderr}")

        os.remove(os.path.join(input_path, file))
        b = time.time()
        print("{} seconds used".format(round((b - a), 4)))
        print("Output: {}".format(outfile))
    else:
        print('{} is not a ts file, will skip'.format(file))
        continue
