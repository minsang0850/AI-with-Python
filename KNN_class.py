import math
import heapq

def maximum(a,b,c):     #0,1,2가 나온 횟수 카운팅, 가장 많이 나온 숫자 반환
    if a>=b and a>=c:
        return 0
    elif b>=a and b>=c:
        return 1
    else:
        return 2

class KNN_class:
    K=[3,5,10]          #k값
    X=None              #data
    Y=None              #target
    y_name=None         #target_name

    def __init__(self,iris):    #constructor
        self.X = iris.data[:, :4]
        self.Y = iris.target
        self.y_name = iris.target_names

    def cal_dist(self, x1, x2):   #두 점 사이의 거리를 구하는 함수
        answer = 0.0
        for i in range(0, 4):
            answer = answer + abs(x1[i]-x2[i])**2
        return answer**0.5

    def maj_vote(self):
        for k in range(0,3):    #k값만큼 반복
            print('K:',self.K[k])
            for i in range(0,10):   #test case 10개
                h=[]                #가장 가까운 값을 추리기 위해 최소힙 사용
                a=0
                b=0
                c=0
                for j in range(0,150):      #총 input 150개
                    if (j+1)%15!=0:         #i*15 + 0~13번째 인덱스 확인, 15번째(test data)가 아닐때에만 비교
                        dist=self.cal_dist(self.X[j], self.X[15*(i+1)-1])     #거리 구하기
                        heapq.heappush(h,(dist,self.Y[j]))
                for j in range(0,self.K[k]):
                    hp=heapq.heappop(h)
                    if hp[1]==0:
                        a=a+1
                    elif hp[1]==1:
                        b=b+1
                    else:
                        c=c+1
                #print('a:',a,'b:',b,'c:',c)
                print('Test Data Index:', i, ' Computed class:',self.y_name[maximum(a,b,c)], 'True class:', self.y_name[self.Y[15*(i+1)-1]])

    def weighted_maj_vote(self):
        print ('weighted_maj_vote')
        for k in range(0,3):    #k값만큼 반복
            print('K:',self.K[k])
            for i in range(0,10):   #test case 10개
                h=[]
                a=0
                b=0
                c=0
                for j in range(0,150):      #총 input 150개
                    if (j+1)%15!=0:         #i*15 + 0~13번째 인덱스 확인, 15번째(test data)가 아닐때에만 비교
                        dist=self.cal_dist(self.X[j], self.X[15*(i+1)-1])     #거리 구하기
                        heapq.heappush(h,(dist,self.Y[j]))
                for j in range(0,self.K[k]):
                    num=1.0         #가중치 계산을 위한 임의의 수
                    const=0.1
                    val=num/(dist+const)
                    hp=heapq.heappop(h)
                    if hp[1]==0:
                        a=a+val*dist        #1이 아닌 가중치와 거리의 곱만큼 더해준다
                    elif hp[1]==1:
                        b=b+val*dist
                    else:
                        c=c+val*dist
                #print('a:',a,'b:',b,'c:',c)
                print('Test Data Index:', i, ' Computed class:',self.y_name[maximum(a,b,c)], 'True class:', self.y_name[self.Y[15*(i+1)-1]])
