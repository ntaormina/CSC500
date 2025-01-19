booksPurchased = int(input("How many books did you purchase?"))

if booksPurchased >= 8:
    print("You Earned 60 Points")
elif booksPurchased < 8 and booksPurchased >= 6:
    print("You earned 30 Points")
elif booksPurchased < 6 and booksPurchased >= 4:
    print("You earned 15 Points")
elif booksPurchased < 4 and booksPurchased >= 2:
    print("You earned 5 Points")
else:
    print("You earned 0 Points")