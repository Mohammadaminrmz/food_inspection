import numpy as np
import pandas as pd
import plotly.express as px
import scipy as sp
from pandas.api.types import CategoricalDtype
import seaborn as sns


df = pd.read_csv('Food_Establishment_Inspection_Data.csv',low_memory=False)
rest=df.groupby(by=['Description'])
print(rest.describe())