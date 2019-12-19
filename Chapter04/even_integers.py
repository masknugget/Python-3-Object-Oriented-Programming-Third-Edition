class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):                
            raise TypeError("Only integers can be added")                    # 类型错误TypeError
        if integer % 2:
            raise ValueError("Only even numbers can be added")               # ValueError
        super().append(integer)                                              # 包装一层，有条件进入父类中
