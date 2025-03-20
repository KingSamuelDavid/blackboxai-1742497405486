from celery import Celery
import os

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task(name="tasks.image_to_video")
def image_to_video(request):
    # Convert images to video
    image_list = " ".join(request["input"])
    os.system(f"python image_to_video.py --input {image_list} --fps {request['fps']}")

    # Apply AI options if selected
    if request["ai_options"].get("superres"):
        os.system(f"python super_resolution.py --input video_output.mp4 --resolution {request['ai_options']['superres']}")

    if request["ai_options"].get("denoise"):
        os.system(f"python denoise.py --input video_output.mp4")

    if request["ai_options"].get("speech2text"):
        os.system(f"python speech_to_text.py --input video_output.mp4")

    if request["ai_options"].get("framerateboost"):
        os.system(f"python framerate_boost.py --input video_output.mp4 --fps {request['ai_options']['framerateboost']}")

    return {"status": "Complete", "output": "video_output.mp4"}