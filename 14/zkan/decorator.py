from functools import wraps


def clip_sentence(func):
    '''Decorator to clip sentence'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        kwargs['text'] = kwargs['text'][0:50]
        return func(*args, **kwargs)
    return wrapper


@clip_sentence
def get_text(text='This is a pen!'):
    return text


if __name__ == '__main__':
    text = 'Big News! We are changing our name to Data Council, ' \
        'we are still the leading global events where the world gathers ' \
        'to explore the future of data. Please follow our new account ' \
        'here: @DataCouncilAI'
    print(get_text(text=text))
