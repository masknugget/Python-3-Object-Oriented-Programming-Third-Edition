import random

some_exceptions = [ValueError, TypeError, IndexError, None]    # 这里包含了None

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:                                               # 对应的是if的选择
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" % (e.__class__.__name__))
else:                                                        # 必然需要执行的，如果不触发异常
    print("This code called if there is no exception")
finally:                                                    # 必然执行的
    print("This cleanup code is always called")
