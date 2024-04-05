import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item interaction matrix
data = {
    'User1': [5, 4, 0, 0, 1],
    'User2': [0, 2, 3, 4, 5],
    'User3': [1, 0, 5, 2, 3],
    'User4': [4, 0, 2, 3, 0]
}

df = pd.DataFrame(data)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(df)
#pip install scikit-learn
# Function to get recommendations for a target user
def get_recommendations(target_user):
    similar_users = user_similarity[target_user]
    ranked_users = sorted(range(len(similar_users)), key=similar_users.__getitem__, reverse=True)
    
    recommendations = []
    
    for user in ranked_users:
        if user != target_user:
            recommendations.extend(df.iloc[user][df.iloc[target_user] == 0].index.tolist())
    
    return list(set(recommendations))

# Example usage
target_user = 0
recommendations = get_recommendations(target_user)
print("Recommendations for User", target_user + 1, ":", recommendations) 