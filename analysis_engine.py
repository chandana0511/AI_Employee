from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier

def perform_regression(df, features, target):
    model = LinearRegression()
    model.fit(df[features], df[target])
    return model

def perform_clustering(df, features, n_clusters=3):
    model = KMeans(n_clusters=n_clusters)
    model.fit(df[features])
    return model

def perform_classification(df, features, target):
    model = DecisionTreeClassifier()
    model.fit(df[features], df[target])
    return model

if __name__ == "__main__":
    df = pd.DataFrame({
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [2, 4, 6, 8, 10],
        'Target': [0, 1, 0, 1, 0]
    })
    regression_model = perform_regression(df, ['Feature1', 'Feature2'], 'Target')
    clustering_model = perform_clustering(df, ['Feature1', 'Feature2'])
    classification_model = perform_classification(df, ['Feature1', 'Feature2'], 'Target')

    print("Regression Coefficients:", regression_model.coef_)
    print("Cluster Centers:", clustering_model.cluster_centers_)
