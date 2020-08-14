import checker.searcher as search
from exploit.exploiting import Explotation
import colorama

colorama.init(autoreset=True)

logo = "\033[0;35m" + r'''
  ____   ___  _        ___  ____  _____ _   _ _____ ____  
 / ___| / _ \| |      / _ \|  _ \| ____| \ | | ____|  _ \ 
 \___ \| | | | |     | | | | |_) |  _| |  \| |  _| | |_) |
  ___) | |_| | |___  | |_| |  __/| |___| |\  | |___|  _ < 
 |____/ \__\_\_____|  \___/|_|   |_____|_| \_|_____|_| \_\
'''
print(logo)

menu = '''
1. SQL check
2. Enter payload
3. Auto extract
0. Exit
'''
seacher_menu = '''
1. One host
2. Mass check
'''
extractor_menu = '''
1. Count columns
2. Database name
3. Tables
4. Columns
5. Data
0. Exit
'''
print('\n' + menu + '\n')
try:
    main_option = input("Select option: ")

    if main_option == '0':
        exit()
    elif main_option == '1':
        print('\n' + seacher_menu + '\n')
        opt_srch = input("Select option: ")
        if opt_srch == "1":
            search.search_vuln(input("Enter url: "))
        elif opt_srch == "2":
            search.mass_search(input("Enter the path to the file with the URLs: "))

    elif main_option == "2":
        expl = Explotation(input("Enter host: ")).manual_exploit()

    # Auto extract
    elif main_option == "3":
        site = input('Enter host: ')
        print(extractor_menu)

        while True:
            extr_option = input("Select option: ")
            if extr_option == "0":
                exit()
            elif extr_option == "1":
                Explotation(site).print_columns()
            elif extr_option == "2":
                Explotation(site).database_extractor()
    else:
        print('Enter correct option')
        exit()
except EOFError:
    print("User ended the work")
except KeyboardInterrupt:
    print("\nTerminal ended the work")
