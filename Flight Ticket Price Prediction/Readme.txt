#Flight Ticket Price Prediction

###Flight ticket prices can be something hard to guess, today we might see a price, check out the price of the same flight tomorrow, it will be a different story. We might have often heard travellers saying that flight ticket prices are so unpredictable.
###And it is a Simple project to predict the price of the flight ticket based on the city

##Data Overview
Here each data point corresponds to trip of flight from one city to another.

- Airline: The name of the airline.

- Date_of_Journey: The date of the journey

- Source: The source from which the service begins.

- Destination: The destination where the service ends.

- Route: The route taken by the flight to reach the destination.

- Dep_Time: The time when the journey starts from the source.

- Arrival_Time: Time of arrival at the destination.

- Duration: Total duration of the flight.

- Total_Stops: Total stops between the source and destination.

- Additional_Info: Additional information about the flight

- Price(target): The price of the ticket

##Table of Content

* __Step 1: Importing the Relevant Libraries__
    
* __Step 2: Data Inspection__
    
* __Step 3: Data Cleaning__
    
* __Step 4: Exploratory Data Analysis__
    
* __Step 5: Building Model__


##Performace Metric
- Since it is an regression problem we will use Root Mean Squared error (RMSE) and R-squared as regression metric.

##Final Output : The RMSE is 0.244 and R-SQUARED is 0.77% 

