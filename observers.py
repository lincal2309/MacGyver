# -*-coding:Utf-8 -*

""" Observateurs pour modifier l'affichage selon la position du personnage"""

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