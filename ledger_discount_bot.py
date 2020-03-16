import requests
import json

url = "https://api.flow.io/ledger/shopify/orders/f7521e416be9/promotion?expand=experience&envelope=request"
headers = {
  'authority': 'api.flow.io',
  'origin': 'https://shop.ledger.com',
  'sec-fetch-dest': 'empty',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
  'content-type': 'text/plain;charset=UTF-8',
  'accept': '*/*',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'cors',
  'referer': 'https://api.flow.io/',
  'accept-language': 'en-US,en;q=0.9'
}

to_write = open("codes.txt", "a+")


def test_code(code):
	global headers, url, to_write
	payload = "{\"method\":\"PUT\",\"headers\":{\"Accept\":\"application/json\",\"Content-Type\":\"application/json\",\"X-Flow-Request-Id\":\"chkeoHar5tEeRN7EF0dLISu\",\"Authorization\":\"Session F51ePh77LGlHuAMRMLw5DaJTmddFJBh9F8scSsrrR41WAOXwELzPyNJ6Atsd81cX\"},\"body\":{\"code\":\"" + code +"\"}}"
	response = requests.request("POST", url, headers=headers, data=payload)
	r_json = response.json()
	if "code" in r_json:
		if r_json["code"] == "generic_error":
			return
		
	discount_amount = r_json["items"][0]["discounts"][0]["label"]
	print(f"code: {code} discount amt: {discount_amount}")
	to_write.write(f"code: {code} discount amt: {discount_amount}")

f = open("words.txt", "r")
word_list = [x.strip() for x in f.readlines()]
f.close()

for word in word_list:
	test_code(word)
to_write.close()