import os
import ffmpeg
import time
import subprocess

path = r'I:\ch1'
output_path = r'I:\carRecording'
height = 602

video_item_list = os.listdir(path)

for item in video_item_list:
# item = video_item_list[0]
	infile = os.path.join(path,item)
	print("processing: {}".format(infile))
	outfile = os.path.join(output_path,item.split('.')[0] + '.mp4')
	a= time.time()

	# stream = ffmpeg.input(infile)
	# audio =  stream.audio
	# video = stream.video.filter('scale', width='-1', height=str(height))
	# stream = ffmpeg.output(audio, video, outfile)
	# ffmpeg.run(stream)
	
	stream = ffmpeg.input(infile)
	audio = stream.audio
	video = stream.video.filter('scale', width='-1', height=str(height))
	stream = ffmpeg.output(audio, video, outfile, vcodec='h264_nvenc',threads=4)
	ffmpeg.run(stream)


	os.remove(infile)

	b=time.time()
	print("{} seconds used".format(round(b-a),4))
	print("output: {}".format(outfile))

def shutdown_computer():
	if os.name == 'nt':
	    # For Windows operating system
	    os.system('shutdown /s /t 0')
	elif os.name == 'posix':
	    # For Unix/Linux/Mac operating systems
	    os.system('sudo shutdown now')
	else:
	    print('Unsupported operating system.')

# Calling the shutdown_computer() function to initiate shutdown
# shutdown_computer()