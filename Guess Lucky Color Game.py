import random

colors = ['pink', 'red', 'blue', 'green']
lucky_color = random.choice(colors)
print('今回、あなたのラッキーカラーはなんでしょうか！\n')

for i in range(len(colors)):
        print('今選択できる色は{}'.format(colors))
        answer = input('上の{}色から一つを入力してください\n\n'.format(len(colors)))
        answer.lower()
        if answer not in colors:
            print('{}はリストに入ってないみたいです。スペルを確認してまた入力してみてください\n'.format(answer))
            continue

        elif answer != lucky_color:
            colors.remove(answer)
            print('{}じゃないです！また当たてみてください。\n'.format(answer))
            continue

        else:
            print('正解！')
            break