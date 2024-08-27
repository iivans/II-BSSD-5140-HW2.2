from PIL import Image

def compare_pixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]   # Comparing red values

def store_pixels(im):
    width = int(im.size[0])
    height = int(im.size[1])
    
    pixel_array = []
    if im.mode == 'RGB':
        for i in range(width):
            for j in range(height):
                r, g, b = im.getpixel((i, j))
                pixel_array.append([(r, g, b), (i, j)])
    elif im.mode == 'L':
        for i in range(width):
            for j in range(height):
                value = im.getpixel((i, j))
                pixel_array.append([(value, value, value), (i, j)])
    return pixel_array



def pixels_to_points(size, pixels, mode='RGB'):
    outimg = Image.new(mode, size)
    for p in pixels:
        outimg.putpixel(p[1], p[0])
    return outimg

def grayscale(im, pixels):
    for i in range(len(pixels)):
        r, g, b = pixels[i][0]
        grayscale_value = int(0.299 * r + 0.587 * g + 0.114 * b)
        pixels[i] = [(grayscale_value, grayscale_value, grayscale_value), pixels[i][1]]