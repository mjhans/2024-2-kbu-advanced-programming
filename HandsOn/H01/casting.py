# input함수를 이용해서 정수를 입력받은뒤 int로 캐스팅하시오
# 입력받은 값의 자료형과 캐스팅 이후 자료형을 출력하세요
# 사용자로부터 정수를 입력받기
user_input = input("정수를 입력하세요: ")

# 입력받은 값의 자료형 출력
print("입력받은 값의 자료형:", type(user_input))

# 입력받은 값을 정수로 캐스팅
casted_input = int(user_input)

# 캐스팅된 값의 자료형 출력
print("캐스팅된 값의 자료형:", type(casted_input))