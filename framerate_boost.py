from rife_ai import RIFE

def increase_fps(input_video, target_fps):
    model = RIFE("rife-v4").cuda()
    smooth_video = model.infer(input_video, target_fps)
    return smooth_video

increase_fps("video_output.mp4", 60)