import openai
import time

openai.api_key = "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"

textToSummarize = """@channel - I hope you are all excited for your first day of classes :party_parrot: We'll see you tomorrow in Studio so here are some logistics that you might find helpful:
Early is on time, on time is late, and late is EXTREMELY late! Anticipate a dramatic increase in elevator traffic if you live in the house (especially around the start of Studio classes that occupies about 90% of the campus) and make sure you are seated and ready to go tomorrow at 2:55 PM. To support Studio means to support complicated logistics, so we cannot and will not wait for you to arrive. Show that you care for us and your team by being punctual. :heart:
Teams 1-42 should be in the Bloomberg Auditorium and Teams 43-84 should go to the Verizon Executive Education Event Space. Be in your seat by 2:55! :heart:
For tomorrow's activity, it is in your team's best interest for every member to bring to this session any recyclables they might have. Make it a challenge today to collect what you use, so you might be able to re-use it tomorrow :wink: Don't bring new materials, glass, metal, aluminum, etc, since you won't be able to use that!
For tomorrow's session, you can expect that you will be occupied from 2:55 until around 6:00 PM. After our event ends, the All Campus BBQ will start at 6:30. We hope to see you there showing your CT spirit :twisty_t:
For Thursday, you will have a rare, but important "double feature" that will occupy your time from 2:55 until 4:10 and from 4:20 until 5:35. Consult Canvas to understand where you need to be with your team when. For the rest of the semester, you can expect to use "team time" to work with your team wherever you are comfortable and should plan to come to your in-person recitations where you will work on course deliverables under the incredible advisement of your Studio Coaches (
@Jori Bell, Studio Coach
, 
@Danielle Boris, Studio Coach
, and 
@Adam Yormark
). Logistics of this are also in Canvas, so check it out!
If you have any questions at this point, please let us know! We look forward to kicking off your semester in the Studio"""

#call Jason's function to retrieve messages over last 3 hours
messages = []


textToSummarize = "Here are the messages from the conversation that you need to summarize: {}.".format(", ".join(messages))


while True:
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that accurately identifies important points in group chat conversations, and provides a brief yet descriptive summary of the highlights of the conversation. Important points include times/dates, events, deadlines, due dates, questions directed to a person named Andre, reminders, and action items. Once you have created the summary, create a nicely formatted list of bullet points which describe action items for the user. Make sure to priority rank the action items based on deadline."},
        {"role": "user", "content": textToSummarize}
        ],
    temperature=0
    )
    
    time.sleep(10800)
    
    
#print(completion.choices[0].message)