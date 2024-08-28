# Synthetic EEG Data Generation for Bias Reduction in Motor Imagery Classification
## Overview

Our project is focused on assisting individuals with motor disabilities by exploring the potential of EEG (Electroencephalography) technology. Specifically, we aim to demonstrate that an EEG headset can detect when a person imagines moving their right or left arm, without any actual physical movements.

![image](https://github.com/user-attachments/assets/1b93a296-52d1-47cb-a6ed-38b6062ca288)


## Problem Statement

While we have successfully shown that a model can be trained to identify binary motor imagery (right or left imagined movement) with high accuracy for a single patient (88% accuracy on training and 76% on validation), a significant challenge remains: generalization across individuals.

Each person's brain waves are unique, which makes it difficult to apply a model trained on one person to another without significant loss of accuracy. The core challenge is to develop a model that is general enough to be used by different individuals with minimal calibration, thereby avoiding the need for retraining from scratch for each new user.
## Synthetic EEG Data Generation using VAE
![image](https://github.com/user-attachments/assets/6161faf1-43bf-4f8a-8579-c8cf93f362a0)


To address the challenge of individual variability in EEG signals, we propose the use of a **Variational Autoencoder (VAE)** to generate synthetic EEG data. VAEs are a type of generative model that can learn the underlying distribution of the data and generate new data points that are similar to the original ones.

### How It Works

1. **Training the VAE**: We start by training a VAE on EEG signals collected from three individuals (user_a, user_b, and user_c), while withholding the data from one individual (user_d) from the training process. Later, we'll use user_d's data as a validation set to monitor improvements. The VAE is trained to encode these signals into a latent space and then decode them back into the original signal space.

2. **Generating Synthetic Data**: Once trained, the VAE can generate synthetic EEG signals by sampling from the latent space. These synthetic signals can be used to augment the training data, providing a more diverse set of examples for training classification models.

3. **Improving Generalization**: By including synthetic data in the training process, the classification model can learn to recognize motor imagery patterns that are common across different individuals, improving its ability to generalize to new users.

### Benefits
- **Bias Mitigation**: By generating diverse synthetic data, the VAE can help reduce biases that may arise from training on a limited or homogeneous dataset, leading to a more fair and inclusive model that performs well across different populations.
- **Reduced Need for Retraining**: With a more generalizable model, the need for retraining on new users is minimized, making the technology more accessible and user-friendly.
- **Data Augmentation**: The synthetic data can enhance the robustness of the model by providing additional training examples, especially in scenarios where real data is scarce or difficult to collect.


## How to Run

In this repository, you will find three main notebooks that contain step-by-step instructions for each phase of the project:

1. **Building the Dataset from Raw Files**  
   - Run `build_raw_emotiv_dataset.ipynb` to generate the dataset needed for training and evaluation. This notebook processes the raw EEG data and prepares it for use in the classifier.

2. **Build the EEG Classifier**  
   - Use `X-BrainNet_LSTM.ipynb` to train the EEG classifier. This notebook guides you through the process of building and training a model to classify motor imagery based on the prepared dataset.

3. **Generate Synthetic Data**  
   - Run `X-BrainVAE.ipynb` to generate synthetic EEG data. This notebook demonstrates how to use a Variational Autoencoder (VAE) to create synthetic data that can be used to improve model generalization and reduce bias.

Follow these notebooks in sequence to replicate the study and explore the potential of EEG-based motor imagery classification.
