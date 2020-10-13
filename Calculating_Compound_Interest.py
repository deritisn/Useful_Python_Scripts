#estimated Yearly Interest

def yearly_interest():
    print('How many years will you be saving?')
    years = int(input('Enter the number of years: '))

    print('How much money is currently in your account?')
    principal = float(input('Enter the current amount in your account: '))

    print('How much money do you plan to invest monthly?')
    monthly_invest = float(input('Enter amount: '))

    print('What do you estimate will be the yearly interest of this investment?')
    interest = float(input('Enter the interest in a decimal number: (10% = 0.1): '))

    print(' ')

    monthly_invest = monthly_invest * 12
    final_amount = 0

    for i in range(0, years):
        if final_amount == 0:
            final_amount = principal

        final_amount = (final_amount + monthly_invest) * (1 + interest)

    print('You will have saved {} after {} years.'.format(str(round(final_amount,2)), years))

yearly_interest()
