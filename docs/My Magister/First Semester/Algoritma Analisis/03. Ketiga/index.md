# Pekan ketiga



## Diskusi

!!! question "pertanyaan"

    1. Jelaskan konsep dasar algoritma Brute Force
    2. Jelaskan kelebihan dan kekurangan algoritma Brute Force
    3. Berikan contoh penerapan algoritma brute force untuk menyelesaikan berbagai masalah.

!!! notes "Jawaban"
    1. Brute force adalah algortima yang sederhana yang mana algortima ini secara sistematis mencoba semua opsi hingga masalah yang dipecahkan algoritma ini terjawab atau ditemukan. Menurut saya, algortima brute force ini secara umum banyak digunakan karena penggunaan dan pendefinisian-nya sangat mudah namun sangat tidak efesien untuk pemecahan algoritma pada data dengan skala yang besar.

    ```python
    class SampleCode:

        data = [{'user_name':'farras','password':'123456'},{'user_name':'tania','password':'0864'}
        ,{'user_name':'faris','password':'5678'},{'user_name':'noah','password':'1357'}
        ,{'user_name':'Hilyah','password':'2468'}]

        def brute_force(self, username, password):
            print(f"Input {username} : {password}")

            # Brutoforce disini, mencoba semua kemungkinan
            for it in self.data:
                print (f'Apakah sama dengan {it["user_name"]} dan password {it["password"]}')
                if it['user_name'] == username and it['password']==password:
                    return 'Match'
            
            return 'Not Match'

    sample_code = SampleCode()
    print(sample_code.brute_force('noah','1357'))

    # Output
    # Input noah : 1357
    # Apakah sama dengan farras dan password 123456
    # Apakah sama dengan tania dan password 0864
    # Apakah sama dengan faris dan password 5678
    # Apakah sama dengan noah dan password 1357
    # Match
    ```