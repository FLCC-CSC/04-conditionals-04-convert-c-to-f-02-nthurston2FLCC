# FILE NAME - convert_C_to_F_02.py

# NAME: Nicholas Thurston
# DATE: 2/26/2026
# BRIEF DESCRIPTION: C to F Program  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    def cf_conversion():
        print('===== Temperature Converter =====')
        print('1. Convert from Celsius to Fahrenheit')
        print('2. Convert from Fahrenheit to Celsius')
        print("")

        # ask user what they would like to convert
        user_answer = int(input('Please choose from the above menu: '))
        temperature = float(input('Enter a temperature to convert: '))
        print("")

        if user_answer == 1:
          # Logic for option 1
          ## fahrenheit conversion
          to_fahrenheit_conversion = temperature * 9/5 + 32
          print(temperature,'degrees Celsius is',to_fahrenheit_conversion,'degrees Fahrenheit')
        elif user_answer == 2:
          # Logic for option 2
          ## celsius conversion
          to_celsius_conversion = (temperature - 32) * 5/9
          print(temperature,'degrees Fahrenheit is',to_celsius_conversion,'degrees Celsius.')
        else:
           print("Invalid input.")
          
    cf_conversion()
main()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

Sometimes it's best to break down the logic of the code piece by piece and then put it into the final program once it's been tested and is working.





'''
