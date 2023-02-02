from django import template

# если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются
register = template.Library()


# регистрируем наш фильтр под именем censor, чтоб django понимал, что это именно фильтр, а не простая функция
# @register.filter(name='Censor')
# def Censor(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
#    # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон
#    return str(value) * arg


censor_list = ['Ублюдок', 'говно', 'засранец', 'трахнуть', 'трахну', 'онанист', 'онанист', 'трахать', 'дерьмо', 'сука', 'падла', 'жопа']


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '*****')
    return value
