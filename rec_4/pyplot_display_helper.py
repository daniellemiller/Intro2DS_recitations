import math
import matplotlib.pyplot as plt
import numpy as np

def output_multi_scatter(df, columns):
    '''
    display subplots with scatter plots of the different columns.

    df:
        input dataframe

    columns:
        list of strings.
        the columns to use from df.

    '''

    # calculate number of plots
    number_of_plots = int(
        math.factorial(len(columns)) / (2*math.factorial(len(columns)-2))
    )

    # create a side by side view of that many plots
    fig, ax = plt.subplots(1, number_of_plots)

    # this is for compatability with the case of one plot.
    if number_of_plots == 1:
        ax = [ax]

    counter = 0
    for i in range(len(columns)):
        for j in range(len(columns)):
            if i>=j:
                continue

            scatp1 = df.loc[:, columns].plot.scatter(
                x=i,
                y=j,
                figsize=(20, 10),
                cmap='jet',
                c=df['diagnosis'],
                ax=ax[counter]
            )
            counter += 1



if __name__ == '__main__':
    from sklearn import datasets
    import pandas as pd

    data = datasets.load_breast_cancer()

    df = pd.DataFrame(
        data['data'],
        columns=data['feature_names']
    )


    df['diagnosis'] = data['target']

    selected_columns = ['mean area', 'mean smoothness']#, 'mean symmetry']

    output_multi_scatter(df, selected_columns)
