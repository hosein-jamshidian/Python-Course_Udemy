import requests

params={
    'amount':10,
    'type':'boolean'
}

#point: I used below code instead of : requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')

# ------------------------------------------ Get Data From Open Trivia DB ---------------------------------------------
req=requests.get(url='https://opentdb.com/api.php', params= params)
total_question= req.json()['results']