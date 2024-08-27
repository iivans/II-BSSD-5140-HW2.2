from SortFunctions import quick_sort, binary_search_sub
from PixelFunctions import compare_pixels, store_pixels, pixels_to_points, grayscale
from PIL import Image

def main():
    IMG_NAME = 'monkey'
    try:
        with Image.open(IMG_NAME + '.jpg') as im:
            pixels = store_pixels(im)
            print("Stored pixels.")
            
            # Sort the pixels using quick_sort
            sorted_pixels = pixels.copy()
            quick_sort(sorted_pixels, compare_pixels)
            print("Sorted pixels.")
            
            # Convert to grayscale
            grayscale_img = im.convert('L')  # Convert the image to grayscale
            grayscale_pixels = store_pixels(grayscale_img)  # Get grayscale pixel data
            
            # Save and display the grayscale image
            grayscale_img.save('grayscale_' + IMG_NAME + '.jpg', 'JPEG')
            
            # Prompt user for a threshold
            try:
                threshold = int(input("Enter the red value threshold (0-255): "))
                if not (0 <= threshold <= 255):
                    raise ValueError("Threshold must be between 0 and 255.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                return
            
            # Binary search for the threshold value
            sorted_reds = [r[0][0] for r in sorted_pixels]
            subi = binary_search_sub(sorted_reds, 0, len(sorted_reds) - 1, threshold)
            print("Sublist of reds starts at index:", subi)
            
            # Highlight pixels that match or exceed the threshold
            highlighted_pixels = sorted_pixels[subi:]
            
            # Create an image from the highlighted pixels
            highlighted_img = pixels_to_points(im.size, highlighted_pixels, mode='RGB')
            highlighted_img.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
            
            # Create an overlay image with highlighted pixels
            overlay_img = Image.new('RGB', im.size)
            overlay_pixels = store_pixels(overlay_img)
            
            # Populate overlay_pixels with highlighted pixel data
            for i, px in enumerate(highlighted_pixels):
                if i < len(overlay_pixels):
                    overlay_pixels[i] = (px[0], px[1])  # Ensure px[0] is (r, g, b) and px[1] is (x, y)
            
            # Create the overlay image
            overlay_img = pixels_to_points(im.size, overlay_pixels, mode='RGB')
            
            # Combine grayscale and overlay images
            final_img = Image.blend(grayscale_img.convert('RGB'), overlay_img, alpha=0.5)
            final_img.save('final_' + IMG_NAME + '.jpg', 'JPEG')
            print("Final image saved.")
            
    except FileNotFoundError:
        print(f"File '{IMG_NAME}.jpg' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()