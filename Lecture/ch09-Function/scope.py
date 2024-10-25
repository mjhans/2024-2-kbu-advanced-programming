animal = 'fruitbat' # 전역 변수

def change_and_print_global(animal):
    #global animal    # 전역변수를 사용하고 싶다면 global 키워드 사용
    print(f'inside change_and_print_global: {animal = }, {id(animal) = }') # 함수내에서 animal를 수정하므로 지역변수로 인식
    animal = 'wombat'
    print(f'after the change: {animal = }, {id(animal) = }')

change_and_print_global(animal)
print(f"{animal = }, {id(animal) = }")