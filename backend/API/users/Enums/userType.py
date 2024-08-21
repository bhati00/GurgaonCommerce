from enum import IntEnum

class UserType(IntEnum) :
    SELLER = 1
    BUYER = 2
    
    @classmethod
    def choices(cls) :
         return [(key.value, key.name) for key in cls]

