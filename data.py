# dependencies
import pandas as pd

# read data into dataframe
df = pd.read_csv('Resources/cities.csv')

# save to html
table = df.to_html('data.html', index=False)
print(table)
