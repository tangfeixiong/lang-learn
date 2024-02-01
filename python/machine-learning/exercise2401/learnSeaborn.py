#!/usr/bin/env python3

import seaborn as sns
import matplotlib.pyplot as plt

def apiCatplot():
    """https://seaborn.pydata.org/generated/seaborn.catplot.html"""
    
    df = sns.load_dataset("titanic")
    print(df.columns, sep="\n")
    #sns.catplot(data=df, x="age", y="class")
    #sns.catplot(data=df, x="age", y="class", kind="box")
    #sns.catplot(data=df, x="age", y="class", hue="sex", kind="boxen")
    #sns.catplot(data=df, x="age", y="class", hue="sex",
    #    kind="violin", bw_adjust=.5, cut=0, split=True,)
    #sns.catplot(data=df, x="class", y="survived", col="sex",
    #    kind="bar", height=4, aspect=.6,)

    #sns.catplot(data=df, x="age", y="class", kind="violin", color=".9", inner=None)
    #sns.swarmplot(data=df, x="age", y="class", size=3)

    # Use methods on the returned FacetGrid to tweak the presentation:
    print(df.head().loc[:,["who","survived","class"]])
    g = sns.catplot(
        data=df, x="who", y="survived", col="class",
        kind="bar", height=4, aspect=.6,
    )
    g.set_axis_labels("", "Survival Rate")
    g.set_xticklabels(["Men", "Women", "Children"])
    g.set_titles("{col_name} {col_var}")
    g.set(ylim=(0, 1))
    g.despine(left=True)

    plt.show()


if __name__ == "__main__":
   import ssl
   ssl._create_default_https_context = ssl._create_unverified_context

   apiCatplot()
