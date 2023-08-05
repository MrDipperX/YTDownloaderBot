from pytube import YouTube
import os


def available_resolutions(link):
    yt = YouTube(link)
    videos = yt.streams.filter(mime_type='video/mp4', progressive=True)
    return set(tuple(str(video.resolution) for video in videos))


def downloader_video(link, quality=None):
    yt = YouTube(link)
    video = yt.streams.filter(mime_type='video/mp4', progressive=True, res=quality).desc().first()
    video_path = video.download()

    return video_path, video.title


def downloader_audio(link):
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    out_file = audio.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    if not os.path.exists(new_file):
        os.rename(out_file, new_file)
    return new_file, audio.title


a = "https://www.youtube.com/watch?v=eXLSBdxm_cs"
