import streamlit as st
import process_info
import time


def create_progress_bar():
    progress_text = "Generating prediction..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()


def show_prediction(image, real_class):
    prediction = process_info.make_prediction(image)
    prediction_value = prediction[0]
    if prediction_value < 0.5:
        st.markdown(
            '<font size="6">Result: <b>Parasitized</b></font>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<font size="6">Result: <b>Uninfected</b></font>',
            unsafe_allow_html=True,
        )
    if real_class is not None:
        st.markdown(
            f'<font size="4">Real classification: <b>{real_class}</b></font>',
            unsafe_allow_html=True,
        )


def create_columns(image, selected_image_name, image_class=None):
    col1, col2 = st.columns(2)
    with col1:
        if image_class is not None:
            st.image(
                image, caption=f"{selected_image_name}: '{image_class}'", width=300
            )
        else:
            st.image(image, caption=f"{selected_image_name} ", width=300)
    with col2:
        if st.button("Test on model", key=image_class):
            create_progress_bar()
            show_prediction(image, image_class)
