import http.client

conn = http.client.HTTPSConnection("api.coincap.io")
payload = ''
headers = {}
conn.request("GET", "/v2/assets/bitcoin/history?interval=m1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))