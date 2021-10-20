from tkinter import *
import ipaddress
from tkinter import filedialog
import time
import hashlib
from datetime import datetime

flag1 = 0
flag2 = 0
flag3 = 0
prev_hash = 0
x1 = 0
root = Tk()
root.title("PyBlock")
root.geometry("800x800")

label_0 = Label(root, text="Py Block", width=20, font=("helvetica", 20))
label_0.place(x=200, y=30)

label_1 = Label(root, text="Config File :", width=20, font=("helvetica", 14))
label_1.place(x=50, y=130)

entry_1 = Entry(root, width=50)
entry_1.place(x=240, y=130)


def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def Genesisblk():
    list_gen = []
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    body = hash_file("sample1.txt")
    header = {'Bid': 0, 'Timestamp': current_time, 'Previous Hash': None, 'Data Hash': body}
    curr_hash = str(header['Bid']) + header['Timestamp'] + str(header['Previous Hash']) + header['Data Hash']
    result = hashlib.sha512(curr_hash.encode())
    result = result.hexdigest()
    header['Current Hash'] = result
    Genesis_block = [header, body]
    global prev_hash
    prev_hash = result
    list_gen.append(Genesis_block)
    list_gen.append(prev_hash)
    global flag3
    flag3 = 1
    return list_gen


def Blocks(prev_hash):
    global x1
    x1 = int(x1)
    i = 0
    block_list = []
    while (i < x1):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        body = hash_file("sample1.txt")
        header = {'Bid': i + 1, 'Timestamp': current_time, 'Previous Hash': prev_hash, 'Data Hash': body}
        curr_hash = str(header['Bid']) + header['Timestamp'] + str(header['Previous Hash']) + header['Data Hash']
        result = hashlib.sha512(curr_hash.encode())
        result = result.hexdigest()
        header['Current Hash'] = result
        block = [header, body]
        block_list.append(block)
        prev_hash = result
        i += 1
    return block_list


def sync1z():
    if flag3 == 1:
        label_5 = Label(root, text=" Enter the No of nodes to be created ,\n other than Genesis Block!!!!", width=35,
                        font=("helvetica", 14), fg="red")
        label_5.place(x=420, y=500)

        entry_5 = Entry(root, width=13)
        entry_5.place(x=500, y=570)

        def ent():
            global x1
            x1 = entry_5.get()
            num = int(x1)
            newWindow = Toplevel()
            newWindow.title("Genesis Block Details")
            newWindow.geometry("750x750")

            block_list1 = Blocks(prev_hash)

            i = 0
            while (i < num):
                newWindow = Toplevel()
                newWindow.title("Block " + str(i + 1) + " Details")
                newWindow.geometry("750x750")

                Label(newWindow, text="\n\n1. Bid (Block Id):\t" + str(block_list1[i][0]['Bid']),
                      font=("helvetica", 13, "bold")).place(x=55, y=30)
                Label(newWindow, text="\n\n2. Timestamp:\t" + block_list1[i][0]['Timestamp'],
                      font=("helvetica", 13, "bold")).place(x=55, y=100)
                Label(newWindow, text="\n\n3. Previous Hash:\t" + str(block_list1[i][0]['Previous Hash']),
                      font=("helvetica", 13, "bold")).place(x=55, y=170)
                Label(newWindow, text="\n\n4. Data Hash:\t" + block_list1[i][0]['Data Hash'],
                      font=("helvetica", 13, "bold")).place(x=55, y=240)
                Label(newWindow, text="\n\n5. Current Hash:\t" + block_list1[i][0]['Current Hash'],
                      font=("helvetica", 13, "bold")).place(x=55, y=330)
                Label(newWindow, text="\n\n6. Body:\t" + str(block_list1[i][1]), font=("helvetica", 13, "bold")).place(
                    x=60, y=400)
                i += 1

        Button(root, text='Ok', bg='brown', bd=5, fg='white', font=('helvetica', 10, "bold"), command=ent).place(
            x=500, y=610)

    else:
        label_4 = Label(root, text=" First Create your Genesis Block \n then Sync all the nodes!!!!", width=25,
                        font=("helvetica", 14), fg="red")
        label_4.place(x=270, y=210)
        time.sleep(4)
        label_4.after(3000, label_4.destroy)


def nod():
    if flag1 == 1:
        racerfile = open("sample1.txt", 'r')
        global i
        racer = []

        for line in racerfile:
            racer = line.split(',')

        try:
            for i in racer:
                if ipaddress.IPv4Address(i):
                    my_list.insert(END, "{}  is connected...".format(i))
            else:
                my_list.insert(END, "{} Not connected. Invalid IP...".format(i))
        except ValueError as err:
            my_list.insert(END, "{} Not connected. Invalid IP...".format(err))

        racerfile.close()

    else:
        label_3 = Label(root, text=" First Browse then connect!!!!", width=25, font=("helvetica", 14), fg="red")
        label_3.place(x=270, y=210)
        time.sleep(4)
        label_3.after(3000, label_3.destroy)

    global flag2
    flag2 = 1


def file_open():
    filename = filedialog.askopenfilename(filetypes=(("text files", "*.txt"), ("All files", "*.*")))
    entry_1.insert(END, filename)
    global flag1
    flag1 = 1


def genesis():
    if flag2 == 1:
        Gen_blk, prev_hash = Genesisblk()

        newWindow = Toplevel()
        newWindow.title("Genesis Block Details")
        newWindow.geometry("800x800")

        Label(newWindow, text="\n\n 1. Bid (Block Id):\t" + str(Gen_blk[0]['Bid']),
              font=("helvetica", 13, "bold")).place(x=55, y=30)
        Label(newWindow, text="\n\n 2. Timestamp:\t" + Gen_blk[0]['Timestamp'], font=("helvetica", 13, "bold")).place(
            x=55, y=100)
        Label(newWindow, text="\n\n 3. Previous Hash:\t" + str(Gen_blk[0]['Previous Hash']),
              font=("helvetica", 13, "bold")).place(x=55, y=170)
        Label(newWindow, text="\n\n 4. Data Hash:\t" + Gen_blk[0]['Data Hash'], font=("helvetica", 13, "bold")).place(
            x=55, y=240)
        Label(newWindow, text="\n5. Current Hash:\t" + Gen_blk[0]['Current Hash'],
              font=("helvetica", 13, "bold")).place(x=55, y=330)
        Label(newWindow, text="\n\n 6. Body:\t" + str(Gen_blk[1]), font=("helvetica", 13, "bold")).place(x=55, y=400)

        Button(newWindow, text='Exit', bg='brown', bd=10, fg='white', font=('helvetica', 10, "bold"),
               command=newWindow.destroy).place(
            x=250,
            y=500)


    else:
        label_4 = Label(root, text="First Connect all Nodes \nand the send block!!!!", width=35, font=("helvetica", 14),
                        fg="red")
        label_4.place(x=452, y=330)
        time.sleep(4)
        label_4.after(3000, label_4.destroy)


Button(root, text='Browse', bg='brown', fg='white', bd=5, font=('helvetica', 10, "bold"), command=file_open).place(
    x=600,
    y=130)
Button(root, text='Connect', bg='brown', fg='white', bd=5, font=('helvetica', 10, "bold"), command=nod).place(x=270,
                                                                                                              y=170)

label_2 = Label(root, text=" Connected Systems/Nodes:", width=25, font=("helvetica", 14))
label_2.place(x=10, y=250)

Button(root, text='Genesis Block', bg='brown', bd=5, fg='white', font=('helvetica', 10, "bold"), command=genesis).place(
    x=450,
    y=300)

Button(root, text='Sync all ', bg='brown', fg='white', bd=5, font=('helvetica', 10, "bold"), command=sync1z).place(
    x=450,
    y=430)

my_list = Listbox(root, width=50, height=20, font=('helvetica', 10, "bold"))
my_list.place(x=25, y=300)

root.mainloop()
