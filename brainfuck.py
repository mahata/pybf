#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [8 operators]
# >  : Increment the data pointer (go to the next cell).
# <  : Decrement the data pointer (go to the previous cell).
# +  : Increment the value in current cell.
# -  : Decrement the value in current cell.
# ,  : Read a character from stdin, and write it to the current cell.
# .  : Print the character in the current cell.
# [  : If the value in the current cell is greater than 0, go read the next instruction else jump to the closing “]”.
# ]  : Jump to the opening “[“.

# Hello World!
# ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.


import sys


# README: I'm making a mistake because there should be ProgramCounter and DataPointer
class BF(object):
    def __init__(self, src):
        self.__pc = 0
        self.__src = list(src)
        self.__tape = [0] * 30000
        self.__tp = 0
        self.__bracket_pairs = {}

    def gt(self):
        self.__tp = (self.__tp + 1) % 256

    def lt(self):
        self.__tp = (self.__tp - 1) % 256

    def plus(self):
        self.__tape[self.__tp] += 1

    def minus(self):
        self.__tape[self.__tp] -= 1

    def comma(self):
        c = ord(sys.stdin.read(1))
        self.__tape[self.__pc] = c

    def period(self):
        sys.stdout.write(chr(self.__tape[self.__pc]))
        sys.stdout.flush()

    def lbracket(self):
        if self.__tape[self.__tp] == 0:
            self.__pc = self.__bracket_pairs[self.__pc]

    def rbracket(self):
        # Dumb
        for key in self.__bracket_pairs:
            if self.__bracket_pairs[key] == self.__pc:
                self.__pc = key
                return

        raise Exception("Matching rbracket was not found - It should not happen.")

    # My original spec
    def semicolon(self):
        sys.exit(0)

    def parse(self):
        # What to do:
        # 1. Build matching bracket pairs
        # 2. Execute things in the tape

        # 1.
        parse_stack = []
        for idx, cell in enumerate(self.__src):
            pass
            if cell == '[':
                parse_stack.append(idx)
            elif cell == ']':
                self.__bracket_pairs[parse_stack.pop()] = idx

        # print(self.__bracket_pairs)

        # 2.
        while True:
            cell = self.__src[self.__pc]
            print(self.__pc, cell)

            if cell == '>':
                self.gt()
            elif cell == '<':
                self.lt()
            elif cell == '+':
                self.plus()
            elif cell == '-':
                self.minus()
            elif cell == ',':
                self.comma()
            elif cell == '.':
                self.period()
            elif cell == '[':
                self.lbracket()
            elif cell == ']':
                self.rbracket()
            elif cell == ';':
                self.semicolon()

            self.__pc += 1


if __name__ == "__main__":
    bf = BF("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.;")
    bf.parse()
