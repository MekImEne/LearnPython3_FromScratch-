"""
Exceptions are errors
"""

def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0
        # c = 10

        d= (a+b)/c
        print(d)
    except:
        print('In the except block, this is not possible')
        raise Exception('This is an exception')
    else:
        print('Because there was no exception , else executed')
    finally:
        print('Finally ! always executed')

exceptionHandling()