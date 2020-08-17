import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = Nonedf['weight'] / (df['height'] * 10**-2)**2

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def converter(data):
    if data > 25:
        return 0
    else:
        return 1

df['overweight'] = df['overweight'].apply(converter)

def normalizer(data):
    if data == 1:
        return 0
    else:
        return 1

df['gluc'] = df['gluc'].apply(normalizer)

df['cholesterol'] = df['cholesterol'].apply(normalizer)



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df[['cholesterol', 'gluc', 'smoke', 'alco', 'cardio', 'active', 'overweight']], 
            id_vars= 'cardio')



    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'
    fig, ax = plt.subplots(1, 1, figsize = (10,6))
    sns.catplot(x = 'variable', col= 'cardio', hue = 'value', data = df_cat, kind = 'count' )

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    
    df_heat = df[df['ap_lo']<= df['ap_hi']]

    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)];

    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)];

    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]

    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.tril(np.ones_like(corr, dtype=np.bool), k=-1)





    # Set up the matplotlib figure
    fig, ax = plt.subplots(1, 1, figsize = (10,6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(u, annot= True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
