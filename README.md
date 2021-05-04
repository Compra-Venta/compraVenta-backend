# Compra-Venta

A Virtual Crypto Currency Trading Platform (backend)


 **Compra Venta is live at** https://compraventalive.herokuapp.com/ 
***
# Motivation

Our project is a website based on a virtual trading platform which will provide
budding investors a platform to dive into the trading of cryptocurrencies without
having any fear of losing anything.
***
# Features
* **User authentication**- Each user will be provided its own username and
password and details of the user will be stored in the database along with its
activities.
* **Virtual Trading**- Each user will be provided with some virtual money with
the help of which a user can trade into the choice of his own cryptocurrency
which will help a user well versed with cryptocurrency trading gradually.
* **Real-time price updation**- The actual price of each cryptocurrency will be
updated regularly without a long delay with the help of API’s.
* **Price Prediction of Cryptocurrency**- With the help of machine learning
model, we will be able to predict the price of cryptocurrency and trends in the
market.
* **Latest News**- Related news regarding cryptocurrencies and cryptocurrency
trading is refreshed on our platform in order to make users familiar with the
environment.
* **User Support**- If users need some assistance/clarification regarding
cryptocurrency trading, the model will help them accordingly.
* **Learn** - If users are not familiar about cryptotrading and other features
or want to furnish their knowledge, we have a provided a platform to learn
***
# Backend Endpoints
* **’/register** ``` GET ```-  This api is used to register a new user along with the user's details in the form of a document in a collection of the User's database and does not allows same user to register twice, thus reducing redundancy.
```
{
	“message”: “registered successfully”
}
```
* **’/login'** ``` POST ```-  This api is used to help users to login into the website by matching
the credentials entered by the user with the information present in the database and in return sends jwt token.

```
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjIwMTIwNTI1LCJqdGkiOiIwNGU4NGQ0My0zMjlmLTRlYzMtODIzOC03MzAzYzFjMjkyMjUiLCJuYmYiOjE2MjAxMjA1MjUsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiJrYXJhbnN0YXIyMzk3QGdtYWlsLmNvbSIsImV4cCI6MTYyMDEyNDEyNX0.I-xvXj81i9WXW6eBcF3nroHLf4eCtVuuSY6FpZNBYyI",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMDEyMDUyNSwianRpIjoiNjJiNTZhOGMtNjc1Mi00OTVkLTgyNmEtMzFlNjNlZDM1ZGU3IiwibmJmIjoxNjIwMTIwNTI1LCJ0eXBlIjoicmVmcmVzaCIsInN1YiI6ImthcmFuc3RhcjIzOTdAZ21haWwuY29tIiwiZXhwIjoxNjIyNzEyNTI1fQ.krd2aNnphJDnVdp0jWdg4WopVvrqlho3q07Hm76ng-E"
}

```
* **’/myprofile'** ``` GET ```-   This api helps a user to view it's own profile. User can also check its current rating in the virtual trading platform to analyse themselves.

```
{
    "user_id": "6091132cfdbf4ca0c1d61305",
    "email": "karanstar2397@gmail.com",
    "name": "Jaskaran Singh",
    "age": 20,
    "country": "India",
    "PhoneNo": "9646411782"
}

```
* **’/reauth'** ``` GET ```-  This api is used to send access token whenever it tends to
expire by using the refresh token which ensures that a user don't have to login again and again and thereby ensuring.

```
{
    "user_id": "6091132cfdbf4ca0c1d61305",
    "email": "karanstar2397@gmail.com",
    "name": "Jaskaran Singh",
    "age": 20,
    "country": "India",
    "PhoneNo": "9646411782"
}

```
* **’/password/change'** ``` POST ```-  This api provides the facility of changing password 
at his/her own convenience.

```
{
    "message": "Password changed successfully."
}

```
* **’/password/get_new'** ``` PUT ```-  In case a user forgests his /her own password ,this
api comes in the picture with a rescue operation. It send user a random password at his/her mail with the help of which user can login into the website and can later update the password at its own convenience.


```
{
    "message": "Password Changed"
}

```
* **’/watchlist'** ``` GET ```-  This api is used to retrieve all the coin pairs from the databse<br />
regarding which a person to have a close look at to analyse its trend carefully.

```
{
    "watchlist": []
}

```
* **’/watchlist/<string:symbol>'** ``` POST ```-  This api is used to add a symbol pair
into the watchlist for careful analysis of that coin pair.

```
{
    "message": "symbol added to watchlist"
}

```
* **’/watchlist/<string:symbol>'** ``` DEL ```-  This api is used to remove a symbol
pair from the watchlist database in case a user does not wishes to track that coin pair.

```
{
    "message": "symbol removed from watchlist"
}

```
* **’/wallet'** ``` GET ```-  This api is used to show the wallet of the logged in user from the database which contains all the information regardng the amount of coin a user has of a all the currencies available

```
{
    "email": "karanstar2397@gmail.com",
    "profit": 50000.0,
    "balance": {
        "BTC": 0.0,
        "ETH": 0.0,
        "LTC": 0.0,
        "XRP": 0.0,
        "BNB": 0.0,
        "USDT": 50000.0
    },
    "fixed_balance": {
        "BTC": 0.0,
        "ETH": 0.0,
        "LTC": 0.0,
        "XRP": 0.0,
        "BNB": 0.0,
        "USDT": 0.0
    }
}

```
* **’/wallet/<string:coin>'** ``` GET ```-  This api is used to show the amount of coin of a
particular currency in which user is interested in.
```
{
    "coin": "BTC",
    "balance": 0.0,
    "fixed_balance": 0.0
}

```
* **’/order/market'** ``` POST ```-  This api is used to place a market order of a particular coin pair and checks the feasibility of the transaction from the wallet of the user and stores the information regarding transaction in the database 

```
{
    "status": "successful",
    "order_id": "fa45bf8ffc1f4e01915f1620123173karanstar2397@gmail"
}

```
* **’/transactions/closed'** ``` GET ```-  This api is used to retrieve all the market order
transactions that user has placed from the database.

```
{
    "closed": [
        {
            "order_id": "fa45bf8ffc1f4e01915f1620123173karanstar2397@gmail",
            "base": "BTC",
            "quote": "USDT",
            "b_amount": 0.5,
            "price": 56403.82,
            "date": "2021-04-17",
            "time": "16:34:15",
            "order_type": "M",
            "side": "BUY"
        }
    ]
}

```
* **’/transactions/closed/<string:coin>'** ``` GET ```-  This api is used to get all the transactions of the logged in user of a particular currency in which user might be interested in.
```
{
    "closed": [
        {
            "order_id": "fa45bf8ffc1f4e01915f1620123173karanstar2397@gmail",
            "base": "BTC",
            "quote": "USDT",
            "b_amount": 0.5,
            "price": 56403.82,
            "date": "2021-04-17",
            "time": "16:34:15",
            "order_type": "M",
            "side": "BUY"
        }
    ]
}

```
* **’/order/stoploss'** ``` POST ```- This api is used to place a stoploss order of a particular coin
pair and will place the transaction in stoploss database till the transaction hasn't happened. Once the price of a currency hits the desired price then the transaction is deleted from the open transaction database and the transaction details will  then be placed in closed transaction database.<

```
{
    "status": "successful",
    "order_id": "12d59aa787c848f5b6ea1620123546karanstar2397@gmail"
}

```
* **’/transactions/open'** ``` GET ```-  This api is used to retrieve all the stoploss order
transactions that user has placed from the database.

```
{
    "open": [
        {
            "order_id": "12d59aa787c848f5b6ea1620123546karanstar2397@gmail",
            "base": "BTC",
            "quote": "USDT",
            "b_amount": 0.01,
            "price": 54268.0,
            "date": "2021-04-17",
            "time": "15:48:15",
            "order_type": "TP",
            "side": "BUY"
        }
    ]
}

```
* **’/order/stoploss'** ``` DEL ```-  This api is used to delete a stoploss order.
```
{
    "status": "successful",
    "message": "Stoploss order with order id 12d59aa787c848f5b6ea1620123546karanstar2397@gmail cancelled."
}

```
* **’/reset'** ``` PUT ```-  This api is used to reset a user's account.
```
{
    "msg": "Account reset successful"
}
```
* **’/predict'** ``` GET ```-  This api is used to predict the price of entered base currency in terms of entered quote currency.
```
{
    "prediction": 56340.60385972957
}
```
* **’/logout'** ``` GET ```-  This api is used to revoke access token and logout the current user.
```
{
    "msg": "Access token revoked"
}
```


***
# External API Reference
### **CandleStick Historical Data**
```
     https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}
            
```
***   
# Web Sockets
 * **Market Trades**- wss://stream.binance.com:9443/ws/{symbol}@trade

 * **WatchList**-wss://stream.binance.com:9443/ws/!miniTicker@arr

***

# Tech/Framework Used
<a href="https://flask-restful.readthedocs.io/en/latest//"><img src="https://https://www.pngitem.com/pimgs/m/206-2066888_flask-restful-hd-png-download.png"/></a> &nbsp;<a href="https://pymongo.readthedocs.io/en/stable/tutorial.html"> <img src="https://1000logos.net/wp-content/uploads/2020/08/MongoDB-Emblem.jpg></a>
 ### Other Technologies Used 
  * [Pymongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)
  * [Postman](https://www.postman.com/)

***
# Databases
<a href="https://docs.mongodb.com/"><img src="https://webassets.mongodb.com/_com_assets/cms/MongoDB_Logo_FullColorBlack_RGB-4td3yuxzjs.png"/></a> &nbsp;<a href="https://redislabs.com/lp/python-redis/"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQfY4oW9fnv3DmNiKU7DXeaSKgeyUYboJtCl178P9NlnnXnVINrhjJxtLp9-YDuODRuA0&usqp=CAU></a>

***

# Contributors
* [**Daksh Verma** ](https://github.com/dakshverma2411/ "Connect on Github")
* [**Jaskaran Singh** ](https://github.com/jaskaran-23 "Connect on Github")
* [**Tanveer Sodhi** ](https://github.com/TanveerSodhi "Connect on Github")
* [**Aseem Mangla** ](https://github.com/manglaaseem28 "Connect on Github")





