import random 

def get_response(message: str) -> str:
    p_message = message.lower()

    

    if p_message == '/hello':
        zaza = random.randint(1,6)
        if zaza == 1:
            return 'hello there!'
        if zaza == 2:
            return "👋"
        if zaza == 3:
            return "Howdy!"
        if zaza == 4:
            return "Hey!"
        if zaza == 5:
            return "hi"
        if zaza == 6:
            return "hello"
        # return "👋"
        
    if p_message == '/vote':
        poop = random.randint(1,2)
        if poop == 1:
            return ':white_check_mark:'
        if poop == 2:
            return ":x: "

    if p_message == '/eatMyBooty':
        eat = random.randint(1,8)
        if eat == 1:
            return 'bet what time?'
        if eat == 2:
            return "lemme go for @SmortBlerb"
        if eat == 3:
            return "I think Esrom's a better option"
        if eat == 4:
            return "I'm hungryyyyyyyyy. Me want foood"
        if eat == 5:
            return "hmmmm.... I think I'll pass, but I would want to go to @TacticalRalsei"
        if eat == 6:
            return "ur zesty."
        if eat == 7:
            return "@bread is better than a trash can like u."
        if eat == 8:
            return "."
        # if eat == 9:

        #     with open("filename","rb") as f:
        #         image=f.read()
        #     return image
        #     return ""

    if p_message == '/compliment':
        # yaso == random.randint(1,3)
        # if yaso == 1:
        #     return 'You look really good!'
        # if yaso == 2:
        #     return 'I think your personality is really nice.'
        # if yaso == 3:
            return "I can't see you, but I'm sure you look nice."
    if p_message == '/dice':
        return str(random.randint(1,6))
    
    if p_message == '/news':
        return "|BREAKING NEWS|\n This is pasta news and we're here to report that @f3ttucineK1d is working on creating fetaMarshmallow, a new bot that will assisst with extra duties needed."

    if p_message == '/insult':
        lalo = random.randint(1,7)
        if lalo == 1:
            return 'Tbh ur dumber than I thought'
        if lalo == 2:
            return "you wouldn't have to worry about the zombie apocolypse. They only eat people with brains."
        if lalo == 3:
            return "When you talk to me, I wish I could meet you again for the first time…and walk past."
        if lalo == 4:
            return "You were so happy for the negativity of your Covid test, I didn’t want to spoil the happiness by telling you it was IQ test."
        if lalo == 5:
            return "You are the reason why there are instructions on shampoo bottles."
        if lalo == 6:
            return "Everyone is allowed to act stupid once, but you… you are abusing that privilege."
        if lalo == 7:
            return "i can insult you later when im less busy with ur mom."
    if p_message == '/help':
        return "Here are the commands:\n/hello will give you a hello\n/dice will give a simulated dice roll\n/insult will roast you so bad you'll cry back to ur mama\n/news will give you some new news updates related with bots in Zobby Jobby\nReplace any of the slashes with dots and type the following letters of the command for a direct message."

    