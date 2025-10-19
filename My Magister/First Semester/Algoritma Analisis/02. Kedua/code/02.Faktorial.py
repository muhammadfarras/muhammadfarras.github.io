langkah = 1
def faktorial(number=1):
    global langkah
    result  = number
    for a in range(1, number):
        langkah+=1
        result = result * a

    return result


n = 4
print(f'Faktorial {n} adalah {faktorial(n)}') # 24
print(f'Number of step {langkah}') # 4