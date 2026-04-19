import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    df = pd.read_csv("medical_examination.csv")
    df['overweight'] = (df['weight'] / ((df['height']/100)**2)) > 25

    sns.countplot(x='cardio', data=df)
    plt.savefig("catplot.png")