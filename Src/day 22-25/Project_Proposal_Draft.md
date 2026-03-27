# Capstone Project Proposal: Plant Disease Diagnosis

**Sector:** Agriculture

## 1. Industry Context
Crop diseases and pests cause massive agricultural and financial losses. By utilizing AI vision systems (such as cameras and drones), we can detect these issues early before they spread and destroy the harvest.

## 2. Problem Statement
The objective of this project is to develop an image-based plant disease detector. The model will analyze images of leaves and fruits to classify them into two primary categories: healthy vs. diseased.

## 3. Key Stakeholders
* **Farmers:** Primary users who need rapid, on-field diagnostics.
* **Agricultural Scientists:** To monitor disease spread and trends.
* **NGOs:** To deploy sustainable farming technologies in rural areas.

## 4. Proposed System Features
To ensure the system is useful in real-world scenarios, it will include:
* **Image Capture Interface:** A simple method to upload or snap plant photos.
* **Real-Time Results:** Instant classification of the plant's health.
* **Treatment Recommendations:** Actionable advice based on the detected disease.
* **Offline Mobile Model:** Ensuring functionality in rural areas without internet access.

## 5. Technical Scope & Stack
This project will be built using the following computer vision and machine learning technologies:
* **Algorithms:** Convolutional Neural Networks (CNN) like MobileNet or ResNet.
* **Image Processing:** OpenCV.
* **Data Preparation:** Data augmentation to expand the training dataset.
* **Deployment:** TensorFlow Lite (for the offline mobile model) and a Backend API.