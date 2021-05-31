print('__file__={0:<35} |\n __name__={1:<20} |\n __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import RandomPeopleAssigner.random.cycle as cycle


U = cycle.PermutationAleatoire(12)
print(U)
