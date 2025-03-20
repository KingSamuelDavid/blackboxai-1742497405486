import whisper

def transcribe_audio(input_video):
    model = whisper.load_model("large").cuda()
    result = model.transcribe(input_video)
    with open("subtitles.srt", "w") as f:
        f.write(result["text"])

transcribe_audio("video_output.mp4")