
def get_profit(wallet):
    assets = wallet.balance.copy()
    amount = {}
    done={}
    count = 0
    total = 0
    for i in wallet.fixed_balance.keys():
        assets[i] = assets[i] + wallet.fixed_balance[i]
        amount[i] = 0
        done[i+"USDT"] = False
    while count<5:
        from utils.StoplossThreads import data
        prices = data.copy()
        for d in prices:
            if d['s'] in set(done.keys()):
                i = d['s'][:3]
                amount[i] = round(float(d['c'])*assets[i],8)
                if done[d['s']] == False:
                    count+=1
                    done[d['s']] = True
    
    amount["USDT"] = assets["USDT"]
    for i in amount.values():
        total+=i

    return total
                