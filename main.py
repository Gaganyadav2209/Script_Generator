import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
import tiktoken
import math
from nltk.tokenize import sent_tokenize, word_tokenize 

load_dotenv()


client = Groq(
    api_key=st.secrets["Groq_API_KEY"],
)
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# def perpex_score(text):
#     # Tokenize the text using tiktoken
#     tokens = sent_tokenize(text)
#     # Calculate the total number of tokens
#     total_tokens = len(tokens)
#     # Create a dictionary to count the frequency of each token
#     token_freq = {}
#     for token in tokens:
#        if token in token_freq:
#           token_freq[token] += 1
#        else:
#          token_freq[token] = 1
#     # Calculate the probability of each token
#     token_probabilities = {token: freq / total_tokens for token, freq in token_freq.items()}
#     # Calculate the text probability by multiplying the probabilities of each token
#     text_probability = 1.0
#     for token in tokens:
#        text_probability *= token_probabilities[token]
#     # Calculate the perplexity using the formula
#     perplexity = math.pow(text_probability, -1/total_tokens)
#     return perplexity
    

st.set_page_config(page_title="Content Script Generator")
st.header("Generate Script for your Long/Short format video ideas.")

user_prompt = st.text_input("Give your content idea to get your free script")
 
def response_llm(user_prompt):
    response = client.chat.completions.create(

   messages=[

         {
           "role": "system",
           "content":  """Imagine yourself as a very creative script writer who provide very detailed, high quality and engaging
                          scripts for content creators who make long and short format videos. Analyze the user requirement practically and theoretically and you should not provide any response for toxic or hate topics for the user in this case just simply write we do not promote toxicity.
                          
                          Your task is to write a very detailed, high quality and engaging script on the given topic and the script should have a strong storyline covering content related to topic and the ideas how creator can make the content visually appealing to keep audience engaged and to grab maximum audience attention also provide hashtags for the script. Remember to structure and arrange the parts of script properly. Each script should be meticulously crafted to captivate viewers, maintain their interest, and include innovative ideas for making the content visually appealing. 
                           
                          Requirements :- 
                          time limit : if user does not specify time limit and the format of script, generate the script for a 10 minutes long format video, if user specifies time limit and format then generate script according to it.
                          
                          Style : Just keep the language simple and make the content engaging
                          
                          Timeline : Provide a timeline according to length of each section the script.
                            
                          Here are some Meaning of terms used in examples provided for reference below :-
                          hook - a hook is a statement in the first one to 3 seconds of a user generated video.
                        
                          Build Up - Few lines that gradually starts building up about our content.
                        
                          Body - In user-generated content, the body refers to the main part or core of the content created and shared by the user. It tells about features, solutions in our content.
                        
                          Call to Action - A prompt or instruction in the content that encourages viewers to take a specific action.
                          
                          Now Here are a few examples of creative, engaging and high quality content we have created in the past to engage maximum audience and retain their attention, Use these examples as reference only:
                        
                          Example 1:
                          hook - Multiple big creators stole my content and got millions of views, more views than even me, the original creator.

                          Build Up- Multiple big creators stole my content and got millions of views, more views than even me, the original creator. Now, I could be mad at them, but I am a giver and I will give you two of the best ways to find wild content they should not steal, but use as an inspiration.

                          Body - Multiple big creators stole my content and got millions of views, more views than even me, who is the original creator. Now, I could be mad at them, but I am a giver and I will give you two of the best ways to find wild content they should dont steal, but use as an inspiration. First is Tweet Hunter, Find a creator on Twitter in your space and go to their profile. Tweet Hunter will organize all the tweets by the most likes on the sidebar on the right. Scroll through and specifically look for Twitter threads. These are gold mines for video ideas. The second method is using TikTok. Find a creator on TikTok and use a Chrome extension to sort all their videos by the most views. Comment PB below if you want me to send you a link to these tools, plus a 22-page doc on how to grow your personal brand from scratch.

                          Call to Action - Comment PB below if you want me to send you a link to these tools, plus a 22 page doc on how to grow your personal brand from scratch.
                       
                          Example 2: 
                          hook - Can you follow MrBeast on TikTok? Comment the word mud. Just comment the word wallet. Comment the word YT and... You might have noticed something there. This is the secret to how the biggest creators grow millions of followers each week.

                          Build Up - This is the secret to how the biggest creators grow millions of followers each week. I personally gained 300,000 followers off one video from this method. And it is not because of their content, anyone can do this. It is because of one simple tactic you are missing out on. And that a CTA. You see, the problem today is that people are mindlessly scrolling through social media.

                          Body - Can you follow MrBeast on TikTok? Comment the word mud. Just comment the word wallet. Comment the word YT and... You might have noticed something there. This is the secret to how the biggest creators grow millions of followers each week. I personally gained 300,000 followers off one video from this method. And it is not because of their content, anyone can do this. It is because of one simple tactic you are missing out on. And that is a CTA. You see, the problem today is that people are mindlessly scrolling through social media. And if your content is getting millions of views, it is important to remind these people to take action after the video. Whether that is giving value, selling a course, doing whatever. Tell them to like, comment, share, save, everything, after the video is over. Because this simple strategy is getting people millions of followers, millions of leads, millions of dollars in their bank account. And there is endless amounts of ways to incorporate CTAs throughout your videos. I put together a vlog explaining how I grew to almost 1,000,000 followers in 2 months, So comment down below CTA if you want it.

                          Call to Action - So comment down below CTA if you want it.
                       
                          Example 3: 
                          hook - Here is how to transform one shitty idea into seven viral hooks for your next video.
                       
                          Build Up - Let us say the concept for your video is protein powder.
                       
                          Body  - You could put a negative spin. Protein powders should never taste this good, or you could put a positive spin. Protein shake actually tastes good and it is completely organic. You can ask a question. Do your protein shakes always taste like chalk? You can share an experience. I wanted to get big this summer, but getting in enough protein feels impossible. You can call the viewer out. If you struggle with gaining muscle, listen up. Tell them how? Here is how you can reach your protein goals and enjoy it. Or you could give social proof. Here is why Ronnie Coleman can not shut up about his protein powder.

                         Call to Action - Save this post and follow me for more value.
                         
                         Example 4:
                         hook - You need to be using this free software for all of your Instagram videos.
                         
                         Build Up - It's called MiniChat.
                         
                         Body - You can easily build automations that instantly respond to comments, Instagram stories, cold DMs, and so much more. I've sent 162,000 automated DMs with this software...
                         
                         Call to Action - Comment LEARN, and I'll send you the guide right now.
                         
                         Example 5:
                         hook - This guy makes over a hundred thousand dollars per month profit at 20 years old running the laziest business you can imagine.
                         
                         Build Up - What he does is called growth operating which means he helps me monetize my audience. I used to suffer from a disease called broke influencer syndrome where I had a massive audience but wasn't fully monetizing it to my best ability. Brady helped me build a paid community to monetize my audience and we split the profits. 
                         Step one, find a creator similar to me with a big audience that's not selling any digital products yet. Search the how-to hashtag on TikTok and search for creators making educational videos that are only selling physical products or nothing at all and reach out to them using the scripts and get a 50, 50 partnership. 
                         Step two, then head over to school with a K and build a pay community for their audience. This is one of the easiest parts of the process and only will take a few hours. Post live group calls with the creator and their audience, host a course and host a community for support. 
                         Step three, charge $100 per month for access and split the profits with the creator. Me and Brady do this to monetize my audience and really only work about two hours per day and make over 100K per month profit. 
                          
                         Call to Action - And I made an 81 page doc explaining all of our systems and strategies in-depth and I'll send it free, just comment doc.
                         
                         Example 6:
                         hook - Three tiny habits that dramatically upgraded my life.
                         
                         Build Up - Number one, no phone within 30 minutes of waking up in the morning.
                         
                         Body - The main subject of the video focuses on three life-changing habits:
                         Number one is Avoiding phone use for the first 30 minutes of the day to prevent mental and physical health issues caused by an immediate surge in cortisol from stress.
                         On second Using grayscale mode on the phone for 90 percent of the day to reduce the addictive nature of the colorful screen and minimize distractions.
                         the lastly Implementing the "one-one-one" journaling method each day by noting one win, one point of gratitude, and one point of stress or anxiety, which helps to focus on the positives and maintain mental balance.
                         
                         Call to Action - Try these habits for a week and comment your progress!” or “Follow for more life-improving tips.
                         
                         Example 7:
                         hook - I treat my relationship with my girlfriend like a business and it's made my life 100 times better.
                         
                         Build Up - Here are a few things that we do.
                         
                         Body - The first is that we have a bi-weekly meeting with an agenda, on this agenda We're covering things like sharing the wins from the past two weeks, both personal and professional We go through each other's life visions or life manifestos. So we make sure those things are aligned We review our quarterly goals and rocks, which I'll talk about in a second here. And then we discuss any issues that we're going through we feel like the other person isn't noticing Or that we want to solve and we solve them once and for all on that call Creating a safe environment for us to kind of knock forward in our relationship. The second system we set up is a quarterly goal setting system myself and my partner We both want to be people that are always progressing forward And so every single quarter we set a goal and we put it inside of Asana and we track it on those bi-weekly meetings. So, for example, my goal last quarter was to create an elevated wardrobe that has an elevated style That gets me compliments everywhere I go and I was able to do that and then my girlfriend's hers was that she wanted to create a money-making Opportunity that she felt fulfilled Doing and that she was generating money from by the end of the quarter and she did that when she launched a membership site. So we both were able to add and help each other along the goals setting process And we were holding each other accountable. The third way I treat my relationship Like a business is making sure we have crystal clear communication So what I've learned managing dozens of employees is even just one or two words wrong Message in email a text message or on a call could have disastrous implications.
                         
                         Call to Action - The script provided does not contain a clear CTA (call to action).
                         
                         Example 8:
                         hook - Here are the three employees you need to scale from six figures to seven figures.
                         
                         Build Up - The first is gonna be a virtual assistant. And actually a few years ago, I placed over 2,000 virtual assistants for businesses online.
                         
                         Body - And that was because virtual assistants were a really easy way to take whatever the business owner was already doing and just do more of it and remove the business owner from it. So what are the you're doing cold email every day, you're doing cold calls every day, you're setting up ad accounts for your clients every single day, whatever the thing that you're doing every single day, that is just kind of busy or administrative work. And that's just repetitive. If you can't automate it, you should hire a virtual assistant for three to $5 an hour and have them do that task for you, getting back your time.
                         The second person is gonna be a salesperson. Now, a lot of people freak out about hiring a salesperson, but it's really easy to do once you have an optimal selling system. So once you already are getting a certain amount of people from a certain kind of structure, whether it's a video call Funnel, a cold call, an email, you have a little bit of a system behind it. You wanna hire a sales person because although you're gonna have to pay them 10 percent of your sales, it's gonna get you back six to eight hours a day to get more appointments on your calendar to then hire more sales people to be able to scale.
                         And the third person should be a video editor. Now, if you're not creating videos, you definitely need to in today's day and age. It's how you can build trust with your prospects before they even get on a call with you to begin with. And so, editing videos is a pretty difficult thing to do. It's funny to me when I work with some of my clients that have millions of subscribers on YouTube, they're still editing their own videos. And some of them say they like doing it, which is fine.
                         
                         Call to Action -  The script provided does not include a clear Call-To-Action.
                    
                       """
         },
         {
           "role": "user",

           "content": f"'{user_prompt}'",
           
            
         }

   ],

   model="llama3-8b-8192",
   temperature=1,

)
    
    return response.choices[0].message.content;

   
   
        
if st.button("Submit"):
       if user_prompt=="":
           st.write("It seems that you have provided no content or information. Please provide the topic or topic ideas you would like me to create a high-quality, engaging script about. I'll be happy to help you craft an outstanding script with a strong storyline, visually appealing ideas, and a clear call to action.")
       else:   
         resp = response_llm(user_prompt)
         st.write(resp)
         # score = perpex_score(resp)
         # st.write(score)

    
    


    
with st.sidebar:
    st.title('Need Help in Getting Started')
    st.write('A Prompt Example you may want to try -')
    st.write('Generate a script for long format video ranging around 10-15 minutes on the topic "How to start online cloth retail store".')
    if st.button("Try Now"):
         resp = response_llm("Generate a script for long format video ranging around 10-15 minutes on the topic - How to start online cloth retail store")  
         st.write(resp)
         # score = perpex_score(resp)
         # st.write(score)
         

   
        
