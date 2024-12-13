import math

# semiconductor Calculations에 쓰이는 상수 값 이다.
# 열에너지[eV] : KT (일반적으로 300K에서 0.0259 eV)
KT = 0.0259
# 진공의 유전율[F/m] : ε0
ε0 = 8.85e-12
# Si유전상수 : Ks
Ks = 11.8
# 전자전하[C] : q (전자 하나의 전하 크기)
q = 1.6e-19

# PNP BJT(No Bias) 관련 계산을 위한 함수이다.
def PNP_calculation():
    # 사용자로부터 입력 받는 변수들(PNP BJT(No Bias) 관련 계산에 필요)이다.
    # 실수값과 과학적 표기값을 처리하기위해 float()로 입력값을 받았다.
    # Emitter의 도핑 농도
    N_AE = float(input("N_AE 값을 입력하세요 [/cm^3]: "))

    # Collector의 도핑 농도
    N_AC = float(input("N_AC 값을 입력하세요 [/cm^3]: "))

    # Base의 도핑 농도
    N_DB = float(input("N_DB 값을 입력하세요 [/cm^3]: "))

    # 순수 실리콘에서의 고유 전하 캐리어 농도
    ni = float(input("ni[/cm^3] 값을 입력하세요: "))

    # 베이스의 전체 폭 (마이크로미터 단위)
    Wb = float(input("Wb 값을 입력하세요 [um]: "))

    # PNP BJT의 주요 식 계산
   
    """
    |Eᵢ-E𝒻|Emitter =  KT * ln(N_AE / ni) :Emitter에서의 에너지 차이
    |Eᵢ-E𝒻|Base = KT * ln(N_DB / ni) : Base에서의 에너지 차이
    |Eᵢ-E𝒻|Collector = KT * ln(N_AC / ni) : Collector에서의 에너지 차이
    |qV_bi|BE = |Eᵢ-E𝒻|Emitter + |Eᵢ-E𝒻|Base : Base-Emitter 접합의 내부 전위 장벽
    |qV_bi|BC = |Eᵢ-E𝒻|Base + |Eᵢ-E𝒻|Collector : Base-Collector 접합의 내부 전위 장벽
    |q(ΔV))EC = |Eᵢ-E𝒻|Emitter - |Eᵢ-E𝒻|Collector :  Emitter와 Collector 사이의 전위 차이
    (Xₙ)BE = {(2*Ks*ε0)/(q*N_DB)*|V_bi|BE}^(1/2) :Base-Emitter 영역의 확산 길이
    (Xₙ)BC = {(2*Ks*ε0)/(q*N_DB)*N_AC/(N_AC + N_DB)*|V_bi|BE}^(1/2) : Base-Collector 영역의 확산 길이
    W = Wb - (Xₙ)BE - (Xₙ)BC : Base의 준중성폭
    """
    # 각 영역에서의 에너지 차이 계산
    # Emitter에서의 에너지 차이
    E_emitter = KT * math.log(N_AE / ni)

    # Base에서의 에너지 차이
    E_base = KT * math.log(N_DB / ni)

    # Collector에서의 에너지 차이
    E_collector = KT * math.log(N_AC / ni)

    # Base-Emitter 접합의 내부 전위 장벽
    qV_bi_BE = E_emitter + E_base

    # Base-Collector 접합의 내부 전위 장벽
    qV_bi_BC = E_base + E_collector

    # Emitter와 Collector 사이의 전위 차이
    qDeltaV_EC = E_emitter - E_collector

    
    # 확산 길이 계산 (단위: 마이크로미터이므로 1e3을 각각 곱해주었다.)
    # Base-Emitter 영역의 확산 길이
    Xn_BE = (math.sqrt((2 * Ks * ε0) / (q * N_DB) * qV_bi_BE)) * 1e3

    # Base-Collector 영역의 확산 길이
    Xn_BC = (math.sqrt((2 * Ks * ε0) / (q * N_DB) * (N_AC / (N_AC + N_DB)) * qV_bi_BC)) * 1e3

    # Base의 준중성폭 계산
    W = Wb - Xn_BE - Xn_BC

    # 각각의 PNP BJT(No Bias)계산식과 그에 따른 계산값들을 단위를 포함해 출력해준다.
    print(f"|Eᵢ - E𝒻|Emitter = KT * ln(N_AE / ni) = {E_emitter} eV")
    print(f"|Eᵢ - E𝒻|Base = KT * ln(N_DB / ni) = {E_base} V")
    print(f"|Eᵢ - E𝒻|Collector = KT * ln(N_AC / ni) = {E_collector} eV")
    print(f"|qV_bi|BE = |Eᵢ - E𝒻|Emitter + |Eᵢ - E𝒻|Base = {qV_bi_BE} eV")
    print(f"|qV_bi|BC = |Eᵢ - E𝒻|Base + |Eᵢ - E𝒻|Collector = {qV_bi_BC} eV")
    print(f"|q(ΔV))EC = |Eᵢ - E𝒻|Emitter - |Eᵢ - E𝒻|Collector = {qDeltaV_EC} eV")
    print(f"(Xₙ)BE = {{(2*Ks*ε0)/(q*N_DB)*|V_bi|BE}}^1/2 = {Xn_BE} um")
    print(f"(Xₙ)BC = {{(2*Ks*ε0)/(q*N_DB)*N_AC/(N_AC + N_DB)*|V_bi|BE}}^1/2 = {Xn_BC} um")
    print(f"W = Wb - (Xₙ)BE - (Xₙ)BC = {W} um")

# 사칙연산 함수들
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# Perform Arithmetic Operations
# 사칙연산 기능 선택
def arithmetic_operations():
   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")

   choice = input("Enter choice(1/2/3/4):")

   # 첫 번째 피연산자 입력
   num1 = float(input("Enter first number: "))
   # 두 번째 피연산자 입력
   num2 = float(input("Enter second number: "))

   # 선택한 기능에 따른 결과 출력
   if choice == '1':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '3':
      print(num1,"*",num2,"=", multiply(num1,num2))

   elif choice == '4':
      print(num1,"/",num2,"=", divide(num1,num2))
   else:
      # 선택한 기능에 따른 결과 출력
      print("Invalid input")

# 프로그램의 메인 흐름
# 프로그램 시작 시 옵션 2개를 주고 1을 선택하면 사칙연산을 수행, 2를 선택하면 반도체 계산을 수행한다
print("Select an option:")
print("1. Perform Arithmetic Operations")
print("2. Perform semiconductor Calculations")

option = input("Enter choice (1/2): ")

if option == '1':
    # 옵션1(Arithmetic Operations)을 골랐을 때 arithmetic_operations()을 실행한다.
    arithmetic_operations()
elif option == '2':
    # 옵션2(emiconductor Calculations)를 골랐을 때 한번 더 옵션 선택으로 원하는 종류의 반도체 계산 실행(확장 가능성을 위해 옵션을 추가했다.)
    print("Select an option for semiconductor calculation:")
    print("1. Perform PNP BJT(No Bias) Calculations")

    choice = input("Enter choice (1): ")

    if choice == '1':
        #PNP_calculation(): 필요한 변수 값을 입력 받고 정의된 함수를 통해 계산 값 출력을 한다.
        PNP_calculation()
    else:
        #잘못된 입력일 때 출력
        print("Invalid input")
else:
    #잘못된 입력일 때 출력
    print("Invalid input")