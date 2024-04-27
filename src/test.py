from ai.text_to_image.dreamlike_art.diffusion_dreamlike_art_text_to_image import DiffusionDreamlikeArtTextToImage
import matplotlib.pyplot as plt

text_to_image = DiffusionDreamlikeArtTextToImage()

prompt = """dreamlikeart, a grungy woman with rainbow hair, travelling between dimensions, dynamic pose, happy, soft eyes and narrow chin,
extreme bokeh, dainty figure, long hair straight down, torn kawaii shirt and baggy jeans
"""

image = text_to_image.generate(prompt)

print("[PROMPT]: ",prompt)
plt.imshow(image);
plt.show()
plt.axis('off');