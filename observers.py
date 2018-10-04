# -*-coding:Utf-8 -*

""" Observers et decorators - Reusable patterns """

class Observer:
    """
    Elements to be observed
    """
    _observers = []

    def __init__(self):
        self._observers.append(self)
        self._observables = {}


    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event():
    """
    Events launching oberved elements
    """

    def __init__(self, name, *args, autofire=True):
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
    """ Decorator for singleton classes """
    instances = {}
    def get_instance():
        if new_class not in instances:
            instances[new_class] = new_class()
        return instances[new_class]
    return get_instance


##### Following code is for testing purposes #####
class Room(Observer):

    """ Observer pattern test """

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