#  schedule

## π schedule λΌμ΄λΈλ¬λ¦¬
schedule μ μκ°μ λ§μΆ° μ΄λ€ μΌμ ν  λ μ¬μ©νλ ν¨ν€μ§ μ΄λ€. 

```
pip install schedule
```

<br>

## βοΈ μ¬μ© ν  λ§ν κΈ°λ₯
```
import schedule
import time

schedule.every(s).seconds.do(ν¨μ) # s μ΄ λ§λ€ νλ²μ© ν¨μ μ€ν

schedule.every(s).minutes.do(ν¨μ) # s λΆ λ§λ€ νλ²μ© ν¨μ μ€ν

schedule.every(s).hour.do(ν¨μ) # s μκ° λ§λ€ νλ²μ© ν¨μ μ€ν

schedule.every(s).days.do(ν¨μ) # s μΌ λ§λ€ νλ²μ© ν¨μ μ€ν

schedule.every(s).weeks.do(ν¨μ) # s μ£Όλ§λ€ νλ²μ© ν¨μ μ€ν

schedule.every().day.at("13:30").do(ν¨μ) # λ§€μΌ μ ν΄μ§ μκ°μ λ°λΌ μ€ν

# λ§μ½μ μΈμλ₯Ό λ°λ ν¨μκ° μ‘΄μ¬νλ€λ©΄ λ€μκ³Ό κ°μ΄ μ¬μ©

def message2(text):
    print(text)

schedule.every(2).seconds.do(message2,'2μ΄λ§λ€ μλ €μ€κ²μ')
```

## βοΈ μ¬μ© λ°©λ²

```
# step1.κ΄λ ¨ ν¨ν€μ§ λ° λͺ¨λ import
import schedule
import time

# step2.μ€νν  ν¨μ μ μΈ


def message():
    print("μ€μΌμ₯΄ μ€νμ€...")


# step3.μ€ν μ£ΌκΈ° μ€μ 
schedule.every(1).seconds.do(message)

# step4.μ€μΊμ₯΄ μμ
while True:
    schedule.run_pending() # μ€μΌμ₯΄ μ€ν
    time.sleep(1)
```

## βοΈ μ€μ§ λ°©λ²

```
1. whileλ¬Έμ μ‘°κ±΄μ κ±Έμ΄μ λ¬΄νλ£¨νλ₯Ό μ’λ£μν€κ³  νμ΄μ¬ νμΌμ μ’λ£νλ€.

2. sys λͺ¨λμ exit( ) ν¨μλ‘ νμ΄μ¬ νμΌμ κ°μ  μ’λ£

3. schedule ν¨ν€μ§μ cancel_job( ) ν¨μ μ¬μ©
```