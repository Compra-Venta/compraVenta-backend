# Compra-Venta

**About** <br />
Today’s world has advanced a lot in terms of cryptocurrency exchange or digital currency exchange and <br />
the main reason that these digital currencies are overtaking physical currency is that it is not governed <br />
by any one single authority and is totally secure since it uses the blockchain technology. It is becoming <br />
investors' choice to trade into crypto currencies. But since this concept is relatively new and many people <br />
fear to adapt to invest in cryptocurrency, it has still not reached its potential. Many people who trade into<br />
this market without any prior knowledge face severe losses and fear using it again. So our aim is to provide <br />
a virtual trading platform which will provide budding investors a platform to dive into the trading of crypto-<br/>
currencies without having any fear of losing anything.<br />

Main **features** of our project are - <br />
<br />
● **Virtual Trading-** Each user will be provided with some virtual money with the help of which a user can trade<br />
into the choice of his own cryptocurrency which will help a user well versed with cryptocurrency trading gradually.<br />
● **Real-time price updation-** The actual price of each cryptocurrency will be updated regularly without a long delay<br />
with the help of API’s.<br />
● **Price Prediction of Cryptocurrency-** With the help of machine learning model, we will be able to predict the <br />
price of cryptocurrency and trends in the market.<br />
● **User authentication-** Each user will be provided its own username and password and details of the user will <br />
be stored in the database along with its activities.<br />
● **Latest News-** Related news regarding cryptocurrencies and cryptocurrency trading is refreshed on our platform<br />
in order to make users familiar with the environment.<br />
● **User Support-** If users need some assistance/clarification regarding cryptocurrency trading, the model will<br />
help them accordingly.<br />
<br />
So, we feel that our project will give a kickstart to all the users who are interested in Cryptocurrency trading who don't know where to start from and which will eventually help this cryptocurrency trading industry to reach its potential.
<br />

**End points** of backend-<br />
*1* **api.add_resource(RegisterUser, '/register') -** This api is used to register a new user along with the <br />
user's details in the form of a document in a collection of the User's database and does not allows same user to <br />
register twice, thus reducing redundancy.<br />
*2* **api.add_resource(UserLogin, '/login') -** This api is used to help users to login into the website by matching<br />
the credentials entered by the user with the information present in the database and in return sends jwt token<br />
(access and refresh) for authorisation.<br />
*3* **api.add_resource(Profile,'/myprofile')-** This api helps a user to view it's own profile. User can also check<br />
its current rating in the virtual trading platform to analyse themselves.<br />
*4* **api.add_resource(RefreshLogin, '/reauth') -** This api is used to send access token whenever it tends to <br />
expire by using the refresh token which ensures that a user don't have to login again and again and thereby ensuring<br />
good user experience.<br />
*5* **api.add_resource(UpdatePassword, '/password/change') -** This api provides the facility of changing password <br />
at his/her own convenience.<br />
*6* **api.add_resource(Predict,'/predict') -** This api comes in very handy to a user as it helps a user to predict<br />
the price of base asset coin in terms of the quote asset coin which helps user to make better decisions to trade coins.<br />
*7* **api.add_resource(ForgotPassword,'/password/get_new') -** In case a user forgests his /her own password ,this<br />
api comes in the picture with a rescue operation. It send user a random password at his/her mail with the help of <br />
which user can login into the website and can later update the password at its own convenience.<br />
*8* **api.add_resource(get_watchlist,'/watchlist') -** This 



