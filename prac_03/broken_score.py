def score_get():
    try:
        score_student = int(input("Enter scores: "))
    except ValueError:
        print("Score must be an integer")
        score_get()

    return score_student

import random


def main():
    score_result = score_get()
    print("your score is {}".format(score_result))
    score_ran = random.randint(1, 100)
    print(score_ran)

if __name__ == '__main__':
    main()