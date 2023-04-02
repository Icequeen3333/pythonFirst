def waterDrank(drankInL: int):
    if drankInL > 3.7:
        return "Congrats, you drank your daily reccomended amount of water! How you know how much you drank is beyond me."

    return "You have drank " + str(drankInL/3.7*100) + "% of your daily amount of water, don't be dehydrated!"


print(waterDrank(2))

print(waterDrank(4))

