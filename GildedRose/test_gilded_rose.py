from approvaltests.combination_approvals import verify_all_combinations
from gilded_rose import GildedRose
from item import Item

def test_what_does_update_items_do():

    name = [
        "Default Item",
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
        "Sulfuras, Hand of Ragnaros",
    ]
    sell_in = [-1, 0, 1, 5, 6, 10, 11]
    quality = [-1, 0, 1, 2, 48, 49, 50]

    # result = update_item('foo', 0, 0)
    # verify(result, reporter)
    verify_all_combinations(update_item, [name, sell_in, quality])


def update_item(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    result = ""
    for item in gilded_rose.items:
        result += f"name: {item.name} sell_in: {item.sell_in} quality: {item.quality}"
    return result
