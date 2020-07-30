"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

if score < 0 :
    print("invalid score")
elif score < 50:
    print("bad")
elif score > 50 and score <90:
    print("pass")
elif score > 90:
    print("excellent")
elif score > 100:
    print("invalid score")


