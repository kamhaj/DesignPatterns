'''

define a 'one-to-many' relationship between objects

when the state of one object changes, the rest are notified.
(like notification from YouTube when you subscrib to a channel)

'''

""" Example: Dashboard for a tech support center.

Key Performance Indicators (KPIs):
    - Open Tickets/Issues
    - New Tickets in last hour
    - Closed Tickets in last hour


Dashboard is the Observer (few observers possible). Observers are interested in any change in a Subject
KPI source is a Publisher/Subject.

Bug warning: dangling reference (it can stop garbage collector). 
Solution: add __enter__ and __exit__ methods to AbsObserver and AbsSubject classes (abstract observer classes) 
so it can detach itself. Use 'with' statements with context managers. 
These 2 functions are required to turn a class definition into a context manager.
"""

from kpis import KPIs
from current_kpis import CurrentKPIs
from forecast_kpis import ForecastKPIs


''' USING CONTEXT MANAGERS '''

with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(25, 10, 5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

print('\n***Exited context managers.***\n\n')
kpis.set_kpis(150, 110, 120) # this will not display anything, no subscribers left





''' WITHOUT CONTEXT MANAGERS

## Report on current KPI values
# instanciate KPIs
kpis = KPIs()

# instanciate 2 observers
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)

# set different set of ticket amount values
kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)

print('\n***Detaching the current KPIs observer.***\n\n')
kpis.detach(currentKPIs)
kpis.set_kpis(150, 110, 120)
'''