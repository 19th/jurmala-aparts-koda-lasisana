
import csv

apartamenti = []

with open('jurmala_all_17_03_25.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartamenti.append(row)

apartamenti.pop(0)

while True:
    print("1. Pirmais dzīvoklis")
    print("2. Pirmie 10 dzīvokļi")
    print("3. Dargākie par 100k dzīvokļi (filtrēšana)")
    print("4. Top 10 letākie dzīvokļi (kārtošana)")
    print("5. Top 10 dargākie dzīvokļi (kārtošana)")
    
    choice = input("Ievadi komandu: ")

    print("==========================")
    # Pirmais dzīvoklis
    if choice == '1':
        pirmie_apartamenti = apartamenti[0]

        print("Teksts:", pirmie_apartamenti[2])
        print("Tips:", pirmie_apartamenti[7])
        print("Adrese:", pirmie_apartamenti[3])
        print("Platums:", pirmie_apartamenti[4])
        print("Cena:", pirmie_apartamenti[8])
        print("Links:", pirmie_apartamenti[0])

    # Pirmie 10 dzīvokļi
    elif choice == '2':
        pirmie_10_apartamenti = apartamenti[:10]

        for apartment in pirmie_10_apartamenti:
            kvadrata_cena = int(apartment[8]) / int(apartment[5])
            
            print("Tips:", apartment[7])
            print("Adrese:", apartment[3])
            print("Istabas:", apartment[4])
            print("Platums:", apartment[5])
            print("Kvadrātmetra cena:", kvadrata_cena)
            print("Cena:", apartment[8])
            print("Links:", apartment[0])
            print("--------------------------")

    # Dargākie par 100k dzīvokļi (filtrēšana)
    elif choice == '3':
        dargie_apartamenti = []

        for apartment in apartamenti:
            cena = int(apartment[8])
            if cena > 100000:
                dargie_apartamenti.append(apartment)

        for apartment in dargie_apartamenti:
            print("Tips:", apartment[7])
            print("Adrese:", apartment[3])
            print("Istabas:", apartment[4])
            print("Platums:", apartment[5])
            print("Cena:", apartment[8])
            print("Links:", apartment[0])
            print("--------------------------")
    
    # Top 10 letākie dzīvokļi (kārtošana)
    elif choice == '4':
        apartamenti.sort(key=lambda apartaments: int(apartaments[8]))

        top_10_letakie_apartamenti = apartamenti[:10]

        for apartment in top_10_letakie_apartamenti:
            print("Tips:", apartment[7])
            print("Adrese:", apartment[3])
            print("Istabas:", apartment[4])
            print("Platums:", apartment[5])
            print("Cena:", apartment[8])
            print("Links:", apartment[0])
            print("--------------------------")
            
    # Top 10 dargākie dzīvokļi (kārtošana)
    elif choice == '5':
        apartamenti.sort(key=lambda apartaments: int(apartaments[8]), reverse=True)

        top_10_dargie_apartamenti = apartamenti[:10]

        for apartment in top_10_dargie_apartamenti:
            print("Tips:", apartment[7])
            print("Adrese:", apartment[3])
            print("Istabas:", apartment[4])
            print("Platums:", apartment[5])
            print("Cena:", apartment[8])
            print("Links:", apartment[0])
            print("--------------------------")
    else:
        break

    print("==========================")


