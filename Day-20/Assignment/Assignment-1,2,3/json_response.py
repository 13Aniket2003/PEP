## student course detail task---1
import pandas as pd
data=pd.read_json("http://127.0.0.1:8000/api/student/?format=json")
print(data)