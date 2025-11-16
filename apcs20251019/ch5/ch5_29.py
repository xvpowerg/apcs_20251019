def testScore(s):
    if s < 0 or s > 100:
        raise Exception
    else:
        print(f"{s}正確的成績!")

testScore(10)
testScore(-25)
