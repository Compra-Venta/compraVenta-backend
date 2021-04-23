from models.OrderStoploss import OrderSL
from binance.client import Client
from binance.websockets import BinanceSocketManager
import threading
import time
from models.Wallet_model import Wallet
from utils.config import api_key, secret_key

class OrderStoploss:
	def __init__(self, email, base, quote, date, time, order_type, side, b_amount, stop):
		self.email = email
		self.base = base
		self.quote = quote
		self.date = date
		self.time = time
		self.side = side
		self.b_amount = b_amount
		self.stop = stop


client = Client(api_key, secret_key)

bm = BinanceSocketManager(client)

data = []

def process_message(msg):
    global data
    data = msg

class StoplossThread(threading.Thread):
    def __init__(self,order,id_):
        threading.Thread.__init__(self)
        self.order = order 
        self.running = True
        self.name = id_
        self.transaction_complete = 0

    def run(self):
        try:
            symbol = self.order.base + self.order.quote
            stop = self.order.stop
            side = self.order.side 
            global data 
            if side == 'BUY':
                if self.order.order_type == 'SL':
                    while(self.running):
                        flag = False
                        m = data.copy()
                        for d in m:
                            if d['s'] == symbol:
                                print(d['c'])
                                if float(d['c']) >= stop:
                                    print('done at -', d['c'])
                                    from models.TransactionClosed import TransactionClosed
                                    from models.TransactionOpen import TransactionOpen
                                    q_amount = self.order.b_amount * self.order.stop
                                    # Wallet.decrease_fixed_balance_currency_amt(self.order.email, self.order.quote, q_amount)
                                    # Wallet.increase_balance_currency_amt(self.order.email, self.order.base, self.order.b_amount )
                                    Wallet.do_wallet_updation(self.order.email,self.order.quote, self.order.base, -q_amount, self.order.b_amount, 'fixed_balance', 'balance')
                                    TransactionClosed.insert(self.order.email, self.order.base, self.order.quote,self.order.b_amount, self.order.date, self.order.time, self.order.order_type, self.order.side, self.order.stop)
                                    TransactionOpen.delete(self.order.email, self.name, True)
                                    flag = True
                                    self.transaction_complete = 1
                                    break
                        if flag:
                            break
                else:
                    while(self.running):
                        flag = False
                        m = data.copy()
                        for d in m:
                            if d['s'] == symbol:
                                print(d['c'])
                                if float(d['c']) < stop:
                                    print('done at -', d['c'])
                                    from models.TransactionClosed import TransactionClosed
                                    from models.TransactionOpen import TransactionOpen
                                    q_amount = self.order.b_amount * self.order.stop
                                    # Wallet.decrease_fixed_balance_currency_amt(self.order.email, self.order.quote, q_amount)
                                    # Wallet.increase_balance_currency_amt(self.order.email, self.order.base, self.order.b_amount )
                                    Wallet.do_wallet_updation(self.order.email,self.order.quote, self.order.base, -q_amount, self.order.b_amount, 'fixed_balance', 'balance')
                                    TransactionClosed.insert(self.order.email, self.order.base, self.order.quote,self.order.b_amount, self.order.date, self.order.time, self.order.order_type, self.order.side, self.order.stop)
                                    TransactionOpen.delete(self.order.email, self.name, True)
                                    flag = True
                                    self.transaction_complete = 1
                                    break
                        if flag:
                            break

            else:
                if self.order.order_type == 'SL':
                    while(self.running):
                        flag = False
                        m = data.copy()
                        for d in m:
                            if d['s'] == symbol:
                                print(d['c'])
                                if float(d['c']) <= stop:
                                    print('done at -', d['c'])
                                    from models.TransactionClosed import TransactionClosed
                                    from models.TransactionOpen import TransactionOpen
                                    q_amount = self.order.b_amount * self.order.stop
                                    # Wallet.decrease_fixed_balance_currency_amt(self.order.email, self.order.base, self.order.b_amount)
                                    # Wallet.increase_balance_currency_amt(self.order.email, self.order.quote, q_amount )
                                    Wallet.do_wallet_updation(self.order.email,self.order.base, self.order.quote, -self.order.b_amount, q_amount, 'fixed_balance', 'balance')
                                    TransactionClosed.insert(self.order.email, self.order.base, self.order.quote,self.order.b_amount, self.order.date, self.order.time, self.order.order_type, self.order.side, self.order.stop)
                                    TransactionOpen.delete(self.order.email, self.name, True)
                                    flag = True
                                    break
                        if flag:
                            break
                else:
                    while(self.running):
                        flag = False
                        m = data.copy()
                        for d in m:
                            if d['s'] == symbol:
                                print(d['c'])
                                if float(d['c']) > stop:
                                    print('done at -', d['c'])
                                    from models.TransactionClosed import TransactionClosed
                                    from models.TransactionOpen import TransactionOpen
                                    q_amount = self.order.b_amount * self.order.stop
                                    # Wallet.decrease_fixed_balance_currency_amt(self.order.email, self.order.base, self.order.b_amount)
                                    # Wallet.increase_balance_currency_amt(self.order.email, self.order.quote, q_amount )
                                    Wallet.do_wallet_updation(self.order.email,self.order.base, self.order.quote, -self.order.b_amount, q_amount, 'fixed_balance', 'balance')
                                    TransactionClosed.insert(self.order.email, self.order.base, self.order.quote,self.order.b_amount, self.order.date, self.order.time, self.order.order_type, self.order.side, self.order.stop)
                                    TransactionOpen.delete(self.order.email, self.name, True)
                                    flag = True
                                    break
                        if flag:
                            break

        except Exception as e:
            print(e)

conn_key = bm.start_miniticker_socket(process_message,3000)

bm.start()


def startStoplossThread(order, id_):
    t = StoplossThread(order,id_)
    t.start()

def stopStoplossThread(id_):
    for thread in threading.enumerate():
        if thread.name == id_:
            thread.running = False



# order = OrderStoploss('daksh','BTC','USDT','date','time','SL','BUY', 0.001, 64400)
# startStoplossThread(order,"daksh")

# time.sleep(5)
# stopStoplossThread("daksh")
# time.sleep(5)

# for thread in threading.enumerate():
#     print(thread.name)


 
