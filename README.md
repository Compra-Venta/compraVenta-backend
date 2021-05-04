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
* **’/logout'** ``` POST ```-  This api is used to revoke access token and logout the current user.
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
<a href="https://flask-restful.readthedocs.io/en/latest//"><img src="https://https://www.pngitem.com/pimgs/m/206-2066888_flask-restful-hd-png-download.png"/></a> &nbsp;
<a href="https://pymongo.readthedocs.io/en/stable/tutorial.html"><img src="https://1000logos.net/wp-content/uploads/2020/08/MongoDB-Emblem.jpg"/></a>
 ### Other Technologies Used 
  * [Pymongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)
  * [Postman](https://www.postman.com/)

***
# Databases
<a href="https://docs.mongodb.com/"><img src="https://webassets.mongodb.com/_com_assets/cms/MongoDB_Logo_FullColorBlack_RGB-4td3yuxzjs.png"/></a> &nbsp;
<a href="https://redislabs.com/lp/python-redis/"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcYAAABvCAMAAABB2JCJAAABC1BMVEX///+jJCLcOCxJTE1FSEk+QUJAREVDRkesJySgIyE2OjubnZ2wsbE6PT89QEHKy8vDw8R0ERPa29twcnPl5uZOUVJXWlv09PTh4uLXNivatragFhPy8vK3uLiqq6vbMiV1d3d+gIDMjo6LjY3bLR+fCAHIMSjRNCqxKSS8LSbHyMhhY2SLGRgvMzWTlJVcX2DaJhXldG387Ovyvrv53dviX1baHADeQjf1z83top7pi4bhWlDvran65+bkaWHrlI/fTUSpMzEmKyzp0NCuREPoh4L0xcLuq6fsn5rnfnh8FBXkcGn30tBpCxDut7XhhIC0VFLCe3vToqG8GQ7gvr29bWzQVlDBcnG2Xl1ToVlBAAAbsUlEQVR4nO2de1/bxtKAbbSSQLIkR1dTW75gA8EKtuMQSHMB2jRpOEk5Kad92+//Sd5dXfcui/TXhNbzF9haXfbRzM7Mzq5brX+tzM2hW/7jd8xu1Ky9qUwbtqCaL76g9VYy8RNVU7Vp/t8QqJodutIWlHQNxerc//qwuRHfv/lWMgl1BYpqpv90VPQPUAYNTgDbaOb9rw+bq8P7N99KKrGlpKKl5LK/m/XrFuM3IFM9x+jAf1w1+weMG5xhi/EbkBJjF/7jajlGr8EZthi/AdliLGX97Purqw+3Z1/7Pu4jBMZBblT1SYMz/DMwPnt3cb6aQVmd77x8/7XvprEQGFtepo5Wkwjg4WOMXtyMZrOdUmaz0btPX/eWmgqJ0Q8QR3XZ5AwPHePZ1TXOMCc5urxdf827aigkxpY7CUAwaRI2PmyM0e3H1WxEQ0QyWl28fDjDJIURKqTba3aGB4zxxcvRisswV8nVq9cPRCUZjI3loWI8uxqtCmP6ilTJUfHPaLa6fPYQSP5LMa7fX+5UA+Lo6Zur60IvoYJePq2gjmYPwbj+KzGevbwmjenqLAc7mu0///msdUX4PLPRx9svmcP5G+Tfh3H98/Nz2qsZPUXfnH2/c5lG/2t6wBytdq7+HpWM/IHfyMPMZEOMEfR8BC/kw8L44t05z6s5JyL+D0wAAlXy/OKL/B13aA4r59GNF+PxJCaARc5iaWSSmI78ZPFkaZ2eBuEkziYVaYxxEoznZJtBPFVODcs4DaZdzosiwYiuZpyeguW061cfjhf4C0FiHHTNyTIMw8nQqXkn/Xi6BKenp4pnOptaPBgijjiEkCfzDjtsfc0PQWY7N/fOCkx0VVNB9qC+uQS2BoCuhhWt3iLUNJBPMQFNCzuiDvCHiaLq2aG6ChJ0IIVxagP4FU6lNw3U/Bj4TTBlppRFGKPYK64Gb1jxis4ONGtBNi8wRnMvUOHjwQZA1YKJ5I2E8a2aPzTQ9MD0xYeW9/PscsYNEWez66sz/E34dCEKQ2aze2YFTDu9VxtqSDQM1BJXkLOKTCXPZxcC7CU3l4Y3zw8M44jEOMyuZpQdOFhQp9f0CQVSgNFJbOpqXnbWUzLzXmGcUy10dSwA6U90PXs99Ow9UZU6kGcv+WxGs9nNe1qb18+e84mnWYH7jJLFDOCy1Uss7BntDJWb2AojwB6zZsYlmhdn8TyAY8z/0YuaDjdQmTa6MSXUnYsxWhggJaFpuq5p6fsD7FQLBRj9MdkCcdI1bplOL00ZQhM0nk6mY0VNE4iKpJBkfQu9Gj6Vy2f8Jm9eP1/xNRKOktc/vxFfjCe+kXee1QXEq5r1XEzqV/WtQtu+js09sjxpirFHTVS5BreRBnB152H0E4Rfs+EIDJEP3M7YSPs6GYgwOgByA6oxLVpMLHQKNWS1zA/gXen2onhEd6Ghk1uJYIj8dLMjUC0oF9fXz5++/HD7/tMZqWTrs9trUaPRbPT8fRPjWmJUqA5V0cvX4ahifnRA2iNTeCSOkZpvTPuLKzb26nMw9lCBDxyxMK31F2go0xOfj7GLjKMadjASvqkgsgEzGI/hx+oExztYaPAzi+fwrj88ZxPfJJMRNKyr1Ww0uk1bvHn/89XN5fPrC3mr1XUD41phpLvdRbooxkI+fodjUOsxTjTx4VV/sxgjhF+dULlZN4FdrXmRwWDUhi66P3VB+Wb+GN4ACKnzdNWyAgw7uacCg8X47GbEhIipcMlcIwVbZ0ipQ45P2ieMSs6eCiwyIyKMNhy95hhFgKwrdAgr9QFB1dNdCW8xRlfHvof+IK6alRPEwYh632a9ngF6LbQpYDCCaQg/BJzIFRkRfUkaSzia86a1hwFdLfvm+53VjOj31fn56PoSyvXo/Jyd2VhdwVavOUPi0ePd3Se/PGofMyq5c7VRCMLBCDTbsEzC5AHD67j+oOd2Eqvse618Vh9vrtswkjMsWtE4GKflMcDSx4upZ1RviVXFlgzGIVQtm+ubTO10cKAxpp8Brlc6hM+vjfFPInhXRn0h7fr1K8KYwh7/+OE95pms3394Sjuvo7NW9JyGe3yyi+TJIyhPTvapb2G08qHeuDIYITGzmz6FVwKzveqxetOyr8sq3qRSK6BOUAjvO2ZIaigHY1B8py4zRYngW5Kf/LQammiMLrKogkLw7J4ZjOgzQWxhwq8NXE8ddI913Xb2jkqazrhTTtCDJWc2LlsvyIF0HylihfHRo//sHdEqOdv5+KLmfiiMQB+7uenADCU5JrjLAsYyG2u6lXujJyXwQYdwYFiMvfKrKsCI4uzkWlJdj8YITSfwBE7jIBBgFJeNJNDe4mYVPjdIRAdncntJeTWjndeiRM+zC5zj+aen+L/HJwXEEiNSyccUSKjql3KNJDFqy8qWLQsIOpU7a0WFa5L7kxUujRhT/CU2+LEYXYCrZiEDE9i2lmB+IoUR0beERq+jcTFKSvFcCjLSxkB4dAuBYeL8C0knrwmOeIxxVDEkMD765RFHJaUcCYx4VD8vvuAtgFhkjmn21nZLL5UcZCCSsNJHCUbq3fe7MWEAKYzQCsoK6xLe2KioksFuqhENBvKxMbpkXZSVtNLtEzceyUdELsaUJAVydSu7Bo5RxXtnkmsSv8vyb9NS8EmZwGMqpTCOEqOqJ9J0O4VRl3sgaLEB6+KMJefvARIzDBuBKNJvtb7nOJrnsttvtXgUaYgUxv+0jyhfZ/Wd7BIYRsIiDkr/g1s5kxecolyWX5Iy2EMdCcbKxQFgLJlvIDHCCBCEkgdCN85gVOlxgRD4HuJxIoqDdE/0pvyXo1sraVBwxg0i90mTSmBk/dWd48MNMYIE70nH4A1clSwylzDEbGqZKCW6SBdjrAIOlEWfLDouVwdIjGk0L3uiqc5iDKWTUiiyxFuYadgy5Vd+HXAwjl7JTs9EGCWaEw7GXx7t0uMiUt72phgt4o01tYKN6/Ckk09HRa1FCYM3B+AW568L/xVdU41g0mFJkhjh5bQ6G8yE//K1Bj14jyF+XROlenULxsrswQd9Ti+PLoQRwadrWaoOU8knuSJyFPekvbcpRmr4KLVIt7iS89Dclsd1OEtJ8BkOKhlnMik83TaYySMSI7xcIK2QdCw2GScvHojQsxLE3CVK9APVsJNph5w0PujvPaaTLSgD9/EFL2588ZSfl+Oo5JNHvzzZZc+cQWxvitEmHVJPlLQmRe1GJSe+qSvUmocxGnOSeLpGeTwkh7DORPbYnGpdEQcKHamXB6Wr0skvXQUBXgxx0Id9ygO5ur65fbMukUfrN7d0jgCjjn2ej5JPOCNimmtFEDfGaJBlG8mmGAdh/qfFdyPyJAp/RVXk8ZKxgNQeAmMUUAaQEU5q3K4p5/JYjK3ImSTAzu5Xt8NFYQFSjO09zgA2mq1WF68+3lxBufn46mLFKxcfodU4o4unH4mvjk8eH3EUEdrcvQzixhjJ/NPGGOd+gVEQBRQpHsHCuKmtc05rj0kOTTC2OBiljiofI7qW210EelbAounTbOjPMEKQ7RNex6ezUrMZO8cxQpTPd56/fP0eBfLCqUYc4m7BcHOMlBO/oVG1oy/E2HLHBgekjXm9pFFdghqMHKNq1yzgQnMaIrfJd4ZJ6gloWeqowIhAcmwrH+xqtfP85ur1p3L4fCefotzBrOkXYRxvgBGOG3GrxCiwXFKjmoo7AWzlgNXFz4BhhDcWSMti3OYuDnoE2ZyGb6KqDqCjYyqMKUg6SicJIn7XlzcfnmGDJpL3dRSPH5MQ74uxqIRSglAsqPhpsMwPFPTVQuLilDfRGYeoIg9/RapsNRNwCDWnOJzGyI1oKxlAh5lTy0HcIfLc08gax5gOkjzHJBdoQV+c8RxYfoFjKdCaUhDvi3FYlFp5A18kqVNUjqKCgGMpCTjw+3DjxRJgk5SVOpIYYzWrLxHKgg3/a2YsUIhSM6eRTWjZQwYjBLn3mBNJpnIjyLU+lSnj/gmtiF+A0RV8zkoZYXLTdrLwn5HeEJRzXlUc2ywZhywkm1OVTgOjjIJcX5GgDHrIwZi5O1yVHK12vueUuN1KKGK+KSH9H6QVViKMZRyh1Xh5pd7yk+jlGLvhFg7DctarNHPU4Aa/MiQWsMtLjUsHxwE0GLa8Fh5JhDI7Lhej0G/d2ZldPKUTPGuJIu5yNRHq4md5xaMIYzk41pobt0zFcGYBu1XJx4Y7cfjlPGeh3PRElabwq0szGXMnqgKJcxurshmNSmCPQJfuLRejxN0ZrS7JwoAbgTJCiHyG7X7/oG6lggijU9Cxa1IgVYgJmPRKL5DNcLTiyZgtwJ/UYETzW5pQHec6/ZakGCXqiJRxo7U6Qy3NVP3WPuR3tsS2jrAVjM/4Vcasb1qedu/X2uJjIcZWOVXIqeuDD489XpmJoaeNI+m0cWti6EC3aM0qXaZCtzlFHOJ54/SKvCIO4eiIXGmwyVIxqI1ZwvHuB4FGit2d2fmrfAXjG1556j7PNy3fjQ1WlosxVhU2Bt1p/tQwbLOwQ1EVvmseriY9eRFHXtuqJkQPFwUiRaEPi9EPBJW/ZWsORtZSFF9bdKGO4ECUP1Iz27H+72NBp4sjkNEsW5vxkTWpAt+0PNtotv+upjhOjLFV5eOo6fk4TAvtx8X/lToqICizyINhTUlVqXZg4hbrfpyyyE7kqeY9r3MTMygq0HmeKlB0j4sH1eLq+PAfecGUa7LRKqI08RC9vhzB0E7EUeLu7Dx98ZqhKLam7fZuMdzOdj7w7qkUCUa3YgD0SXeQad+gO85zLlVFMGY7FXu5iN2eE09rCxzLyX80qTE1O/FwmlSFqlUCjU3DIJ1TBcXD2pAsrUFWBXjwldE8TkAUI4eIyAp1DEULOed20DOgsOTsVTZtIQoN2hLbyu7LIbGm5Enk9T4SjMR0oG4Bb2qai7FSVJJifoFD5F8027IsJuPNYhxjhwBdU1WVqBsvlUdQ/G/QXstgYqf1RFROFfpq+sJH1eEKTSdC5clUUmh+imp16YUFyL+Bn8NPX1QkJMZQrJKbWlPaXdqwpIoXUk8IhYJdreEJM2y5TP0SDg5GR9YIq8fjJEUHqJpVDXHDGnVQPbs1YVZUIYzTVg+9IoaHExt00Io3QNcSzNGqG90gXOhseaCBHpjcfEGmkm1hdicTiTXlzIP9715ZnKxrPPFaGfj8WKw1FK3okWCEb7gw/46Xd/Fy2wMP1ctooen6USuKfGeRLklMlwRwMbbcJRojddii58MGvfkkXVqpsRtm+2NkcHRtuXB6/mDgux0vNROZ+l/NNodRjW1NIKJmrN7eLxmXc0yEHPWASO+Il9CJMbbmgeD0Gl4VLlimmr4DqhYmnpeE6fyuFqTqycfYGqSrFqDJD0LYQEnXogCNu+9ZHNrpl7YSJsswWwOr57XzB/9rYBqRp8m1rcdCLeZa46P23pdgbEUTAR4qTICdDbiqBYoBMM1n01kcf8xd3GpPqD0Y+IvGsy0DAMiurKm5hynACP8Ktexu8lsFaiLINEIvWyUO1ctlLAd9TsGM2FFBngpz/JEwXuFmENLpYznG6DTrOWFAHascjdFP2XSY63GWDkO/NR9f0+nIQf5SVNFEd0m3Airlirin+il3LnM+ObU1HWHUVaNanK+oBp7o9g29TGA4Y6tooVkWvSMIefKpban5oTY2Uh7027yaKnqWlwBJhJL7R6Kc2x6vNGT/KDuxHGO6VlBRJHUOg6lO7cyg6owjl0ocWuSBNjJE2c7/eohfDV/C1PWMaowEuhWadH4znohmpqKuOUmSZDzFSxH9xZA4gzMeEi2mXpJ4E3Nem0Z1O1N09skixiISlBrnei9iPFmD430ox0eSIZHzdlR51hqMPorlgS2bqPHNJN1mRUnfTCUxRQWGUTwOrOJttxUv3XnFT2wA7GXWz+mafUAta3NNL9QtW7UsJZnMm26hFEVN9+mKGjRhDs1nOLiRoZgR1DTouexKbC9vSMRVvAZjq+fBALgu/Z1uehSil7jLL+0uxJ8PJ16yRAcWsAedsVdavMFUCRI2A+O7btxxhRtVfUNSTlRxs24S2yoRfrqADGbqMKI+/Duev5DoHjuWfUOCzTfyvBdpKNlAERn3tx7jVhoIMW3MjwwbqeSmSr3F+JcKPfvPxYCm8TdTRO5rwBtitxj/UmGLOPj1qhvYVoFR5vtBh7997Sf/Rwm3pGqPp1Sy7E5bEOkL7fHh71/7wf9Zcscv4RCopDCU5IIX5ln7/YOv/dz/MBl8ltRU8WwrjwxPE/ePRGVx7b3Pb7/2Y//jJPr1UFiKw1sovH9Cj3VciJJk3uP/ewi/DfDgZH0gSdZwVRL3Wvba7BFifyh1g0bndbU4W2ks69fXO8KSUoG7cwwbpLLLYpYkY8vMwGx29bUf+x8mL16t5COZIC1zfHR0dHzMbrEheSPwkFRei7OVhlLV4oinfusLOEqIkiJjUqvltThbaSgvsSIO+by/dOljKtKyOEqh5bU4W2ko5PZGdZOMEobFfDC3JePK1tTibKWhMLU4sklG8WpkaaU40wi+LFuMf6kc9B/TnXx8IlJI0VoA8eIpngpvUIuzlYZy0OdF79J6VdpvFWvi3h7r425Wi7OVZpLW4nCmJuQ1VZiZlIT6u8xOY9VZawocu12X/JcttOl1zanZYX+oiWqbitvtYsdFXVxke4RFbgwvErN1CC5+BsGaYKf4mm4+IK5flR30io/mDuemnDimfyIgXkymMbahCm+isMbdOTk+Pj46eSwKN3nWFA9H5Bjnp0Q1YHx6SpfldBPFslXb0qqdmoq2hqFQbH3F+hE7qqdbdrnNHHPmSgZmCNKLKAm999/itDqDseTX6niGnW9kR5X5OD9WjS1s455OeVI9SJif3Bobp8T7EpmKpWqqraCdR6S1OLLVUUgH95oUGZO+kxyjYxG7jcQ2tfDWH1uaGiReslRUNSALDR2dqQNeqMSuqj20p1QhgXADjXmoanoILxLqqk3tZGpq1RlCzm8qIUF75SABKrCISmXXwjeEqU4cq8Xnga3ZS0rJJ7pFfOKpWpAkS6Cj3wLCa3E4g+S9aqo4vmnDWpwajH6oqct5WtbmmhawCBIQo2ITrzLaKJjECMK0njATwT10VPQzYehEkTu2dY3gaGrAqTvDGFhur+f77sIg9reCGOHTcRrHqjZMPxr05mNLt8hqZgrj0M7q0Z3E8OhaHF4mvGFNFX+gZU7xJRgjALCdq90AEOXbCCO5STxa68ZgrBPHwDcX7miAWMINMdYW7o2BkTOC75GKXd+1+DsbxSq2t44DH4sotqYwWmVFvcNub8S3rZurJG+RBzcS/RKMU43YMKarEks6HS0Y6/gu3Y4OTK0pxiggd2w0beKaG2IsyJsavn51I4wtVwXEJlUkRtcgtpzj1uLwZi02Icm1pnxH6VA6cyzF6Fvk86Gf7MR63NEUJ8C3bUg0zzeaYuzY5HYmgyWwMXANMToWAWgjjIg9sUcEgXFuEbrJ3ReHN18syZyLW4lrcX6V9oAUY0elesE18MVKDuxh2CHl2981bGfQFGPkUduntoaqSmyD0whj11Yx3dkQ48AgflCF1kbi/oS1OKxxlNZU8YZVYaq837+T94AU40Snt2UkFsojjK2lXoCKQjhQNtZGH9BbePrEu9IQ45Sw8htibCUAvwg1NgKg4xx/F2yLw1tdKgTDcXLF0PuHf9ZtjENh7OIYBwmwqZhqgvdSitHRixZD2+o1x4iWjlMXUXBT3gyjA4i9eSBG7oZWNMaFho9/FMauAbSgUz3V3Q/C/Y02dHc4ZXRir6jf/72+oAr2YrKYFrLwAI4xBPQmXQsNe8IUY2ui6Wkf+iFaKEVjVJRxJp5go+iuzez0FZIYlaEzz0QUsRQYB91AJX6NEcaNYXF9/F2hMQ5V3HDScSP6zWY1GJfpqfVBW1hUxcvFUIQ4miieJen3/9ykKg6txTUqIbZX9xUORszMZhh7IBvKFqo14GHM0yU/CnI4MGikMRImDm0Rx6ZhSBkDMJ5MJuPQsMdEpglt91hcH/fVaIxdW4ax1VsomqZb1S9zr+92RRrJc1yQvcwwoWocJnEqTuIdHh5sVkvlWMCLK5nqtdpIGVW0p5DdQ1u5pT+MyRjVoJufWsBgzmpjgA/AEKN1mosYo2IZhqXrC+oIt3o6IslHYyT/ZzCi5PDE1gC+N9bdT+I6R15mDa3q2N19zHwjsaaHP91tulBQ5uLAsdGiNmya4DmWHGMUoBzAWEu3AG8+Nhp/xdhodx2nowN6F/JNXRxoZLAEAAdjC/2+sVVsNpZK9NvvUtvKlqLuc0qMJdb09982X+3Z0FMN8B7OMaLU1ty1Mke/uafKbMvXM/CfdmmQxTFVegeDTTEqQBF7qqUsdOpsbw6EmwDKd68ubK3QmvbbfzQqFJdiHNJxI9nDBUYYdCRTNTONjTGycWNsa/eLGyNPJ5O+m2KEIwv+Y3cijPBp6M1l19/90Mi2UgOmoOVh/6B2601SpBjRjzcRLoOpkT9Ymfcw2j/PyKxS8yzO0KZ+5sYDxj2zOL4OyIM3xAjDqAXxLx8j9BU4ewS//UMMUlwex0l+F4p4+Ln5RH9dTlUntpghvcoSIwo6cnPWHGMLbTKE/Tu07p9TnRvkhpubYexYIMBbURjLJ3YBf1tlaFuFfmubu1WueF6y3/71Pstu5BgHAIDqZ9K7ASAmkSqMvTINeg+Mjo1PWw51sk+bhf9TjRgeN8I4BAo5U0ViNEOn/Fz0W3Xru8/9zW2rBOIPTa1pLjXzjU6gq17HRzNzzlQDOjnfWPWwX7DjYKydb4TkVC8eRK1oEHuqTv6ySTOM0RLYdE5VNt+IrqgBaqqcwOjburJAHeBPVXr3ZlzeShZa4aHkvnA6sn/Yvrvv0qm62X83tHXVCrylbmkqIP1Wh9PDbPgfFALEs/9A1W079AINzcXTs/+NcqouAHZ1A2g7+/L6ATn7n4lq65pKbfBCamNsaJqReImmqUvpb66s7yTuzt7jkyMoJ8I68f7h71+wLLy+FideGraq2rYRDCl1mhvsDt7+j0QtjoZliER5HCjRMDBUKLbB7JmzODUElqwSz/qx2n311KiMsvMjdn2iFgdt36pmj2XW1OL4EKtl2xazgSsr3/0pBInyOMJSHBjpH3zRGkafTK/4vGyLHw+nJueXRXvmkHk9ozjGK+NcXKQb4rhDczGM2dfdjbvSdkjiIbZBmY9diLx+dYxrDnNha/vg6xl3yPuInA48cqNg/O3BTxJ3RwCx//m77ULUb0zWdz8J3R0+xI2S31v520Xi7tByuHtP33Qrf4OsD8SZc0wR7xPpb+XvlOi3P2tsK7SmDZLfW/la8vZXcea83W9vMKm/lW9Cortdvm3tH26HxAclv3Ey5/3+r9sA46EJtK1EKNlv1/8C3Fa+QUlDyX5uTe+b/d7KNyBv7/74/NNPn/882Dqn34L8P1VK8lWRIheoAAAAAElFTkSuQmCC"/></a>

***

# Contributors
* [**Daksh Verma** ](https://github.com/dakshverma2411/ "Connect on Github")
* [**Jaskaran Singh** ](https://github.com/jaskaran-23 "Connect on Github")
* [**Tanveer Sodhi** ](https://github.com/TanveerSodhi "Connect on Github")
* [**Aseem Mangla** ](https://github.com/manglaaseem28 "Connect on Github")





