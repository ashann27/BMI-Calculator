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

    points = 0
    incorrect_words = {}
    playing = true

    for key, value in dictionary.items():
        answer = input('{}はなんでしょうか？\n'
          '単語を入力してください。また、「h」ヒント　「p」パス  「q」やめる'.format(value[0]))

        if answer == 'h':
            print('\n Hint:{}'.format(value[1]))

        elif answer == 'p':
            print('答えは{}でした'.format(key))
            incorrect_words[key] = None
        elif answer == 'q':
            playing=false
        else:
            print(answer + 'ではないです')
    print('\nScore: {}/{}'.format(points, len(dictionary)))
    print('Incorrect Words:')
    for key in incorrect_words:
        print(key)





    

add_word()
list_all_words()
remove_word()
list_all_words()
test_yourself()