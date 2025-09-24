import pandas as pd
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load the data into a pandas DataFrame
data = pd.read_csv('user_item_ratings.csv')

# Define the Reader object
# The Reader class is used to parse a file containing ratings.
reader = Reader(rating_scale=(1, 5))

# Load the data into the Dataset object
data = Dataset.load_from_df(data[['user_id', 'item_id', 'rating']], reader)

# Split the data into 75% training and 25% testing
trainset, testset = train_test_split(data, test_size=0.25)

# Use the KNNWithMeans algorithm
algo = KNNWithMeans(k=50, sim_options={'name': 'cosine', 'user_based': True})

# Train the algorithm on the trainset
algo.fit(trainset)
# Predict ratings for the testset
predictions = algo.test(testset)

# Compute and print Root Mean Squared Error (RMSE)
accuracy.rmse(predictions)
# Predict ratings for the testset
predictions = algo.test(testset)

# Compute and print Root Mean Squared Error (RMSE)
accuracy.rmse(predictions)