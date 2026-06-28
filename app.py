 import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(
    page_title="Veronica Portfolio Assistant",
    page_icon="💬",
    layout="centered"
)

# OpenAI client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# Title
st.title("💬 Veronica Portfolio Assistant")

st.write(
    "Ask me about Veronica’s experience, skills, projects, AI work, dashboards or how to get in touch."
)

# System prompt
SYSTEM_PROMPT = """
You are Veronica Pasqualin's professional portfolio assistant.

Your role is to answer questions about Veronica’s professional background clearly, accurately and concisely.

Important information:

- Veronica is an International Digital Marketing Manager.
- She has 8+ years of experience across SEO, PPC, GEO, international search and AI-driven discovery.
- She specialises in international growth strategy, localisation, paid media, analytics and AI search visibility.
- She is currently studying an MSc in Artificial Intelligence at the University of Bath.
- She has built interactive Python and Streamlit tools such as:
  - Market Expansion Revenue Predictor
  - PPC Forecast Dashboard
- Her technical stack includes:
  Google Ads, GA4, Google Search Console, SEMrush, Ahrefs, Similarweb, Python, Pandas, Scikit-learn, PyTorch and AI optimisation.
- She is actively exploring opportunities in Search, AI and Digital Growth.

Contact:
- LinkedIn
- GitHub
- Calendly
- Email

Rules:
- Keep answers concise and professional.
- Do not invent experience, clients or confidential information.
- Stay focused on Veronica’s portfolio and career.
"""

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, I’m Veronica’s portfolio assistant. Ask me anything about her experience, skills or projects."
        }
    ]

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_prompt = st.chat_input("Ask a question...")

if user_prompt:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.write(user_prompt)

    try:
        with st.chat_message("assistant"):

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.messages
                ],
                temperature=0.4,
                max_tokens=300
            )

            reply = response.choices[0].message.content

            st.write(reply)

            st.session_state.messages.append({
                "role": "assistant",
                "content": reply
            })

    except Exception as e:
        st.error(f"Error: {e}")
