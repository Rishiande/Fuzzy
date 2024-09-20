import streamlit as st

# College Information
college_info = {
    "general": (
        "Velagapudi Ramakrishna Siddhartha Engineering College (VRSEC) is a deemed university located in Vijayawada, "
        "Andhra Pradesh, India. It offers undergraduate education in engineering and postgraduate education in engineering, "
        "business administration, and computer applications. It was the first private institution to offer engineering education "
        "in the United Andhra Pradesh and was approved as a deemed university by the University Grants Commission (UGC) in 2024."
    ),
    "vision": (
        "To nurture excellence in various fields of engineering by imparting timeless core values to the learners and to mould "
        "the institution into a centre of academic excellence and advanced research."
    ),
    "mission": (
        "To impart high quality technical education in order to mould the learners into globally competitive technocrats who are "
        "professionally deft, intellectually adept and socially responsible."
    ),
    "quality_policy": (
        "V.R. Siddhartha Engineering College strives to impart knowledge, skills, and attitude through continuous improvement "
        "to meet the ever-changing needs of industry and for the sustainable development of society."
    ),
    "management": (
        "Siddhartha Academy of General and Technical Education was formed in 1975 by a team of 250 philanthropists with a vision "
        "to promote educational institutions of excellence. The Academy has established 15 institutions from KG to PG, including "
        "public schools, arts & science colleges, engineering colleges, and more, serving 23,500 students."
    ),
    "pioneering_ventures": [
        "First private engineering college in the composite state of AP (1977).",
        "First private medical college in the composite state of AP (taken over in 1981).",
        "First private PG center in the region (1987).",
        "First private pharmacy college in the composite state of AP (1994)."
    ]
}

# Mapping of keywords to categories
keywords = {
    "general": ["vrsec", "college", "about the college", "tell me about vrsec"],
    "vision": ["vision", "what is the vision", "college vision", "tell me about the vision"],
    "mission": ["mission", "what is the mission", "college mission", "tell me about the mission", "tell me about the mission of vrsec"],
    "quality_policy": ["quality", "quality policy", "what is the quality policy", "tell me about quality", "quality policy?"],
    "management": ["management", "college management", "who manages the college", "college governance"],
    "pioneering": ["pioneering", "first college", "achievements", "pioneering ventures"]
}

# Streamlit interface
st.title("VRSEC College Chatbot")
st.write("Ask anything about the college, and the chatbot will provide the information!")

# User Input
user_input = st.text_input("Enter your question:")
submit_button = st.button("Submit")

def get_response(question):
    question_str = question.lower().strip()

    # Check against all keywords
    for category, keys in keywords.items():
        if any(key in question_str for key in keys):
            # Return the information for the matched category
            return college_info.get(category, "I'm sorry, I don't have information on that topic.")

    return "I'm sorry, I don't have information on that topic."

# Generate response if user asks a question
if submit_button and user_input:
    response = get_response(user_input)
    st.text_area("Response:", value=response, height=150, max_chars=None, key=None)

# Deployment
st.write("This chatbot provides information based on the details of VRSEC.")