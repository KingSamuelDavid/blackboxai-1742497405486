import ffmpeg

def denoise_video(input_video):
    ffmpeg.input(input_video).filter("hqdn3d_cuda", 4.0).output("denoised.mp4").run()

denoise_video("video_output.mp4")