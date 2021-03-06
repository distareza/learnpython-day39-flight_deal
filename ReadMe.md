### 1. Make Your Own Copy of the Starting Google Sheet  
Make a copy of the Google sheet. ( https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing )
File Name : Flight Deals


#### APIs Required
* Google Sheet Data Management - https://sheety.co/

* Kiwi Partners Flight Search API (Free Signup, No Requires Credit Card Details) - https://partners.kiwi.com/

* Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

* Twilio SMS API - https://www.twilio.com/docs/sms

#### Objective:
1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

    https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports

2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

4. The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.


#### Connect sheety.co api your google account
1. Make a copy of Google Sheet ( https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing ) and Name it with : "Flight Deals"  
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.01.png?raw=true)
2. Open https://sheety.co/ and connect to your google account (https://dashboard.sheety.co/)
3. Click New Project > From Google Sheet
4. Paste the Google Sheet url that you created earlier   
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.02.png?raw=true)
5. Click Create Project
6. Enable the PUT option so that you can write to your Google sheet
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.03.png?raw=true)


### Register with the Kiwi Partners Flight Search API 
1. Open https://partners.kiwi.com/ click Register an account https://tequila.kiwi.com/portal/login/register 
2. Select Personal Account
3. Enter Detail (like name, birth and email)
4. open your mail and enter verification link that they send via mail
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.04.png?raw=true)
5. follow the instruction to activate the user account
6. Login to your account ( https://tequila.kiwi.com/ )
7. Create a solution
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.05.png?raw=true)
8. Select "Meta Search API integration"
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.06.png?raw=true)
9. Choose "One-Way and Return"
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.07.png?raw=true)
10. Enter Solution Name "myflightsearch"
    ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.08.png?raw=true)
11. Click Create button
12. Get API Key
    ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-01.10.png?raw=true)


Solution Code : 
https://gist.github.com/angelabauer/99301f807578ad8b6f54e8fb8ec7162b


### Step 2 - Create the Customer Acquisition Code
In order for other users to access our customer acquisition program, we're going to use repl.it to host our code and share the link to the console with our users.  

Objectives 
1. Create a new Repl.it project.  https://repl.it/
2. Create a new Sheet (Tab) in your Copy of Flight Deals Google Sheet:  
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-02.01.png?raw=true)
3. Add 3 new column headings - "First Name", "Last Name", "Email" to this new user Sheet:
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-02.02.png?raw=true)
4. Sync the new sheet in Sheety. Note: you might have to log in again to Sheety, also you'll need to re-check the PUT checkbox in the prices endpoint.  
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-02.03.png?raw=true)
5. Enable the POST method in the users endpoint:  
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-02.04.png?raw=true)
6. Code up the Repl.it project so that it asks the user for their first name, last name and email. Make sure to get them to type their email twice for validation. If the two emails match, then tell them that they're in the club. e.g.  
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-02.05.png?raw=true)
7. Use the Sheety API to POST the data that the user enters into the user sheet in your Copy of Flight Deals Google Sheet.
   This is what you're aiming for:  
   ![alt text](https://github.com/distareza/learnpython-day39-flight_deal/blob/master/resources/step-02.06.gif?raw=true)

