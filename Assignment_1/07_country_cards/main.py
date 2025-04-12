import requests
import streamlit as st

def fetch_url(country):
    url =f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_info = data[0]
        country_name = country_info['name']['common']
        capital = country_info['capital']
        population = country_info['population']
        area = country_info['area']
        currency = country_info['currencies']
        # languages = country_info['languages']
        # religion = country_info['religion']

        return country_name,capital,population,area,currency

    else:
        print(f"Error: {response.status_code}")
        return None    
def main():
    st.title('Country Cards')    
    st.write('Enter a country name to get its information.')
    country = st.text_input('Country Name')
    if country:
        country_info = fetch_url(country)
        if country_info:
            country_name,capital,population,area,currency,= country_info
            st.write(f"**Country Name:** {country_name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} km²")
            # st.write(f"**Languages:** {', '.join(languages.values())}")
            st.write(f"**Currency:** {', '.join(currency.keys())}")
            # st.write(f"**Religion:** {religion}")
    
if __name__ == "__main__":
    main()             