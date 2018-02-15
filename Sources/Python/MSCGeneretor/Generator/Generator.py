
import datetime
import os
import time

def create_spec_file():

    current_time = time.strftime("%H:%M:%S")
    print('current time :'+current_time)
    file_name = str(current_time) + '.signalling'
    print('************ file name ************')
    print(file_name)
    with open(os.path.join('../msc_files/test.signalling'),'w+') as file:
        file.write("msc { ")
        file.write('A, B, C, D;')
        file.write('|||;')
        file.writelines(['A box A [label="box"],','A box A [label="box"],','C abox C [label="abox"],','D note D [label="note"];',' A abox B [label="abox", textbgcolour="#ff7f7f"];'])
        file.writelines(['B rbox C [label="rbox", textbgcolour="#7fff7f"];','C note D [label="note", textbgcolour="#7f7fff"]; }'])

if __name__ == "__main__":
    print('start parsing...')
    create_spec_file()

