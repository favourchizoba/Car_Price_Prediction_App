import streamlit as st
import pandas as pd
import joblib
import warnings 
warnings.filterwarnings('ignore')


data = pd.read_csv('CarPrice.csv')


st.markdown("<h1 style = 'color: #1D267D; text-align: center; font-size: 60px; font-family: Georgia'>CAR PRICE PREDICTION</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #A0153E; text-align: center; font-family: italic'>Built By Frances </h4>", unsafe_allow_html = True)

st.markdown("<br>", unsafe_allow_html=True)

# #add image
st.image('pngwing.com (26).png')

st.markdown("<h2 style = 'color: #132043; text-align: center; font-family: montserrat '>Background Of Study</h2>", unsafe_allow_html = True)

primaryColor="#FF4B4B"  
backgroundColor="#70E6D2"
secondaryBackgroundColor="#B4F2E8"
textColor="#31333F"
font="serif"

st.markdown("<p>The automotive industry is one of the largest and most dynamic sectors in the global economy, with a significant market for both new and used vehicles. As cars are a major financial investment for consumers, accurately predicting car prices has become increasingly important for various stakeholders, including buyers, sellers, dealerships, and financial institutions. The primary objective of this machine learning project is to develop an accurate and robust predictive model for estimating the price of a car based on its various features. By leveraging advanced machine learning algorithms, the aim is to create a model that can analyze and learn from historical car data, encompassing attributes such as make, model, year, mileage, engine type, fuel efficiency, and other relevant parameters,By developing an accurate and reliable car price prediction model, this project can assist both buyers and sellers in making informed decisions, ultimately leading to a more efficient and transparent car market.</p>", unsafe_allow_html = True)

st.sidebar.image('pngwing.com (27).png',caption = 'Welcome User')


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.header('Project Data')
st.dataframe(data, use_container_width = True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)


st.sidebar.subheader('User Input Variables')

sel_cols = ['CarName','curbweight','symboling','carheight','carlength','carbody','horsepower','price']


car = st.sidebar.selectbox('CarName', data['CarName'].unique())
curb = st.sidebar.number_input('curbweight', data['curbweight'].min(), data['curbweight'].max())
symbol = st.sidebar.number_input('symboling', data['symboling'].min(), data['symboling'].max())
height = st.sidebar.number_input('carheight', data['carheight'].min(), data['carheight'].max())
length = st.sidebar.number_input('carlength', data['carlength'].min(), data['carlength'].max())
body = st.sidebar.selectbox('carbody', data['carbody'].unique())
horse = st.sidebar.number_input('horsepower', data['horsepower'].min(), data['horsepower'].max())




#users input
input_var = pd.DataFrame()
input_var['CarName'] = [car]
input_var['curbweight'] = [curb]
input_var['symboling'] = [symbol]
input_var['carheight'] = [height]
input_var['carlength'] = [length]
input_var['carbody'] = [body]
input_var['horsepower'] = [horse]


st.markdown("<br>", unsafe_allow_html= True)
st.divider()
st.subheader('Users Inputs')
st.dataframe(input_var, use_container_width = True)


# import the transformers
car = joblib.load('CarName_encoder.pkl')
body = joblib.load('carbody_encoder.pkl')



# transform the users input with the imported scalers
input_var['CarName'] = car.transform(input_var[['CarName']])
input_var['carbody'] = body.transform(input_var[['carbody']])


# st.header('Transformed Input Variable')
# st.dataframe(input_var, use_container_width = True)



#modelling
model = joblib.load('CarPriceModel.pkl')


#to have a button for the user
if st.button('Predict Price'):
    predicted_price = model.predict(input_var)
    st.success(f"The Price of this Car is  {predicted_price[0].round()}")
    



