from pymessenger import Bot
from wit import Wit
from pprint import pprint
at = "5BZGY2L3DILPVCP6UJFXRLIID4IROHPZ"
client = Wit(access_token = at)

def get_wit_response(message_text):
    wit_response = client.message(message_text)
    pprint(wit_response)
    entity = None
    try:
        entities = list(wit_response['entities'].keys())
        for key in entities:
            entity = key
    except:
        pass
    return (entity)


def generate_user_response(messaging_text):

    entity = get_wit_response(messaging_text)
    print(entity)
    if entity == "sendGreeting:sendGreeting":
        response = "Hello!!"
        print(response)
    elif entity =="offer:offer":
        response = "No offers avialable right now , ask us later . "
    elif entity == "price:price":
        response = "Available books: \n1. These violent delights -> 60 LE \n2. The midnight library -> 70 LE \n3. The final revival of opal&Nev -> 60 LE \n4. The song of achilles -> 80 LE \n5. Yellow wife -> 70 LE \n6. Six of crows -> 60 LE  \n7. Ordinary grace -> 80 LE \n8. The invisible life of addie larue -> 100 LE \n9. The hill we climb -> 100 LE \n10. Klara and the sun -> 100 LE "
    elif entity == "available:available":
        response = "Available books: \n1. These violent delights \n2. The midnight library  \n3. The final revival of opal&Nev \n4. The song of achilles \n5. Yellow wife  \n6. Six of crows  \n7. Ordinary grace \n8. The invisible life of addie larue \n9. The hill we climb  \n10. Klara and the sun "
    elif entity == "order:order":
        response = "Someone will assist you as soon as possible !"
    elif entity =="delivery:delivery":
        response = "Areas for delivery :\n1. Cairo ->30 LE \n2. Giza->30 LE \n3. Alexandria ->40LE \n  "
    else:
        response = "Someone will text you back in minutes ."
        print(response)
    return (response)

generate_user_response("hello")
