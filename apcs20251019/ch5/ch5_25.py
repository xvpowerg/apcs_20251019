scores = {"Ch":100,"En":80,"Ma":95}
print(scores)
scores["Cp"] = 77#Key在更新Key不在新增
print(scores)
s1 = scores.pop("En")
print(s1)
print(scores)
s2 = scores.pop("Td",-1)#可給預設值
print(s2)
