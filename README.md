# Text Classification App

This application helps companies allocate user requests to specific departments. It is designed to handle multilingual inputs.

## Problem Statement

Companies often receive user requests in various languages and need to route them to the appropriate department. This application provides a solution by leveraging **Sentence Transformers** ([documentation](https://www.sbert.net/)) for embedding user requests and a **K-Nearest Neighbors (KNN)** algorithm to classify them into the correct department.

## Solution Overview

1. **Sentence Transformers**: Used to generate semantic embeddings of user requests, enabling the model to understand the meaning of text inputs, even in different languages.
2. **KNN Algorithm**: Classifies the embedded requests into predefined categories (departments).
3. **Multilingual Support**: Handles requests in multiple languages, with Bulgarian used as an example in the sample data.
4. **Exploration Notebook**: Includes a Jupyter Notebook for:
   - Exploring the dataset.
   - Saving artifacts such as the label encoder (for target classes) and KNN model.
   - Evaluating model accuracy and visualizing the confusion matrix.
5. **Deployment**: The application is deployed using Docker, Django, and Gunicorn:
   - **Django**: Provides a flexible framework for building both a user-friendly UI (HTML templates) and an API for programmatic access.
   - **Gunicorn**: Ensures efficient handling of web requests in production.

## Quick Start

1. Make sure you have Docker and Docker Compose installed.
2. Clone this repository.
3. Run the application:
   ```sh
   docker-compose up
