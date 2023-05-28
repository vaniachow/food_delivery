# Order Delivery Time Prediction using LSTM

This repository contains a project that focuses on predicting the delivery time for orders based on distance and the number of items per trip using an LSTM (Long Short-Term Memory) model.

## Introduction

The project involves analyzing a dataset that provides information about dispatch time, customer location, longitude, latitude, trip ID, and courier ID. The dataset is cleaned and processed to calculate the distance between the store's location and the customer's location, as well as the number of items per trip.

## Dependencies

To run this project, the following dependencies are required:

- pandas version: 2.0.1
- numpy version: 1.24.3
- plotly.express
- scikit-learn
- keras

Please make sure you have the necessary dependencies installed before executing the code.

## Setup

To get started with this project, follow these steps:

1. Clone the repository or download the code files.
2. Install the required dependencies using the following command:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Set the path to the CSV file containing the dataset in the `csv_file_path` variable in the code.

## Usage

Follow these instructions to use the project:

1. Run the `main.py` file.
2. The program will read the dataset from the CSV file and perform data cleaning and preprocessing.
3. It will then generate scatter plots to visualize the relationship between time taken and distance, as well as the relationship between time taken and the number of items per trip.
4. The generated graphs will be displayed as follows:

   ### Relationship Between Time Taken and Distance
   
   ![Scatter Plot: Time Taken vs. Distance](/Users/vaniachow/Desktop/Screenshots/Screenshot 2023-05-28 at 4.50.49 PM.png)
   
   ### Relationship Between Time Taken and Number of Items per Trip
   
   ![Scatter Plot: Time Taken vs. Number of Items per Trip](/Users/vaniachow/Desktop/Screenshots/Screenshot 2023-05-28 at 4.51.02 PM.png)

5. Next, an LSTM model will be built to make predictions.
6. The model will be trained using the dataset, and the training progress will be displayed.
7. After training, the program will prompt you to enter a distance and the number of items per trip.
8. The LSTM model will use the provided input to predict the estimated delivery time.
9. The estimated delivery time will be displayed on the console.
