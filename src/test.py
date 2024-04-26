from helpers.audio_youtube_download import audio_youtube_download 
from ai.transcription_video.openai_transcription_video import OpenaiTranscriptionVideo
    
transcription_video = OpenaiTranscriptionVideo()

result_audio = audio_youtube_download("https://www.youtube.com/watch?v=mYcznTcpKdU");
print(result_audio)
transcription_mp3 = transcription_video.transcription(result_audio)