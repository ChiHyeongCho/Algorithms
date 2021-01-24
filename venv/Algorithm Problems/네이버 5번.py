

def solution(companies, applicants):
    answer = []

    notDecision = len(applicants)

    for i in range(len(applicants)):

        applicants[i] += " " + "0"

    answerList = [0]*len(companies)
    middlelist = [0]*len(companies)

    print(applicants)

    while True:

        if notDecision == 0:
            break

    for i in range(len(applicants)):

        string = applicants[i]
        want = string[1][applicants[3]]

        middlelist

    middlelist
    return answerList


print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))