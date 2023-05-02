def sub_menu(variant=0):
    """
    Task 5: Display a sub menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a suitable error should be displayed
    and the value 0 should be returned.
    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:
    '[1] Reviews for Hotel', '[2] Reviews for Dates', '[3] Reviews for Nationality,
    '[4] Reviews Summary'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Positive/Negative Pie Chart', '[2] Reviews Per Nationality Chart', '[3] Animated Summary'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] All Reviews', '[2] Reviews for Specific Hotel'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Reviews for Hotel', 2 for 'Reviews for Dates' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: 0 if invalid selection otherwise an integer for a valid selection
    """
    variant = int(input("Enter value:"))
    if variant == 0 or variant == ' ':
        print("       Error has occurred. "
              "Please choose a different option.")
        return 0
    elif variant == 1:
        sub = int(input("Please select an option from the menu:\n[1] Reviews for Hotel\n[2] Reviews for Dates\n[3] Reviews for Nationality\n[4] Reviews Summary\n"))
        return variant
    elif variant == 2:
        sub = int(input("Please select an option from the menu:\n[1] Positive/Negative Pie Chart\n[2] Reviews Per Nationality Chart\n[3] Animated Summary\n"))
        return variant
    elif variant == 3:
        sub = int(input("Please select an option from the menu:\n[1] All Reviews\n[2] Reviews for Specific Hotel\n"))
        return variant
    else:
        print("No such option! Please try again.")





sub_menu()