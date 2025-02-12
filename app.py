import streamlit as st
from transformers import pipeline

# Load pre-trained model from Hugging Face
generator = pipeline('text-generation', model='gpt2')

# Streamlit UI to get user inputs
st.title('AI Personalized Email Generator')

recipient_name = st.text_input('Enter Recipient Name:')
event_details = st.text_area('Enter Event Details:')
special_instructions = st.text_area('Enter Special Instructions (Optional):')

# Generate email button
if st.button('Generate Email'):
    if recipient_name and event_details:
        # Construct the prompt for the model
        prompt = f"Dear {recipient_name},\n\nI hope this message finds you well. I wanted to inform you about the following event: {event_details}. "
        if special_instructions:
            prompt += f"Additionally, please note the following instructions: {special_instructions}. "
        prompt += "\n\nLooking forward to hearing from you soon.\nBest regards,\nYour Name"
        
        # Generate the personalized email
        email_content = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
        
        # Display the generated email
        st.subheader('Generated Email:')
        st.write(email_content)
    else:
        st.warning('Please fill in both Recipient Name and Event Details.')