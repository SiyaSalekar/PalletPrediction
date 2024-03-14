import numpy as np
import cv2
import math
from PIL import Image
import os
import random


main_folder = "C:\\Users\\nfeda\\yr4\\Collab\\Processed_data_cnn\\good_data"
#files = os.listdir(folder_path)


# Initialize lists to store images for top and bottom rows
top_images = []
bottom_images = []

# Iterate through each subfolder, select images whose filenames end with "_100", and load them
for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)
    if os.path.isdir(folder_path):
        # Get list of images in the folder
        images = [f for f in os.listdir(folder_path) if f.endswith(('_300.jpg'))]
        for image_name in images:
            image_path = os.path.join(folder_path, image_name)
            
            # Load the image
            image = cv2.imread(image_path)
            
            # Draw a box around some predefined coordinates
            # Example coordinates (replace with your own)
            x, y, w, h = 96, 400, 384, 80
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Append the image to the appropriate list
            if len(top_images) < len(bottom_images):
                top_images.append(image)
            else:
                bottom_images.append(image)

# Concatenate top and bottom images horizontally
top_concatenated_image = np.hstack(top_images)
bottom_concatenated_image = np.hstack(bottom_images)

# Stack top and bottom images vertically
final_image = np.vstack([top_concatenated_image, bottom_concatenated_image])

# Show the final image
cv2.imshow('Top and Bottom Images', final_image)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()