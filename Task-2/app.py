
import streamlit as st
import pandas as pd

# Load the financial data
df = pd.read_csv("Data\Report_Data_cleaned.csv")

# Function to process user query
def chatbot_response(query):
    query = query.lower()
    for _, row in df.iterrows():
        company = row['Company'].lower()
        year = str(row['Year'])

        if f"total revenue for {company} in {year}" in query:
            return f"The total revenue for {row['Company']} in {year} was {row['Total Revenue']}."
        elif f"net income did {company} make in {year}" in query:
            return f"{row['Company']} made a net income of {row['Net Income']} in {year}."
        elif f"total assets of {company} in {year}" in query:
            return f"The total assets of {row['Company']} in {year} were {row['Total Assets']}."
        elif f"{company}'s cash flow changed from" in query:
            for compare_year in df['Year'].unique():
                if f"from {compare_year} to {year}" in query:
                    try:
                        cash_flow_current = df[(df['Company'].str.lower() == company) & (df['Year'] == int(year))]['Cash Flow'].values[0]
                        cash_flow_previous = df[(df['Company'].str.lower() == company) & (df['Year'] == int(compare_year))]['Cash Flow'].values[0]
                        return f"{row['Company']}'s cash flow changed from {cash_flow_previous} in {compare_year} to {cash_flow_current} in {year}."
                    except:
                        return "I couldn't find cash flow data for the specified years."
    return "Sorry, I can only respond to predefined queries based on available data."

# Streamlit UI
st.title("📊 Financial Data Chatbot")
st.markdown("Ask predefined queries about company financials. Example queries:")
st.markdown("""
- What is the total revenue for Tesla in 2024?
- How much net income did Microsoft make in 2023?
- What are the total assets of Tesla in 2023?
- How has Microsoft's cash flow changed from 2023 to 2024?
""")

user_query = st.text_input("Enter your question:")
if user_query:
    response = chatbot_response(user_query)
    st.write("🤖", response)
