import os
import numpy as np
import cv2
import trimesh

def load_image(file_path):
    """Load and preprocess the image."""
    img = cv2.imread(file_path)
    img = cv2.resize(img, (256, 256))  # Resize image to 256x256
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0  # Normalize the image
    return img

def load_stl(file_path):
    """Load and preprocess the STL file."""
    mesh = trimesh.load(file_path)
    vertices = mesh.vertices
    faces = mesh.faces
    return vertices, faces

def preprocess_data(image_dir, stl_dir):
    """Preprocess all images and STL files."""
    images = []
    stl_data = []
    for img_file in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_file)
        stl_path = os.path.join(stl_dir, img_file.replace('.jpg', '.stl'))
        images.append(load_image(img_path))
        stl_data.append(load_stl(stl_path))
    return np.array(images), stl_data

image_dir = 'path/to/image_directory'
stl_dir = 'path/to/stl_directory'
images, stl_data = preprocess_data(image_dir, stl_dir)
