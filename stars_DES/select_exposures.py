""" Script to select the exposures with lower horizintal banding
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load table
    tab = '2reg_stat_g.csv'
    df = pd.read_csv(tab)
    # expnum,ccdnum,nite,t_eff,band,region,mad,mean,std,npix

    # By CCD, reflect stats
    ccd = df['ccdnum'].unique()
    
    print(df.columns)

    fig, ax = plt.subplots(2, 2, figsize=(6, 6), sharex=True, sharey=True)
    for i, axis in enumerate(ax.flatten()):
        aux_df = df.loc[(df['ccdnum'] == ccd[i])]
        axis.scatter(aux_df['mean'], aux_df['mad'], s=5) # mad
        axis.set_title(ccd[i])
    plt.show()

