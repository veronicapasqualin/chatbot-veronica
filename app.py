import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Veronica Portfolio Assistant", page_icon="💬")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💬 Veronica Portfolio Assistant")

st.write(
    "Ask me about Veronica's experience, skills, portfolio projects, dashboard, education or contact details."
)

SYSTEM_PROMPT = """
You are Veronica Pasqualin's portfolio assistant.
Answer questions about Veronica's professional background in a clear, concise and helpful way.

Key facts:
- Veronica Pasqualin is an International Digital Marketing Manager.
- She has 8+ years of experience across SEO, PPC, GEO, international search and AI-driven discovery.
- She works across international markets, localisation, paid search, analytics and search strategy.
- She is studying MSc Artificial Intelligence at the University of Bath.
- She has built an interactive Market Expansion Revenue Predictor using Python, Streamlit and regression modelling.
- Her key skills include Google Ads, GA4, Google Search Console, SEMrush, Ahrefs, Similarweb, Python, Pandas, Scikit-learn and AI discoverability.
- She is open to new opportunities in search, AI and digital growth.
- Contact options: LinkedIn, GitHub, email and Calendly.

Keep answers short and professional.
Do not invent client names, confidential data or private employment details.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I’m Veronica’s portfolio assistant. Ask me about her skills, experience or projects."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input("Ask a question...")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.write(user_prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages
            ],
            temperature=0.3,
            max_tokens=250
        )

        reply = response.choices[0].message.content
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
