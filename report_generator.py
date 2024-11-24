import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_report(df, title="Data Analysis Report"):
    sns.pairplot(df)
    plt.suptitle(title)
    plt.savefig('report.png')
    plt.show()

    with open('report_summary.txt', 'w') as f:
        summary = df.describe()
        f.write(summary.to_string())
    print("Report generated successfully!")

if __name__ == "__main__":
    df = pd.DataFrame({
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [2, 4, 6, 8, 10],
        'Target': [0, 1, 0, 1, 0]
    })
    generate_report(df)
