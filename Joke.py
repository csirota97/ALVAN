import random

jokes = ["Why did the chicken cross the road? To get to the other side!",
"Doctor: I'm sorry but you suffer from a terminal illness and have only 10 to live. Patient: What do you mean, 10? 10 what? Months? Weeks? Days?! Doctor: Nine.",

]

def joke():
    return random.choice(jokes)

print(joke())