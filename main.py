from app import Property

property = Property()

def main_info():

    print("\n>   >  >  >>     Rental Property ROI CALCULATOR     <<  <  <   <\n")
    print('')

    while True:
        input("\nAre you ready to start your Rental Property Return On Investiment Calculation? yes or no > ").lower()
        if input == 'no':
            print(">  >>   Thank you for checking it out!  <<  <")
            break
        else:
            print("\n Please use whole numbers rounded up.\n\tLet's get started!\n")
            print("\n- - - -  Property's Monthly Income  - - - -\n")
            property.income_user()

            print("\n- - - -  Property's Monthly Expenses  - - - -\n")
            property.expenses_user()
            
            print("\n- - - -  Property's Monthly Cash Flow  - - - -\n")
            property.cash_flow_user()
            
            print("\n- - - - -  Total Investment  - - - - -\n")
            property.investment_user()

            print("\n- - - -   Cash on Cash Return On Investment   - - - -\n")
            property.coc_roi_user()
            print('\n- - - - - - - - - - - - - - - - - - - - - - - - - - - \n')
            print('\n\n> > >>   H a p p y   I n v e s t m e n t s  !   << < <\n\n')
            break
            

# if __name__ == "__main__":
main_info()