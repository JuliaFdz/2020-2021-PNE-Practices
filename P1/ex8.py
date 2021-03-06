from Seq1 import test_sequence

def print_result(i, sequence):
    print('Sequence ' + str(1) + ': (Length ' + str(sequence.len()) + ' ) ' + str(sequence))
    print('Bases:', sequence.count())
    print('Rev:', sequence.reverse())
    print('Comp: ', sequence.complement())

print('-----| Practice 1, Exercise 8 |------')
#  for future knowledge
list_sequences = list(test_sequence())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])
    print()