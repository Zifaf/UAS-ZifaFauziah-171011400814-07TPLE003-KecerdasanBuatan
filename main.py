print("Prediksi Penilaian Driver Ojek Online")
print("")

print("=====Keramahan Driver=====")
print("[1] Sangat Ramah")
print("[2] Ramah")
print("[3] Tidak Ramah")
keramahandriver = input("Keramahan Driver[1-3]: ")
print("")

print("=====Cara Mengemudi=====")
print("[1] Sangat Nyaman")
print("[2] Nyaman")
print("[3] Tidak Nyaman")
caramengemudi = input("Cara Mengemudi[1-3]: ")
print("")

print("=====Lama Penjemputan=====")
print("[1] Cepat")
print("[2] Rata-rata")
print("[3] Lama")
lamapenjemputan = input("Lama Penjemputan[1-3]: ")
print("")

print("=====Kalayakan Armada=====")
print("[1] Sangat Layak")
print("[2] Layak")
print("[3] Kurang Layak")
kelayakanarmada = input("Kelayakan Armada[1-3]: ")
print("")

print("=====Pemilihan Rute=====")
print("[1] Sesuai")
print("[2] Tidak Sesuai")
pemilihanrute = input("pemilihanrute[1-2]: ")
print("")

print("")
if keramahandriver == "1":
    if caramengemudi == "1":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 5
                elif pemilihanrute == "2":
                    poin = 4.9
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.8
                elif pemilihanrute == "2":
                    poin = 4.7
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4.6
                elif pemilihanrute == "2":
                    poin = 4.5

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.8
                elif pemilihanrute == "2":
                    poin = 4.7
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.6
                elif pemilihanrute == "2":
                    poin = 4.5
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4.4
                elif pemilihanrute == "2":
                    poin = 4.3

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.6
                elif pemilihanrute == "2":
                    poin = 4.5
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.4
                elif pemilihanrute == "2":
                    poin = 4.3
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4.2
                elif pemilihanrute == "2":
                    point = 4.1

    elif caramengemudi == "2":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.8
                elif pemilihanrute == "2":
                    poin = 4.7
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.6
                elif pemilihanrute == "2":
                    poin = 4.5
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4.4
                elif pemilihanrute == "2":
                    poin = 4.3

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.6
                elif pemilihanrute == "2":
                    poin = 4.5
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.4
                elif pemilihanrute == "2":
                    poin = 4.3
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4.2
                elif pemilihanrute == "2":
                    poin = 4.1

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.4
                elif pemilihanrute == "2":
                    poin = 4.3
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.2
                elif pemilihanrute == "2":
                    poin = 4.1
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4
                elif pemilihanrute == "2":
                    poin = 3.9

    if caramengemudi == "3":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.2
                elif pemilihanrute == "2":
                    poin = 4.1
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4
                elif pemilihanrute == "2":
                    poin = 3.9
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.8
                elif pemilihanrute == "2":
                    poin = 3.7

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4
                elif pemilihanrute == "2":
                    poin = 3.9
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.8
                elif pemilihanrute == "2":
                    poin = 3.7
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.6
                elif pemilihanrute == "2":
                    poin = 3.5

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.8
                elif pemilihanrute == "2":
                    poin = 3.7
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.6
                elif pemilihanrute == "2":
                    poin = 3.5
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.4
                elif pemilihanrute == "2":
                    poin = 3.3

if keramahandriver == "2":
    if caramengemudi == "1":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.7
                elif pemilihanrute == "2":
                    poin = 4.5
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.5
                elif pemilihanrute == "2":
                    poin = 4.3
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4.2
                elif pemilihanrute == "2":
                    poin = 4.1

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.5
                elif pemilihanrute == "2":
                    poin = 4.4
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.2
                elif pemilihanrute == "2":
                    poin = 4.1
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 4
                elif pemilihanrute == "2":
                    poin = 3.9

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.3
                elif pemilihanrute == "2":
                    poin = 4.2
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 4.1
                elif pemilihanrute == "2":
                    poin = 4
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.9
                elif pemilihanrute == "2":
                    poin = 3.8

    elif caramengemudi == "2":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4.1
                elif pemilihanrute == "2":
                    poin = 4
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.9
                elif pemilihanrute == "2":
                    poin = 3.8
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.7
                elif pemilihanrute == "2":
                    poin = 3.6

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.9
                elif pemilihanrute == "2":
                    poin = 3.8
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.7
                elif pemilihanrute == "2":
                    poin = 3.6
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.5
                elif pemilihanrute == "2":
                    poin = 3.4

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.7
                elif pemilihanrute == "2":
                    poin = 3.6
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.5
                elif pemilihanrute == "2":
                    poin = 3.4
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.3
                elif pemilihanrute == "2":
                    poin = 3.2

    if caramengemudi == "3":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.9
                elif pemilihanrute == "2":
                    poin = 3.8
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.7
                elif pemilihanrute == "2":
                    poin = 3.6
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.5
                elif pemilihanrute == "2":
                    poin = 3.4

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.7
                elif pemilihanrute == "2":
                    poin = 3.6
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.5
                elif pemilihanrute == "2":
                    poin = 3.4
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.3
                elif pemilihanrute == "2":
                    poin = 3.2

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.5
                elif pemilihanrute == "2":
                    poin = 3.4
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.3
                elif pemilihanrute == "2":
                    poin = 3.2
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.1
                elif pemilihanrute == "2":
                    poin = 3

if keramahandriver == "3":
    if caramengemudi == "1":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 4
                elif pemilihanrute == "2":
                    poin = 3.9
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.8
                elif pemilihanrute == "2":
                    poin = 3.7
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.6
                elif pemilihanrute == "2":
                    poin = 3.5

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.8
                elif pemilihanrute == "2":
                    poin = 3.7
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.6
                elif pemilihanrute == "2":
                    poin = 3.5
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.4
                elif pemilihanrute == "2":
                    poin = 3.3

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.6
                elif pemilihanrute == "2":
                    poin = 3.5
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.4
                elif pemilihanrute == "2":
                    poin = 3.3
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3.2
                elif pemilihanrute == "2":
                    poin = 3.1

    elif caramengemudi == "2":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.4
                elif pemilihanrute == "2":
                    poin = 3.3
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3.2
                elif pemilihanrute == "2":
                    poin = 3.1
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 3
                elif pemilihanrute == "2":
                    poin = 2.9

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3.2
                elif pemilihanrute == "2":
                    poin = 3.1
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 3
                elif pemilihanrute == "2":
                    poin = 2.9
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 2.8
                elif pemilihanrute == "2":
                    poin = 2.7

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 3
                elif pemilihanrute == "2":
                    poin = 2.9
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 2.8
                elif pemilihanrute == "2":
                    poin = 2.7
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 2.6
                elif pemilihanrute == "2":
                    poin = 2.5

    if caramengemudi == "3":
        if lamapenjemputan == "1":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 2.8
                elif pemilihanrute == "2":
                    poin = 2.7
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 2.6
                elif pemilihanrute == "2":
                    poin = 2.5
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 2.4
                elif pemilihanrute == "2":
                    poin = 2.3

        elif lamapenjemputan == "2":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 2.6
                elif pemilihanrute == "2":
                    poin = 2.5
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 2.4
                elif pemilihanrute == "2":
                    poin = 2.3
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 2.2
                elif pemilihanrute == "2":
                    poin = 2.1

        elif lamapenjemputan == "3":
            if kelayakanarmada == "1":
                if pemilihanrute == "1":
                    poin = 2.4
                elif pemilihanrute == "2":
                    poin = 2.3
            elif kelayakanarmada == "2":
                if pemilihanrute == "1":
                    poin = 2.2
                elif pemilihanrute == "2":
                    poin = 2.1
            elif kelayakanarmada == "3":
                if pemilihanrute == "1":
                    poin = 2
                elif pemilihanrute == "2":
                    poin = 1



print("Prediksi Poin:",poin)