import queue


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        # self.q1 = queue.Queue()
        # self.q2 = queue.Queue()
        # self.q3 = queue.Queue()
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)
        self.s3 = threading.Semaphore(0)
        self.s4 = threading.Semaphore(0)
        self.cur = 1

    # printFizz() outputs "fizz"
    def fizz(self):
        while True:
            self.q1.get()
            if self.cur > self.n:
                break
            print("Fizz")

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.q2.get()
            if self.cur > self.n:
                break
            printBuzz()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.q3.get()
            if self.cur > self.n:
                break
            printFizzBuzz()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            if (self.cur % 3) != 0 and (self.cur % 5) != 0:
                print(self.cur)
            elif (self.cur % 3) == 0 and (self.cur % 5) != 0:
                self.q1.put(0)
            elif (self.cur % 5) == 0 and (self.cur % 3) != 0:
                self.q2.put(0)
            else:
                self.q3.put(0)
            self.cur += 1
            if self.cur > self.n:
                break

#信号方法：
import threading

class Foo:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        printThird()

class QueNum(object):
    def __init__(self,n):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.n = n
        self.cur = 1

    def fun1(self):
        print("funo1_before")
        num = self.q1.get()
        print(num)
        print("fun01_test")

    def fun2(self):
        print("fun02_before")
        num2 = self.q2.get()
        print(num2)
        print("fun02_test")

    def num(self):
        while True:
            if (self.cur % 3) != 0 and (self.cur % 5) != 0:
                print(self.cur)
            elif (self.cur % 3) == 0 and (self.cur % 5) != 0:
                self.q1.put(0)
                self.fun1()
            elif (self.cur % 5) == 0 and (self.cur % 3) != 0:
                self.q2.put(0)
                self.fun2()
            self.cur += 1
            if self.cur > self.n:
                break


# test1 = QueNum(15)
# test1.num()

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        num = len(nums)
        if nums and k:
            # nums = nums[num-k:num]+nums[:num-k]
            # return nums
            # for i in range(num-k):
            #     nums.insert(0,nums[num-1])
            #     print(nums)
            #     nums.pop(0)
            #     print(nums)
            # print(nums)
            # nums.reverse()
            # print(nums)
            # nums[0:k].reverse()
            # print(nums)
            # return nums
            n = len(nums)
            k %= n
            for _ in range(k):
                nums.insert(0, nums.pop())

nums = [1,2,3,4,5,6,7]
k = 3
test1 = Solution()
res = test1.rotate(nums,k)
print(res)
print(nums)

class Solution:
    def singleNumber(self, nums):
        # numa = 0
        # for i in nums:
        #     #if nums.count(i)<2:
        #     #    return i   #执行超时
        #     numa ^= i
        # return numa
        #return 2*sum(set(nums)) - sum(nums)
        len_num = len(nums)
        if not nums:
            return nums
        elif len_num == 1:
            return nums[0]
        else:
            nums.sort()
            left = 0
            right = len_num
            print(nums)
            while left < right:
                mid = (left + right) // 2
                print(mid)
                if (nums[mid] ^ nums[mid+1])!=0:
                    if (nums[mid] ^ nums[mid-1])!=0:
                        print(nums[mid-1])
                        print(">>>>%s"%nums[mid])
                        return nums[mid]
                    else:
                        if mid%2 == 0:
                            right = mid
                        elif (right-mid)>3:
                            left = mid
                        else:
                            print(nums[mid])
                            return nums[mid+1]
                elif mid%2 == 0:
                    left = mid
                elif mid%2 !=0:
                    right = mid

class Solution:
    def majorityElement(self, nums):
        left,right = 0,len(nums)
        nums.sort()
        # while left < right:
        #     mid = (left+right)//2
        #     if nums[mid+1]^nums[mid-1]==0:
        #         return nums[mid]
        #     elif nums[mid]^nums[mid+1] == 0:
        #         return nums[mid]
        #     else:
        #         return nums[]
        return nums[(left+right)//2]


# class FruitFactory(object,Apple,Pear):
#     def __init__(self,target):
#         if target == "苹果":
#             return Apple()
#         elif target == "苹果":
#             return Pear()
#         else:
#             return ("暂时没有这种水果")



list0 = [-1,1,1,3,3]
list1 = [-1,-1,1,1,2,2,3,3,4]
list2 = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
list3 = [2,2,1]
list4 = [4,1,2,1,2]
# test = Solution()
# ret = test.singleNumber(list4)
# print("result>>",ret)

list1 = [3,2,3]
list2 = [2,2,1,1,1,2,2]
[1,1,1,2,2,2,2]

if __name__ == '__main__':
    pass


#给定两个有序整数数组 nums1 和 nums2，
# 将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#说明:
#初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
#你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）
# 来保存 nums2 中的元素。

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mn = m + n
        m -= 1
        n -= 1
        while n >= 0:
            mn -= 1
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[mn] = nums1[m]
                m -= 1
            else:
                nums1[mn] = nums2[n]
                n -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
nums11= [4,0,0,0,0,0]
mm = 1
nums22= [1,2,3,5,6]
nn = 5
test2 = Solution()
test2.merge(nums11,mm,nums22,nn)
print(nums11)