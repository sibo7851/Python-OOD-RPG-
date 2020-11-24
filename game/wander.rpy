init python:
    from Python import itemFactory
    from Python import inventory
    from Python import item
    from Python import character
    from random import randint
    from Python import ledger

transform popup_place:
    xpos 0.1 xanchor 0.0 ypos 0.1 yanchor 0.0


label wander:

    e "You wandered around in search of something"
    $rando=randint(0,100)
    if rando>=50:
        $foundItem=inventory.findRandomItem()
        $itemName=foundItem.itemName
        $Player.inventory.addItem(foundItem)
        e "You found a [itemName]!"
    else:
        e "You were caught trespassing, you owe $500"
        $Player.ledger.addBill(ledger.bill("Trespassing fine",500))
        $Player.stats.money=Player.stats.money-500.0


    return