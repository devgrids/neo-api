from ai.random_video.pexels_random_video import PexelsRandomVideo
from flask import jsonify, request

random_video = PexelsRandomVideo()

def handle():  
    try:
        data = request.get_json()
        query = data['query']
        quantity = data['quantity']

        videos = random_video.search(query, quantity)
        url_videos = []

        for video in videos:
            url_videos.append(random_video.get_data(video))
 
        return jsonify({"data": url_videos})
    except Exception as e:
        return jsonify({"data": str(e)})
