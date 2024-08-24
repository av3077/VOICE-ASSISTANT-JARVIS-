
from groq import Groq

# Option 1: Set the API key directly
client = Groq(
    api_key="ENTER YOUR API KEY"
)



chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system","content": "you are a virtual assitant named jarvis skilled in general tasks like alexa",},
        {"role":"user","content":"what is coding"}
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
