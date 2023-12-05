import requests, time
from dhooks import Webhook, Embed

webhook = Webhook("https://discord.com/api/webhooks/1181311899682484284/6Iby-ndBjwlniNkfZDVrJhW5xvO550RZGqPse1X0hb4B2pewHZIUXBBUIc6sHBIty3KW")


url = "https://api.bloxflip.com/chat/history"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0',
}

image1 = "https://upload.wikimedia.org/wikipedia/commons/3/39/Robloxi_valuuta_%22Robux%22_Ikoon.png"
while True:
    ra = requests.get(url, headers=headers).json()['rain']


    if ra['active'] == True:
        host = ra['host']
        prize = ra['prize']
        embed = Embed(color=0x0025ff, timestamp='now')
        embed.set_author(name=f'{host} hosted a rain!!', icon_url=image1)
        embed.add_field(name='Rain!', value=f'Active Rain ${prize}\n[join rain](https://bloxflip.com)')
        embed.set_timestamp()
        webhook.send("@bloxflip")
        #webhook.send(embed=em)




        time.sleep(120)



    else:
        prize = ra['prize']
        embed = Embed(description="[join rain](https://bloxflip.com)",
                      color=0x0025ff,
                      timestamp='now')
        embed.set_author(name=f' hosted a rain!!', icon_url=image1)
        embed.add_field(name='Rain!', value=f'Active Rain ${prize}')
        webhook.send(f"<@&1181379945390407791>{prize}")
        webhook.send(embed=embed)


        time.sleep(3)


