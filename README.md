<h1>🧠 Customer Segmentation Using K-Means Clustering</h1>

<p><strong>Internship:</strong> Prodigy InfoTech Virtual Internship</p>
<p><strong>Project By:</strong> Prakrathi</p>
<p><strong>Topic:</strong> K-Means Clustering on Mall Customer Data</p>

<hr>

<h2>🔍 Project Overview</h2>
<p>This machine learning project uses the K-Means clustering algorithm to segment mall customers based on their <strong>Annual Income</strong> and <strong>Spending Score</strong>. Clustering helps identify distinct customer groups for targeted marketing.</p>

<hr>

<h2>📊 Features Used for Clustering</h2>
<ul>
  <li><code>Annual Income (k$)</code> – Yearly income of a customer</li>
  <li><code>Spending Score (1-100)</code> – Score assigned by the mall based on customer spending behavior</li>
</ul>

<hr>

<h2>⚙️ Steps Performed</h2>
<ol>
  <li>📥 Load and clean dataset (<code>Mall_Customers.csv</code>)</li>
  <li>🔍 Extract relevant features for clustering</li>
  <li>📏 Standardize data using <code>StandardScaler</code></li>
  <li>🧪 Train K-Means model with <code>n_clusters = 5</code></li>
  <li>🎯 Take user input and predict which cluster the customer belongs to</li>
  <li>📈 Visualize all clusters and highlight the user's input</li>
  <li>📋 Show average characteristics of each cluster</li>
</ol>

<hr>

<h2>🧠 Algorithm Used</h2>
<ul>
  <li><strong>K-Means Clustering</strong> with <code>k=5</code></li>
  <li>Initialization with <code>k-means++</code></li>
  <li><code>n_init=10</code> and <code>random_state=42</code> for reproducibility</li>
</ul>

<hr>

<h2>📸 Visualization</h2>
<ul>
  <li>Clusters are displayed in different colors using Seaborn</li>
  <li>User input is shown as a <span style="color:red;"><strong>red 'X'</strong></span> marker on the graph</li>
  <li>X-axis: Annual Income</li>
  <li>Y-axis: Spending Score</li>
</ul>

<hr>

<h2>🧪 Sample Output</h2>
<pre>
=== Enter Customer Details ===
Annual Income (k$): 70
Spending Score (1-100): 85

Prediction: This customer belongs to Cluster 4

=== Cluster Characteristics ===
         Annual Income (k$)  Spending Score (1-100)
Cluster                                            
0                     25.0                   79.0
1                     88.0                   17.0
2                     30.0                   35.0
3                     75.0                   50.0
4                     60.0                   85.0
</pre>

<hr>

<h2>📁 Files Required</h2>
<ul>
  <li><code>K-means clustering.py</code> – Project code</li>
  <li><code>Mall_Customers.csv</code> – Input dataset</li>
</ul>

<hr>

<h2>📌 Libraries Used</h2>
<ul>
  <li><code>Pandas</code></li>
  <li><code>Matplotlib</code></li>
  <li><code>Seaborn</code></li>
  <li><code>scikit-learn</code></li>
</ul>

<hr>

<h2>🙌 Learnings</h2>
<ul>
  <li>How to apply K-Means Clustering for unsupervised learning</li>
  <li>How to scale features properly for clustering</li>
  <li>How to interpret and visualize clusters</li>
  <li>How to integrate real-time user prediction with visualization</li>
</ul>

<hr>

<h2>🏁 Conclusion</h2>
<p>This project demonstrates customer segmentation using clustering techniques, helping businesses target the right group of customers based on spending habits and income.</p>

<p><strong>✅ Completed as part of the Prodigy InfoTech Internship Program</strong></p>
