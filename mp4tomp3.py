# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:35:17 2023

@author: sijian
"""
from moviepy.editor import VideoFileClip

def convert_to_mp3(input_video, output_audio, target_size_mb=20):
    # Step 1: Extract audio from the video
    video_clip = VideoFileClip(input_video)
    audio = video_clip.audio

    # Step 2: Adjust bitrate to achieve target file size
    while True:
        current_size_mb = (audio.write_audiofile(output_audio, codec="mp3").getbuffer().nbytes / (1024 * 1024))
        if current_size_mb <= target_size_mb:
            break

        # Adjusting bitrate to reduce file size
        audio = audio.set_audio_params(
            bitrate=int(audio.fps * 0.9),
            codec='pcm_s16le'
        )

if __name__ == "__main__":
    input_video_path = r"G:\方脸说：马督工被封禁，王刚做蛋炒饭被迫道歉，中国的言论自由进一步衰减！中国的言论自由，是如何一步一步衰退到如今的地步的？言论管控有对我们产生了哪些影响？.mp4"
    output_audio_path = r"G:\方脸说：马督工被封禁，王刚做蛋炒饭被迫道歉，中国的言论自由进一步衰减！中国的言论自由，是如何一步一步衰退到如今的地步的？言论管控有对我们产生了哪些影响？.mp3"
    target_size_mb = 20

    convert_to_mp3(input_video_path, output_audio_path, target_size_mb)