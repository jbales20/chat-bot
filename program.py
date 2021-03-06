import random

response1 = ["Alexandria: That's awesome, what book are you reading?", "Alexandria: That's cool. what is your book that you're currently reading, or last read about?", "Alexandria: What do you enjoy most about the book you're currently reading, or last read?"]
response2 = ["Alexandria: You should, reading is fun.", "Alexandria: That's too bad, you should check out my library. Wait, nevermind, there was a fire", "Alexandria: I enjoy reading myself."]


print("Hey there, I'm a Alexandria. I am kind of a book nerd. So I'll just ask book related questions.") 
print("For the first question it's yes or no, the rest answer however you'd like. Type 'done' when you're ready to leave.")

print("")

# I used randint instead of choice so I can detect the index to ask more than one question depending on the previous response.

def get_bot_response(user_response):
    which = random.randint(0, (len(response1)-1))
    which2 = random.randint(0, (len(response2)-1))

# Uses a randomize predetermined response from user for either Yes or No.
    if user_response == "yes" or user_response == "Yes":
        reading = 1
        print(response1[which])
    elif user_response == "no" or user_response == "No":
        reading = 0
        print(response2[which2])
        return("")

# The user's escape from the loop.
    elif user_response == "done":
        reading = 0
        return("Alexandria: Okay, nice talking to you.")
 # Detects if the user inputs anything besides yes, no or done       
    else:
        reading = 0
        return ("Alexandria: My pardon?")

# If the user answered Yes, the three possible questions asked after the user saying Yes, has two possibly responses depending on the question. 
    if which == 0 and reading == 1:
        book = input()
        print("Alexandria: I'll have to read " + book)
        return("")
    elif reading == 1:
        none = input()
        print("Alexandria: Sounds interesting. I'll have to check it out.")
        return("")

read = ""

# The while loop that causes it to cycle over again.
while read != "done":
    print("Alexandria: Do you read?")
    read = input()
    print(get_bot_response(read))
    print("")