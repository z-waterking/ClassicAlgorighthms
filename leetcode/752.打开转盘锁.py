#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set()
        queue = [[0, 0, 0, 0]]

        count = 0
        visited.add("0000")

        while len(queue) != 0:
            for i in range(len(queue)):
                
                code = queue.pop(0)
                if "".join([str(i) for i in code]) in deadends:
                    continue
                if "".join([str(i) for i in code]) == target:
                    return count
                

                for j in range(4):
                    # 上拨
                    new_code_add = code[:]
                    if code[j] == 9:
                        new_code_add[j] = 0
                    else:
                        new_code_add[j] = code[j] + 1
                    
                    if "".join([str(i) for i in new_code_add]) not in visited:
                        queue.append(new_code_add)
                        visited.add("".join([str(i) for i in new_code_add]))

                    # 下拨
                    new_code_sub = code[:]
                    if code[j] == 0:
                        new_code_sub[j] = 9
                    else:
                        new_code_sub[j] = code[j] - 1
                    if "".join([str(i) for i in new_code_sub]) not in visited:
                        queue.append(new_code_sub)
                        visited.add("".join([str(i) for i in new_code_sub]))
            count += 1
        return -1


# @lc code=end

