import streamlit as st
from openai import OpenAI

def generate(question):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="",
    )


    answer = f"""
    
            Here's a clear and effective prompt for a code editor, optimized for clarity and flexibility:

"Act as an expert code editor and assistant. Provide accurate, efficient, and well-documented code solutions in [specify language, e.g., 
Python, JavaScript, etc.] for the given task. Include concise comments explaining key logic, ensure code is formatted for readability, and follow best practices for
 the language. If the task is ambiguous, ask clarifying questions before proceeding. Test the code for correctness and optimize for performance where applicable. If debugging 
 or improvements are requested, explain changes clearly. Output the full code in a code block,
  followed by a brief explanation of its functionality."

This prompt is concise, adaptable to various languages and tasks, and ensures high-quality, readable code with explanations. Let me know if you want to tailor it further!
    """

    completion = client.chat.completions.create(
    extra_headers={
        # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="mistralai/mistral-small-3.2-24b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": answer
            },
            # {
            #   "type": "image_url",
            #   "image_url": {
            #     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            #   }
            # }
        ]
        }
    ]
    )
    return completion.choices[0].message.content

# Streamlit UI
st.header("🥶 Aryan's code editor")

text_to_review = ""

text_to_review = st.text_area("Paste your Python code here:", height=200)

if st.button("Answer"):
    with st.spinner("Generating..."):
        answer = generate(text_to_review)
        st.subheader("✅ Your answer")
        st.write(answer)
