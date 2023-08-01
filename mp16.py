import cv2
import os

def resize_image(input_image_path, output_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new dimensions (50% of the original size)
    new_width = int(width * 0.5)
    new_height = int(height * 0.5)

    # Resize the image to the new dimensions
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)

# Prepare the input and output directories
input_dir = '/Users/auchitya/VS pro/summer school/rand100'
output_dir = '/Users/auchitya/VS pro/summer school/rand200'
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory
input_files = os.listdir(input_dir)

# Process each image and resize to 50%
for filename in input_files:
    input_image_path = os.path.join(input_dir, filename)
    output_image_path = os.path.join(output_dir, filename)

    resize_image(input_image_path, output_image_path)
