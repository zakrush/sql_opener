import checker.searcher as search
from exploit.exploiting import manual_exploit

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
0. Exit
'''
seacher_menu = '''
1. One host
2. Mass check
'''
print('\n' + menu + '\n')
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
    manual_exploit(input("Enter host: "))
else:
    print('Enter correct option')
    exit()
