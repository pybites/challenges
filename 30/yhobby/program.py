'''
docstring
'''
import webbrowser

import api


def main():
    '''docstring'''
    print('******* SEARCH TALK PYTHON *******')
    keyword = input('What keywords to search for? ')
    data = api.search(keyword)

    print(f'There are {len(data)} matching episodes:')

    outputs = []
    for idx, episode in enumerate(data, 1):
        outputs.append((idx, episode))
        print(idx, '. ', episode.title, sep='')

    id_number = int(input('If you want to view any of them, '
                      'use the episode ID returned from '
                      'the service (e.g. 142)): '))

    for id, output in outputs:
        if id == id_number:
            full_url = 'talkpython.fm' + output.url
            webbrowser.open(full_url, new=2)


if __name__ == '__main__':
    main()