from classes.ninja import Ninja, ZombieNinja
from classes.pirate import Pirate, RumPirate

michelangelo = Ninja("Michelanglo")
donatello = ZombieNinja("Donatello")


jack_sparrow = RumPirate("Jack Sparrow")
bootstrap_bill = Pirate("Bootstrap Bill")


michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats().taunt(michelangelo)
donatello.bite(jack_sparrow)
jack_sparrow.alcoholism().gassy(donatello).show_stats()
bootstrap_bill.attack(donatello).show_stats()
