import imageio

def get_image_size(file_path):
    image = imageio.imread(file_path)
    image_width, image_height = image.shape[1], image.shape[0]
    return image_width, image_height