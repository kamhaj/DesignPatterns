from observer.subject_abc import AbsSubject

class KPIs(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickers = -1

    @property
    def open_tickets(self):
        return self._open_tickets
    
    @property
    def closed_tickets(self):
        return self._closed_tickets   
    
    @property
    def new_tickets(self):
        return self._new_tickers

    ## set attributes to new values and notify 
    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickers = new_tickets
        self.notify()
    