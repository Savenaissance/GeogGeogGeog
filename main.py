import streamlit as st
import openai
import json
import pandas as pd


user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)

prompt = """
Act as AI Geographer. You will recieve text in English and you will find and count  proper places appeared in the text, then you will list these those places informations in table form:
 Column
1. Place : Place name you found
2. Latitude : Latitude of that place (2 Decimals)
3. Longitude : Longitude of that place (2 Decimals)
4. Location :  Location of that place now as Country, Province(if know)
5. Continent : Continent where that place located
6. Climate: Climate Zone of that place
( Climate zone classification: Tropical,Dry,Temperate,Continential,Polar)
7. No. Mentioned : Number of those places appeared in the text
each place you found for each row
If no information found in text , the table will give "No (Column_name) found" in that column. 
In case there are place with the same name :  choose to show only one of the most possible place  according to text.
        """    

st.header("PA4-Basic Prog NLP", divider="red")
st.title(':green[*What!* **Where!!** ***How???***]')
st.markdown(':violet[This AI will give you Geo info of places from your text.] :smiley:')

user_input = st.text_area(":rainbow[Enter your text here ]", " I can show you the world ")

if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_so_far
    )

    st.markdown('***AI response:***')
    GeoInfo_dictionary = response.message.content

    gd = json.loads(GeoInfo_dictionary)

    print (gd)
    GeoInfo_df = pd.DataFrame.from_dict(gd)
    print(GeoInfo_df)
    st.table(GeoInfo_df)
    st.success('Successfully Done!', icon="✅")