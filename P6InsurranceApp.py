"""The following is an example of the object-oriented concept called polymorphism
Different types of Policy objects are added to a list.
The for loop iterates through the list and calculates the premium and displays the object.
The question is....which calculatePremium method is called? The one in the LifePolicy class
or the one in the AutomobilePolicy class?
Also....
Since the print statement has an object inside parenthesis the __str__ method is called.
The question is which __str__ method is called?
...the one in the Policy class or the LifePolicy class or the AutomobilePolicy class?
The list maintains the TYPE of object that is in the list so it examines the
type of object and executes that class's calculatePremium method and __str__ method...cool, huh?"""

from AutomobilePolicy import AutomobilePolicy
from LifePolicy import LifePolicy
from Policy import Policy
policies = [ ]
life = LifePolicy("32115","10-20-20018","Jane Doe","3422 Howard Ave. Dallas Mo",200,65,"True",5)
auto = AutomobilePolicy("32145","10-22-20018","Thomas Smith","3422 Main Columbia Mo",100,2,1,"High")
policies.append(life)
policies.append(auto)
for i in range(len(policies)):
    policies[i].calculatePremium()
    print (policies[i])
