class Tomato:
    states=['Missing','Blossom','Green','Red']
    def __init__(self,index):
        self._index=index
        self._state=Tomato.states[0] # свойства _index и _state являются protected - доступ из класса и подклассов
    def grow(self):
        if self._state==Tomato.states[0]: self._state=Tomato.states[1]
        elif self._state==Tomato.states[1]: self._state=Tomato.states[2]
        elif self._state==Tomato.states[2]: self._state=Tomato.states[3]
    def is_ripe(self):
        return self._state==Tomato.states[3]
class TomatoBush:
    def __init__(self,num):
        self.tomatoes=[]
        for i in range(num):
            self.tomatoes.append(Tomato(i))
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
    def all_are_ripe(self):
        for i in self.tomatoes:
            if not i.is_ripe(): return False
        return True
    def give_away_all(self):
        self.tomatoes.clear()
class Gardener:
    def __init__(self,name,bush):
        self.name=name # это свойство публично - доступно для чтения и записи везде
        self._plant=bush # это свойство protected - доступ для класса и подклассов
    def work(self):
        self._plant.grow_all()
        print("Поработали, поухаживали..")
    def harvest(self):
        if not self._plant.all_are_ripe(): print("Не все плоды ещё созрели.")
        else:
            self._plant.give_away_all()
            print("Урожай собран!")
    @staticmethod
    def knowledge_base():
        print("Инструкция по садоводству:")
        print("Для садоводства необходимо создать сначала куст с помидорами - объект TomatoBush с количеством помидоров,")
        print("затем садовода - объект Gardener со ссылкой на объект TomatoBush. Для ухаживания за кустом используйте для")
        print("садовода метод work(), а для сбора урожая - метод harvest(). Собрать можно только созревший урожай. Продол-")
        print("жайте работать над кустом, и получите урожай.")
Gardener.knowledge_base()
tb=TomatoBush(6)
grd=Gardener("Manfred",tb)
grd.work()
grd.harvest()
grd.work()
grd.work()
grd.harvest()