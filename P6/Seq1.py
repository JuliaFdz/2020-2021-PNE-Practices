import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases=NULL_SEQUENCE):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print('Null seq created')
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence_2(strbases):
                print('New seq has been created')
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INCORRECT seq detected')



    def print_bases(self):
        print(self.strbases)

    @staticmethod
    def is_valid_sequence(bases):
        for c in bases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def is_valid_sequence_2(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True
    @staticmethod
    def print_seq(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequences'+ str(i) +':(length:' +  str(list_sequences[i].len()) + ')' + str(list_sequences[i])
            termcolor.cprint(text,'yellow')



    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """ Calculate the length of the sequence """
        if self.strbases == Seq.NULL_SEQUENCE:
            return 0
        else:
            return len(self.strbases)


    def count_bases(self): #null seq does not work
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
              return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, t, g, = self.count_bases()
        return {'A': a, 'C' : c, 'G': g, 'T' : t }

    def count_base_1(self, base):
        return self.strbases.count(base)

    def seq_complement(self):
        comp_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
        string = ""
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            for base in self.strbases:
                base = comp_dict[base]
                string += base
            return string

    def seq_reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'Null'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'Invalid Sequence' #Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]


    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ''
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif ch == "T":
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find('\n') + 1:].replace('\n', '')

    def seq_read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())
        return self.strbases
        # return take_out_first_line(Path(filename).read_text())

    def most_frq_base(self):
        frq_base = ''
        gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for d in self.strbases:
            gene_dict[d] += 1
        for n in gene_dict.keys():
            if gene_dict[n] == max(gene_dict.values()):
                frq_base += n + ' '
        return frq_base

    @staticmethod
    def processing(gene_dict):
        list_values = gene_dict.values()
        most_common_base = max(list_values)
        for base, n in gene_dict.items():
            if n == most_common_base:
                return base, n



def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number): # sequences as number chosen
        list_seq.append(Seq(pattern * (i + 1))) # i = 0 -> A // i = 1 -> AA
    return list_seq



def test_sequence():
    s1 = Seq()
    s2 = Seq('ACTG')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3

# tuple of 3 things -> list-> able to be iterate