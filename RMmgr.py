import ui
import saleItem
import items
import lists
import datetime
import theDB



def main():

    main_choice = ui.show_main_menu()
    if main_choice == '1':
        RM_choice = ui.start_RM_program()
        if RM_choice == '1':
            ui.message('you chose 1')
        elif RM_choice =='2':
            ui.message('you chose 2')
        elif RM_choice =='3':
            ui.message('you chose 3')
        elif RM_choice =='4':
            ui.add_items()
            main()
        elif RM_choice == '5':
            main()




if __name__== main():
    main()
    theDB.main()
