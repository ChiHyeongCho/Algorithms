

def moving_z(r, c, a):


    #1
    ar, ac, aa = r, c+1, a+1

    if ar == R and ac == C:
        return ar, ac, True, aa

    #2
    ar, ac, aa = r+1, c, aa+1

    if ar == R and ac == C:
        return ar, ac, True, aa

    #3
    ar, ac, aa = r+1, c+1, aa+1

    if ar == R and ac == C:
        return ar, ac, True, aa

    return ar, ac, False, aa


def moving_right(r, c, a):

    ar, ac, aa = r-1, c+1, a+1

    if ar == R and ac == C:
        return ar, ac, True, aa

    return ar, ac, False, aa


def moving_bottom(r, c, a):

    ar, ac, aa = r + 1, 0, a + 1

    if ar == R and ac == C:
        return ar, ac, True, aa

    return ar, ac, False, aa



def moving(r, c , answer):

    state = False

    next_r, next_c, state, next_answer = moving_z(r, c, answer)

    if state == True:
        print(next_answer)
        return


    if next_c + 1 != (2**N):

        next_r, next_c, state, next_answer = moving_right(next_r, next_c, next_answer)

        if state == True:
            print(next_answer)
            return

        moving(next_r, next_c, next_answer)

    else:

        next_r, next_c, state, next_answer = moving_bottom(next_r, next_c, next_answer)

        if state == True:
            print(next_answer)
            return

        moving(next_r, next_c, next_answer)



N, R, C = map(int, input().split())

moving(0, 0, 0)
