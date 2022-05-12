weight = input('体重を入力してください')
height = input('センチ単位身長を入力してください')
bmi = int(weight)/((int(height)/100)**2)
print('あなたのBMIは {}'.format(round(bmi, 1)))

if bmi < 18.5:
    print ('あなたのBMIはやせです。もう少し食べてください！')

elif bmi > 25:
    print ('あなたのBMIは肥満です。ダイエットしてください！')

else:
    print ('あなたのBMIは標準です。食事はそのままで続けてください！')