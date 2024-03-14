import pandas as pd
import numpy as np

prices_ds = pd.Series(
    [1.5, 2, 2.5, 3],
    index=["apples", "oranges", "bananas", "strawberries"]
)

suppliers_ds = pd.Series(
    ["supplier1", "supplier2", "supplier4", "supplier3"],
    index=["apples", "oranges", "bananas", "strawberries"]
)

fruits_df = pd.DataFrame({
    "prices": prices_ds,
    "suppliers": suppliers_ds
})

print(fruits_df)