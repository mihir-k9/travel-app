import os
import streamlit as st

# from dotenv import load_dotenv
from backend import * 

# load_dotenv()
hf_token = os.environ.get('HUGGING_FACE_TOKEN')


def main():
    st.set_page_config(page_title='Cool Travel Spots')
    st.header("Upload an image to get recommendation for similar travel spots")
    uploaded_img = st.file_uploader(label='Upload an image', type='jpg')

    if uploaded_img:
        data = uploaded_img.getvalue()
        
        with open(uploaded_img.name, 'wb') as f:
            f.write(data)

        st.image(uploaded_img, caption='Uploaded Image', use_column_width=True)
        
        img_labels = classify_image(uploaded_img.name)
        label_type = img_labels[1]['label']
        
        travel_location = get_location(label_type, hf_token)
        location = show_output(travel_location)

        with st.expander('Labels returned'):
            st.write(label_type)
        
        with st.expander('Suggested location'):
            st.write(location)


if __name__ == "__main__":
    main()
