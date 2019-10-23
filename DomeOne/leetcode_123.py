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