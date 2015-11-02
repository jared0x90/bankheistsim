import random
import sys

print "gamba sim"
print
print "bankheist example # 1"
print "---------------------"
print "20k starting balance, 65% win rate, bet 5% of balance a game, play 1000 games, 1.5x payout on win"
print
print "python " + sys.argv[0] + " 20000 65 5 1000 1.5"
print
print
print "bankheist example # 2"
print "---------------------"
print "20k starting balance, 65% win rate, bet 1000 a game, play 1000 games, 1.5x payout on win, fixed bet on (y)"
print
print "python " + sys.argv[0] + " 20000 65 5 1000 1.5 y"
print
print
print "dragrace example"
print "-----------------"
print "python " + sys.argv[0] + " 20000 13 500 1000 7 y"
print
print
print
print "starting sim"
print
print
print


if len(sys.argv) == 6 or len(sys.argv) == 7:
    balance = int(sys.argv[1])
    chance = int(sys.argv[2])
    betpct = int(sys.argv[3])
    bets = int(sys.argv[4])
    payout = float(sys.argv[5])
    fixed_bet = False
    if(len(sys.argv)) == 7:
        if (sys.argv[6] == 'y'): fixed_bet = True

    for i in range(0,bets):
        if(fixed_bet):
            bet_amount = betpct
        else:
            bet_amount = int(balance * betpct / 100.0)
        roll = random.randint(1,100)
        out = "bet " + str(i+1) + " - "
        out += "balance: " + str(balance) + ", "
        out += "bet: " + str(bet_amount) + ", "
        out += "chance: " + str(chance) + ", "
        out += "roll: " + str(roll) + ", "
        if (roll <= chance):
            winnings = int(bet_amount * payout)
            balance += winnings - bet_amount
            out += "win! payout " + str(winnings)
        else:
            balance -= bet_amount
            out += "lose!"
        print out


