init python:
    from Python import itemFactory
    from Python import inventory
    from Python import item
    from Python import character

transform popup_place:
    xpos 0.1 xanchor 0.0 ypos 0.1 yanchor 0.0


label wander:

    e "You wandered around in search of something"
    $foundItem=inventory.findRandomItem()
    $itemName=foundItem.itemName
    $Player.inventory.addItem(foundItem)
    e "You found a [itemName]!"

    return