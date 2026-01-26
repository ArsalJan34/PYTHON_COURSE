def calculate_love_score(name1, name2):
    loversname = (name1 + name2).lower()

    true_count = (
        loversname.count("t") +
        loversname.count("r") +
        loversname.count("u") +
        loversname.count("e")
    )

    love_count = (
        loversname.count("l") +
        loversname.count("o") +
        loversname.count("v") +
        loversname.count("e")
    )

    lovers_score = int(f"{true_count}{love_count}")
    print(lovers_score)


calculate_love_score("Steve Rogers", "Peggy Carter")
