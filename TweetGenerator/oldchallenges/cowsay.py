import sys

'''

Run python3 cowsay.py <INSERT WHAT YOU WANT YOUR COW TO SAY>

'''


def cowsay(text):
    print(" ______________________ ")
    print("< {} >".format(text))
    print("----------------------\n")


    print(r"""
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
                    """)

cowsay(' '.join((sys.argv[1:])))