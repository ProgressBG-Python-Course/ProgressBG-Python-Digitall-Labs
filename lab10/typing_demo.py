from typing import List, Optional, Union

Number = Union[int,float]
def add(x:Number, y:Number=1)->Number:
    return x+y


add( 3, 4 )
add( 3.23, 6 )
add( 'a', 6 )


# x:int = 3
# x = 'a'

l:List[int] = [1,2,3]
l[0] = 'a'

# print(x)