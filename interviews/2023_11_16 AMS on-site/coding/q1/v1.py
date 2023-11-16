from typing import List

def collide(objects: List[int]) -> List[int]:
    objs = []
    for obj in objects:
        obj_ = obj # objs = [], obj = 5, obj_ = 5
        while obj_ and objs: # objs = []
            curr = objs.pop()
            if curr > 0 and obj < 0:
                if abs(obj) > abs(curr):
                    obj_ = obj
                    continue
                elif abs(obj) < abs(curr):
                    objs.append(curr)
                    obj_ = None
                else:
                    obj_ = None
            else:
                objs.append(curr)
                break

        if obj_: # obj_ = 5
            objs.append(obj_) # [] -> [5]

    return objs
