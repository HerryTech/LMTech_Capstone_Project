import joblib
import streamlit as st

model = joblib.load("House-Prediction/rf_model.pkl")

def main():
    st.title("House Price Prediction")

    # Sidebar descriptions
    st.sidebar.title("Input Field Descriptions")
    st.sidebar.write("**Bedrooms:** Number of bedrooms in the house.")
    st.sidebar.write("**Bathrooms:** Number of bathrooms in the house.")
    st.sidebar.write("**Sqft Living:** Square footage of living area.")
    st.sidebar.write("**Sqft Lot:** Square footage of the lot.")
    st.sidebar.write("**Floors:** Number of floors in the house.")
    st.sidebar.write("**View:** View rating (0-4).")
    st.sidebar.write("**Condition:** Condition rating (1-5).")
    st.sidebar.write("**Grade:** Grade rating (1-13).")
    st.sidebar.write("**Sqft Above:** Square footage above ground.")
    st.sidebar.write("**Sqft Basement:** Square footage of the basement.")
    st.sidebar.write("**Year Built:** Year the house was built.")
    st.sidebar.write("**Zipcode:** Zip code of the property.")
    st.sidebar.write("**Lat:** Latitude of the property.")
    st.sidebar.write("**Long:** Longitude of the property.")
    st.sidebar.write("**Sqft Living15:** Square footage of the living area of the nearest 15 neighbors.")
    st.sidebar.write("**Sqft Lot15:** Square footage of the lot of the nearest 15 neighbors.")

    # Input variables on the main page
    bedrooms = st.text_input('Bedrooms')
    bathrooms = st.text_input('Bathrooms')
    sqft_living = st.text_input('Sqft Living')
    sqft_lot = st.text_input('Sqft Lot')
    floors = st.text_input('Floors')
    view = st.text_input('View')
    condition = st.text_input('Condition')
    grade = st.text_input('Grade')
    sqft_above = st.text_input('Sqft Above')
    sqft_basement = st.text_input('Sqft Basement')
    yr_built = st.text_input('Year Built')
    zipcode = st.text_input('Zipcode')
    lat = st.text_input('Lat')
    long = st.text_input('Long')
    sqft_living15 = st.text_input('Sqft Living15')
    sqft_lot15 = st.text_input('Sqft Lot15')

    def validate_numeric(input_value, field_name):
        try:
            return float(input_value)
        except ValueError:
            st.error(f"Please enter a numeric value for {field_name}")
            return None

    # Perform validation and prediction only when button is clicked
    if st.button('Predict'):
        # Validate inputs after button click
        bedrooms = validate_numeric(bedrooms, "Bedrooms")
        bathrooms = validate_numeric(bathrooms, "Bathrooms")
        sqft_living = validate_numeric(sqft_living, "Sqft Living")
        sqft_lot = validate_numeric(sqft_lot, "Sqft Lot")
        floors = validate_numeric(floors, "Floors")
        view = validate_numeric(view, "View")
        condition = validate_numeric(condition, "Condition")
        grade = validate_numeric(grade, "Grade")
        sqft_above = validate_numeric(sqft_above, "Sqft Above")
        sqft_basement = validate_numeric(sqft_basement, "Sqft Basement")
        yr_built = validate_numeric(yr_built, "Year Built")
        zipcode = validate_numeric(zipcode, "Zipcode")
        lat = validate_numeric(lat, "Latitude")
        long = validate_numeric(long, "Longitude")
        sqft_living15 = validate_numeric(sqft_living15, "Sqft Living15")
        sqft_lot15 = validate_numeric(sqft_lot15, "Sqft Lot15")
        
        # Proceed with prediction if all inputs are valid
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



