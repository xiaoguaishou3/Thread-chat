# @ Time    : 2020/2/7 10:51
# @ Author  : Emily
'''
天猫精灵:小爱同学
小爱同学:在
天猫精灵:现在几点了？
小爱同学：你猜猜现在几点了
'''
"""
cond  Condition是复杂情况下的线程锁
wait
noti
"""
import threading


class XiaoAi(threading.Thread):   
    def __init__(self, cond):
        super().__init__(name='小爱同学')
        self.cond = cond   #这里不用Lock锁的方法用cond


    def run(self):
        with self.cond:
            print("--11--")
            self.cond.wait()
            print("{}:在".format(self.name))
            print("--3--")
            self.cond.notify()
            print("--4--")
            self.cond.wait()
            print("--8--")
            # --7----8--
            # 小爱同学: 你猜猜现在几点了
            # --9--

            # --7----8--
            #
            # 小爱同学: 你猜猜现在几点了

            # --7----8--
            # 小爱同学: 你猜猜现在几点了
            #

            print("{}:你猜猜现在几点了".format(self.name))
            print("--9--")
            # self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond   #这里不用Lock锁的方法用cond


    def run(self):
        #这里使用直接的cond启用关闭方式
        self.cond.acquire()

        print("{}:小爱同学".format(self.name))
        print("--1--")
        self.cond.notify()
        print("--2--")
        self.cond.wait()
        print("--5--")

        print("{}:现在几点了？".format(self.name))
        self.cond.notify()
        print("--6--")
        # self.cond.wait()

        self.cond.release()
        print("--7--")


if __name__ == '__main__':
    cond = threading.Condition()   #这里改用Condition方法
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    #这里需要根据实际的需要来按顺序启动，避免出现互相等待的错误状况
    xiaoai.start()   #这里还是用start的方式启动Condition
    tianmao.start()