from observer.observer_abc import AbsObserver

class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis): #takes reference to a Subject in a constructor
        self._kpis = kpis
        kpis.attach(self)

    ## retrieve values from Subject's properties 
    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    ## display results
    def display(self):
        print(f'Curent open tickets: {self.open_tickets}')
        print(f'New tickets in last hour: {self.new_tickets}')
        print(f'Tickets closed in last hour: {self.closed_tickets}')
        print('*****\n')

    # Python ensures it will run when the context ends
    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)