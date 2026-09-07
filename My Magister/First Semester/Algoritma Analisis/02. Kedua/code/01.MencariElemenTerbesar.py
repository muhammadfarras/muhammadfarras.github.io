langkah = 0

def elemenTerbesar(list = [] ):

    global langkah

    nilai_terbesar = 0
    for a in list:
        # Get number of steps
        langkah+=1

        if a > nilai_terbesar:
            nilai_terbesar = a
        
    return nilai_terbesar


print(f'Nilai terbesar {elemenTerbesar(range(0,50,3))}')
print(f'Number of step {langkah}')
