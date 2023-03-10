# monopoly.md
Monopoly game project overview

```
browser {
    game {
        ui {
            menu {
                start,
                pause,
                restart,
                timer
            },
            modal {
                eventInfo,
                propertyInfo,
                diceInfo,
                cardInfo
            },
            players {
                color,
                names,
                balance,
                currentTurn
            }
        }
        board {
            background {
                logo
            },
            tiles {
                color,
                name,
                price,
                deed,
                events {
                    buy,
                    payRent,
                    upgrade,
                    sellUpgrade,
                    mortgage,
                    trade,
                    declareBankruptcy
                },
                streets[22],
                special {
                    go,
                    communityChest,
                    incomeTax,
                    railroad[4],
                    chance,
                    jail,
                    electricCompany,
                    waterWorks,
                    freeParking,
                    goToJail,
                    luxuryTax
                },
                upgrades {
                    house,
                    hotel
                },
                state {
                    canPurchase,
                    owned,
                    occupiedBy,
                    rentValue
                }
            },
            cards {
                communityChest[16],
                chance[16]
            },
            tokens {
                battleship,
                boot,
                cannon,
                thimble,
                topHat,
                iron
            }
        },
        turnOrder {
            currentPlayer,
            playerOrder[p]
        }
        players[p] {
            currentBalance,
            deeds[d],
            monopolies {
                brown[2],
                lightBlue[3],
                pink[3],
                orange[3],
                red[3],
                yellow[3],
                green[3],
                blue[2],
                railroad[4],
                utility[2]
            }
        },
        dice[2] {
            roll,
            currentRoll,
            numDoubles
        },
        bank {
            balance,
            money {
                500[20],
                100[20],
                50[30],
                20[50],
                10[40],
                5[40],
                1[40]
            },
            events {
                give200,
                collectTax,
                buyMortgage,
                collectMortgateInterest,
                collectBankruptBalance
            }
        }
    }
}
```