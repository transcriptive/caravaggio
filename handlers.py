import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

class Pictures:
    # class used to store the image or stack of images being worked with
    # later on add optional kwargs so you can pass the directory pass when instantiating the class

    def __init__ (self):
        self.images_dict = {}

    def load(self, directory, resize=None):
        # right now this auto converts to greyscale, but that should be parametric in the future

        """
        Load grayscale images from the specified directory and store them as NumPy arrays in a dictionary.
        Optionally resize the images to the specified dimensions.

        Parameters:
        directory_path (str): Path to the directory containing the images.
        resize (tuple, optional): Tuple specifying the (width, height) to resize the images. If None, no resizing is performed.

        Returns:
        dict: Dictionary with file names (without extensions) as keys and NumPy arrays as values.
        """
        # Ensure the provided directory is a valid path
        if not isinstance(directory, str):
            raise ValueError("The path must be a string.")

        # Loop through all files in the directory, return errors as needed
        try: 
            for filename in os.listdir(directory):
                if filename.endswith(('.png', '.jpg', '.jpeg')):  # Add more extensions if needed
                    # Construct the full file path
                    file_path = os.path.join(directory, filename)
                    
                    # Open the image and convert to grayscale
                    with Image.open(file_path).convert('L') as img:
                        # Resize the image if resize dimensions are provided
                        if resize:
                            img = img.resize(resize, Image.LANCZOS)
                        
                        # Convert the image to a NumPy array
                        image_array = np.array(img)
                        
                        # Get the image title without the extension
                        title = os.path.splitext(filename)[0]
                        
                        # Store the image array in the dictionary with the title as the key
                        self.images_dict[title] = image_array
        except FileNotFoundError:
            print(f"The directory {directory} does not exist.")
        except PermissionError:
            print(f"Permission denied for accessing the directory {directory}.")
