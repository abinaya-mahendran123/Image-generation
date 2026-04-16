import requests
prompt="panda with flower."

url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
img=requests.get(url).content
with open("pt.png","wb") as f:
    f.write(img)
    