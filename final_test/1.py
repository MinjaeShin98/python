dic = {'a':10,'b':20,'c':30,'d':40}
keyList = dic.keys()
valueList = dic.values()
print(keyList)
print(valueList)
#dict_keys(['a', 'b', 'c', 'd'])
#dict_values([10, 20, 30, 40])

members = {'홍':'111','박':'222','정':'333'}
members['최'] = '555'
members.update({'강':'666'})
members['김'] = '777'
members.update({'최':'888'})
print(members)
#{'홍': '111', '박': '222', '정': '333', '최': '888', '강': '666', '김': '777'}
members['최'] = '555'
print(members)
#{'홍': '111', '박': '222', '정': '333', '최': '555', '강': '666', '김': '777'}
members.pop('홍')
print(members)
#{'박': '222', '정': '333', '최': '555', '강': '666', '김': '777'}


carDict = {'h101':('2017','3000'),
           'k301':('2022','2000'),
           'h401':('2020','3200'),
           'd221':('2020','1500'),
           'h111':('2022','3000'),
           'm201':('2022','2700')
           }
print(carDict)
print(carDict.items())
#1
for key in carDict.keys():
    print(key,carDict[key])
#2
for key,value in carDict.items():
    print(key,value)

h101 ('2017', '3000')
k301 ('2022', '2700')
h401 ('2020', '3200')
d221 ('2020', '1500')
h111 ('2022', '3000')
m201 ('2022', '2700')

#생산년도로 구성된 각 요소가 int형인 yearList 리스트를 생성하고 출력하는 코드
#실행결과 [2017, 2022, 2020, 2020, 2022]
yearList=[]
for value in carDict.values():
    yearList.append(int(value[0])) #yearList에 튜플로 value를 넣어줌
    print("year,배기량", value[0],value[1])
print(yearList)

year,배기량 2017 3000
year,배기량 2022 2700
year,배기량 2020 3200
year,배기량 2020 1500
year,배기량 2022 3000
[2017, 2022, 2020, 2020, 2022]

#생산년도를 입력받아, 해당 년도에 생성된 자동차가 몇대인지 출력하는 코드를 작성 
#for문을 쓰지 말고, 한번만 실행하고 종료한다
#실행결과
#생산년도를 입력하세요 :2020
#2020의 등록차는 2대입니다.
#여기서 2020은 사용자가 입력한 값입니다
#1
year = input("생산년도를 입력하세요.") #'2020' string 형식으로 input받아서 int로 바꿔줌
print(year,"의 등록차량은",yearList.count(int(year)),"대입니다.")
#2
count = 0
year = input("생산년도를 입력하세요.") #'2020'
for value in carDict.values():
    if value[0] == year :
        count += 1
print(count)

#구기종목과 인원과 관계
#두개의 list를 zip으로 묶어서 dictionary로 나타낸후
#사용자로부터 종목이름을 입력받아서, 그에 맞는 인원수를 출력하라
#while문을 돌려서 할것, quit을 만나면 종료할것
#다른 종목 들어오면 "몰라요" 다시 입력 받을것
#continue,break를 활용할것

sport=['축구','야구','농구','배구']
num = [11,9,5,6]
sports = dict(zip(sport,num))
print(sport)
while 1:
    i = input("스포츠 경기를 입력하세요 : ")
    if i ==  'quit':
        print("너는 quit을 입력했다. 종료")
        break
    if i in sports.keys():
        #인원수 출력
        print("인원수 : ", sports[i])             
    else :
        print("다른 종목을 입력했습니다. 다시 입력하세요")
        continue

    print("홍길동 님은 지금 ",i,"에 대한 정보를 서치하셨습니다.")

print("종료")

#lambda 함수 작성하기:간단한 함수 작성할 때
# map,filter
#입력 숫자 하나 받고, 출력으로 숫자 +1 을 하는 함수

def addone(num):
    return num+1

print(addone(10))

#lambda 입력값 : return값
print((lambda num : num+1)(10))

#1.숫자 두개 입력 받아서, 합을 return 하는 함수
print('합',(lambda n1,n2:n1+n2)(10,20))
def sum1(n1,n2):
    return n1+n2
#2.숫자 두개 입력 받아서, a,b 입력 a%b를 출력하라
print('나누기',(lambda n1,n2:n1%n2)(100,3))
def cal (n1,n2):
    return n1%n2
#map(),filter()랑 함께쓰이는 lambda
print((lambda num:num+1)(10))
#[20,21,22,23,24,25,26]
#=>[21,22,23,24,25,26,27]
#map(function, 입력값 리스트)
print(list(map(lambda num:num+1,[20,21,22,23,24,25,26])))
list1=[100,200,300,400]
list2=[5,2,4,10]

#map(function,list1,list2)
#1.숫자 두개 입력 받아서, 합을 return 하는 함수
print(list(map(lambda n1,n2 : n1+n2,list1,list2)))

#2.숫자 두개 입력 받아서, a,b 입력 a%b를 출력하라
print(tuple(map(lambda n1,n2 : n1%n2,list1,list2)))
print(tuple(map(lambda n1,n2 : n1/n2,list1,list2)))

#filter(function, list)
#3.filter를 사용하여 리스트 [1,-2,3,-5,8,-3]에서 음수를 모두 제거해 보자.
print(filter(lambda x:x>0,[1,-2,3,-5,8,-3]))
print(list(filter(lambda x:x>0,[1,-2,3,-5,8,-3])))

#__name__ **중요**

1.py       __name__ <='1'
2.py =run  __name__ <='__main__'
3.py       __name__ <='3'  

if __name__ == "__main__":
    실행문
else:
    실행문