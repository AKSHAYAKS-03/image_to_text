import requests
import streamlit as st

st.title("image captioning")
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(filename):
        data = filename
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
inp_img_link = st.text_input("Enter image link")
button_sub = st.button("Submit")

#output = query("https://images.unsplash.com/photo-1606115915090-be18fea23ec7?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8anBlZ3xlbnwwfHwwfHx8MA%3D%3D")

if button_sub:
    try:
        st.image(inp_img_link,caption="UPLOADED IMAGE")
    
        output = query(inp_img_link)
   # print(output[0]['generated_text'])
        st.write(output[0]['generated_text'])
    except:
        st.write("pass valid url")