import pandas as pd
import streamlit as st

data = { "name": ['John','Alice','Bob','Mary'],
        "age" : [23,45,32,34]
}

df = pd.DataFrame(data)




st.write(df)