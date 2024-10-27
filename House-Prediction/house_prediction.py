import joblib
import streamlit as st
import os

# Load the pre-trained model with error handling
model_path = os.path.join("House-Prediction", "rf_model.joblib")
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Please check the path.")
    model = None

def main():
    st.title("House Price Prediction")

    # Sidebar descriptions
    st.sidebar.title("Input Field Descriptions")
    # Add descriptions...

    # Input variables on the main page
    bedrooms = st.text_input('Bedrooms', '3')  # Example default value
    # Add other input fields...

    # Validation function...
    
    if st.button('Predict'):
        # Validate inputs after button click...
        
        if None not in [bedrooms, bathrooms, sqft_living, sqft_lot, floors, view, condition, 
                        grade, sqft_above, sqft_basement, yr_built, zipcode, 
                        lat, long, sqft_living15, sqft_lot15]:
            
            # Prediction code
            make_prediction = model.predict([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, view, condition, 
                                              grade, sqft_above, sqft_basement, yr_built, zipcode, 
                                              lat, long, sqft_living15, sqft_lot15]])
            
            result = make_prediction
            st.success(f'The price of the house is ${result[0]:,.0f}')
        else:
            st.error("Please correct the errors above before submitting.")

if __name__ == '__main__':
    main()
