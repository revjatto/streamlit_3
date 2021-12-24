import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Registration Form Application",
                   page_icon="bar_chart", layout="wide")


st.image('Kings.PNG', width=900)


register = st.sidebar.selectbox("Select an option", ["Registration Form", "GPS", "Data Visualization", "quiz"])
if register == 'Registration Form':
    st.header('Streamlit registration form')

    st.subheader("Complete the form to register")
    first, last = st.columns(2)

    first.text_input("First Name")
    last.text_input("Surname")

# instead of interger, you can also pass a list[]
    email, mob = st.columns([2, 1])
    email.text_input("Email Address")
    mob.text_input("Mobile Number")

    user, pw, pw2 = st.columns(3)  # using 3 columns here
    user.text_input('Username')
    pw.text_input('Password', type='password')
    pw2.text_input('Confirm Password', type='password')

    ch, bl, sub = st.columns(3)
    ch.checkbox("I Agree")
    sub.button("Submit")
elif register == 'GPS':
    city = pd.DataFrame({
        'nigerian_cities': ['Lagos', 'Abeokuta', 'Port Harcourt', 'Maiduguri', 'Kano',
                            'Katsina', 'Nnewi, Anambra', 'Agbor, Ika South', 'Ikeja, Lagos', 'Ughelli', 'Akure'],
        'latitude': [6.465422, 7.145244, 4.824167, 11.833333, 12.000000, 12.985531, 6.010519, 6.264092, 6.605874, 5.500187, 7.250771],
        'longitude': [3.406448, 3.327695, 7.033611, 13.150000, 8.516667, 7.617144, 6.910345, 6.201883, 3.349149, 5.993834,  5.210266]
    })
    st.subheader('Nigerian city Lat and Long')
    st.map(city)
elif register == 'Data Visualization':
        st.subheader('Data Visualization project')
        
        
        #setup file upload

        uploaded_file = st.sidebar.file_uploader(
        label='Upload your csv or Excel File.', type=['csv', 'xlsx'])

        global df
        if uploaded_file is not None:
            print(uploaded_file)
            st.write('File Uploaded successfully!')
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            st.image('data-visualization.jpg')
            df = pd.read_excel(uploaded_file)

        global numeric_columns
        try:
            print(df)
            numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
        except Exception as e:
            print(e)
            st.write('Please upload a csv or xlsx file to start')

#add select widget to the sidebar

        chart_select = st.sidebar.selectbox(
        label="Select a chart type",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot'])


        if chart_select == 'Scatterplots':
            st.sidebar.subheader('Scatterplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
            plot = px.scatter(data_frame=df, x=x_values, y=y_values)
             # displaying the chart
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

elif register == 'quiz':
    
    st.subheader('Small quiz project')
    qual = st.radio('What is your highest qualification',
                   ('Bachelors Degree', 'Masters', 'PHD'))
    if qual == 'Bachelors Degree':
        st.write('You have done 16 years of education')
    elif qual == 'Masters':
        st.write('You have done 18 years of education')
    else:
        st.write('Congratulations! You are a highly qualified person')

#st.selectbox('Select', [1,2,3,4])
    option = st.selectbox('What is your favourite social media platform?', ('Facebook', 'Instagram', 'WhatsApp',
                                                                        'Linkedl', 'Snapchat'))
    if option == 'Facebook':
        st.write('The Facebook platform is good for friends and family getting together')
        st.image('facebook.jpg')
    elif option == 'Instagram':
        st.write('Showing off your small movie clips and pictures on social media')
        st.image('Instagram.jpg')
    elif option == 'WhatsApp':
        st.write('WhatsApp users will now have the option to turn on disappearing messages by default for all new chats')
        st.image('WhatsApp.png')
    elif option == 'Linkedl':
        st.write('For professional and business connection')
        st.image('Linkedin.jpg')

    else:
        st.write('Snapchat Puts Additional Emphasis on Advertising in New Features')
        st.image('snapchat.jpg')


    cars = st.multiselect('What are your favourite car brands',['Toyota', 'Aston Martin', 'Rolls Royce', 'BMW', 'Mercedes Benz', 'Audi'] )
    st.write('You selected:', cars)
    st.image('toyota.jpg')

    

####### End of Registration Form Project ###########

    