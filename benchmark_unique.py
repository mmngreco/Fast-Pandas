from Benchmarker import Benchmarker
import numpy as np


def pandas_unique(df):
    return df["A"].unique()


def numpy_unique(df):
    return np.unique(df["A"].values)


params = {
    "df_generator": 'pd.DataFrame(np.random.randn(1, df_size, (df_size, 2)), columns=list("AB"))',
    "functions_to_evaluate": [pandas_unique, numpy_unique],
    "title": "Pandas Unique vs Numpy Unique",
}

benchmark = Benchmarker(**params)
benchmark.benchmark_all()
benchmark.print_results()
benchmark.plot_results()
