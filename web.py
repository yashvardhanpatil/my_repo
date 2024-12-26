import pandas as pd
import streamlit as st

data = { "name": ['John','Alice','Bob','Mary','yash'],
        "age" : [23,45,32,34,24]
}

df = pd.DataFrame(data)




st.write(df)