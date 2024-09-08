import streamlit as st
import nltk
from nltk import NaiveBayesClassifier
from nltk.classify import apply_features
from joblib import load

# Download NLTK resources if not already downloaded
nltk.download('names')

# Function to extract features from a name
def extract_gender_features(name):
    name = name.lower()
    features = {
        "suffix": name[-1:],
        "suffix2": name[-2:] if len(name) > 1 else name[0],
        "suffix3": name[-3:] if len(name) > 2 else name[0],
        "suffix4": name[-4:] if len(name) > 3 else name[0],
        "suffix5": name[-5:] if len(name) > 4 else name[0],
        "suffix6": name[-6:] if len(name) > 5 else name[0],
        "prefix": name[:1],
        "prefix2": name[:2] if len(name) > 1 else name[0],
        "prefix3": name[:3] if len(name) > 2 else name[0],
        "prefix4": name[:4] if len(name) > 3 else name[0],
        "prefix5": name[:5] if len(name) > 4 else name[0]
    }
    return features

# Load the trained Naive Bayes classifier
bayes = load('gender_prediction.joblib')

# Streamlit app
def main():
    # st.title('Gender Prediction App')
    # st.write('Enter a name to predict its gender.')

    # # Input for name
    # input_name = st.text_input('Name:')
    
    # if st.button('Predict'):
    #     if input_name.strip() != '':
    #         # Extract features for the input name
    #         features = extract_gender_features(input_name)
            
    #         # Predict using the trained classifier
    #         predicted_gender = bayes.classify(features)
            
    #         # Display prediction
    #         st.success(f'The predicted gender for "{input_name}" is: {predicted_gender}')
    #     else:
    #         st.warning('Please enter a name.')


    # Define the title of the app
    st.title('Salary Prediction App')
    
    # Create input fields for all features
    st.sidebar.header('Input Features')
    
    work_year = st.sidebar.slider('Work Year', 2020, 2023, 2023)
    job_title = st.sidebar.selectbox('Job Title', ['Data DevOps Engineer', 'Data Scientist', 'Software Engineer'])  # add more job titles as needed
    job_category = st.sidebar.selectbox('Job Category', ['Data Engineering', 'Data Science', 'Software Development'])  # add more categories as needed
    employee_residence = st.sidebar.selectbox('Employee Residence', ['Germany', 'United States', 'India'])  # add more countries as needed
    experience_level = st.sidebar.selectbox('Experience Level', ['Junior', 'Mid-level', 'Senior', 'Executive'])
    employment_type = st.sidebar.selectbox('Employment Type', ['Full-time', 'Part-time', 'Contract', 'Internship'])
    work_setting = st.sidebar.selectbox('Work Setting', ['Hybrid', 'On-site', 'Remote'])
    company_location = st.sidebar.selectbox('Company Location', ['Germany', 'United States', 'India'])  # add more countries as needed
    company_size = st.sidebar.selectbox('Company Size', ['S', 'M', 'L'])


if __name__ == '__main__':
    main()
