import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

#1. Load Dataset (Replace with your file path)
file_path = 'Mall_Customers.csv'  # Change to your dataset path
df = pd.read_csv(file_path)

#2. Select Features for Clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

#3. Standardize Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#4. Train K-Means (5 Clusters)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42, n_init=10)
kmeans.fit(X_scaled)
df['Cluster'] = kmeans.labels_  # Save clusters to DataFrame

#5. Take User Input & Predict Cluster
try:
    print("\n=== Enter Customer Details ===")
    annual_income = float(input("Annual Income (k$): "))
    spending_score = float(input("Spending Score (1-100): "))
    
    # Scale input and predict
    user_data = pd.DataFrame([[annual_income, spending_score]], 
                            columns=['Annual Income (k$)', 'Spending Score (1-100)'])
    user_scaled = scaler.transform(user_data)
    user_cluster = kmeans.predict(user_scaled)[0]
    print(f"\nPrediction: This customer belongs to Cluster {user_cluster}")

#6. Visualize Clusters (Including User Input)
    plt.figure(figsize=(12, 7))
    
    # Plot all customers (colored by cluster)
    sns.scatterplot(
        x='Annual Income (k$)', 
        y='Spending Score (1-100)', 
        hue='Cluster', 
        data=df, 
        palette='viridis',
        s=80,
        alpha=0.7,
        legend='full'
    )
    
    # Highlight the user's input in RED
    plt.scatter(
        annual_income, 
        spending_score, 
        color='red', 
        s=200, 
        marker='X', 
        label='Your Input'
    )
    
    plt.title('Customer Segmentation (K-Means Clustering)')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.grid(True)
    plt.show()

#7.Show Cluster Stats
    print("\n=== Cluster Characteristics ===")
    print(df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean())

except ValueError:
    print("Error: Please enter valid numbers.")
