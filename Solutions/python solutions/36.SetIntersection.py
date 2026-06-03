def common_skills():
    set1 = {"Python", "Java", "C++"}
    set2 = {"Python", "HTML", "Java"}

    if len(set1) == 0 or len(set2) == 0:
        print("Invalid Input")
    else:
        common = set1 & set2
        print("Common Skills:", common)

common_skills()
