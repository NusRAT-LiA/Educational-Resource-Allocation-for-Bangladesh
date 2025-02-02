import pandas as pd
import joblib
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/education_data.csv")
X = df[["Total_Students", "Budget", "Teachers", "Internet_Access"]]

num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(X)

df["Cluster"] = kmeans.labels_
infra_features = ["Internet_Access", "Budget", "Teachers"]

# Normalize using Min-Max Scaling
scaler = MinMaxScaler()
df[infra_features] = scaler.fit_transform(df[infra_features])

weights = {
    "Internet_Access": 0.2,  # 20%
    "Budget": 0.5,           # 50%
    "Teachers": 0.3          # 30%
}

df["Infrastructure_Score"] = (
    df["Internet_Access"] * weights["Internet_Access"] +
    df["Budget"] * weights["Budget"] +
    df["Teachers"] * weights["Teachers"]
)
# df["Infrastructure_Score"] = df["Infrastructure_Score"].clip(0, 10)


joblib.dump(kmeans, "/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/models/kmeans_model.pkl")
df.to_csv("/Users/macbook/Documents/GitHub/Educational-Resource-Allocation-for-Bangladesh/backend/data/education_data_clustered.csv", index=False)
