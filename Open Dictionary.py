dictionary = {}
import random

def add_word():
    #Each word has a key (word), and 2 values (definition) (hint)
    word = input("新しい単語を追加しましょう！\n"
          "まずは単語を入力してください\n")
    word = word.lower()

    definition = input("次は意味を追加しましょう！\n"
                 "意味を入力してください\n")

    hint = input("最後はヒントを追加しましょう！\n"
                       "ヒントを入力してください\n")

    dictionary[word] = [definition, hint]

def remove_word():
    word = input('削除したい単語を入力してください')
    word = word.lower()
    if word in dictionary:
        del dictionary[word]

    else:
        print('その単語は辞書に入ってないみたいです！スペルを確認してください')

def list_all_words():
    for key, value in dictionary.items():
        print('{} - {} \nHint: {}'.format(key, value[0], value[1]))

def test_yourself():
    playing = True
    if not bool(dictionary):
        print('\nまだ辞書に単語が入ってないです！まずは単語をつかしてください\n')
        playing = not playing
    points = 0
    incorrect_words = {}
    while playing == True:
        for key, value in dictionary.items():

                still_trying = True

                while still_trying == True:
                    answer = input('{}はなんでしょうか？\n'
                        '単語を入力してください。また、「h」ヒント　「p」パス  「q」やめる\n'.format(value[0]))
                    answer = answer.lower()
                    if answer == key:
                        print('正解！')
                        points  += 1
                        still_trying = not still_trying
                    elif answer == 'h':
                        print('\nHint:{}\n'.format(value[1]))
                    elif answer == 'p':
                        print('答えは{}でした'.format(key))
                        incorrect_words[key] = None
                        still_trying = not still_trying
                    elif answer == 'q':
                        still_trying = not still_trying
                        playing = not playing

                    else:
                        print(answer + 'ではないです')
        print('\n点数: {}/{}'.format(points, len(dictionary)))
        print('間違った単語:')
        for key in incorrect_words:
            print(key)
        playing = not playing

while True:
    cmd = input("""\nオープン辞書へようこそ!
1) テスト　
2) 単語を追加して
3) 単語を削除して
4) 追加した単語の発表
5) やめる\n""")

    if cmd == '1':
        test_yourself()
    elif cmd == '2':
        add_word()
    elif cmd == '3':
        remove_word()
    elif cmd == '4':
        list_all_words()
    elif cmd == '5':
        break