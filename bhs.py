import random
import sys

print "bankheist sim"

if len(sys.argv) == 5:
    balance = int(sys.argv[1])
    chance = int(sys.argv[2])
    betpct = int(sys.argv[3])
    bets = int(sys.argv[4])

    for i in range(0,bets):
        bet_amount = int(balance * betpct / 100.0)
        roll = random.randint(1,100)
        out = "bet " + str(i+1) + " - "
        out += "balance: " + str(balance) + ", "
        out += "bet: " + str(bet_amount) + ", "
        out += "chance: " + str(chance) + ", "
        out += "roll: " + str(roll) + ", "
        if (roll <= chance):
            payout = int(bet_amount * 1.5)
            balance += payout - bet_amount
            out += "win! payout " + str(payout)
        else:
            balance -= bet_amount
            out += "lose!"
        print out


