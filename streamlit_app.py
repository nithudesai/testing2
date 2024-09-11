import streamlit as st
import pandas as pd

# Load your DataFrame (replace with your actual data)
data = {'description': ['apple', 'banana', 'orange', 'grape', 'chicken soup', 'ramen', 'green apple']
       , 'id': ['1', '2', '3', '4', '5', '6', '7']
       }
df = pd.DataFrame(data)
# Concatenate 'id' with 'description' using a lambda function
df['combined'] = df.apply(lambda row: f"{row['id']} | {row['description']}", axis=1)


def radio_change(label):
    if label == 'Reject':
        st.text_area(label='Reject Reason')
        st.text_input('Keyword search:', '')


def search_dropdown(search_keyword):
    if search_keyword:
        # Filtering logic
        filtered_df = 'test'

        # Display filtered results in a dropdown
        selected_item = st.selectbox('Select a suggestion:', ['Opt 1', 'Opt 2', 'Opt 3', ])

        st.write(f'Selected item: **{selected_item}**')


label_options = ['Accept', 'Reject']
selected_label = st.radio("Select Label:", label_options, key='label_radio')

with st.form('test'):
    if selected_label == 'Reject':
        reject_text = st.text_area(label='Reject Reason')
        search_keyword = st.text_input('Keyword search:', '')

        # Displays a dropdown populated with search results from search_keyword
        search_dropdown(search_keyword)
    submit_button = st.form_submit_button('Submit')
