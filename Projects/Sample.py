import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv("your_file.csv", encoding='ISO-8859-1')

# Drop serial number if not needed
df.drop(columns=['s/no'], inplace=True)

# Check for nulls
df.dropna(inplace=True)

# Extract features and labels
X = df['text']
y = df['class']
