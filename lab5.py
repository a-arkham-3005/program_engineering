class SiteLogger:
    def __init__(self,f):
        print('> Класс SiteLogger, метод __init__, успешный запуск.')
        self.f=f
    def __call__(self):
        print('> Проверка перед запуском '+self.f.__name__)
        self.f()
        print('> Проверка безопасного выключения')
@SiteLogger
def site():
    print('Успешная работа сайта')
if __name__=="__main__":
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')