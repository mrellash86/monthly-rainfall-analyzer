#***************************************************************
#
#  Developer:    Ell Ash
#
#  Program :    Montly Rainfall Statistics
#     
#  Due Date:     13APR2025
#
#  Description: This program reads monthly rainfall data from a file,
#               calculates total and average rainfall, and identifies
#               months with the lowest and highest rainfall amounts.
# #############################################################################
def developerInfo():
    """
    Displays the developer's information.
    This function must be copied exactly from Program1.
    """
    print("Name:    Ell Ash")
    print("Course:  Programming Fundamentals I")
    print("Program: 7")
    print()   
# ==============================================================================
#                              READ RAINFALL DATA
# ==============================================================================
def read_rainfall_data(filename):
   
    rainfall_list = []
    try:
        with open(filename, 'r') as infile: 
            for line in infile: 
                try:
                    
                    rainfall = float(line.strip()) 
                    rainfall_list.append(rainfall) 
                except ValueError:
                    print(f"Error: Invalid data found in {filename}. Skipping line: {line.strip()}")
            
            if len(rainfall_list) != 12: 
                 print(f"Warning: Expected 12 months of data, but found {len(rainfall_list)} in {filename}.")
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        return []
    except IOError:
        print(f"Error: Could not read from file '{filename}'.")
        return []

    return rainfall_list 
# ==============================================================================
#                              CALCULATE TOTAL
# ==============================================================================
def calculate_total(rainfall_list):
   
    total = 0.0
    for amount in rainfall_list: 
        total += amount         
    return total
# ==============================================================================
#                              CALCULATE AVERAGE
# ==============================================================================
def calculate_average(rainfall_list):
   
    list_length = len(rainfall_list)
    if list_length == 0:
        return 0.0

    total = calculate_total(rainfall_list) 
    average = total / list_length 
    return average

# ==============================================================================
#                          FIND MIN/MAX MONTHS
# ==============================================================================
def find_min_max_months(rainfall_list, month_names):
    
    if not rainfall_list:
        return [], []

    min_rainfall = min(rainfall_list) 
    max_rainfall = max(rainfall_list) 

    min_months = [] 
    max_months = [] 

    
    for i in range(len(rainfall_list)): 
        if rainfall_list[i] == min_rainfall: 
            min_months.append(month_names[i]) 

        if rainfall_list[i] == max_rainfall: 
            max_months.append(month_names[i]) 
    return min_months, max_months
# ==============================================================================
#                              DISPLAY RESULTS
# ==============================================================================
def display_results(total, average, min_months_list, max_months_list):
    print("\n--- Rainfall Statistics ---")
    print(f"Total yearly rainfall: {total:.1f}") 
    print(f"Average monthly rainfall: {average:.1f}") 

    min_months_str = ", ".join(min_months_list) 
    max_months_str = ", ".join(max_months_list) 

    print(f"Month(s) with the lowest rainfall: {min_months_str}") 
    print(f"Month(s) with the highest rainfall: {max_months_str}") 
    print("---------------------------")
# ==============================================================================

#***************************************************************
#
#  Function:     main
# 
#  Description:  Returns none
#
#  Parameters:   none
#
#
#  Returns:     None
#
#
#
#**************************************************************
# ==============================================================================
#                                 MAIN FUNCTION
# ==============================================================================
def main():
 
    
    developerInfo() 

    
    INPUT_FILENAME = "Program7.txt" 
    MONTH_NAMES = [ 
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]


    rainfall_data = read_rainfall_data(INPUT_FILENAME) 

    
    if rainfall_data:
       
        total_rainfall = calculate_total(rainfall_data) 

        average_rainfall = calculate_average(rainfall_data) 

    
        min_months, max_months = find_min_max_months(rainfall_data, MONTH_NAMES) 

       
        display_results(total_rainfall, average_rainfall, min_months, max_months) 
    else:
        print("\nProgram cannot proceed due to errors reading the input file.") 

# ==============================================================================
#                          CALL MAIN & RUN PROGRAM
# ==============================================================================
if __name__ == "__main__": 
    main()

