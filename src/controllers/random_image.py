from ai.random_image.pexels_random_image import PexelsRandomImage
from ai.random_image.unsplash_random_image import UnsplashRandomImage
from flask import jsonify, request

# random_image = UnsplashRandomImage()
random_image = PexelsRandomImage()

def handle():  
    try:
        data = request.get_json()
        query = data['query']
        quantity = data['quantity']

        images = random_image.search(query, quantity)
        url_images = []

        for image in images:
            url_images.append(random_image.get_data(image))
 
        return jsonify({"data": url_images})
    except Exception as e:
        return jsonify({"data": str(e)})
