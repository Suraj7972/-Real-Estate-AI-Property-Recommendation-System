# -Real-Estate-AI-Property-Recommendation-System

Dubai Property Recommendation System

This project provides a user-friendly interface to recommend suitable properties based on user preferences. It leverages a dataset of over 80,000 Dubai real estate listings scraped from Bayut using the "instascrap" extension.

![Screenshot 2024-11-09 123331](https://github.com/user-attachments/assets/c7c39adf-f099-4d7e-99aa-a9e7fc0dad2d)


Dataset:

Source: Bayut website (scraped)
Size: 80,000+ rows
Features:
id (unique identifier)
price
size_in_sqft
no_of_bedrooms
quality
neighborhood
Technology Stack:

Python
Tkinter (GUI library)
Pandas (data manipulation)
Scikit-learn (machine learning)
StandardScaler (numerical feature scaling)
OneHotEncoder (categorical feature encoding)
ColumnTransformer (combines transformers)
NearestNeighbors (recommendation algorithm)
ttkthemes (optional - for theming the GUI)
Code Structure:

Data Preprocessing:

Loads the dataset from a CSV file (properties_data.csv).
Drops unnecessary columns for recommendations (e.g., id).
Handles missing values by dropping rows with missing entries.
Separates numerical and categorical columns.
Creates transformers for numerical feature scaling (StandardScaler) and categorical feature encoding (OneHotEncoder) using ColumnTransformer.
Fits the transformers on the training data.
Recommendation Model:

Creates a Nearest Neighbors model with cosine similarity for finding similar properties.
Fits the model on the preprocessed data.
GUI Implementation:

Defines a function (get_recommendations) to recommend properties based on user input.
Creates the main GUI window with a background image and themed style using ttkthemes.
Utilizes a frame to organize widgets like labels, entry fields, comboboxes, and buttons.
Labels and entry fields allow users to specify their desired price, size, number of bedrooms, quality, and location.
Comboboxes provide options based on unique values from the dataset for quality and location.
A submit button triggers the on_submit function upon click.
The on_submit function:
Extracts user input values.
Creates a DataFrame with user preferences.
Preprocesses user input features.
Uses the model to fetch recommendations (similar properties) based on user preferences.
Displays the recommended properties in a dedicated label within the GUI.
Running the Application:

Install Dependencies:
Bash
pip install pandas scikit-learn tkinter ttkthemes
Use code with caution.

Download the Dataset: Place the scraped Dubai real estate dataset (properties_data.csv) in the same directory as the Python script. (Note: Downloading scraped data might violate terms of service. Ensure you have the right to use the data)
Run the Script:
Bash
python property_recommendation_system.py
Use code with caution.

![Screenshot 2024-11-09 123352](https://github.com/user-attachments/assets/3355c251-7e36-45c5-9671-e976b3d648a3)

![Screenshot 2024-11-09 124343](https://github.com/user-attachments/assets/35c59ab0-3e38-4c22-9292-d6d214200141)



Disclaimer:

This project is for educational purposes only. The dataset used is for demonstration purposes and might not be redistributable.

