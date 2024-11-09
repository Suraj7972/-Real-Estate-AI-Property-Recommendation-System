import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import NearestNeighbors
from ttkthemes import ThemedStyle

# Load the dataset
dataset_path = 'properties_data.csv'
df = pd.read_csv(dataset_path)

# Drop unnecessary columns for recommendation
df = df[['id', 'price', 'size_in_sqft', 'no_of_bedrooms', 'quality', 'neighborhood']]

# Drop rows with missing values
df = df.dropna()

# Separate numerical and categorical columns
numerical_cols = ['price', 'size_in_sqft', 'no_of_bedrooms']
categorical_cols = ['quality', 'neighborhood']

# Create transformers
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Create preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Create a Nearest Neighbors model using cosine similarity
knn_model = NearestNeighbors(n_neighbors=5, metric='cosine')

# Fit the preprocessor
X_preprocessed = preprocessor.fit_transform(df[numerical_cols + categorical_cols])

# Fit the Nearest Neighbors model
knn_model.fit(X_preprocessed)

# Function to get property recommendations
def get_recommendations(property_features):
    property_features_preprocessed = preprocessor.transform(property_features)
    indices = knn_model.kneighbors(property_features_preprocessed)[1][0]
    recommended_properties = df.iloc[indices]
    return recommended_properties

# GUI setup
def on_submit():
    input_property = {
        'price': float(price_entry.get()),
        'size_in_sqft': float(size_entry.get()),
        'no_of_bedrooms': int(bedrooms_entry.get()),
        'quality': quality_combobox.get(),
        'neighborhood': location_combobox.get()
    }
    
    input_features = pd.DataFrame([input_property], columns=numerical_cols + categorical_cols)
    recommendations = get_recommendations(input_features)
    
    result_label.config(text=recommendations)

# Create the main GUI window
root = tk.Tk()
root.title("Property Recommendation System")

# Load background image
background_image = Image.open("Dubai Real estate background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Set the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configure a themed style
style = ThemedStyle(root)
style.set_theme("arc")  # Choose your preferred theme

# Create and place GUI widgets using frames
frame = ttk.Frame(root, padding="20")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

price_label = ttk.Label(frame, text="Price:", font=('Helvetica', 14))
price_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

price_entry = ttk.Entry(frame, font=('Helvetica', 14))
price_entry.grid(row=0, column=1, padx=10, pady=5)

size_label = ttk.Label(frame, text="Size in sqft:", font=('Helvetica', 14))
size_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

size_entry = ttk.Entry(frame, font=('Helvetica', 14))
size_entry.grid(row=1, column=1, padx=10, pady=5)

bedrooms_label = ttk.Label(frame, text="Number of Bedrooms:", font=('Helvetica', 14))
bedrooms_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

bedrooms_entry = ttk.Entry(frame, font=('Helvetica', 14))
bedrooms_entry.grid(row=2, column=1, padx=10, pady=5)

quality_label = ttk.Label(frame, text="Quality:", font=('Helvetica', 14))
quality_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

quality_values = df['quality'].unique()
quality_combobox = ttk.Combobox(frame, values=quality_values, font=('Helvetica', 14))
quality_combobox.grid(row=3, column=1, padx=10, pady=5)

location_label = ttk.Label(frame, text="Location:", font=('Helvetica', 14))
location_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

location_values = df['neighborhood'].unique()
location_combobox = ttk.Combobox(frame, values=location_values, font=('Helvetica', 14))
location_combobox.grid(row=4, column=1, padx=10, pady=5)

submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="", font=('Helvetica', 14))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
