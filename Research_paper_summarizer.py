import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate, load_prompt

#Loading API and chatmodel
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(model="gpt-4o-mini",api_key=OPENAI_API_KEY)

#Streamlit 
st.title("Srijan's Research Paper Summarizer", divider="rainbow")
st.subheader(f"Powered by: GPT-4o-mini")
paper= st.selectbox("Select a research paper to summarize",["Attention is all you Need","BERT: Pre-training of Deep bidirectional Transformers","GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis","The AAA+ chaperone VCP disaggregates Tau fibrils and generates aggregate seeds"])
style= st.selectbox("Select explanation style",["Beginner-friendly","Non-technical","Technical","Application-based"])
length= st.selectbox("Select explanation length", ["Short (1 paragraph)","Medium (1-2 pargraphs)", "Long (detailed explanation)"])
#user_input= st.text_input("Enter your prompt")
#Template

template= load_prompt('template_summarizer.json')

#Fill the placeholders


if st.button("Summarize"):
    chain = template | chat_model
    result = chain.invoke({
    "paper_input":paper,
    "style_input":style,
    "length_input":length})
#The value of template.invoke is going directly to model.invoke with the help of chain. Otherwise we have to give that value to model.invoke via a variable called "prompt".   
    #prompt = template.invoke({
    #"paper_input":paper,
    #"style_input":style,
    #"length_input":length})
    #result = model.invoke(prompt)
    st.write(result.content)
    st.success("Research paper summarized!")

