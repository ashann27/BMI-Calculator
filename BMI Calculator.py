weight = input('体重を入力してください')
height = input('センチ単位身長を入力してください')
bmi = int(weight)/((int(height)/100)**2)
print('Your BMI is {}'.format(round(bmi, 1)))
