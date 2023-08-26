from slack import testing
import openai

openai.api_key = "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"


completionChat = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.8,
    max_tokens = 255,
    messages = [
        {"role": "user", "content": "summarize the following messages from slack. List out any important events, dates, reminders, and filter out any meaningless content that wouldn't boost my productivity/know about: NYC Hackathon happening tn!! Yo what time?? It's at 8am come an hour between though. I love nature valley bars."}
    ]
)

completion = openai.Completion.create(
    model="text-davinci-003",
    prompt="Say this is a test",
    max_tokens=7,
    temperature=0
)

print(completionChat.choices[0].message)
# print(completion.choices[0].text)