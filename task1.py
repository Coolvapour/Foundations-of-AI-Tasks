# Unit: CCS 2226 Foundations of AI
# Student Name: Moses Kiprono Leleito
# Registration Number: CIT-227-073/2024
# Task: Practical Task One - MNIST Dataset

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def run_mnist_classifier():
    # Load the MNIST dataset from OpenML
    print("Loading MNIST dataset...")
    # I am using parser='liac-arff' to ensure compatibility with my local environment
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='liac-arff')
    X, y = mnist["data"], mnist["target"]

    # Split the data into training (60k) and testing (10k) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Stochastic Gradient Descent (SGD) classifier
    # This is efficient for handling the 70k images in the dataset
    clf = SGDClassifier(random_state=42, max_iter=1000, tol=1e-3)

    print("Training the classifier on digits 0-9...")
    clf.fit(X_train, y_train)

    # Evaluate performance on the test set
    y_pred = clf.predict(X_test)

    print("\n--- Model Evaluation Results ---")
    print(classification_report(y_test, y_pred))

    # Verification: Display a sample image and its prediction
    sample_idx = 0
    plt.imshow(X_test[sample_idx].reshape(28, 28), cmap='binary')
    plt.title(f"Actual: {y_test[sample_idx]} | Predicted: {y_pred[sample_idx]}")
    plt.axis('off')
    print(f"Showing visualization for test sample {sample_idx}...")
    plt.show()

if __name__ == "__main__":
    run_mnist_classifier()