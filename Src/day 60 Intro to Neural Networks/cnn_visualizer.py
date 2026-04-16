import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, Input
import matplotlib.pyplot as plt

print("Starting Deep Learning CNN & Visualization Pipeline...")

# Create an output directory to save our processed images and model
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# 1. Load and Preprocess Data (MNIST digits)
print("1. Loading Data...")
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# 2. Build the CNN Model
print("2. Building Convolutional Neural Network...")
model = models.Sequential([
    Input(shape=(28, 28, 1)), 
    layers.Conv2D(32, (3, 3), activation='relu', name='conv_layer_1'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu', name='conv_layer_2'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 3. Train the Model
print("3. Training the model...")
model.fit(train_images, train_labels, epochs=1, batch_size=64)

# Save the model architecture and weights
model.save(f'{output_dir}/mnist_cnn_model.keras')
print(f"Model saved to {output_dir}/mnist_cnn_model.keras")

# 4. Network Visualization
print("4. Visualizing Convolutional Filters / Feature Maps...")
test_img = test_images[0] # Grab a single test image (a handwritten '7')
img_tensor = np.expand_dims(test_img, axis=0) 

# Save original image
plt.imshow(test_img.reshape(28, 28), cmap='gray')
plt.title("Original Input Image")
plt.savefig(f'{output_dir}/0_original_input.png')
plt.close()

# Create a sub-model to look inside the hidden layers
layer_outputs = [layer.output for layer in model.layers[:1]] 
activation_model = models.Model(inputs=model.inputs, outputs=layer_outputs)

# Get the feature maps for the test image
activations = activation_model.predict(img_tensor)

# Plot the first 4 feature maps (how the AI sees the image)
fig, axes = plt.subplots(1, 4, figsize=(15, 4))
for i in range(4):
    # FIXED: Extracting the 1st image [0], all pixels [:, :], and the i-th filter [i]
    axes[i].imshow(activations[0, :, :, i], cmap='viridis')
    axes[i].set_title(f'Filter {i+1}')
    axes[i].axis('off')
    
plt.savefig(f'{output_dir}/1_feature_maps.png')
plt.close()

print(f"✅ Pipeline Complete! Model and Visualizations saved in '{output_dir}' folder.")