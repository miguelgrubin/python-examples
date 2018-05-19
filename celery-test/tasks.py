import time
import subprocess
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/1')


@app.task
def add(x, y):
    time.sleep(10)
    return x + y


@app.task
def ffmpeg_to_mp4(file_path):
    dst = "/tmp/" + file_path.split('/')[-1]
    cmd = [
        "ffmpeg", "-i", file_path, "-f", "mp4",
        "-vcodec", "libx264",
        "-preset", "fast", "-profile:v", "main",
        "-acodec", "aac", dst, "-hide_banner"
    ]
    p_compress = subprocess.Popen(cmd)
    p_compress.wait()
    p_move = subprocess.Popen(["mv", dst, file_path])
    p_move.wait()
