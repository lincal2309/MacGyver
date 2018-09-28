# -*-coding:Utf-8 -*

""" Observateurs et décorateurs - Classes et fonctions génériques réutilisables """

class Observer:
    """
    Classe destinée à définir les modalités d'observation des évènements
    """
    _observers = []

    def __init__(self):
        self._observers.append(self)
        self._observables = {}


    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event():
    """
    Liste des évènements observables
    """

    def __init__(self, name, *args, autofire = True):
        self.name = name
        self.arg = args
        if autofire:
            self.fire()

    def fire(self):
        print(self.arg)
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](*self.arg)

def singleton(new_class):
    """ Décorateur destiné à gérer les classes Singleton """
    instances = {}
    def get_instance():
        if new_class not in instances:
            instances[new_class] = new_class()
        return instances[new_class]
    return get_instance


##### La suite du code est uniquement destinée aux tests #####
class Room(Observer):

    """ Test de l'observation d'un évènement"""

    def __init__(self):
        Observer.__init__(self) # Observer's init needs to be called
        print("La chambre est prête.")

    def someone_arrived(self, who, place):
        print(who, "est arrivé à", place, "!")


def main():
    room = Room()
    room.observe("someone arrived",  room.someone_arrived)

    Event("someone arrived", "Tof", "Toulouse")



if __name__ == "__main__":
    main()