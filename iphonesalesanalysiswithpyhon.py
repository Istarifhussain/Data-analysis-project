# For the iphon sales analysis task,I have a collect a dataset cotaining data about the sales of iphones in india on flipkart.It will be an ideal dataset to analyze the sales of iphones in India.

# Importing necessary Python libraries
import pandas as pd                # For data manipulation and analysis
import numpy as np                 # For numerical operations (not used directly here but useful in data analysis)
import plotly.express as px        # For creating interactive and quick visualizations
import plotly.graph_objects as go  # For advanced/custom visualizations (not used directly here)

# Reading the dataset 'apple_products.csv' into a pandas DataFrame
data = pd.read_csv("apple_products.csv")

# print(data.head())              # Shows the first 5 rows of the dataset to understand the structure
# print(data.isnull().sum())      # Checks for missing values in each column
# print(data.describe())          # Provides basic statistics (mean, std, min, max, etc.) for numerical columns



# Sorting the dataset by 'Star Rating' in descending/ascending order to get top-rated products first
highest_rated = data.sort_values(by=["Star Rating"], ascending=False)

# Taking only the top 10 highest rated products
highest_rated = highest_rated.head(10)
# print(highest_rated['Product Name'])    # Prints the product names of top 10 rated iPhones


# iphone = highest_rated['Product Name'].value_counts()   # Counts how many times each product appears
# label = iphone.index                                    # Gets product names as labels
# count = highest_rated["Number Of Ratings"]              # Gets the number of ratings
# figure = px.bar(highest_rated, x=label, y=count, title="Number of ratings of highest Rated Iphone")
# figure.show()                                           # Shows the bar chart


# iphone = highest_rated['Product Name'].value_counts()   # Again counting occurrences of iPhone models
# label = iphone.index                                    # Gets product names
# count = highest_rated["Number Of Reviews"]              # Gets review counts
# figure = px.bar(highest_rated, x=label, y=count, title="Number of Reviews of highest Rated Iphone")
# figure.show()                                           # Shows the plot


# figure = px.scatter(
#     data_frame=data,
#     x="Number Of Ratings",
#     y="Sale Price",
#     size="Discount Percentage",
#     title="Relationship between sale price and number of ratings of iphones"
# )
# figure.show()


figure = px.scatter(
    data_frame=data,
    x="Number Of Ratings",          # X-axis: Number of ratings
    y="Discount Percentage",        # Y-axis: Discount given on the product
    size="Sale Price",              # Size of bubble = sale price of iPhone
    title="Relationship between Discount Percentage and number of ratings of iphones"
)
figure.show()                       # Display the interactive scatter plot
