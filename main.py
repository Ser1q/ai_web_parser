import streamlit as st
from scraper import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama
import re

st.title('AI Web Scraper')
url = st.text_input('Enter a Website URL: ')

if st.button('Scrape Site'):
    if url == '':
        st.write('Please enter the website url!')
    else:   
        st.write('Scraping Website...')
        
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        
        st.session_state.dom_content = cleaned_content
        
        with st.expander('View DOM content'):
            st.text_area('DOM content', cleaned_content, height=300)


if 'dom_content' in st.session_state:
    parse_description = st.text_area('Tell me what you desire')
    
    if st.button('Parse Content'):
        if parse_description:
            st.write('Parsing...')
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            
            
            # Remove <think>...</think> including the content
            cleaned_text = re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL)
            print(cleaned_text.strip())
            
            st.write(cleaned_text)
            