results = {"Ken":0,"Amy":0,"Sean":0}
for i in range(5):
    vote = input("投票給")
    if vote not in  results:
        print("選票無效")
        continue
    results[vote] += 1

print(results)    
