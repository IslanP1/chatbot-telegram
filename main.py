from telebot import TeleBot
import requests

BOT_TOKEN = ''

api_key = ''
endpoint = 'https://api.openai.com/v1/completions'

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'], func=lambda msg: True)
def mensagem(message):
    bot.reply_to(message, 'Use o comando /bot seguido da mensagem. Ex.: /bot oi, tudo bem?')
    
@bot.message_handler(commands=['bot'], func=lambda msg: True)
def mensagem(message):
    lista = []
    lista.append(message.text)
    pergunta = lista[0]
  
    prompt = str(pergunta[6:500])
    
    model = 'text-davinci-003'
    
    data = {
        "prompt": prompt,
        "model": model,
        "max_tokens": 200
    }
    
    response = requests.post(endpoint, json=data, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    })
    
    textoJson = response.json()
    
    bot.reply_to(message, textoJson['choices'][0]['text'])
    lista.clear()   

    
bot.infinity_polling()