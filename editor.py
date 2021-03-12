formatters = 'plain bold italic link inline-code header ordered-list unordered-list line-break'.split()
post_format = []


def plain_bold_italic_inline():
    text = input('- Text:')
    if choice == 'bold':
        post_format.append('**' + text + '**')
    elif choice == 'italic':
        post_format.append('*' + text + '*')
    elif choice == 'inline-code':
        post_format.append('`' + text + '`')
    else:
        post_format.append(text)


def link():
    label = input('- Label:')
    url = input('- URL:')
    post_format.append('[' + label + ']' + '(' + url + ')')


def header():
    level = int(input('- Level:'))
    text = input('- Text:')
    post_format.append(''.join('#' for n in range(level)) + ' ' + text + '\n')


def line_break():
    post_format.append('\n')


def ordered_unordered_list():
    while True:
        rows = int(input('Number of rows:'))
        if rows < 1:
            print('The number of rows should be greater than zero')
        else:
            break
    if choice == 'ordered-list':
        for n in range(1, rows + 1):
            text = input(f'Row #{n}:')
            post_format.append(str(n) + '. ' + text + '\n')
    else:
        for n in range(1, rows + 1):
            text = input(f'Row #{n}:')
            post_format.append('* ' + text + '\n')


while True:
    choice = input('- Choose a formatter:')
    if choice == '!help':
        print(r'Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break'
              + '\n' + r'Special commands: !help !done')
    elif choice == '!done':
        with open('output.md', 'w') as file:
            file.write(''.join(post_format))
        break
    elif choice.lower() not in formatters:
        print('Unknown formatting type or command. Please try again')
    else:
        if choice == 'plain' or choice == 'bold' or choice == 'italic' or choice == 'inline-code':
            plain_bold_italic_inline()
        elif choice == 'link':
            link()
        elif choice == 'header':
            header()
        elif choice == 'line-break':
            line_break()
        elif choice == 'ordered-list' or choice == 'unordered-list':
            ordered_unordered_list()
        else:
            pass
    print(''.join(post_format))