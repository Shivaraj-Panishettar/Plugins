# -*- coding: utf-8 -*-
"""rgb to pcd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LF3ekRsexQE4C9Rd0daP34q4fgPjFxLK
"""

pip install numpy open3d Pillow

# Step 2: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Change this to your image file nameimage_path = '/content/drive/My Drive/pothole.jpeg'

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Specify the path to your RGB image
image_path = '/content/drive/My Drive/pothole.jpeg'  # Change this

# Load the RGB image
img = Image.open(image_path)
img_np = np.array(img)

# Convert the RGB image to grayscale for depth simulation
gray_img = np.mean(img_np, axis=2)  # Average across the color channels
depth_img = (255 - gray_img).astype(np.uint8)  # Invert for depth

# Display the depth image
plt.imshow(depth_img, cmap='gray')
plt.axis('off')
plt.show()

# Save the depth image
depth_image_path = '/content/depth_image.png'
Image.fromarray(depth_img).save(depth_image_path)

import open3d as o3d
import numpy as np
from PIL import Image

# Specify the paths to your images
rgb_image_path = '/content/drive/My Drive/pothole.jpeg'  # Change this
depth_image_path = '/content/drive/MyDrive/depth.png'  # Change this if saved elsewhere

# Load the RGB image
rgb_img = Image.open(rgb_image_path)
rgb_np = np.array(rgb_img)

# Load the depth image
depth_img = Image.open(depth_image_path)
depth_np = np.array(depth_img)

# Ensure the depth image is single-channel and convert to float
depth_np = depth_np.astype(np.float32) / 255.0  # Normalize to [0, 1]

# Get the dimensions of the images
height, width, _ = rgb_np.shape

# Create the point cloud
x, y = np.meshgrid(np.arange(width), np.arange(height))
z = depth_np.flatten()  # Flatten the depth array

# Stack points and colors
points = np.column_stack((x.flatten(), y.flatten(), z))
colors = rgb_np.reshape(-1, 3) / 255.0  # Normalize RGB values

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

# Save the point cloud to PCD format
output_path = '/content/output.pcd'
o3d.io.write_point_cloud(output_path, pcd)

# Step 3: Import Libraries
import open3d as o3d
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Step 4: Load RGB Image
rgb_image_path = '/content/drive/My Drive/pothole.jpeg'  # Change this
rgb_img = Image.open(rgb_image_path)
rgb_np = np.array(rgb_img)

# Step 5: Create Synthetic Depth Image
gray_img = np.mean(rgb_np, axis=2)  # Average across the color channels
depth_img = (255 - gray_img).astype(np.uint8)  # Invert for depth

# Step 6: Resize Depth Image to Match RGB Image Dimensions
depth_img_resized = Image.fromarray(depth_img).resize((rgb_np.shape[1], rgb_np.shape[0]))
depth_np = np.array(depth_img_resized)

# Step 7: Ensure Depth Image is Single-Channel and Normalize
depth_np = depth_np.astype(np.float32) / 255.0  # Normalize to [0, 1]

# Step 8: Create the Point Cloud
height, width = rgb_np.shape[:2]
x, y = np.meshgrid(np.arange(width), np.arange(height))
z = depth_np.flatten()  # Flatten the depth array

# Stack points and colors (simulate LiDAR-like distribution)
points = np.column_stack((x.flatten(), y.flatten(), z))  # (x, y, z) coordinates
colors = rgb_np.reshape(-1, 3) / 255.0  # Normalize RGB values

# Step 9: Create Open3D Point Cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

# Step 10: Downsample the Point Cloud using Voxel Grid Filter
voxel_size = 0.05  # Adjust this size to see a noticeable effect
downsampled_pcd = pcd.voxel_down_sample(voxel_size)

# Step 11: Save the Downsampled Point Cloud to PCD Format
downsampled_output_path = '/content/downsampled_output.pcd'
o3d.io.write_point_cloud(downsampled_output_path, downsampled_pcd)

# Step 12: Download the Downsampled PCD File
from google.colab import files
files.download(downsampled_output_path)

# Optional: Visualize the Downsampled Point Cloud
o3d.visualization.draw_geometries([downsampled_pcd])

# Optional: Print number of points before and after downsampling
print("Original point cloud size:", len(pcd.points))
print("Downsampled point cloud size:", len(downsampled_pcd.points))

import cv2
import numpy as np
import open3d as o3d

# Load your RGB image from Google Drive
image_path = '/content/drive/My Drive/pothole.jpeg'  # Change this to your image path
rgb_image = cv2.imread(image_path)

# Placeholder for depth map (simulate random depth for demonstration)
# In a real application, use a depth estimation model here
depth_map = np.random.rand(*rgb_image.shape[:2]) * 10  # Random depth values

# Intrinsic parameters (example values)
fx, fy = 525, 525  # Focal lengths
cx, cy = rgb_image.shape[1] // 2, rgb_image.shape[0] // 2  # Center of the image

# Create point cloud
points = []
colors = []

for y in range(rgb_image.shape[0]):
    for x in range(rgb_image.shape[1]):
        Z = depth_map[y, x]
        if Z > 0:  # Only consider valid depth values
            X = (x - cx) * Z / fx
            Y = (y - cy) * Z / fy
            rgb = rgb_image[y, x]
            points.append([X, Y, Z])
            colors.append(rgb / 255.0)  # Normalize RGB to [0, 1]

# Convert to Open3D format
points = np.array(points)
colors = np.array(colors)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

# Save to PCD file
pcd_output_path = '/content/drive/MyDrive/point_cloud.pcd'  # Change this to your desired output path
o3d.io.write_point_cloud(pcd_output_path, pcd)

# Visualize the point cloud (optional)
o3d.visualization.draw_geometries([pcd])

print(f'Point cloud saved to {pcd_output_path}')