import pandas as pd

df = pd.read_html("https://www.webscraper.io/test-sites/tables/tables-multiple-header-rows")
print(df[0])