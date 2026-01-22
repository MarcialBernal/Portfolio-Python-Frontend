import streamlit as st
import pandas as pd
import time
from services.data_visual import Plots
from ui.sidebar import render_sidebar

render_sidebar()


st.set_page_config(page_title="Data Visualization", page_icon="📊",layout= "wide",)

title_placeholder = st.empty()
title_text = "📊 Data Visualization"

if "dataviz_title_done" not in st.session_state:
    st.session_state["dataviz_title_done"] = False

if not st.session_state["dataviz_title_done"]:
    for i in range(1, len(title_text) + 1):
        title_placeholder.markdown(f"# {title_text[:i]}")
        time.sleep(0.03)
    st.session_state["dataviz_title_done"] = True
else:
    title_placeholder.markdown(f"# {title_text}")


####
with st.expander("Introduction", expanded=True):
    st.markdown("""
                This project is an interactive data visualization dashboard built with Python, Pandas, Plotly, and Streamlit.  
                It allows users to explore datasets in a flexible and visual way.

                The app comes with a built-in CSV dataset, but users can also upload their own CSV files to explore.  
                Once loaded, the dashboard enables selecting which columns to plot, choosing the X and Y axes, 
                and picking the type of plot — all dynamically, as long as the data is compatible. 

                The goal of the project is to demonstrate practical data analysis and visualization skills,  
                allowing users to interact with data, generate plots, and gain insights quickly.  
                It showcases the ability to combine data manipulation, interactive plotting, and a user-friendly front-end.
                """)
    
    
try:
    test_df = pd.read_csv('data/Mental_Health_and_Social_Media_Balance_Dataset.csv')
    st.success(f"Test data set uploaded successfully!")
    plot = Plots()
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            plot.pie_plot(
                test_df, 
                x_col='Social_Media_Platform', 
                title='Average User Social Media Platform'
            )
            
        with col2:
            plot.bar_plot(
                test_df, 
                y_col='Happiness_Index(1-10)', 
                x_col='Social_Media_Platform', 
                title='Average Happiness by Social Media Platform'
            )
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            plot.line_plot(
                test_df, 
                x_col='Days_Without_Social_Media', 
                y_col='Sleep_Quality(1-10)', 
                title='Average Sleep Quality vs Days Without Social Media'
                )
            
        with col2:
            plot.screen_vs_sleep_plot(
                test_df,
                x_col='Daily_Screen_Time(hrs)',
                y_col='Sleep_Quality(1-10)',
                size_col='Happiness_Index(1-10)',
                color_col='Social_Media_Platform',
                title="Daily Screen Time vs Sleep Quality"
            )
except:
        st.error("An error has ocurred")





# Interactive plots
uploaded_file = st.file_uploader("Upload an CSV file", type=["csv"])

if uploaded_file:
    try:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        df = pd.read_csv(uploaded_file)
        
        plot_type= st.selectbox("Select chart type", ["Pie", "Bar", "Line"])
        col1 = st.selectbox("Select first column", df.columns)
        col2 = None
        if plot_type in ["Bar", "Line"]:
            col2 = st.selectbox("Select second column", df.columns)
            
        if st.button("Update Chart"):
            plot.interactive_plot(df, plot_type, col1, col2)

    except:
        st.error("An error has ocurred, maybe the file type its not correct")


