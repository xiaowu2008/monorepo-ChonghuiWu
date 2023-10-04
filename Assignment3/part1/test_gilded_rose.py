# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item_before_sell_in(self):
        item = Item("Normal Item", 5, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 4)

    def test_normal_item_after_sell_in(self):
        item = Item("Normal Item", 0, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, -1)

    def test_brie_before_sell_in(self):
        item = Item("Aged Brie", 5, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 11)
        self.assertEqual(item.sell_in, 4)

    def test_brie_after_sell_in(self):
        item = Item("Aged Brie", 0, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 12)
        self.assertEqual(item.sell_in, -1)

    def test_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 80)
        self.assertEqual(item.sell_in, 5)

    def test_backstage_passes_more_than_10_days(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 21)
        self.assertEqual(item.sell_in, 14)

    def test_backstage_passes_less_than_10_days(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 22)
        self.assertEqual(item.sell_in, 9)

    def test_backstage_passes_less_than_5_days(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 23)
        self.assertEqual(item.sell_in, 4)

    def test_backstage_passes_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 0)
        self.assertEqual(item.sell_in, -1)

    def test_conjured_item_before_sell_in(self):
        item = Item("Conjured", 5, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, 4)

    def test_conjured_item_after_sell_in(self):
        item = Item("Conjured", 0, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 6)
        self.assertEqual(item.sell_in, -1)

    def test_conjured_mana_cake_before_sell_in(self):
        item = Item("Conjured Mana Cake", 5, 10)
        shop = GildedRose([item])
        shop.update_quality()
        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, 4)


if __name__ == '__main__':
    unittest.main()
