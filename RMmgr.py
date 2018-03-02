import ui
import saleItem
import items
import dicts
import datetime
import theDB



def main(MC):

    while MC == True:
        main_choice = ui.show_main_menu()
        if main_choice == '1':
            RM = True
            MC = False
            while RM == True:
                RM_choice = ui.start_RM_program()
                if RM_choice == '1':
                    ui.add_a_sale()
                elif RM_choice =='2':
                    ui.message('you chose 2')
                elif RM_choice =='3':
                    ui.message('you chose 3')
                elif RM_choice =='4':
                    ui.add_edit_items()
                elif RM_choice == '5':
                    RM = False
                    MC = True
                    main(MC)
                    return MC
        elif main_choice == '2':
            print('main choice 2')
        elif main_choice == '3':
            print('main choice 3')
        elif main_choice == '4':
            print('main choice 4')
        elif main_choice == '5':
            print('main choice 5')
        elif main_choice == 'q':
            print('Bye Felicia')
            quit()



if __name__== main(MC=True):
    # MC=True
    main(MC)
    theDB.main()
