"""
Write a function can_vote(age, citizenship) that determines if a person is eligible to vote. A person is eligible to vote if they are:

At least 18 years old
A citizen of the country
The function should return a string "Eligible to vote" if the person meets both conditions, otherwise, it should return "Not eligible to vote".
"""


# def can_vote(age: int, citizenship: str):
#     if age >= 18 and (citizenship.lower()) == "indian":
#         print("Eligible to vote")
#     else:
#         print("Not eligible to vote")


# can_vote(17, "candaian")

def can_vote(age: int, citizenship: str):
    return "Eligible to vote" if age >= 18 and (citizenship.lower()) == "indian" else "Not eligible to vote"


print(can_vote(15, "indian"))
