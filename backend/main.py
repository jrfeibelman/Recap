from typing import Union
from fastapi import FastAPI, APIRouter
import uvicorn
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import cohere
import pdb
# the following line needs your Twilio Account SID and Auth Token
client = Client("AC6bcd4e8259a0c93b2b71e6a0824d099f", "97987b4f8e1a7f836db063e7bd649197")

co = cohere.Client('7mbMs5jteG3Hayr664s5uPZfgyBQgugFw152cQNm')



app = FastAPI()
api_router = APIRouter()
app.include_router(api_router)



@app.get("/")
async def root():
    return {"msg": "Hello world!"}



slack_response = {'ok': True, 'oldest': '1693070589.295512', 
             'messages': [{'client_msg_id': 'f04af9c9-2b36-4b8f-afa4-7194d5f2a562', 'type': 'message', 
                           'text': ';(', 'user': 'U05PPC8K96E', 'ts': '1693081194.407869', 
                           'blocks': [{'type': 'rich_text', 'block_id': 'l/A', 
                                    'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': ';('}]}]}], 
                           'team': 'T05PLEQHFN1'},
                          {'bot_id': 'B05PRRL7Z1S', 'type': 'message', 'text': 'Hello from your app! :tada:', 'user': 'U05QD3UHG72', 'ts': '1693075602.953839', 'app_id': 'A05PGNVN26A', 
                           'blocks': [{'type': 'rich_text', 'block_id': 'Kk1k', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Hello from your app! '}, {'type': 'emoji', 'name': 'tada', 'unicode': '1f389'}]}]}], 'team': 'T05PLEQHFN1', 'bot_profile': {'id': 'B05PRRL7Z1S', 'deleted': False, 'name': 'Recap', 'updated': 1693073647, 'app_id': 'A05PGNVN26A', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'team_id': 'T05PLEQHFN1'}}, {'client_msg_id': '773401f7-b56a-44f5-8463-eb5ec32a9ae2', 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'type': 'message', 'text': '** - I hope you are all excited for your first day of classes :party_parrot: We’ll see you *tomorrow* in Studio so here are some logistics that you might find helpful:\n\n1. *Early is on time, on time is late, and late is EXTREMELY late!* Anticipate a dramatic increase in elevator traffic if you live in the house (especially around the start of Studio classes that occupies about 90% of the campus) and make sure you are seated and ready to go tomorrow at 2:55 PM. To support Studio means to support complicated logistics, so we cannot and will not wait for you to arrive. Show that you care for us and your team by being punctual. :heart:\n2. Teams 1-42 should be in the Bloomberg Auditorium and Teams 43-84 should go to the Verizon Executive Education Event Space. Be in your seat by 2:55! :heart:\n3. For tomorrow’s activity, it is in your team’s best interest for every member to bring to this session any recyclables they might have. Make it a challenge today to collect what you use, so you might be able to re-use it tomorrow :wink: Don’t bring new materials, glass, metal, aluminum, etc, since you won’t be able to use that!\n4. For tomorrow’s session, you can expect that you will be occupied from 2:55 until around 6:00 PM. After our event ends, the All Campus BBQ will start at 6:30. We hope to see you there showing your CT spirit :twisty_t:\n5. For Thursday, you will have a rare, but important “double feature” that will occupy your time from 2:55 until 4:10 and from 4:20 until 5:35. Consult Canvas to understand where you need to be with your team when. For the rest of the semester, you can expect to use “team time” to work with your team wherever you are comfortable and should plan to come to your in-person recitations where you will work on course deliverables under the incredible advisement of your Studio Coaches (@Jori Bell, Studio Coach, @Danielle Boris, Studio Coach, and @Adam Yormark). Logistics of this are also in Canvas, so check it out!\nIf you have any questions at this point, please let us know! We look forward to kicking off your semester in the Studio :shuffle_parrot:', 'user': 'U05PPC8M9V0', 'ts': '1693075061.222449', 'blocks': [{'type': 'rich_text', 'block_id': 'GiL9', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'broadcast', 'range': 'channel', 'style': {'bold': True}}, {'type': 'text', 'text': ' - I hope you are all excited for your first day of classes '}, {'type': 'emoji', 'name': 'party_parrot'}, {'type': 'text', 'text': ' We’ll see you '}, {'type': 'text', 'text': 'tomorrow', 'style': {'bold': True}}, {'type': 'text', 'text': ' in Studio so here are some logistics that you might find helpful:\n\n'}]}, {'type': 'rich_text_list', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Early is on time, on time is late, and late is EXTREMELY late!', 'style': {'bold': True}}, {'type': 'text', 'text': ' Anticipate a dramatic increase in elevator traffic if you live in the house (especially around the start of Studio classes that occupies about 90% of the campus) and make sure you are seated and ready to go tomorrow at 2:55 PM. To support Studio means to support complicated logistics, so we cannot and will not wait for you to arrive. Show that you care for us and your team by being punctual. '}, {'type': 'emoji', 'name': 'heart', 'unicode': '2764-fe0f'}]}, {'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Teams 1-42 should be in the Bloomberg Auditorium and Teams 43-84 should go to the Verizon Executive Education Event Space. Be in your seat by 2:55! '}, {'type': 'emoji', 'name': 'heart', 'unicode': '2764-fe0f'}]}, {'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'For tomorrow’s activity, it is in your team’s best interest for every member to bring to this session any recyclables they might have. Make it a challenge today to collect what you use, so you might be able to re-use it tomorrow '}, {'type': 'emoji', 'name': 'wink', 'unicode': '1f609'}, {'type': 'text', 'text': ' Don’t bring new materials, glass, metal, aluminum, etc, since you won’t be able to use that!'}]}, {'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'For tomorrow’s session, you can expect that you will be occupied from 2:55 until around 6:00 PM. After our event ends, the All Campus BBQ will start at 6:30. We hope to see you there showing your CT spirit '}, {'type': 'emoji', 'name': 'twisty_t'}]}, {'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'For Thursday, you will have a rare, but important “double feature” that will occupy your time from 2:55 until 4:10 and from 4:20 until 5:35. Consult Canvas to understand where you need to be with your team when. For the rest of the semester, you can expect to use “team time” to work with your team wherever you are comfortable and should plan to come to your in-person recitations where you will work on course deliverables under the incredible advisement of your Studio Coaches (@Jori Bell, Studio Coach, @Danielle Boris, Studio Coach, and @Adam Yormark). Logistics of this are also in Canvas, so check it out!'}]}], 'style': 'ordered', 'indent': 0, 'border': 0}, {'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '\nIf you have any questions at this point, please let us know! We look forward to kicking off your semester in the Studio '}, {'type': 'emoji', 'name': 'shuffle_parrot'}]}]}], 'team': 'T05PLEQHFN1'}, {'type': 'message', 'subtype': 'channel_join', 'ts': '1693073872.736069', 'user': 'U05QD3UHG72', 'text': '<@U05QD3UHG72> has joined the channel', 'inviter': 'U05PPC5CJ82'}, {'client_msg_id': 'aeed2644-6818-4036-a6b9-ea932cf90403', 'type': 'message', 'text': '', 'user': 'U05QD3JQ472', 'ts': '1693073433.477249', 'blocks': [{'type': 'rich_text', 'block_id': '+nDh4', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'link', 'url': 'https://docs.cohere.com/docs/model-prompting#when-to-stop'}]}]}], 'team': 'T05PLEQHFN1', 'attachments': [{'from_url': 'https://docs.cohere.com/docs/model-prompting#when-to-stop', 'service_icon': 'https://files.readme.io/8028ad6-small-cohere-icon.png', 'id': 1, 'original_url': 'https://docs.cohere.com/docs/model-prompting#when-to-stop', 'fallback': 'Cohere AI: Prompt Engineering', 'text': "In this chapter, you'll learn how to use the Cohere Playground and the basics of constructing good prompts for generative models.", 'title': 'Prompt Engineering', 'title_link': 'https://docs.cohere.com/docs/model-prompting#when-to-stop', 'service_name': 'Cohere AI'}]}, {'type': 'message', 'subtype': 'channel_join', 'ts': '1693073404.081249', 'user': 'U05QD3JQ472', 'text': '<@U05QD3JQ472> has joined the channel'}, {'client_msg_id': '84F86B57-3280-4F58-AB9F-826C9112C501', 'type': 'message', 'text': 'Can you take me to the park tomorrow to play frisbee? Lets get some ramen after. I love suckling down those sweet sweet noodles after a long day of playing frisbee', 'user': 'U05PPC8K96E', 'ts': '1693073387.460779', 'blocks': [{'type': 'rich_text', 'block_id': 'pWfIE', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Can you take me to the park tomorrow to play frisbee? Lets get some ramen after'}, {'type': 'text', 'text': '.'}, {'type': 'text', 'text': ' I love suckling down those sweet sweet noodles after a long day of playing frisbee'}]}]}], 'team': 'T05PLEQHFN1'}, {'type': 'message', 'subtype': 'channel_join', 'ts': '1693073285.892649', 'user': 'U05PPC8K96E', 'text': '<@U05PPC8K96E> has joined the channel'}, {'type': 'message', 'subtype': 'channel_join', 'ts': '1693073248.651399', 'user': 'U05PPC8M9V0', 'text': '<@U05PPC8M9V0> has joined the channel'}, {'client_msg_id': '9fb0af47-f693-4794-8127-407349608c97', 'type': 'message', 'text': 'September 2nd sound good?', 'user': 'U05PPC5CJ82', 'ts': '1693073204.388979', 'blocks': [{'type': 'rich_text', 'block_id': 'HeVQ4', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'September 2nd sound good?'}]}]}], 'team': 'T05PLEQHFN1'}, {'client_msg_id': '12340476-e319-4b4a-90b7-3dc5fad0a463', 'type': 'message', 'text': 'Something for next weekend', 'user': 'U05PPC5CJ82', 'ts': '1693073179.555599', 'blocks': [{'type': 'rich_text', 'block_id': 'dCTF', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Something for next weekend'}]}]}], 'team': 'T05PLEQHFN1'}, {'client_msg_id': '550097ba-a89e-4d68-8856-09f4eff3f3ea', 'type': 'message', 'text': 'anyone down?', 'user': 'U05PPC5CJ82', 'ts': '1693073155.708619', 'blocks': [{'type': 'rich_text', 'block_id': '1bQ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'anyone down?'}]}]}], 'team': 'T05PLEQHFN1'}, {'client_msg_id': 'ed63bde4-8c35-4eb9-8244-a63f9901a489', 'type': 'message', 'text': "I'm looking to start a Cornell Tech based hackathon", 'user': 'U05PPC5CJ82', 'ts': '1693073153.538589', 'blocks': [{'type': 'rich_text', 'block_id': 'ZsR', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "I'm looking to start a Cornell Tech based hackathon"}]}]}], 'team': 'T05PLEQHFN1'}, {'client_msg_id': '3b1a77f4-3e6e-4bf0-917a-65270f2ad0f5', 'type': 'message', 'text': 'my name is Maanas', 'user': 'U05PPC5CJ82', 'ts': '1693073142.923229', 'blocks': [{'type': 'rich_text', 'block_id': 'L8X', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'my name is Maanas'}]}]}], 'team': 'T05PLEQHFN1'}, {'client_msg_id': '93b4822d-3d1d-49eb-8163-5775941ef125', 'type': 'message', 'text': "yo what's up", 'user': 'U05PPC5CJ82', 'ts': '1693073139.680799', 'blocks': [{'type': 'rich_text', 'block_id': 'R4fG', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "yo what's up"}]}]}], 'team': 'T05PLEQHFN1'}, {'type': 'message', 'subtype': 'channel_join', 'ts': '1693072973.508299', 'user': 'U05PPC5CJ82', 'text': '<@U05PPC5CJ82> has joined the channel'}], 'has_more': False, 'pin_count': 0, 'channel_actions_ts': None, 'channel_actions_count': 0}


pdb.set_trace()

clean_messages = []
for m in slack_response['messages']:
    print('here')
    if ('client_msg_id' in  m):
        print('here1')
        clean_message = f"From {m['client_msg_id']}: {m['text']}"
        clean_messages.append(clean_message)

    script = "\n".join(reversed(clean_messages))


pdb.set_trace()


@app.get("/items/")
def update_item():
    # change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number

    response = co.summarize(
    text=text,
    model='command',
    length='medium',
    extractiveness='medium'
    )

    summary = response.summary
    
    client.messages.create(to="+14126089699",
                           from_="+18777993630",
                       body="Hello from Python!")
    return


