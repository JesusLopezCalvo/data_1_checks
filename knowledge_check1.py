import requests
import pandas as pd

response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
print(response.status_code)
print(response.json())
data = response.json()['data']
datausa = pd.DataFrame(data)
datausa.shape

# I dont understand why "datausa.shape" does not work in .py but works in .ipynb