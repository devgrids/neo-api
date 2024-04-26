def audio_youtube_download(link):
    import os
    import shutil
    from pytube import YouTube
    
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio = True).first()
    print("downloading audio")
    output_file = audio.download()

    if os.path.exists(output_file):
        print("downloaded audio!")
    else:
        print("download error!")

    basename = os.path.basename(output_file)
    nombre, formato = basename.split(".")
    audio_file = f"{nombre}.mp3"
    audio_file = audio_file.replace(" ", "_")
    os.rename(basename,audio_file)
    shutil.move(audio_file, "assets/audios")
    return "assets/audios/" + audio_file