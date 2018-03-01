import datetime
import os
import time


def create_spec_file():
    """
        Simple test to write a basic .signalling file who can be read by MSC Generator application.
        return:: Sources\Python\MSCGeneretor\msc_files\test.signalling
    """
    current_time = time.strftime("%H:%M:%S")
    file_name = str(current_time) + '.signalling'
    with open(os.path.join('../msc_files/test.signalling'), 'w+') as file:
        file.write("msc { ")
        file.write('A, B, C, D;')
        file.write('|||;')
        file.writelines(
            ['A box A [label="box"],', 'A box A [label="box"],', 'C abox C [label="abox"],', 'D note D [label="note"];',
             ' A abox B [label="abox", textbgcolour="#ff7f7f"];'])
        file.writelines(
            ['B rbox C [label="rbox", textbgcolour="#7fff7f"];', 'C note D [label="note", textbgcolour="#7f7fff"]; }'])


if __name__ == "__main__":
    print('start parsing...')
    create_spec_file()
