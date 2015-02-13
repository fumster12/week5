## machine.py

class CoinDispenser:
    coins = [25, 10, 5, 1]

    def make_change(self, amount):
        if amount < 5:
            return [0,0,0, amount]
        elif amount == 5:
            return [0,0,1,0]
        elif amount < 10:
            amount = amount - 5 
            return [0,0,1,amount]
        elif amount == 10:
            return [0,1,0,0]
        elif amount < 15:
            amount = amount - 10
            return [0,1,0, amount]
        elif amount == 15:
            return [0,1,1,0]
        elif amount < 20:
            amount = amount - 15
            return [0,1,1, amount]
        elif amount == 25:
            return [1,0,0,0]

## I tried many different variations of code but I still couldn't figure this out.
        elif amount > 25:
            coins = []
            coins.append([amount // 25])
            amount = amount % 25
            if:
                coins.append([0])
            if amount > 10:
            coins.append([amount // 10])
            amount = amount % 10
            else:
            coins.append([0])
        if amount > 5:
            coins.append([amount // 5])
            amount = amount % 5
        else:
            coins.append([0])
        if amount < 5:
            coins.append([amount / 1])
            return coins
            



    #print(make_change(se45))


##            
##            coins = [25, 10, 5, 1]
##            coins[0] = amount/25 
##            amount = coins[0] - amount
##            coins[1] = amount/ 10
##            amount = coins[1] - amount
##            coins[2] = amount/5
##            amount = coins[2] - amount
##            coins[3] = amount                
##            return coins


            
        
    





    
    
##    def coi():
##        Coins = {"quarter": 25, "dime": 10, "nickel": 5, "penny": 1}
##        for coin in coins:
##            print(coin)
##            
        
        
