def this_fails():
    x = 1/0

# this_fails()

try:
    this_fails()
except ZeroDivisionError as err:
    raise err 
    # print('Handling run-time error:', err)

