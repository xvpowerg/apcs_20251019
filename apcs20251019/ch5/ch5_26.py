scores = {"Ch":100,"En":80,"Ma":95}
del scores["Ch"]
print(scores)
delKey = "XX"
if delKey in scores:
    del scores[delKey]
print(scores)
