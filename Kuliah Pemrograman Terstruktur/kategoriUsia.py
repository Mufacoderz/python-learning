umur = int(input("Masukkann umur anda: "))

if umur < 13:
    print("anda masih anak-anak")
elif umur >= 13 and umur <= 17:
    print("anda masih remaja")
elif umur >= 18 and umur <= 59:
    print("dah dewasa")
else:
    print("dah tua bangka")