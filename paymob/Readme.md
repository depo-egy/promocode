# Promocode Redeem


## Description:
This project is implementing rest api to make a promo code redemption.


## Assumptions:
<ol>
<li>One promocode per tranaction</li>
<li>In suggest working on trasportation companies like uber or swvl , however it is applicable to anysystem</li>
<li>promocode table has a one to many relationship with promo_history</li>
<li>I have added a client table </li>
<li>The endpoint will be used by a frontend client (web or mobile app)</li>
<li>We are talking about promocodes generated today</li>
<li>I Completed transaction table as I thought</li>
<li>I understood the Promo_code.quantity as the max number of usage of the promocode , while freq_of_use as how many it is used until a current moment</li>
</ol>

## EndPoint:
Method Get : Retreive all the data of the promocode with the promocode value

## Use Case Example:
In Transaction table: 
If we have a ride for (amount) 50 dollars. And you have a promo code for 10 dollars. Ride charge should
be (billed_amount) 40 dollars


## Testing:
I did not consider test coverage , just I showed my skills by testing one table


## Disclaimer:
My solution contain all points in the task
Due to time I did not do what i first intended to do , I planned to design more than one api for many purposes.
for example: <br>
            METHOD POST : Request BODY JSON {user_email, promocode (promo_codes.code), transaction_id} and what happens if the api response is not 200 due to expiration for example