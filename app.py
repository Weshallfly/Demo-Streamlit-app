import streamlit as st
import pickle

# Load the machine learning model from pickle file
# with open('model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

def predict_salary(gender, age, sector ):
    if gender == 'Male':
        b_gender = 1
    else:
        b_gender = 0
    if sector == 'Private':
        b_sector = 1
    else:
        b_sector = 0
    return b_gender*10 + age + b_sector*10 

def main():
    st.sidebar.title("Multi-Purpose Application")
    tool = st.sidebar.radio("Select any one tool",("Salary Predictor", "Calculator"))
    
    if tool == "Salary Predictor":
        st.title("Salary Prediction App")
        st.write("Enter details")

        gender = st.selectbox("Gender", ('Male', 'Female'))
        sector = st.radio("Sector", ('Private', 'Public'))
        age = st.number_input("Age", min_value=18, max_value=100, value=30)

        if st.button("Predict Salary"):
            predicted_salary = predict_salary(gender, age, sector)
            st.write(f"Predicted Salary: {predicted_salary:.0f} Rupees per hour")
            if predicted_salary < 20:
                st.write("Poor guy")
            else:
                st.write("Rich guy")
            
            
    if tool == "Calculator":
        st.title("Simple Calculator")
    
        num1 = st.number_input("Enter the first number:")
        num2 = st.number_input("Enter the second number:",value = 5)

        operation = st.radio("Select operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Division by zero!!! You fool !!!")
                return

        st.write(f"Answer: {result}")
        
if __name__ == "__main__":
    main()
