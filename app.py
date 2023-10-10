import os
import pandas as pd
import streamlit as st

# local testing only
from dotenv import load_dotenv
from backend import * 

# local testing only
load_dotenv()
hf_token = os.environ.get('HUGGING_FACE_TOKEN')

def increment(x):
    if x < 4:
        return x + 1


def main():
    st.set_page_config(page_title='Cool Travel Spots')
    st.header("Travel Spots Recommender")
    uploaded_img = st.file_uploader(label='Upload an image', type='jpg')

    if uploaded_img:
        attempt = 0
        data = uploaded_img.getvalue()

        with open(uploaded_img.name, 'wb') as f:
            f.write(data)

        st.image(uploaded_img, caption='Uploaded Image', use_column_width=True)
        
        runtime_classify, img_labels = classify_image(uploaded_img.name)
        label_type = img_labels[0]['label']
        
        runtime_api, travel_location = get_location(label_type, hf_token)
        location = show_output(travel_location)

        with st.sidebar:
            st.subheader("Behind the Scenes")
    
            st.info(runtime_classify)
            df = pd.DataFrame.from_dict(img_labels).sort_values('score', ascending=False)
            st.dataframe(df)

            st.text(f"Label sent: {df.iloc[attempt]['label']}")
            st.info(runtime_api)
        
        with st.expander('Suggested location'):
            st.write(location)

        # st.button(label='Retry', on_click=increment(attempt))

if __name__ == "__main__":
    main()
