#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def userGuide_pandas10Minutes():
    """ https://pandas.pydata.org/docs/user_guide/10min.html """
    
    print('https://pandas.pydata.org/docs/user_guide/10min.html#basic-data-structures-in-pandas')
    print(dir(pd.Series), dir(pd.DataFrame), sep='\n')

    print('# https://pandas.pydata.org/docs/user_guide/10min.html#object-creation')
    s = pd.Series([1, 3, 4, np.nan, 6, 8])
    print(repr(s))

    dates = pd.date_range("20130101", periods=6)
    print(repr(dates))

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(repr(df))

    df2 = pd.DataFrame({
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    })
    print(repr(df2))
    print(df2.dtypes)
    print(dir(df2))

    print('# https://pandas.pydata.org/docs/user_guide/10min.html#viewing-data')
    print(df.head())
    print(df.tail())
    print(df.index)
    print(df.columns)
    print(repr(df.to_numpy()))
    print(df2.dtypes, repr(df2.to_numpy()), sep='\n')

    print(df, df.describe(), df.T, sep='\n')
    print(df.sort_index(axis=1, ascending=False))
    print(df.sort_values(by="B"))

    # https://pandas.pydata.org/docs/user_guide/10min.html#selection
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#getitem')
    print(df, df["A"], sep='\n')
    print( df[0:3], df["20130102": "20130104"], sep='\n')

    print('# https://pandas.pydata.org/docs/user_guide/10min.html#selection-by-label')
    print(df, dates, sep='\n')
    print(df.loc[dates[0]])
    print(df.loc[:, ["A", "B"]])
    print(df.loc["20130102":"20130104", ["A", "B"]])
    print(df.loc["20130102", ["A", "B"]])
    print(df.loc[dates[0], "A"])
    print(df.at[dates[0], "A"])
   
    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#selection-by-position') 
    print(df.iloc[3])
    print(df.iloc[3:5, 0:2])
    print(df.iloc[[1, 2, 4], [0, 2]])
    print(df.iloc[1:3, :])
    print(df.iloc[:, 1:3])
    print(df.iloc[1, 1], df.iat[1, 1], sep='\n')

    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#boolean-indexing')
    print(df[df["A"] > 0])
    print(df[df > 0])
    df2 = df.copy()
    df2["E"] = ["one", "one", "two", "three", "four", "three"]
    print(df2)
    print(df2[df2["E"].isin(["two", "four"])])

    # https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#setting
    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#setting')
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
    print(s1)
    
    df["F"] = s1
    df.at[dates[0], "A"] = 0
    df.iat[0, 1] = 0
    df.loc[:, "D"] = np.array([5] * len(df))
    print(df)

    df2 = df.copy()
    df2[df2 > 0] = -df2
    print(df2)

    # https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#missing-data
    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#missing-data')
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
    df1.loc[dates[0]: dates[1], "E"] = 1
    print(df1)
    print(df1.dropna(how="any"))
    print(df1.fillna(value=5))
    print(pd.isna(df1))

    # https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#operations
    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#stats')
    print(df.mean())
    print(df.mean(1))

    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
    print(s)
    print(df.sub(s, axis="index"))

    print(df)
    print(df.apply(np.cumsum))
    print(df.apply(lambda x: x.max() - x.min()))
   
    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#histogramming') 
    s = pd.Series(np.random.randint(0, 7, size=10))
    print(s)
    print(s.value_counts())

    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#string-methods')
    s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
    print(s.str.lower())

    # https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#merge
    print('# https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/10min.html#concat')
    df = pd.DataFrame(np.random.randn(10, 4))
    print(df)
    pieces = [df[:3], df[3:7], df[7:]] # break into pieces
    print(pd.concat(pieces))

    print('# https://pandas.pydata.org/docs/user_guide/10min.html#join')
    left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
    right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
    print(left, right, sep="\n")
    print(pd.merge(left, right, on="key"))

    left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
    right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
    print(left, right, sep="\n")
    print(pd.merge(left, right, on="key"))

    # https://pandas.pydata.org/docs/user_guide/10min.html#grouping
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#grouping')
    df = pd.DataFrame({
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "bar"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8)})
    print(df)
    print(df.groupby("A")[["C", "D"]].sum())
    print(df.groupby(["A", "B"]).sum())

    # https://pandas.pydata.org/docs/user_guide/10min.html#reshaping
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#stack')
    arrays = [["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
              ["one", "two", "one", "two", "one", "two", "one", "two"]]
    index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
    df2 = df[:4]
    print(df2)

    try:
        stacked = df2.stack(future_stack=True)
    except: 
        print(pd.__version__)
        stacked = df2.stack()
    finally:
        print(stacked)
    print(stacked.unstack())
    print(stacked.unstack(1))
    print(stacked.unstack(0))

    # https://pandas.pydata.org/docs/user_guide/10min.html#pivot-tables
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#pivot-tables')
    df = pd.DataFrame({
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),})
    print(df)
    print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
)

    # https://pandas.pydata.org/docs/user_guide/10min.html#time-series
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#time-series')
    rng = pd.date_range("1/1/2012", periods=100, freq="S")
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    print(ts.resample("5Min").sum())

    rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
    ts = pd.Series(np.random.randn(len(rng)), rng)
    print(ts)
    ts_utc = ts.tz_localize("UTC")
    print(ts_utc)
    print(ts_utc.tz_convert("US/Eastern"))

    print(rng)
    print(rng + pd.offsets.BusinessDay(5))

    # https://pandas.pydata.org/docs/user_guide/10min.html#categoricals
    print("# https://pandas.pydata.org/docs/user_guide/10min.html#categoricals")
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                       "raw_grade": ["a", "b", "b", "a", "a", "e"]})
    df["grade"] = df["raw_grade"].astype("category")
    print(df["grade"])

    new_categories = ["very good", "good", "very bad"]
    df["grade"] = df["grade"].cat.rename_categories(new_categories)
    df["grade"] = df["grade"].cat.set_categories(["ver bad", "bad", "medium", "good", "very good"])
    print(df["grade"])
    print(df.sort_values(by="grade"))
    print(df.groupby("grade", observed=False).size())

    # https://pandas.pydata.org/docs/user_guide/10min.html#plotting
    print("# https://pandas.pydata.org/docs/user_guide/10min.html#plotting")
    plt.close("all")
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    ts.plot();

    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"])
    df = df.cumsum()
    plt.figure();
    df.plot();
    plt.legend(loc='best');
    #plt.show()
    
    # https://pandas.pydata.org/docs/user_guide/10min.html#importing-and-exporting-data
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#csv')
    df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
    df.to_csv("foo.csv")
    print(pd.read_csv("foo.csv"))

    df1 = df.rename(columns={0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}) # ValueError: parquet must have string column names
    df1.to_parquet("foo.parquet")
    print(pd.read_parquet("foo.parquet"))
    print(pd.__version__)
    df.to_hdf("foo.h5", "df")
    print(pd.read_hdf("foo.h5", "df"))    

    df.to_excel("foo.xlsx", sheet_name="Sheet1")
    print(pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"]))

    # https://pandas.pydata.org/docs/user_guide/10min.html#gotchas
    print('# https://pandas.pydata.org/docs/user_guide/10min.html#gotchas')
    try:
        if pd.Series([False, True, False]):
            print("I was true")
    except Exception as err:
        print(err)
        if pd.Series([False, True, False]) is not None:
            pass
        if pd.Series([False, True, False]).any():
            pass

        

if __name__ == "__main__":
    userGuide_pandas10Minutes()

