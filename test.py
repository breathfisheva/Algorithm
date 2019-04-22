'''
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

思路：
1.函数get_str，获得字符串st第一个子字符串
用一个临时变量tmp来存字串，如果元素不在tmp里则加入tmp
如果元素在tmp里则返回结果给
(这时候要特别注意处理最后一个元素的情况）

2.函数lengthOfLongestSubstring， 调用get_str函数，最大的子串长度
比如： 'vdvdf’
第一次：vdvdf 调用get_str获得 ”vd“
第二次：dvdf 调用get_str获得 ”dv“
第三次：vdf get_str获得 ”vdf"

'''

s = 'vdf'
class Solution:
    result = []
    max_num = 0
    def get_str(self, st):
        tmp = []
        for index, item in enumerate(st):
            if index == len(st) - 1: #处理最后一个元素的情况
                tmp.append(item)

                tmp_str = ''.join(str(i) for i in tmp)
                self.result.append([tmp_str, len(tmp_str)])
                return [tmp_str, len(tmp_str)]

            elif item not in tmp:
                tmp.append(item)

            else:
                tmp_str = ''.join(str(i) for i in tmp)
                self.result.append([tmp_str, len(tmp_str)])
                return [tmp_str, len(tmp_str)]


    def lengthOfLongestSubstring(self, s: str) -> int:
        for index in range(len(s)):
            num = self.get_str(s[index:])[1]
            if self.max_num < num:
                self.max_num = num
        return self.max_num

# tmp = []
# for index, item in enumerate(s):
#     if index == len(s) - 1:
#         tmp.append(item)
#         print(tmp)
#
#     elif item not in tmp:
#         tmp.append(item)
#
#     else:
#         print(tmp)
#


so = Solution()
print(so.lengthOfLongestSubstring(s))





