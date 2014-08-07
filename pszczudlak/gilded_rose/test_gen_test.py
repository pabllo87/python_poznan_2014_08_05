
import unittest
from gilded_rose import GildedRose, Item

class GildedRoseGenTest(unittest.TestCase):
    

    def test_1(self):
        item = Item("Aged Brie", -10, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2(self):
        item = Item("Aged Brie", -10, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3(self):
        item = Item("Aged Brie", -10, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_4(self):
        item = Item("Aged Brie", -10, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_5(self):
        item = Item("Aged Brie", -10, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_6(self):
        item = Item("Aged Brie", -10, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_7(self):
        item = Item("Aged Brie", -10, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_8(self):
        item = Item("Aged Brie", -10, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_9(self):
        item = Item("Aged Brie", -10, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_10(self):
        item = Item("Aged Brie", -10, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_11(self):
        item = Item("Aged Brie", -10, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_12(self):
        item = Item("Aged Brie", -10, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_13(self):
        item = Item("Aged Brie", -10, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_14(self):
        item = Item("Aged Brie", -10, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_15(self):
        item = Item("Aged Brie", -10, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_16(self):
        item = Item("Aged Brie", -10, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_17(self):
        item = Item("Aged Brie", -10, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_18(self):
        item = Item("Aged Brie", -10, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_19(self):
        item = Item("Aged Brie", -10, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_20(self):
        item = Item("Aged Brie", -10, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_21(self):
        item = Item("Aged Brie", -10, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_22(self):
        item = Item("Aged Brie", -10, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_23(self):
        item = Item("Aged Brie", -10, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_24(self):
        item = Item("Aged Brie", -10, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_25(self):
        item = Item("Aged Brie", -10, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_26(self):
        item = Item("Aged Brie", -10, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_27(self):
        item = Item("Aged Brie", -10, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_28(self):
        item = Item("Aged Brie", -10, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_29(self):
        item = Item("Aged Brie", -10, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_30(self):
        item = Item("Aged Brie", -10, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_31(self):
        item = Item("Aged Brie", -10, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_32(self):
        item = Item("Aged Brie", -10, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_33(self):
        item = Item("Aged Brie", -10, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_34(self):
        item = Item("Aged Brie", -10, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_35(self):
        item = Item("Aged Brie", -10, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_36(self):
        item = Item("Aged Brie", -10, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_37(self):
        item = Item("Aged Brie", -10, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_38(self):
        item = Item("Aged Brie", -10, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_39(self):
        item = Item("Aged Brie", -10, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_40(self):
        item = Item("Aged Brie", -10, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_41(self):
        item = Item("Aged Brie", -10, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_42(self):
        item = Item("Aged Brie", -10, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_43(self):
        item = Item("Aged Brie", -10, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_44(self):
        item = Item("Aged Brie", -10, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_45(self):
        item = Item("Aged Brie", -10, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_46(self):
        item = Item("Aged Brie", -10, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_47(self):
        item = Item("Aged Brie", -10, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_48(self):
        item = Item("Aged Brie", -10, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_49(self):
        item = Item("Aged Brie", -10, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_50(self):
        item = Item("Aged Brie", -10, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_51(self):
        item = Item("Aged Brie", -9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_52(self):
        item = Item("Aged Brie", -9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_53(self):
        item = Item("Aged Brie", -9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_54(self):
        item = Item("Aged Brie", -9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_55(self):
        item = Item("Aged Brie", -9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_56(self):
        item = Item("Aged Brie", -9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_57(self):
        item = Item("Aged Brie", -9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_58(self):
        item = Item("Aged Brie", -9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_59(self):
        item = Item("Aged Brie", -9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_60(self):
        item = Item("Aged Brie", -9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_61(self):
        item = Item("Aged Brie", -9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_62(self):
        item = Item("Aged Brie", -9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_63(self):
        item = Item("Aged Brie", -9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_64(self):
        item = Item("Aged Brie", -9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_65(self):
        item = Item("Aged Brie", -9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_66(self):
        item = Item("Aged Brie", -9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_67(self):
        item = Item("Aged Brie", -9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_68(self):
        item = Item("Aged Brie", -9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_69(self):
        item = Item("Aged Brie", -9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_70(self):
        item = Item("Aged Brie", -9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_71(self):
        item = Item("Aged Brie", -9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_72(self):
        item = Item("Aged Brie", -9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_73(self):
        item = Item("Aged Brie", -9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_74(self):
        item = Item("Aged Brie", -9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_75(self):
        item = Item("Aged Brie", -9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_76(self):
        item = Item("Aged Brie", -9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_77(self):
        item = Item("Aged Brie", -9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_78(self):
        item = Item("Aged Brie", -9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_79(self):
        item = Item("Aged Brie", -9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_80(self):
        item = Item("Aged Brie", -9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_81(self):
        item = Item("Aged Brie", -9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_82(self):
        item = Item("Aged Brie", -9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_83(self):
        item = Item("Aged Brie", -9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_84(self):
        item = Item("Aged Brie", -9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_85(self):
        item = Item("Aged Brie", -9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_86(self):
        item = Item("Aged Brie", -9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_87(self):
        item = Item("Aged Brie", -9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_88(self):
        item = Item("Aged Brie", -9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_89(self):
        item = Item("Aged Brie", -9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_90(self):
        item = Item("Aged Brie", -9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_91(self):
        item = Item("Aged Brie", -9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_92(self):
        item = Item("Aged Brie", -9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_93(self):
        item = Item("Aged Brie", -9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_94(self):
        item = Item("Aged Brie", -9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_95(self):
        item = Item("Aged Brie", -9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_96(self):
        item = Item("Aged Brie", -9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_97(self):
        item = Item("Aged Brie", -9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_98(self):
        item = Item("Aged Brie", -9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_99(self):
        item = Item("Aged Brie", -9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_100(self):
        item = Item("Aged Brie", -9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_101(self):
        item = Item("Aged Brie", -8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_102(self):
        item = Item("Aged Brie", -8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_103(self):
        item = Item("Aged Brie", -8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_104(self):
        item = Item("Aged Brie", -8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_105(self):
        item = Item("Aged Brie", -8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_106(self):
        item = Item("Aged Brie", -8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_107(self):
        item = Item("Aged Brie", -8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_108(self):
        item = Item("Aged Brie", -8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_109(self):
        item = Item("Aged Brie", -8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_110(self):
        item = Item("Aged Brie", -8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_111(self):
        item = Item("Aged Brie", -8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_112(self):
        item = Item("Aged Brie", -8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_113(self):
        item = Item("Aged Brie", -8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_114(self):
        item = Item("Aged Brie", -8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_115(self):
        item = Item("Aged Brie", -8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_116(self):
        item = Item("Aged Brie", -8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_117(self):
        item = Item("Aged Brie", -8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_118(self):
        item = Item("Aged Brie", -8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_119(self):
        item = Item("Aged Brie", -8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_120(self):
        item = Item("Aged Brie", -8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_121(self):
        item = Item("Aged Brie", -8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_122(self):
        item = Item("Aged Brie", -8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_123(self):
        item = Item("Aged Brie", -8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_124(self):
        item = Item("Aged Brie", -8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_125(self):
        item = Item("Aged Brie", -8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_126(self):
        item = Item("Aged Brie", -8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_127(self):
        item = Item("Aged Brie", -8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_128(self):
        item = Item("Aged Brie", -8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_129(self):
        item = Item("Aged Brie", -8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_130(self):
        item = Item("Aged Brie", -8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_131(self):
        item = Item("Aged Brie", -8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_132(self):
        item = Item("Aged Brie", -8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_133(self):
        item = Item("Aged Brie", -8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_134(self):
        item = Item("Aged Brie", -8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_135(self):
        item = Item("Aged Brie", -8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_136(self):
        item = Item("Aged Brie", -8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_137(self):
        item = Item("Aged Brie", -8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_138(self):
        item = Item("Aged Brie", -8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_139(self):
        item = Item("Aged Brie", -8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_140(self):
        item = Item("Aged Brie", -8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_141(self):
        item = Item("Aged Brie", -8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_142(self):
        item = Item("Aged Brie", -8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_143(self):
        item = Item("Aged Brie", -8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_144(self):
        item = Item("Aged Brie", -8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_145(self):
        item = Item("Aged Brie", -8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_146(self):
        item = Item("Aged Brie", -8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_147(self):
        item = Item("Aged Brie", -8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_148(self):
        item = Item("Aged Brie", -8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_149(self):
        item = Item("Aged Brie", -8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_150(self):
        item = Item("Aged Brie", -8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_151(self):
        item = Item("Aged Brie", -7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_152(self):
        item = Item("Aged Brie", -7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_153(self):
        item = Item("Aged Brie", -7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_154(self):
        item = Item("Aged Brie", -7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_155(self):
        item = Item("Aged Brie", -7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_156(self):
        item = Item("Aged Brie", -7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_157(self):
        item = Item("Aged Brie", -7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_158(self):
        item = Item("Aged Brie", -7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_159(self):
        item = Item("Aged Brie", -7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_160(self):
        item = Item("Aged Brie", -7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_161(self):
        item = Item("Aged Brie", -7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_162(self):
        item = Item("Aged Brie", -7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_163(self):
        item = Item("Aged Brie", -7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_164(self):
        item = Item("Aged Brie", -7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_165(self):
        item = Item("Aged Brie", -7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_166(self):
        item = Item("Aged Brie", -7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_167(self):
        item = Item("Aged Brie", -7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_168(self):
        item = Item("Aged Brie", -7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_169(self):
        item = Item("Aged Brie", -7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_170(self):
        item = Item("Aged Brie", -7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_171(self):
        item = Item("Aged Brie", -7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_172(self):
        item = Item("Aged Brie", -7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_173(self):
        item = Item("Aged Brie", -7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_174(self):
        item = Item("Aged Brie", -7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_175(self):
        item = Item("Aged Brie", -7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_176(self):
        item = Item("Aged Brie", -7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_177(self):
        item = Item("Aged Brie", -7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_178(self):
        item = Item("Aged Brie", -7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_179(self):
        item = Item("Aged Brie", -7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_180(self):
        item = Item("Aged Brie", -7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_181(self):
        item = Item("Aged Brie", -7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_182(self):
        item = Item("Aged Brie", -7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_183(self):
        item = Item("Aged Brie", -7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_184(self):
        item = Item("Aged Brie", -7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_185(self):
        item = Item("Aged Brie", -7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_186(self):
        item = Item("Aged Brie", -7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_187(self):
        item = Item("Aged Brie", -7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_188(self):
        item = Item("Aged Brie", -7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_189(self):
        item = Item("Aged Brie", -7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_190(self):
        item = Item("Aged Brie", -7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_191(self):
        item = Item("Aged Brie", -7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_192(self):
        item = Item("Aged Brie", -7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_193(self):
        item = Item("Aged Brie", -7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_194(self):
        item = Item("Aged Brie", -7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_195(self):
        item = Item("Aged Brie", -7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_196(self):
        item = Item("Aged Brie", -7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_197(self):
        item = Item("Aged Brie", -7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_198(self):
        item = Item("Aged Brie", -7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_199(self):
        item = Item("Aged Brie", -7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_200(self):
        item = Item("Aged Brie", -7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_201(self):
        item = Item("Aged Brie", -6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_202(self):
        item = Item("Aged Brie", -6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_203(self):
        item = Item("Aged Brie", -6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_204(self):
        item = Item("Aged Brie", -6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_205(self):
        item = Item("Aged Brie", -6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_206(self):
        item = Item("Aged Brie", -6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_207(self):
        item = Item("Aged Brie", -6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_208(self):
        item = Item("Aged Brie", -6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_209(self):
        item = Item("Aged Brie", -6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_210(self):
        item = Item("Aged Brie", -6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_211(self):
        item = Item("Aged Brie", -6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_212(self):
        item = Item("Aged Brie", -6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_213(self):
        item = Item("Aged Brie", -6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_214(self):
        item = Item("Aged Brie", -6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_215(self):
        item = Item("Aged Brie", -6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_216(self):
        item = Item("Aged Brie", -6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_217(self):
        item = Item("Aged Brie", -6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_218(self):
        item = Item("Aged Brie", -6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_219(self):
        item = Item("Aged Brie", -6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_220(self):
        item = Item("Aged Brie", -6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_221(self):
        item = Item("Aged Brie", -6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_222(self):
        item = Item("Aged Brie", -6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_223(self):
        item = Item("Aged Brie", -6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_224(self):
        item = Item("Aged Brie", -6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_225(self):
        item = Item("Aged Brie", -6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_226(self):
        item = Item("Aged Brie", -6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_227(self):
        item = Item("Aged Brie", -6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_228(self):
        item = Item("Aged Brie", -6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_229(self):
        item = Item("Aged Brie", -6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_230(self):
        item = Item("Aged Brie", -6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_231(self):
        item = Item("Aged Brie", -6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_232(self):
        item = Item("Aged Brie", -6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_233(self):
        item = Item("Aged Brie", -6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_234(self):
        item = Item("Aged Brie", -6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_235(self):
        item = Item("Aged Brie", -6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_236(self):
        item = Item("Aged Brie", -6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_237(self):
        item = Item("Aged Brie", -6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_238(self):
        item = Item("Aged Brie", -6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_239(self):
        item = Item("Aged Brie", -6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_240(self):
        item = Item("Aged Brie", -6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_241(self):
        item = Item("Aged Brie", -6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_242(self):
        item = Item("Aged Brie", -6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_243(self):
        item = Item("Aged Brie", -6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_244(self):
        item = Item("Aged Brie", -6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_245(self):
        item = Item("Aged Brie", -6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_246(self):
        item = Item("Aged Brie", -6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_247(self):
        item = Item("Aged Brie", -6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_248(self):
        item = Item("Aged Brie", -6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_249(self):
        item = Item("Aged Brie", -6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_250(self):
        item = Item("Aged Brie", -6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_251(self):
        item = Item("Aged Brie", -5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_252(self):
        item = Item("Aged Brie", -5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_253(self):
        item = Item("Aged Brie", -5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_254(self):
        item = Item("Aged Brie", -5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_255(self):
        item = Item("Aged Brie", -5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_256(self):
        item = Item("Aged Brie", -5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_257(self):
        item = Item("Aged Brie", -5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_258(self):
        item = Item("Aged Brie", -5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_259(self):
        item = Item("Aged Brie", -5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_260(self):
        item = Item("Aged Brie", -5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_261(self):
        item = Item("Aged Brie", -5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_262(self):
        item = Item("Aged Brie", -5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_263(self):
        item = Item("Aged Brie", -5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_264(self):
        item = Item("Aged Brie", -5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_265(self):
        item = Item("Aged Brie", -5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_266(self):
        item = Item("Aged Brie", -5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_267(self):
        item = Item("Aged Brie", -5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_268(self):
        item = Item("Aged Brie", -5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_269(self):
        item = Item("Aged Brie", -5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_270(self):
        item = Item("Aged Brie", -5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_271(self):
        item = Item("Aged Brie", -5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_272(self):
        item = Item("Aged Brie", -5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_273(self):
        item = Item("Aged Brie", -5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_274(self):
        item = Item("Aged Brie", -5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_275(self):
        item = Item("Aged Brie", -5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_276(self):
        item = Item("Aged Brie", -5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_277(self):
        item = Item("Aged Brie", -5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_278(self):
        item = Item("Aged Brie", -5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_279(self):
        item = Item("Aged Brie", -5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_280(self):
        item = Item("Aged Brie", -5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_281(self):
        item = Item("Aged Brie", -5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_282(self):
        item = Item("Aged Brie", -5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_283(self):
        item = Item("Aged Brie", -5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_284(self):
        item = Item("Aged Brie", -5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_285(self):
        item = Item("Aged Brie", -5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_286(self):
        item = Item("Aged Brie", -5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_287(self):
        item = Item("Aged Brie", -5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_288(self):
        item = Item("Aged Brie", -5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_289(self):
        item = Item("Aged Brie", -5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_290(self):
        item = Item("Aged Brie", -5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_291(self):
        item = Item("Aged Brie", -5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_292(self):
        item = Item("Aged Brie", -5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_293(self):
        item = Item("Aged Brie", -5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_294(self):
        item = Item("Aged Brie", -5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_295(self):
        item = Item("Aged Brie", -5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_296(self):
        item = Item("Aged Brie", -5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_297(self):
        item = Item("Aged Brie", -5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_298(self):
        item = Item("Aged Brie", -5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_299(self):
        item = Item("Aged Brie", -5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_300(self):
        item = Item("Aged Brie", -5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_301(self):
        item = Item("Aged Brie", -4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_302(self):
        item = Item("Aged Brie", -4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_303(self):
        item = Item("Aged Brie", -4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_304(self):
        item = Item("Aged Brie", -4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_305(self):
        item = Item("Aged Brie", -4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_306(self):
        item = Item("Aged Brie", -4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_307(self):
        item = Item("Aged Brie", -4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_308(self):
        item = Item("Aged Brie", -4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_309(self):
        item = Item("Aged Brie", -4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_310(self):
        item = Item("Aged Brie", -4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_311(self):
        item = Item("Aged Brie", -4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_312(self):
        item = Item("Aged Brie", -4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_313(self):
        item = Item("Aged Brie", -4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_314(self):
        item = Item("Aged Brie", -4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_315(self):
        item = Item("Aged Brie", -4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_316(self):
        item = Item("Aged Brie", -4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_317(self):
        item = Item("Aged Brie", -4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_318(self):
        item = Item("Aged Brie", -4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_319(self):
        item = Item("Aged Brie", -4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_320(self):
        item = Item("Aged Brie", -4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_321(self):
        item = Item("Aged Brie", -4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_322(self):
        item = Item("Aged Brie", -4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_323(self):
        item = Item("Aged Brie", -4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_324(self):
        item = Item("Aged Brie", -4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_325(self):
        item = Item("Aged Brie", -4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_326(self):
        item = Item("Aged Brie", -4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_327(self):
        item = Item("Aged Brie", -4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_328(self):
        item = Item("Aged Brie", -4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_329(self):
        item = Item("Aged Brie", -4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_330(self):
        item = Item("Aged Brie", -4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_331(self):
        item = Item("Aged Brie", -4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_332(self):
        item = Item("Aged Brie", -4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_333(self):
        item = Item("Aged Brie", -4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_334(self):
        item = Item("Aged Brie", -4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_335(self):
        item = Item("Aged Brie", -4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_336(self):
        item = Item("Aged Brie", -4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_337(self):
        item = Item("Aged Brie", -4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_338(self):
        item = Item("Aged Brie", -4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_339(self):
        item = Item("Aged Brie", -4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_340(self):
        item = Item("Aged Brie", -4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_341(self):
        item = Item("Aged Brie", -4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_342(self):
        item = Item("Aged Brie", -4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_343(self):
        item = Item("Aged Brie", -4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_344(self):
        item = Item("Aged Brie", -4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_345(self):
        item = Item("Aged Brie", -4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_346(self):
        item = Item("Aged Brie", -4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_347(self):
        item = Item("Aged Brie", -4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_348(self):
        item = Item("Aged Brie", -4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_349(self):
        item = Item("Aged Brie", -4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_350(self):
        item = Item("Aged Brie", -4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_351(self):
        item = Item("Aged Brie", -3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_352(self):
        item = Item("Aged Brie", -3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_353(self):
        item = Item("Aged Brie", -3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_354(self):
        item = Item("Aged Brie", -3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_355(self):
        item = Item("Aged Brie", -3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_356(self):
        item = Item("Aged Brie", -3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_357(self):
        item = Item("Aged Brie", -3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_358(self):
        item = Item("Aged Brie", -3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_359(self):
        item = Item("Aged Brie", -3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_360(self):
        item = Item("Aged Brie", -3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_361(self):
        item = Item("Aged Brie", -3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_362(self):
        item = Item("Aged Brie", -3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_363(self):
        item = Item("Aged Brie", -3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_364(self):
        item = Item("Aged Brie", -3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_365(self):
        item = Item("Aged Brie", -3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_366(self):
        item = Item("Aged Brie", -3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_367(self):
        item = Item("Aged Brie", -3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_368(self):
        item = Item("Aged Brie", -3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_369(self):
        item = Item("Aged Brie", -3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_370(self):
        item = Item("Aged Brie", -3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_371(self):
        item = Item("Aged Brie", -3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_372(self):
        item = Item("Aged Brie", -3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_373(self):
        item = Item("Aged Brie", -3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_374(self):
        item = Item("Aged Brie", -3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_375(self):
        item = Item("Aged Brie", -3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_376(self):
        item = Item("Aged Brie", -3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_377(self):
        item = Item("Aged Brie", -3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_378(self):
        item = Item("Aged Brie", -3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_379(self):
        item = Item("Aged Brie", -3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_380(self):
        item = Item("Aged Brie", -3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_381(self):
        item = Item("Aged Brie", -3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_382(self):
        item = Item("Aged Brie", -3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_383(self):
        item = Item("Aged Brie", -3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_384(self):
        item = Item("Aged Brie", -3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_385(self):
        item = Item("Aged Brie", -3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_386(self):
        item = Item("Aged Brie", -3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_387(self):
        item = Item("Aged Brie", -3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_388(self):
        item = Item("Aged Brie", -3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_389(self):
        item = Item("Aged Brie", -3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_390(self):
        item = Item("Aged Brie", -3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_391(self):
        item = Item("Aged Brie", -3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_392(self):
        item = Item("Aged Brie", -3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_393(self):
        item = Item("Aged Brie", -3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_394(self):
        item = Item("Aged Brie", -3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_395(self):
        item = Item("Aged Brie", -3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_396(self):
        item = Item("Aged Brie", -3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_397(self):
        item = Item("Aged Brie", -3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_398(self):
        item = Item("Aged Brie", -3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_399(self):
        item = Item("Aged Brie", -3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_400(self):
        item = Item("Aged Brie", -3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_401(self):
        item = Item("Aged Brie", -2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_402(self):
        item = Item("Aged Brie", -2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_403(self):
        item = Item("Aged Brie", -2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_404(self):
        item = Item("Aged Brie", -2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_405(self):
        item = Item("Aged Brie", -2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_406(self):
        item = Item("Aged Brie", -2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_407(self):
        item = Item("Aged Brie", -2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_408(self):
        item = Item("Aged Brie", -2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_409(self):
        item = Item("Aged Brie", -2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_410(self):
        item = Item("Aged Brie", -2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_411(self):
        item = Item("Aged Brie", -2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_412(self):
        item = Item("Aged Brie", -2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_413(self):
        item = Item("Aged Brie", -2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_414(self):
        item = Item("Aged Brie", -2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_415(self):
        item = Item("Aged Brie", -2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_416(self):
        item = Item("Aged Brie", -2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_417(self):
        item = Item("Aged Brie", -2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_418(self):
        item = Item("Aged Brie", -2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_419(self):
        item = Item("Aged Brie", -2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_420(self):
        item = Item("Aged Brie", -2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_421(self):
        item = Item("Aged Brie", -2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_422(self):
        item = Item("Aged Brie", -2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_423(self):
        item = Item("Aged Brie", -2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_424(self):
        item = Item("Aged Brie", -2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_425(self):
        item = Item("Aged Brie", -2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_426(self):
        item = Item("Aged Brie", -2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_427(self):
        item = Item("Aged Brie", -2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_428(self):
        item = Item("Aged Brie", -2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_429(self):
        item = Item("Aged Brie", -2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_430(self):
        item = Item("Aged Brie", -2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_431(self):
        item = Item("Aged Brie", -2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_432(self):
        item = Item("Aged Brie", -2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_433(self):
        item = Item("Aged Brie", -2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_434(self):
        item = Item("Aged Brie", -2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_435(self):
        item = Item("Aged Brie", -2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_436(self):
        item = Item("Aged Brie", -2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_437(self):
        item = Item("Aged Brie", -2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_438(self):
        item = Item("Aged Brie", -2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_439(self):
        item = Item("Aged Brie", -2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_440(self):
        item = Item("Aged Brie", -2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_441(self):
        item = Item("Aged Brie", -2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_442(self):
        item = Item("Aged Brie", -2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_443(self):
        item = Item("Aged Brie", -2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_444(self):
        item = Item("Aged Brie", -2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_445(self):
        item = Item("Aged Brie", -2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_446(self):
        item = Item("Aged Brie", -2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_447(self):
        item = Item("Aged Brie", -2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_448(self):
        item = Item("Aged Brie", -2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_449(self):
        item = Item("Aged Brie", -2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_450(self):
        item = Item("Aged Brie", -2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_451(self):
        item = Item("Aged Brie", -1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_452(self):
        item = Item("Aged Brie", -1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_453(self):
        item = Item("Aged Brie", -1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_454(self):
        item = Item("Aged Brie", -1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_455(self):
        item = Item("Aged Brie", -1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_456(self):
        item = Item("Aged Brie", -1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_457(self):
        item = Item("Aged Brie", -1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_458(self):
        item = Item("Aged Brie", -1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_459(self):
        item = Item("Aged Brie", -1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_460(self):
        item = Item("Aged Brie", -1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_461(self):
        item = Item("Aged Brie", -1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_462(self):
        item = Item("Aged Brie", -1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_463(self):
        item = Item("Aged Brie", -1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_464(self):
        item = Item("Aged Brie", -1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_465(self):
        item = Item("Aged Brie", -1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_466(self):
        item = Item("Aged Brie", -1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_467(self):
        item = Item("Aged Brie", -1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_468(self):
        item = Item("Aged Brie", -1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_469(self):
        item = Item("Aged Brie", -1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_470(self):
        item = Item("Aged Brie", -1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_471(self):
        item = Item("Aged Brie", -1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_472(self):
        item = Item("Aged Brie", -1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_473(self):
        item = Item("Aged Brie", -1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_474(self):
        item = Item("Aged Brie", -1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_475(self):
        item = Item("Aged Brie", -1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_476(self):
        item = Item("Aged Brie", -1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_477(self):
        item = Item("Aged Brie", -1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_478(self):
        item = Item("Aged Brie", -1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_479(self):
        item = Item("Aged Brie", -1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_480(self):
        item = Item("Aged Brie", -1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_481(self):
        item = Item("Aged Brie", -1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_482(self):
        item = Item("Aged Brie", -1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_483(self):
        item = Item("Aged Brie", -1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_484(self):
        item = Item("Aged Brie", -1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_485(self):
        item = Item("Aged Brie", -1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_486(self):
        item = Item("Aged Brie", -1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_487(self):
        item = Item("Aged Brie", -1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_488(self):
        item = Item("Aged Brie", -1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_489(self):
        item = Item("Aged Brie", -1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_490(self):
        item = Item("Aged Brie", -1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_491(self):
        item = Item("Aged Brie", -1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_492(self):
        item = Item("Aged Brie", -1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_493(self):
        item = Item("Aged Brie", -1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_494(self):
        item = Item("Aged Brie", -1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_495(self):
        item = Item("Aged Brie", -1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_496(self):
        item = Item("Aged Brie", -1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_497(self):
        item = Item("Aged Brie", -1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_498(self):
        item = Item("Aged Brie", -1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_499(self):
        item = Item("Aged Brie", -1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_500(self):
        item = Item("Aged Brie", -1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_501(self):
        item = Item("Aged Brie", 0, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_502(self):
        item = Item("Aged Brie", 0, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_503(self):
        item = Item("Aged Brie", 0, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_504(self):
        item = Item("Aged Brie", 0, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_505(self):
        item = Item("Aged Brie", 0, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_506(self):
        item = Item("Aged Brie", 0, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_507(self):
        item = Item("Aged Brie", 0, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_508(self):
        item = Item("Aged Brie", 0, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_509(self):
        item = Item("Aged Brie", 0, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_510(self):
        item = Item("Aged Brie", 0, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_511(self):
        item = Item("Aged Brie", 0, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_512(self):
        item = Item("Aged Brie", 0, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_513(self):
        item = Item("Aged Brie", 0, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_514(self):
        item = Item("Aged Brie", 0, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_515(self):
        item = Item("Aged Brie", 0, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_516(self):
        item = Item("Aged Brie", 0, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_517(self):
        item = Item("Aged Brie", 0, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_518(self):
        item = Item("Aged Brie", 0, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_519(self):
        item = Item("Aged Brie", 0, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_520(self):
        item = Item("Aged Brie", 0, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_521(self):
        item = Item("Aged Brie", 0, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_522(self):
        item = Item("Aged Brie", 0, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_523(self):
        item = Item("Aged Brie", 0, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_524(self):
        item = Item("Aged Brie", 0, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_525(self):
        item = Item("Aged Brie", 0, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_526(self):
        item = Item("Aged Brie", 0, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_527(self):
        item = Item("Aged Brie", 0, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_528(self):
        item = Item("Aged Brie", 0, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_529(self):
        item = Item("Aged Brie", 0, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_530(self):
        item = Item("Aged Brie", 0, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_531(self):
        item = Item("Aged Brie", 0, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_532(self):
        item = Item("Aged Brie", 0, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_533(self):
        item = Item("Aged Brie", 0, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_534(self):
        item = Item("Aged Brie", 0, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_535(self):
        item = Item("Aged Brie", 0, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_536(self):
        item = Item("Aged Brie", 0, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_537(self):
        item = Item("Aged Brie", 0, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_538(self):
        item = Item("Aged Brie", 0, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_539(self):
        item = Item("Aged Brie", 0, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_540(self):
        item = Item("Aged Brie", 0, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_541(self):
        item = Item("Aged Brie", 0, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_542(self):
        item = Item("Aged Brie", 0, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_543(self):
        item = Item("Aged Brie", 0, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_544(self):
        item = Item("Aged Brie", 0, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_545(self):
        item = Item("Aged Brie", 0, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_546(self):
        item = Item("Aged Brie", 0, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_547(self):
        item = Item("Aged Brie", 0, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_548(self):
        item = Item("Aged Brie", 0, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_549(self):
        item = Item("Aged Brie", 0, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_550(self):
        item = Item("Aged Brie", 0, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_551(self):
        item = Item("Aged Brie", 1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_552(self):
        item = Item("Aged Brie", 1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_553(self):
        item = Item("Aged Brie", 1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_554(self):
        item = Item("Aged Brie", 1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_555(self):
        item = Item("Aged Brie", 1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_556(self):
        item = Item("Aged Brie", 1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_557(self):
        item = Item("Aged Brie", 1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_558(self):
        item = Item("Aged Brie", 1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_559(self):
        item = Item("Aged Brie", 1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_560(self):
        item = Item("Aged Brie", 1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_561(self):
        item = Item("Aged Brie", 1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_562(self):
        item = Item("Aged Brie", 1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_563(self):
        item = Item("Aged Brie", 1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_564(self):
        item = Item("Aged Brie", 1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_565(self):
        item = Item("Aged Brie", 1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_566(self):
        item = Item("Aged Brie", 1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_567(self):
        item = Item("Aged Brie", 1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_568(self):
        item = Item("Aged Brie", 1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_569(self):
        item = Item("Aged Brie", 1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_570(self):
        item = Item("Aged Brie", 1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_571(self):
        item = Item("Aged Brie", 1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_572(self):
        item = Item("Aged Brie", 1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_573(self):
        item = Item("Aged Brie", 1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_574(self):
        item = Item("Aged Brie", 1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_575(self):
        item = Item("Aged Brie", 1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_576(self):
        item = Item("Aged Brie", 1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_577(self):
        item = Item("Aged Brie", 1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_578(self):
        item = Item("Aged Brie", 1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_579(self):
        item = Item("Aged Brie", 1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_580(self):
        item = Item("Aged Brie", 1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_581(self):
        item = Item("Aged Brie", 1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_582(self):
        item = Item("Aged Brie", 1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_583(self):
        item = Item("Aged Brie", 1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_584(self):
        item = Item("Aged Brie", 1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_585(self):
        item = Item("Aged Brie", 1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_586(self):
        item = Item("Aged Brie", 1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_587(self):
        item = Item("Aged Brie", 1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_588(self):
        item = Item("Aged Brie", 1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_589(self):
        item = Item("Aged Brie", 1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_590(self):
        item = Item("Aged Brie", 1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_591(self):
        item = Item("Aged Brie", 1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_592(self):
        item = Item("Aged Brie", 1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_593(self):
        item = Item("Aged Brie", 1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_594(self):
        item = Item("Aged Brie", 1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_595(self):
        item = Item("Aged Brie", 1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_596(self):
        item = Item("Aged Brie", 1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_597(self):
        item = Item("Aged Brie", 1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_598(self):
        item = Item("Aged Brie", 1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_599(self):
        item = Item("Aged Brie", 1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_600(self):
        item = Item("Aged Brie", 1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_601(self):
        item = Item("Aged Brie", 2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_602(self):
        item = Item("Aged Brie", 2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_603(self):
        item = Item("Aged Brie", 2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_604(self):
        item = Item("Aged Brie", 2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_605(self):
        item = Item("Aged Brie", 2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_606(self):
        item = Item("Aged Brie", 2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_607(self):
        item = Item("Aged Brie", 2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_608(self):
        item = Item("Aged Brie", 2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_609(self):
        item = Item("Aged Brie", 2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_610(self):
        item = Item("Aged Brie", 2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_611(self):
        item = Item("Aged Brie", 2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_612(self):
        item = Item("Aged Brie", 2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_613(self):
        item = Item("Aged Brie", 2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_614(self):
        item = Item("Aged Brie", 2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_615(self):
        item = Item("Aged Brie", 2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_616(self):
        item = Item("Aged Brie", 2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_617(self):
        item = Item("Aged Brie", 2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_618(self):
        item = Item("Aged Brie", 2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_619(self):
        item = Item("Aged Brie", 2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_620(self):
        item = Item("Aged Brie", 2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_621(self):
        item = Item("Aged Brie", 2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_622(self):
        item = Item("Aged Brie", 2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_623(self):
        item = Item("Aged Brie", 2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_624(self):
        item = Item("Aged Brie", 2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_625(self):
        item = Item("Aged Brie", 2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_626(self):
        item = Item("Aged Brie", 2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_627(self):
        item = Item("Aged Brie", 2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_628(self):
        item = Item("Aged Brie", 2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_629(self):
        item = Item("Aged Brie", 2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_630(self):
        item = Item("Aged Brie", 2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_631(self):
        item = Item("Aged Brie", 2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_632(self):
        item = Item("Aged Brie", 2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_633(self):
        item = Item("Aged Brie", 2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_634(self):
        item = Item("Aged Brie", 2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_635(self):
        item = Item("Aged Brie", 2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_636(self):
        item = Item("Aged Brie", 2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_637(self):
        item = Item("Aged Brie", 2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_638(self):
        item = Item("Aged Brie", 2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_639(self):
        item = Item("Aged Brie", 2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_640(self):
        item = Item("Aged Brie", 2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_641(self):
        item = Item("Aged Brie", 2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_642(self):
        item = Item("Aged Brie", 2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_643(self):
        item = Item("Aged Brie", 2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_644(self):
        item = Item("Aged Brie", 2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_645(self):
        item = Item("Aged Brie", 2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_646(self):
        item = Item("Aged Brie", 2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_647(self):
        item = Item("Aged Brie", 2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_648(self):
        item = Item("Aged Brie", 2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_649(self):
        item = Item("Aged Brie", 2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_650(self):
        item = Item("Aged Brie", 2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_651(self):
        item = Item("Aged Brie", 3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_652(self):
        item = Item("Aged Brie", 3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_653(self):
        item = Item("Aged Brie", 3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_654(self):
        item = Item("Aged Brie", 3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_655(self):
        item = Item("Aged Brie", 3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_656(self):
        item = Item("Aged Brie", 3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_657(self):
        item = Item("Aged Brie", 3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_658(self):
        item = Item("Aged Brie", 3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_659(self):
        item = Item("Aged Brie", 3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_660(self):
        item = Item("Aged Brie", 3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_661(self):
        item = Item("Aged Brie", 3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_662(self):
        item = Item("Aged Brie", 3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_663(self):
        item = Item("Aged Brie", 3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_664(self):
        item = Item("Aged Brie", 3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_665(self):
        item = Item("Aged Brie", 3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_666(self):
        item = Item("Aged Brie", 3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_667(self):
        item = Item("Aged Brie", 3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_668(self):
        item = Item("Aged Brie", 3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_669(self):
        item = Item("Aged Brie", 3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_670(self):
        item = Item("Aged Brie", 3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_671(self):
        item = Item("Aged Brie", 3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_672(self):
        item = Item("Aged Brie", 3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_673(self):
        item = Item("Aged Brie", 3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_674(self):
        item = Item("Aged Brie", 3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_675(self):
        item = Item("Aged Brie", 3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_676(self):
        item = Item("Aged Brie", 3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_677(self):
        item = Item("Aged Brie", 3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_678(self):
        item = Item("Aged Brie", 3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_679(self):
        item = Item("Aged Brie", 3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_680(self):
        item = Item("Aged Brie", 3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_681(self):
        item = Item("Aged Brie", 3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_682(self):
        item = Item("Aged Brie", 3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_683(self):
        item = Item("Aged Brie", 3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_684(self):
        item = Item("Aged Brie", 3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_685(self):
        item = Item("Aged Brie", 3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_686(self):
        item = Item("Aged Brie", 3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_687(self):
        item = Item("Aged Brie", 3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_688(self):
        item = Item("Aged Brie", 3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_689(self):
        item = Item("Aged Brie", 3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_690(self):
        item = Item("Aged Brie", 3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_691(self):
        item = Item("Aged Brie", 3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_692(self):
        item = Item("Aged Brie", 3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_693(self):
        item = Item("Aged Brie", 3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_694(self):
        item = Item("Aged Brie", 3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_695(self):
        item = Item("Aged Brie", 3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_696(self):
        item = Item("Aged Brie", 3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_697(self):
        item = Item("Aged Brie", 3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_698(self):
        item = Item("Aged Brie", 3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_699(self):
        item = Item("Aged Brie", 3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_700(self):
        item = Item("Aged Brie", 3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_701(self):
        item = Item("Aged Brie", 4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_702(self):
        item = Item("Aged Brie", 4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_703(self):
        item = Item("Aged Brie", 4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_704(self):
        item = Item("Aged Brie", 4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_705(self):
        item = Item("Aged Brie", 4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_706(self):
        item = Item("Aged Brie", 4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_707(self):
        item = Item("Aged Brie", 4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_708(self):
        item = Item("Aged Brie", 4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_709(self):
        item = Item("Aged Brie", 4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_710(self):
        item = Item("Aged Brie", 4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_711(self):
        item = Item("Aged Brie", 4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_712(self):
        item = Item("Aged Brie", 4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_713(self):
        item = Item("Aged Brie", 4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_714(self):
        item = Item("Aged Brie", 4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_715(self):
        item = Item("Aged Brie", 4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_716(self):
        item = Item("Aged Brie", 4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_717(self):
        item = Item("Aged Brie", 4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_718(self):
        item = Item("Aged Brie", 4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_719(self):
        item = Item("Aged Brie", 4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_720(self):
        item = Item("Aged Brie", 4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_721(self):
        item = Item("Aged Brie", 4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_722(self):
        item = Item("Aged Brie", 4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_723(self):
        item = Item("Aged Brie", 4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_724(self):
        item = Item("Aged Brie", 4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_725(self):
        item = Item("Aged Brie", 4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_726(self):
        item = Item("Aged Brie", 4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_727(self):
        item = Item("Aged Brie", 4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_728(self):
        item = Item("Aged Brie", 4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_729(self):
        item = Item("Aged Brie", 4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_730(self):
        item = Item("Aged Brie", 4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_731(self):
        item = Item("Aged Brie", 4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_732(self):
        item = Item("Aged Brie", 4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_733(self):
        item = Item("Aged Brie", 4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_734(self):
        item = Item("Aged Brie", 4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_735(self):
        item = Item("Aged Brie", 4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_736(self):
        item = Item("Aged Brie", 4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_737(self):
        item = Item("Aged Brie", 4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_738(self):
        item = Item("Aged Brie", 4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_739(self):
        item = Item("Aged Brie", 4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_740(self):
        item = Item("Aged Brie", 4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_741(self):
        item = Item("Aged Brie", 4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_742(self):
        item = Item("Aged Brie", 4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_743(self):
        item = Item("Aged Brie", 4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_744(self):
        item = Item("Aged Brie", 4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_745(self):
        item = Item("Aged Brie", 4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_746(self):
        item = Item("Aged Brie", 4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_747(self):
        item = Item("Aged Brie", 4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_748(self):
        item = Item("Aged Brie", 4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_749(self):
        item = Item("Aged Brie", 4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_750(self):
        item = Item("Aged Brie", 4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_751(self):
        item = Item("Aged Brie", 5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_752(self):
        item = Item("Aged Brie", 5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_753(self):
        item = Item("Aged Brie", 5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_754(self):
        item = Item("Aged Brie", 5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_755(self):
        item = Item("Aged Brie", 5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_756(self):
        item = Item("Aged Brie", 5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_757(self):
        item = Item("Aged Brie", 5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_758(self):
        item = Item("Aged Brie", 5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_759(self):
        item = Item("Aged Brie", 5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_760(self):
        item = Item("Aged Brie", 5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_761(self):
        item = Item("Aged Brie", 5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_762(self):
        item = Item("Aged Brie", 5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_763(self):
        item = Item("Aged Brie", 5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_764(self):
        item = Item("Aged Brie", 5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_765(self):
        item = Item("Aged Brie", 5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_766(self):
        item = Item("Aged Brie", 5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_767(self):
        item = Item("Aged Brie", 5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_768(self):
        item = Item("Aged Brie", 5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_769(self):
        item = Item("Aged Brie", 5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_770(self):
        item = Item("Aged Brie", 5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_771(self):
        item = Item("Aged Brie", 5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_772(self):
        item = Item("Aged Brie", 5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_773(self):
        item = Item("Aged Brie", 5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_774(self):
        item = Item("Aged Brie", 5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_775(self):
        item = Item("Aged Brie", 5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_776(self):
        item = Item("Aged Brie", 5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_777(self):
        item = Item("Aged Brie", 5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_778(self):
        item = Item("Aged Brie", 5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_779(self):
        item = Item("Aged Brie", 5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_780(self):
        item = Item("Aged Brie", 5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_781(self):
        item = Item("Aged Brie", 5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_782(self):
        item = Item("Aged Brie", 5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_783(self):
        item = Item("Aged Brie", 5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_784(self):
        item = Item("Aged Brie", 5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_785(self):
        item = Item("Aged Brie", 5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_786(self):
        item = Item("Aged Brie", 5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_787(self):
        item = Item("Aged Brie", 5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_788(self):
        item = Item("Aged Brie", 5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_789(self):
        item = Item("Aged Brie", 5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_790(self):
        item = Item("Aged Brie", 5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_791(self):
        item = Item("Aged Brie", 5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_792(self):
        item = Item("Aged Brie", 5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_793(self):
        item = Item("Aged Brie", 5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_794(self):
        item = Item("Aged Brie", 5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_795(self):
        item = Item("Aged Brie", 5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_796(self):
        item = Item("Aged Brie", 5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_797(self):
        item = Item("Aged Brie", 5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_798(self):
        item = Item("Aged Brie", 5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_799(self):
        item = Item("Aged Brie", 5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_800(self):
        item = Item("Aged Brie", 5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_801(self):
        item = Item("Aged Brie", 6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_802(self):
        item = Item("Aged Brie", 6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_803(self):
        item = Item("Aged Brie", 6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_804(self):
        item = Item("Aged Brie", 6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_805(self):
        item = Item("Aged Brie", 6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_806(self):
        item = Item("Aged Brie", 6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_807(self):
        item = Item("Aged Brie", 6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_808(self):
        item = Item("Aged Brie", 6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_809(self):
        item = Item("Aged Brie", 6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_810(self):
        item = Item("Aged Brie", 6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_811(self):
        item = Item("Aged Brie", 6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_812(self):
        item = Item("Aged Brie", 6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_813(self):
        item = Item("Aged Brie", 6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_814(self):
        item = Item("Aged Brie", 6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_815(self):
        item = Item("Aged Brie", 6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_816(self):
        item = Item("Aged Brie", 6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_817(self):
        item = Item("Aged Brie", 6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_818(self):
        item = Item("Aged Brie", 6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_819(self):
        item = Item("Aged Brie", 6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_820(self):
        item = Item("Aged Brie", 6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_821(self):
        item = Item("Aged Brie", 6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_822(self):
        item = Item("Aged Brie", 6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_823(self):
        item = Item("Aged Brie", 6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_824(self):
        item = Item("Aged Brie", 6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_825(self):
        item = Item("Aged Brie", 6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_826(self):
        item = Item("Aged Brie", 6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_827(self):
        item = Item("Aged Brie", 6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_828(self):
        item = Item("Aged Brie", 6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_829(self):
        item = Item("Aged Brie", 6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_830(self):
        item = Item("Aged Brie", 6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_831(self):
        item = Item("Aged Brie", 6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_832(self):
        item = Item("Aged Brie", 6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_833(self):
        item = Item("Aged Brie", 6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_834(self):
        item = Item("Aged Brie", 6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_835(self):
        item = Item("Aged Brie", 6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_836(self):
        item = Item("Aged Brie", 6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_837(self):
        item = Item("Aged Brie", 6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_838(self):
        item = Item("Aged Brie", 6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_839(self):
        item = Item("Aged Brie", 6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_840(self):
        item = Item("Aged Brie", 6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_841(self):
        item = Item("Aged Brie", 6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_842(self):
        item = Item("Aged Brie", 6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_843(self):
        item = Item("Aged Brie", 6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_844(self):
        item = Item("Aged Brie", 6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_845(self):
        item = Item("Aged Brie", 6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_846(self):
        item = Item("Aged Brie", 6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_847(self):
        item = Item("Aged Brie", 6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_848(self):
        item = Item("Aged Brie", 6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_849(self):
        item = Item("Aged Brie", 6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_850(self):
        item = Item("Aged Brie", 6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_851(self):
        item = Item("Aged Brie", 7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_852(self):
        item = Item("Aged Brie", 7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_853(self):
        item = Item("Aged Brie", 7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_854(self):
        item = Item("Aged Brie", 7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_855(self):
        item = Item("Aged Brie", 7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_856(self):
        item = Item("Aged Brie", 7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_857(self):
        item = Item("Aged Brie", 7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_858(self):
        item = Item("Aged Brie", 7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_859(self):
        item = Item("Aged Brie", 7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_860(self):
        item = Item("Aged Brie", 7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_861(self):
        item = Item("Aged Brie", 7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_862(self):
        item = Item("Aged Brie", 7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_863(self):
        item = Item("Aged Brie", 7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_864(self):
        item = Item("Aged Brie", 7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_865(self):
        item = Item("Aged Brie", 7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_866(self):
        item = Item("Aged Brie", 7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_867(self):
        item = Item("Aged Brie", 7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_868(self):
        item = Item("Aged Brie", 7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_869(self):
        item = Item("Aged Brie", 7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_870(self):
        item = Item("Aged Brie", 7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_871(self):
        item = Item("Aged Brie", 7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_872(self):
        item = Item("Aged Brie", 7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_873(self):
        item = Item("Aged Brie", 7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_874(self):
        item = Item("Aged Brie", 7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_875(self):
        item = Item("Aged Brie", 7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_876(self):
        item = Item("Aged Brie", 7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_877(self):
        item = Item("Aged Brie", 7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_878(self):
        item = Item("Aged Brie", 7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_879(self):
        item = Item("Aged Brie", 7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_880(self):
        item = Item("Aged Brie", 7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_881(self):
        item = Item("Aged Brie", 7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_882(self):
        item = Item("Aged Brie", 7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_883(self):
        item = Item("Aged Brie", 7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_884(self):
        item = Item("Aged Brie", 7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_885(self):
        item = Item("Aged Brie", 7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_886(self):
        item = Item("Aged Brie", 7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_887(self):
        item = Item("Aged Brie", 7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_888(self):
        item = Item("Aged Brie", 7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_889(self):
        item = Item("Aged Brie", 7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_890(self):
        item = Item("Aged Brie", 7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_891(self):
        item = Item("Aged Brie", 7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_892(self):
        item = Item("Aged Brie", 7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_893(self):
        item = Item("Aged Brie", 7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_894(self):
        item = Item("Aged Brie", 7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_895(self):
        item = Item("Aged Brie", 7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_896(self):
        item = Item("Aged Brie", 7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_897(self):
        item = Item("Aged Brie", 7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_898(self):
        item = Item("Aged Brie", 7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_899(self):
        item = Item("Aged Brie", 7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_900(self):
        item = Item("Aged Brie", 7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_901(self):
        item = Item("Aged Brie", 8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_902(self):
        item = Item("Aged Brie", 8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_903(self):
        item = Item("Aged Brie", 8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_904(self):
        item = Item("Aged Brie", 8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_905(self):
        item = Item("Aged Brie", 8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_906(self):
        item = Item("Aged Brie", 8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_907(self):
        item = Item("Aged Brie", 8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_908(self):
        item = Item("Aged Brie", 8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_909(self):
        item = Item("Aged Brie", 8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_910(self):
        item = Item("Aged Brie", 8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_911(self):
        item = Item("Aged Brie", 8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_912(self):
        item = Item("Aged Brie", 8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_913(self):
        item = Item("Aged Brie", 8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_914(self):
        item = Item("Aged Brie", 8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_915(self):
        item = Item("Aged Brie", 8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_916(self):
        item = Item("Aged Brie", 8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_917(self):
        item = Item("Aged Brie", 8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_918(self):
        item = Item("Aged Brie", 8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_919(self):
        item = Item("Aged Brie", 8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_920(self):
        item = Item("Aged Brie", 8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_921(self):
        item = Item("Aged Brie", 8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_922(self):
        item = Item("Aged Brie", 8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_923(self):
        item = Item("Aged Brie", 8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_924(self):
        item = Item("Aged Brie", 8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_925(self):
        item = Item("Aged Brie", 8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_926(self):
        item = Item("Aged Brie", 8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_927(self):
        item = Item("Aged Brie", 8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_928(self):
        item = Item("Aged Brie", 8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_929(self):
        item = Item("Aged Brie", 8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_930(self):
        item = Item("Aged Brie", 8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_931(self):
        item = Item("Aged Brie", 8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_932(self):
        item = Item("Aged Brie", 8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_933(self):
        item = Item("Aged Brie", 8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_934(self):
        item = Item("Aged Brie", 8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_935(self):
        item = Item("Aged Brie", 8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_936(self):
        item = Item("Aged Brie", 8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_937(self):
        item = Item("Aged Brie", 8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_938(self):
        item = Item("Aged Brie", 8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_939(self):
        item = Item("Aged Brie", 8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_940(self):
        item = Item("Aged Brie", 8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_941(self):
        item = Item("Aged Brie", 8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_942(self):
        item = Item("Aged Brie", 8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_943(self):
        item = Item("Aged Brie", 8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_944(self):
        item = Item("Aged Brie", 8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_945(self):
        item = Item("Aged Brie", 8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_946(self):
        item = Item("Aged Brie", 8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_947(self):
        item = Item("Aged Brie", 8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_948(self):
        item = Item("Aged Brie", 8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_949(self):
        item = Item("Aged Brie", 8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_950(self):
        item = Item("Aged Brie", 8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_951(self):
        item = Item("Aged Brie", 9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_952(self):
        item = Item("Aged Brie", 9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_953(self):
        item = Item("Aged Brie", 9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_954(self):
        item = Item("Aged Brie", 9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_955(self):
        item = Item("Aged Brie", 9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_956(self):
        item = Item("Aged Brie", 9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_957(self):
        item = Item("Aged Brie", 9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_958(self):
        item = Item("Aged Brie", 9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_959(self):
        item = Item("Aged Brie", 9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_960(self):
        item = Item("Aged Brie", 9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_961(self):
        item = Item("Aged Brie", 9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_962(self):
        item = Item("Aged Brie", 9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_963(self):
        item = Item("Aged Brie", 9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_964(self):
        item = Item("Aged Brie", 9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_965(self):
        item = Item("Aged Brie", 9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_966(self):
        item = Item("Aged Brie", 9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_967(self):
        item = Item("Aged Brie", 9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_968(self):
        item = Item("Aged Brie", 9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_969(self):
        item = Item("Aged Brie", 9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_970(self):
        item = Item("Aged Brie", 9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_971(self):
        item = Item("Aged Brie", 9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_972(self):
        item = Item("Aged Brie", 9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_973(self):
        item = Item("Aged Brie", 9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_974(self):
        item = Item("Aged Brie", 9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_975(self):
        item = Item("Aged Brie", 9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_976(self):
        item = Item("Aged Brie", 9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_977(self):
        item = Item("Aged Brie", 9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_978(self):
        item = Item("Aged Brie", 9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_979(self):
        item = Item("Aged Brie", 9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_980(self):
        item = Item("Aged Brie", 9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_981(self):
        item = Item("Aged Brie", 9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_982(self):
        item = Item("Aged Brie", 9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_983(self):
        item = Item("Aged Brie", 9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_984(self):
        item = Item("Aged Brie", 9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_985(self):
        item = Item("Aged Brie", 9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_986(self):
        item = Item("Aged Brie", 9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_987(self):
        item = Item("Aged Brie", 9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_988(self):
        item = Item("Aged Brie", 9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_989(self):
        item = Item("Aged Brie", 9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_990(self):
        item = Item("Aged Brie", 9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_991(self):
        item = Item("Aged Brie", 9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_992(self):
        item = Item("Aged Brie", 9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_993(self):
        item = Item("Aged Brie", 9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_994(self):
        item = Item("Aged Brie", 9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_995(self):
        item = Item("Aged Brie", 9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_996(self):
        item = Item("Aged Brie", 9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_997(self):
        item = Item("Aged Brie", 9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_998(self):
        item = Item("Aged Brie", 9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_999(self):
        item = Item("Aged Brie", 9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1000(self):
        item = Item("Aged Brie", 9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_1001(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1002(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1003(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1004(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1005(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1006(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1007(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1008(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1009(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1010(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1011(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1012(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1013(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1014(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1015(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1016(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1017(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1018(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1019(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1020(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1021(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1022(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1023(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1024(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1025(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1026(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1027(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1028(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1029(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1030(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1031(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1032(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1033(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1034(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1035(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1036(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1037(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1038(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1039(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1040(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1041(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1042(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1043(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1044(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1045(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1046(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1047(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1048(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1049(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1050(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1051(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1052(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1053(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1054(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1055(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1056(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1057(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1058(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1059(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1060(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1061(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1062(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1063(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1064(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1065(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1066(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1067(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1068(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1069(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1070(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1071(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1072(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1073(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1074(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1075(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1076(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1077(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1078(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1079(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1080(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1081(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1082(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1083(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1084(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1085(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1086(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1087(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1088(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1089(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1090(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1091(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1092(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1093(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1094(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1095(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1096(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1097(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1098(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1099(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1100(self):
        item = Item("Sulfuras, Hand of Ragnaros", -9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1101(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1102(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1103(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1104(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1105(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1106(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1107(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1108(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1109(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1110(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1111(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1112(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1113(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1114(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1115(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1116(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1117(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1118(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1119(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1120(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1121(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1122(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1123(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1124(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1125(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1126(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1127(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1128(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1129(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1130(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1131(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1132(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1133(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1134(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1135(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1136(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1137(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1138(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1139(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1140(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1141(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1142(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1143(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1144(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1145(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1146(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1147(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1148(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1149(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1150(self):
        item = Item("Sulfuras, Hand of Ragnaros", -8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1151(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1152(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1153(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1154(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1155(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1156(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1157(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1158(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1159(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1160(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1161(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1162(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1163(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1164(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1165(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1166(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1167(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1168(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1169(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1170(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1171(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1172(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1173(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1174(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1175(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1176(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1177(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1178(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1179(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1180(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1181(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1182(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1183(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1184(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1185(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1186(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1187(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1188(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1189(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1190(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1191(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1192(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1193(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1194(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1195(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1196(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1197(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1198(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1199(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1200(self):
        item = Item("Sulfuras, Hand of Ragnaros", -7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1201(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1202(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1203(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1204(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1205(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1206(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1207(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1208(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1209(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1210(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1211(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1212(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1213(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1214(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1215(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1216(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1217(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1218(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1219(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1220(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1221(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1222(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1223(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1224(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1225(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1226(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1227(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1228(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1229(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1230(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1231(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1232(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1233(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1234(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1235(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1236(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1237(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1238(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1239(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1240(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1241(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1242(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1243(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1244(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1245(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1246(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1247(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1248(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1249(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1250(self):
        item = Item("Sulfuras, Hand of Ragnaros", -6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1251(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1252(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1253(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1254(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1255(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1256(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1257(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1258(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1259(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1260(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1261(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1262(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1263(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1264(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1265(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1266(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1267(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1268(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1269(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1270(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1271(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1272(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1273(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1274(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1275(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1276(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1277(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1278(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1279(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1280(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1281(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1282(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1283(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1284(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1285(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1286(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1287(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1288(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1289(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1290(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1291(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1292(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1293(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1294(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1295(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1296(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1297(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1298(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1299(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1300(self):
        item = Item("Sulfuras, Hand of Ragnaros", -5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1301(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1302(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1303(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1304(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1305(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1306(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1307(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1308(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1309(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1310(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1311(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1312(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1313(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1314(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1315(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1316(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1317(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1318(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1319(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1320(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1321(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1322(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1323(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1324(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1325(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1326(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1327(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1328(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1329(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1330(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1331(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1332(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1333(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1334(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1335(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1336(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1337(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1338(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1339(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1340(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1341(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1342(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1343(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1344(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1345(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1346(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1347(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1348(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1349(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1350(self):
        item = Item("Sulfuras, Hand of Ragnaros", -4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1351(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1352(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1353(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1354(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1355(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1356(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1357(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1358(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1359(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1360(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1361(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1362(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1363(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1364(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1365(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1366(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1367(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1368(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1369(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1370(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1371(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1372(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1373(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1374(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1375(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1376(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1377(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1378(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1379(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1380(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1381(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1382(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1383(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1384(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1385(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1386(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1387(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1388(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1389(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1390(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1391(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1392(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1393(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1394(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1395(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1396(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1397(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1398(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1399(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1400(self):
        item = Item("Sulfuras, Hand of Ragnaros", -3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1401(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1402(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1403(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1404(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1405(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1406(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1407(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1408(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1409(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1410(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1411(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1412(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1413(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1414(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1415(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1416(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1417(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1418(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1419(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1420(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1421(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1422(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1423(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1424(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1425(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1426(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1427(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1428(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1429(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1430(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1431(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1432(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1433(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1434(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1435(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1436(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1437(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1438(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1439(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1440(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1441(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1442(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1443(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1444(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1445(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1446(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1447(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1448(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1449(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1450(self):
        item = Item("Sulfuras, Hand of Ragnaros", -2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1451(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1452(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1453(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1454(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1455(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1456(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1457(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1458(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1459(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1460(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1461(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1462(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1463(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1464(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1465(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1466(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1467(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1468(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1469(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1470(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1471(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1472(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1473(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1474(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1475(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1476(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1477(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1478(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1479(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1480(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1481(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1482(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1483(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1484(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1485(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1486(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1487(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1488(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1489(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1490(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1491(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1492(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1493(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1494(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1495(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1496(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1497(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1498(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1499(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1500(self):
        item = Item("Sulfuras, Hand of Ragnaros", -1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1501(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1502(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1503(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1504(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1505(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1506(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1507(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1508(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1509(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1510(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1511(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1512(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1513(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1514(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1515(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1516(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1517(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1518(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1519(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1520(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1521(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1522(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1523(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1524(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1525(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1526(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1527(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1528(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1529(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1530(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1531(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1532(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1533(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1534(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1535(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1536(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1537(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1538(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1539(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1540(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1541(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1542(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1543(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1544(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1545(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1546(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1547(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1548(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1549(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1550(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1551(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1552(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1553(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1554(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1555(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1556(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1557(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1558(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1559(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1560(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1561(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1562(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1563(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1564(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1565(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1566(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1567(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1568(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1569(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1570(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1571(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1572(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1573(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1574(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1575(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1576(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1577(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1578(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1579(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1580(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1581(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1582(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1583(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1584(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1585(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1586(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1587(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1588(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1589(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1590(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1591(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1592(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1593(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1594(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1595(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1596(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1597(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1598(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1599(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1600(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1601(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1602(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1603(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1604(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1605(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1606(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1607(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1608(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1609(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1610(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1611(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1612(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1613(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1614(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1615(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1616(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1617(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1618(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1619(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1620(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1621(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1622(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1623(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1624(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1625(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1626(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1627(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1628(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1629(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1630(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1631(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1632(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1633(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1634(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1635(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1636(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1637(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1638(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1639(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1640(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1641(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1642(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1643(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1644(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1645(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1646(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1647(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1648(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1649(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1650(self):
        item = Item("Sulfuras, Hand of Ragnaros", 2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1651(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1652(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1653(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1654(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1655(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1656(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1657(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1658(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1659(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1660(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1661(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1662(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1663(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1664(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1665(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1666(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1667(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1668(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1669(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1670(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1671(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1672(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1673(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1674(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1675(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1676(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1677(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1678(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1679(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1680(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1681(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1682(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1683(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1684(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1685(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1686(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1687(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1688(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1689(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1690(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1691(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1692(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1693(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1694(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1695(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1696(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1697(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1698(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1699(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1700(self):
        item = Item("Sulfuras, Hand of Ragnaros", 3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1701(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1702(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1703(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1704(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1705(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1706(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1707(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1708(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1709(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1710(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1711(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1712(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1713(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1714(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1715(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1716(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1717(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1718(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1719(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1720(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1721(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1722(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1723(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1724(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1725(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1726(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1727(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1728(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1729(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1730(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1731(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1732(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1733(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1734(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1735(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1736(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1737(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1738(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1739(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1740(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1741(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1742(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1743(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1744(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1745(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1746(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1747(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1748(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1749(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1750(self):
        item = Item("Sulfuras, Hand of Ragnaros", 4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1751(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1752(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1753(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1754(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1755(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1756(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1757(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1758(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1759(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1760(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1761(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1762(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1763(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1764(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1765(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1766(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1767(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1768(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1769(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1770(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1771(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1772(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1773(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1774(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1775(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1776(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1777(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1778(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1779(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1780(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1781(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1782(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1783(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1784(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1785(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1786(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1787(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1788(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1789(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1790(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1791(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1792(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1793(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1794(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1795(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1796(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1797(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1798(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1799(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1800(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1801(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1802(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1803(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1804(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1805(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1806(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1807(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1808(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1809(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1810(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1811(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1812(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1813(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1814(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1815(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1816(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1817(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1818(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1819(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1820(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1821(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1822(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1823(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1824(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1825(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1826(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1827(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1828(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1829(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1830(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1831(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1832(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1833(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1834(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1835(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1836(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1837(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1838(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1839(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1840(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1841(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1842(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1843(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1844(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1845(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1846(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1847(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1848(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1849(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1850(self):
        item = Item("Sulfuras, Hand of Ragnaros", 6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1851(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1852(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1853(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1854(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1855(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1856(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1857(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1858(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1859(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1860(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1861(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1862(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1863(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1864(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1865(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1866(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1867(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1868(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1869(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1870(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1871(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1872(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1873(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1874(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1875(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1876(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1877(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1878(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1879(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1880(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1881(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1882(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1883(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1884(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1885(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1886(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1887(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1888(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1889(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1890(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1891(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1892(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1893(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1894(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1895(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1896(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1897(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1898(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1899(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1900(self):
        item = Item("Sulfuras, Hand of Ragnaros", 7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1901(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1902(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1903(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1904(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1905(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1906(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1907(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1908(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1909(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1910(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1911(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1912(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1913(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1914(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1915(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1916(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1917(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1918(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1919(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1920(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1921(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1922(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1923(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1924(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1925(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1926(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1927(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1928(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1929(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1930(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1931(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1932(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1933(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1934(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1935(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1936(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1937(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1938(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1939(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1940(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1941(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1942(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1943(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1944(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1945(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1946(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1947(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1948(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1949(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_1950(self):
        item = Item("Sulfuras, Hand of Ragnaros", 8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_1951(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_1952(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_1953(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_1954(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_1955(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_1956(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_1957(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_1958(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_1959(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_1960(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_1961(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_1962(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_1963(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_1964(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_1965(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_1966(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_1967(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_1968(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_1969(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_1970(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_1971(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_1972(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_1973(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_1974(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_1975(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_1976(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_1977(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_1978(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_1979(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_1980(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_1981(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_1982(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_1983(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_1984(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_1985(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_1986(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_1987(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_1988(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_1989(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_1990(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_1991(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_1992(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_1993(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_1994(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_1995(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_1996(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_1997(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_1998(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_1999(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2000(self):
        item = Item("Sulfuras, Hand of Ragnaros", 9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(9, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_2001(self):
        item = Item("Regular", -10, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2002(self):
        item = Item("Regular", -10, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2003(self):
        item = Item("Regular", -10, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2004(self):
        item = Item("Regular", -10, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2005(self):
        item = Item("Regular", -10, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2006(self):
        item = Item("Regular", -10, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2007(self):
        item = Item("Regular", -10, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2008(self):
        item = Item("Regular", -10, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2009(self):
        item = Item("Regular", -10, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2010(self):
        item = Item("Regular", -10, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2011(self):
        item = Item("Regular", -10, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2012(self):
        item = Item("Regular", -10, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2013(self):
        item = Item("Regular", -10, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2014(self):
        item = Item("Regular", -10, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2015(self):
        item = Item("Regular", -10, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2016(self):
        item = Item("Regular", -10, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2017(self):
        item = Item("Regular", -10, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2018(self):
        item = Item("Regular", -10, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2019(self):
        item = Item("Regular", -10, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2020(self):
        item = Item("Regular", -10, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2021(self):
        item = Item("Regular", -10, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2022(self):
        item = Item("Regular", -10, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2023(self):
        item = Item("Regular", -10, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2024(self):
        item = Item("Regular", -10, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2025(self):
        item = Item("Regular", -10, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2026(self):
        item = Item("Regular", -10, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2027(self):
        item = Item("Regular", -10, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2028(self):
        item = Item("Regular", -10, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2029(self):
        item = Item("Regular", -10, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2030(self):
        item = Item("Regular", -10, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2031(self):
        item = Item("Regular", -10, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2032(self):
        item = Item("Regular", -10, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2033(self):
        item = Item("Regular", -10, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2034(self):
        item = Item("Regular", -10, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2035(self):
        item = Item("Regular", -10, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2036(self):
        item = Item("Regular", -10, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2037(self):
        item = Item("Regular", -10, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2038(self):
        item = Item("Regular", -10, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2039(self):
        item = Item("Regular", -10, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2040(self):
        item = Item("Regular", -10, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2041(self):
        item = Item("Regular", -10, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2042(self):
        item = Item("Regular", -10, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2043(self):
        item = Item("Regular", -10, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2044(self):
        item = Item("Regular", -10, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2045(self):
        item = Item("Regular", -10, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2046(self):
        item = Item("Regular", -10, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2047(self):
        item = Item("Regular", -10, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2048(self):
        item = Item("Regular", -10, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2049(self):
        item = Item("Regular", -10, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2050(self):
        item = Item("Regular", -10, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2051(self):
        item = Item("Regular", -9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2052(self):
        item = Item("Regular", -9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2053(self):
        item = Item("Regular", -9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2054(self):
        item = Item("Regular", -9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2055(self):
        item = Item("Regular", -9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2056(self):
        item = Item("Regular", -9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2057(self):
        item = Item("Regular", -9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2058(self):
        item = Item("Regular", -9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2059(self):
        item = Item("Regular", -9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2060(self):
        item = Item("Regular", -9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2061(self):
        item = Item("Regular", -9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2062(self):
        item = Item("Regular", -9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2063(self):
        item = Item("Regular", -9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2064(self):
        item = Item("Regular", -9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2065(self):
        item = Item("Regular", -9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2066(self):
        item = Item("Regular", -9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2067(self):
        item = Item("Regular", -9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2068(self):
        item = Item("Regular", -9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2069(self):
        item = Item("Regular", -9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2070(self):
        item = Item("Regular", -9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2071(self):
        item = Item("Regular", -9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2072(self):
        item = Item("Regular", -9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2073(self):
        item = Item("Regular", -9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2074(self):
        item = Item("Regular", -9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2075(self):
        item = Item("Regular", -9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2076(self):
        item = Item("Regular", -9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2077(self):
        item = Item("Regular", -9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2078(self):
        item = Item("Regular", -9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2079(self):
        item = Item("Regular", -9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2080(self):
        item = Item("Regular", -9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2081(self):
        item = Item("Regular", -9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2082(self):
        item = Item("Regular", -9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2083(self):
        item = Item("Regular", -9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2084(self):
        item = Item("Regular", -9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2085(self):
        item = Item("Regular", -9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2086(self):
        item = Item("Regular", -9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2087(self):
        item = Item("Regular", -9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2088(self):
        item = Item("Regular", -9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2089(self):
        item = Item("Regular", -9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2090(self):
        item = Item("Regular", -9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2091(self):
        item = Item("Regular", -9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2092(self):
        item = Item("Regular", -9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2093(self):
        item = Item("Regular", -9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2094(self):
        item = Item("Regular", -9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2095(self):
        item = Item("Regular", -9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2096(self):
        item = Item("Regular", -9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2097(self):
        item = Item("Regular", -9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2098(self):
        item = Item("Regular", -9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2099(self):
        item = Item("Regular", -9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2100(self):
        item = Item("Regular", -9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2101(self):
        item = Item("Regular", -8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2102(self):
        item = Item("Regular", -8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2103(self):
        item = Item("Regular", -8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2104(self):
        item = Item("Regular", -8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2105(self):
        item = Item("Regular", -8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2106(self):
        item = Item("Regular", -8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2107(self):
        item = Item("Regular", -8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2108(self):
        item = Item("Regular", -8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2109(self):
        item = Item("Regular", -8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2110(self):
        item = Item("Regular", -8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2111(self):
        item = Item("Regular", -8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2112(self):
        item = Item("Regular", -8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2113(self):
        item = Item("Regular", -8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2114(self):
        item = Item("Regular", -8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2115(self):
        item = Item("Regular", -8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2116(self):
        item = Item("Regular", -8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2117(self):
        item = Item("Regular", -8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2118(self):
        item = Item("Regular", -8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2119(self):
        item = Item("Regular", -8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2120(self):
        item = Item("Regular", -8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2121(self):
        item = Item("Regular", -8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2122(self):
        item = Item("Regular", -8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2123(self):
        item = Item("Regular", -8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2124(self):
        item = Item("Regular", -8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2125(self):
        item = Item("Regular", -8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2126(self):
        item = Item("Regular", -8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2127(self):
        item = Item("Regular", -8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2128(self):
        item = Item("Regular", -8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2129(self):
        item = Item("Regular", -8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2130(self):
        item = Item("Regular", -8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2131(self):
        item = Item("Regular", -8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2132(self):
        item = Item("Regular", -8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2133(self):
        item = Item("Regular", -8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2134(self):
        item = Item("Regular", -8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2135(self):
        item = Item("Regular", -8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2136(self):
        item = Item("Regular", -8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2137(self):
        item = Item("Regular", -8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2138(self):
        item = Item("Regular", -8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2139(self):
        item = Item("Regular", -8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2140(self):
        item = Item("Regular", -8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2141(self):
        item = Item("Regular", -8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2142(self):
        item = Item("Regular", -8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2143(self):
        item = Item("Regular", -8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2144(self):
        item = Item("Regular", -8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2145(self):
        item = Item("Regular", -8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2146(self):
        item = Item("Regular", -8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2147(self):
        item = Item("Regular", -8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2148(self):
        item = Item("Regular", -8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2149(self):
        item = Item("Regular", -8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2150(self):
        item = Item("Regular", -8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2151(self):
        item = Item("Regular", -7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2152(self):
        item = Item("Regular", -7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2153(self):
        item = Item("Regular", -7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2154(self):
        item = Item("Regular", -7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2155(self):
        item = Item("Regular", -7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2156(self):
        item = Item("Regular", -7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2157(self):
        item = Item("Regular", -7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2158(self):
        item = Item("Regular", -7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2159(self):
        item = Item("Regular", -7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2160(self):
        item = Item("Regular", -7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2161(self):
        item = Item("Regular", -7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2162(self):
        item = Item("Regular", -7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2163(self):
        item = Item("Regular", -7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2164(self):
        item = Item("Regular", -7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2165(self):
        item = Item("Regular", -7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2166(self):
        item = Item("Regular", -7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2167(self):
        item = Item("Regular", -7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2168(self):
        item = Item("Regular", -7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2169(self):
        item = Item("Regular", -7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2170(self):
        item = Item("Regular", -7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2171(self):
        item = Item("Regular", -7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2172(self):
        item = Item("Regular", -7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2173(self):
        item = Item("Regular", -7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2174(self):
        item = Item("Regular", -7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2175(self):
        item = Item("Regular", -7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2176(self):
        item = Item("Regular", -7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2177(self):
        item = Item("Regular", -7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2178(self):
        item = Item("Regular", -7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2179(self):
        item = Item("Regular", -7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2180(self):
        item = Item("Regular", -7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2181(self):
        item = Item("Regular", -7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2182(self):
        item = Item("Regular", -7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2183(self):
        item = Item("Regular", -7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2184(self):
        item = Item("Regular", -7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2185(self):
        item = Item("Regular", -7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2186(self):
        item = Item("Regular", -7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2187(self):
        item = Item("Regular", -7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2188(self):
        item = Item("Regular", -7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2189(self):
        item = Item("Regular", -7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2190(self):
        item = Item("Regular", -7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2191(self):
        item = Item("Regular", -7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2192(self):
        item = Item("Regular", -7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2193(self):
        item = Item("Regular", -7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2194(self):
        item = Item("Regular", -7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2195(self):
        item = Item("Regular", -7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2196(self):
        item = Item("Regular", -7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2197(self):
        item = Item("Regular", -7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2198(self):
        item = Item("Regular", -7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2199(self):
        item = Item("Regular", -7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2200(self):
        item = Item("Regular", -7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2201(self):
        item = Item("Regular", -6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2202(self):
        item = Item("Regular", -6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2203(self):
        item = Item("Regular", -6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2204(self):
        item = Item("Regular", -6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2205(self):
        item = Item("Regular", -6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2206(self):
        item = Item("Regular", -6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2207(self):
        item = Item("Regular", -6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2208(self):
        item = Item("Regular", -6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2209(self):
        item = Item("Regular", -6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2210(self):
        item = Item("Regular", -6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2211(self):
        item = Item("Regular", -6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2212(self):
        item = Item("Regular", -6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2213(self):
        item = Item("Regular", -6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2214(self):
        item = Item("Regular", -6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2215(self):
        item = Item("Regular", -6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2216(self):
        item = Item("Regular", -6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2217(self):
        item = Item("Regular", -6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2218(self):
        item = Item("Regular", -6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2219(self):
        item = Item("Regular", -6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2220(self):
        item = Item("Regular", -6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2221(self):
        item = Item("Regular", -6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2222(self):
        item = Item("Regular", -6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2223(self):
        item = Item("Regular", -6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2224(self):
        item = Item("Regular", -6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2225(self):
        item = Item("Regular", -6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2226(self):
        item = Item("Regular", -6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2227(self):
        item = Item("Regular", -6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2228(self):
        item = Item("Regular", -6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2229(self):
        item = Item("Regular", -6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2230(self):
        item = Item("Regular", -6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2231(self):
        item = Item("Regular", -6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2232(self):
        item = Item("Regular", -6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2233(self):
        item = Item("Regular", -6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2234(self):
        item = Item("Regular", -6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2235(self):
        item = Item("Regular", -6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2236(self):
        item = Item("Regular", -6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2237(self):
        item = Item("Regular", -6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2238(self):
        item = Item("Regular", -6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2239(self):
        item = Item("Regular", -6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2240(self):
        item = Item("Regular", -6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2241(self):
        item = Item("Regular", -6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2242(self):
        item = Item("Regular", -6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2243(self):
        item = Item("Regular", -6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2244(self):
        item = Item("Regular", -6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2245(self):
        item = Item("Regular", -6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2246(self):
        item = Item("Regular", -6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2247(self):
        item = Item("Regular", -6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2248(self):
        item = Item("Regular", -6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2249(self):
        item = Item("Regular", -6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2250(self):
        item = Item("Regular", -6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2251(self):
        item = Item("Regular", -5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2252(self):
        item = Item("Regular", -5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2253(self):
        item = Item("Regular", -5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2254(self):
        item = Item("Regular", -5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2255(self):
        item = Item("Regular", -5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2256(self):
        item = Item("Regular", -5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2257(self):
        item = Item("Regular", -5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2258(self):
        item = Item("Regular", -5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2259(self):
        item = Item("Regular", -5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2260(self):
        item = Item("Regular", -5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2261(self):
        item = Item("Regular", -5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2262(self):
        item = Item("Regular", -5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2263(self):
        item = Item("Regular", -5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2264(self):
        item = Item("Regular", -5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2265(self):
        item = Item("Regular", -5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2266(self):
        item = Item("Regular", -5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2267(self):
        item = Item("Regular", -5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2268(self):
        item = Item("Regular", -5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2269(self):
        item = Item("Regular", -5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2270(self):
        item = Item("Regular", -5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2271(self):
        item = Item("Regular", -5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2272(self):
        item = Item("Regular", -5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2273(self):
        item = Item("Regular", -5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2274(self):
        item = Item("Regular", -5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2275(self):
        item = Item("Regular", -5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2276(self):
        item = Item("Regular", -5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2277(self):
        item = Item("Regular", -5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2278(self):
        item = Item("Regular", -5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2279(self):
        item = Item("Regular", -5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2280(self):
        item = Item("Regular", -5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2281(self):
        item = Item("Regular", -5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2282(self):
        item = Item("Regular", -5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2283(self):
        item = Item("Regular", -5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2284(self):
        item = Item("Regular", -5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2285(self):
        item = Item("Regular", -5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2286(self):
        item = Item("Regular", -5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2287(self):
        item = Item("Regular", -5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2288(self):
        item = Item("Regular", -5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2289(self):
        item = Item("Regular", -5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2290(self):
        item = Item("Regular", -5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2291(self):
        item = Item("Regular", -5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2292(self):
        item = Item("Regular", -5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2293(self):
        item = Item("Regular", -5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2294(self):
        item = Item("Regular", -5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2295(self):
        item = Item("Regular", -5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2296(self):
        item = Item("Regular", -5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2297(self):
        item = Item("Regular", -5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2298(self):
        item = Item("Regular", -5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2299(self):
        item = Item("Regular", -5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2300(self):
        item = Item("Regular", -5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2301(self):
        item = Item("Regular", -4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2302(self):
        item = Item("Regular", -4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2303(self):
        item = Item("Regular", -4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2304(self):
        item = Item("Regular", -4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2305(self):
        item = Item("Regular", -4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2306(self):
        item = Item("Regular", -4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2307(self):
        item = Item("Regular", -4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2308(self):
        item = Item("Regular", -4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2309(self):
        item = Item("Regular", -4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2310(self):
        item = Item("Regular", -4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2311(self):
        item = Item("Regular", -4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2312(self):
        item = Item("Regular", -4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2313(self):
        item = Item("Regular", -4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2314(self):
        item = Item("Regular", -4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2315(self):
        item = Item("Regular", -4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2316(self):
        item = Item("Regular", -4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2317(self):
        item = Item("Regular", -4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2318(self):
        item = Item("Regular", -4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2319(self):
        item = Item("Regular", -4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2320(self):
        item = Item("Regular", -4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2321(self):
        item = Item("Regular", -4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2322(self):
        item = Item("Regular", -4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2323(self):
        item = Item("Regular", -4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2324(self):
        item = Item("Regular", -4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2325(self):
        item = Item("Regular", -4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2326(self):
        item = Item("Regular", -4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2327(self):
        item = Item("Regular", -4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2328(self):
        item = Item("Regular", -4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2329(self):
        item = Item("Regular", -4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2330(self):
        item = Item("Regular", -4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2331(self):
        item = Item("Regular", -4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2332(self):
        item = Item("Regular", -4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2333(self):
        item = Item("Regular", -4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2334(self):
        item = Item("Regular", -4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2335(self):
        item = Item("Regular", -4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2336(self):
        item = Item("Regular", -4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2337(self):
        item = Item("Regular", -4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2338(self):
        item = Item("Regular", -4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2339(self):
        item = Item("Regular", -4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2340(self):
        item = Item("Regular", -4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2341(self):
        item = Item("Regular", -4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2342(self):
        item = Item("Regular", -4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2343(self):
        item = Item("Regular", -4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2344(self):
        item = Item("Regular", -4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2345(self):
        item = Item("Regular", -4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2346(self):
        item = Item("Regular", -4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2347(self):
        item = Item("Regular", -4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2348(self):
        item = Item("Regular", -4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2349(self):
        item = Item("Regular", -4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2350(self):
        item = Item("Regular", -4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2351(self):
        item = Item("Regular", -3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2352(self):
        item = Item("Regular", -3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2353(self):
        item = Item("Regular", -3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2354(self):
        item = Item("Regular", -3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2355(self):
        item = Item("Regular", -3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2356(self):
        item = Item("Regular", -3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2357(self):
        item = Item("Regular", -3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2358(self):
        item = Item("Regular", -3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2359(self):
        item = Item("Regular", -3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2360(self):
        item = Item("Regular", -3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2361(self):
        item = Item("Regular", -3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2362(self):
        item = Item("Regular", -3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2363(self):
        item = Item("Regular", -3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2364(self):
        item = Item("Regular", -3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2365(self):
        item = Item("Regular", -3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2366(self):
        item = Item("Regular", -3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2367(self):
        item = Item("Regular", -3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2368(self):
        item = Item("Regular", -3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2369(self):
        item = Item("Regular", -3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2370(self):
        item = Item("Regular", -3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2371(self):
        item = Item("Regular", -3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2372(self):
        item = Item("Regular", -3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2373(self):
        item = Item("Regular", -3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2374(self):
        item = Item("Regular", -3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2375(self):
        item = Item("Regular", -3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2376(self):
        item = Item("Regular", -3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2377(self):
        item = Item("Regular", -3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2378(self):
        item = Item("Regular", -3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2379(self):
        item = Item("Regular", -3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2380(self):
        item = Item("Regular", -3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2381(self):
        item = Item("Regular", -3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2382(self):
        item = Item("Regular", -3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2383(self):
        item = Item("Regular", -3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2384(self):
        item = Item("Regular", -3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2385(self):
        item = Item("Regular", -3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2386(self):
        item = Item("Regular", -3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2387(self):
        item = Item("Regular", -3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2388(self):
        item = Item("Regular", -3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2389(self):
        item = Item("Regular", -3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2390(self):
        item = Item("Regular", -3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2391(self):
        item = Item("Regular", -3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2392(self):
        item = Item("Regular", -3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2393(self):
        item = Item("Regular", -3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2394(self):
        item = Item("Regular", -3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2395(self):
        item = Item("Regular", -3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2396(self):
        item = Item("Regular", -3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2397(self):
        item = Item("Regular", -3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2398(self):
        item = Item("Regular", -3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2399(self):
        item = Item("Regular", -3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2400(self):
        item = Item("Regular", -3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2401(self):
        item = Item("Regular", -2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2402(self):
        item = Item("Regular", -2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2403(self):
        item = Item("Regular", -2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2404(self):
        item = Item("Regular", -2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2405(self):
        item = Item("Regular", -2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2406(self):
        item = Item("Regular", -2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2407(self):
        item = Item("Regular", -2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2408(self):
        item = Item("Regular", -2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2409(self):
        item = Item("Regular", -2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2410(self):
        item = Item("Regular", -2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2411(self):
        item = Item("Regular", -2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2412(self):
        item = Item("Regular", -2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2413(self):
        item = Item("Regular", -2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2414(self):
        item = Item("Regular", -2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2415(self):
        item = Item("Regular", -2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2416(self):
        item = Item("Regular", -2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2417(self):
        item = Item("Regular", -2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2418(self):
        item = Item("Regular", -2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2419(self):
        item = Item("Regular", -2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2420(self):
        item = Item("Regular", -2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2421(self):
        item = Item("Regular", -2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2422(self):
        item = Item("Regular", -2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2423(self):
        item = Item("Regular", -2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2424(self):
        item = Item("Regular", -2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2425(self):
        item = Item("Regular", -2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2426(self):
        item = Item("Regular", -2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2427(self):
        item = Item("Regular", -2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2428(self):
        item = Item("Regular", -2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2429(self):
        item = Item("Regular", -2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2430(self):
        item = Item("Regular", -2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2431(self):
        item = Item("Regular", -2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2432(self):
        item = Item("Regular", -2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2433(self):
        item = Item("Regular", -2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2434(self):
        item = Item("Regular", -2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2435(self):
        item = Item("Regular", -2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2436(self):
        item = Item("Regular", -2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2437(self):
        item = Item("Regular", -2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2438(self):
        item = Item("Regular", -2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2439(self):
        item = Item("Regular", -2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2440(self):
        item = Item("Regular", -2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2441(self):
        item = Item("Regular", -2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2442(self):
        item = Item("Regular", -2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2443(self):
        item = Item("Regular", -2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2444(self):
        item = Item("Regular", -2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2445(self):
        item = Item("Regular", -2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2446(self):
        item = Item("Regular", -2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2447(self):
        item = Item("Regular", -2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2448(self):
        item = Item("Regular", -2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2449(self):
        item = Item("Regular", -2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2450(self):
        item = Item("Regular", -2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2451(self):
        item = Item("Regular", -1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2452(self):
        item = Item("Regular", -1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2453(self):
        item = Item("Regular", -1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2454(self):
        item = Item("Regular", -1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2455(self):
        item = Item("Regular", -1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2456(self):
        item = Item("Regular", -1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2457(self):
        item = Item("Regular", -1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2458(self):
        item = Item("Regular", -1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2459(self):
        item = Item("Regular", -1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2460(self):
        item = Item("Regular", -1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2461(self):
        item = Item("Regular", -1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2462(self):
        item = Item("Regular", -1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2463(self):
        item = Item("Regular", -1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2464(self):
        item = Item("Regular", -1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2465(self):
        item = Item("Regular", -1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2466(self):
        item = Item("Regular", -1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2467(self):
        item = Item("Regular", -1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2468(self):
        item = Item("Regular", -1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2469(self):
        item = Item("Regular", -1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2470(self):
        item = Item("Regular", -1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2471(self):
        item = Item("Regular", -1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2472(self):
        item = Item("Regular", -1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2473(self):
        item = Item("Regular", -1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2474(self):
        item = Item("Regular", -1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2475(self):
        item = Item("Regular", -1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2476(self):
        item = Item("Regular", -1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2477(self):
        item = Item("Regular", -1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2478(self):
        item = Item("Regular", -1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2479(self):
        item = Item("Regular", -1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2480(self):
        item = Item("Regular", -1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2481(self):
        item = Item("Regular", -1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2482(self):
        item = Item("Regular", -1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2483(self):
        item = Item("Regular", -1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2484(self):
        item = Item("Regular", -1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2485(self):
        item = Item("Regular", -1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2486(self):
        item = Item("Regular", -1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2487(self):
        item = Item("Regular", -1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2488(self):
        item = Item("Regular", -1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2489(self):
        item = Item("Regular", -1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2490(self):
        item = Item("Regular", -1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2491(self):
        item = Item("Regular", -1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2492(self):
        item = Item("Regular", -1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2493(self):
        item = Item("Regular", -1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2494(self):
        item = Item("Regular", -1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2495(self):
        item = Item("Regular", -1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2496(self):
        item = Item("Regular", -1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2497(self):
        item = Item("Regular", -1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2498(self):
        item = Item("Regular", -1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2499(self):
        item = Item("Regular", -1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2500(self):
        item = Item("Regular", -1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2501(self):
        item = Item("Regular", 0, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2502(self):
        item = Item("Regular", 0, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2503(self):
        item = Item("Regular", 0, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2504(self):
        item = Item("Regular", 0, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2505(self):
        item = Item("Regular", 0, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2506(self):
        item = Item("Regular", 0, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2507(self):
        item = Item("Regular", 0, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2508(self):
        item = Item("Regular", 0, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2509(self):
        item = Item("Regular", 0, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2510(self):
        item = Item("Regular", 0, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2511(self):
        item = Item("Regular", 0, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2512(self):
        item = Item("Regular", 0, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2513(self):
        item = Item("Regular", 0, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2514(self):
        item = Item("Regular", 0, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2515(self):
        item = Item("Regular", 0, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2516(self):
        item = Item("Regular", 0, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2517(self):
        item = Item("Regular", 0, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2518(self):
        item = Item("Regular", 0, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2519(self):
        item = Item("Regular", 0, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2520(self):
        item = Item("Regular", 0, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2521(self):
        item = Item("Regular", 0, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2522(self):
        item = Item("Regular", 0, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2523(self):
        item = Item("Regular", 0, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2524(self):
        item = Item("Regular", 0, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2525(self):
        item = Item("Regular", 0, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2526(self):
        item = Item("Regular", 0, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2527(self):
        item = Item("Regular", 0, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2528(self):
        item = Item("Regular", 0, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2529(self):
        item = Item("Regular", 0, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2530(self):
        item = Item("Regular", 0, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2531(self):
        item = Item("Regular", 0, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2532(self):
        item = Item("Regular", 0, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2533(self):
        item = Item("Regular", 0, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2534(self):
        item = Item("Regular", 0, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2535(self):
        item = Item("Regular", 0, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2536(self):
        item = Item("Regular", 0, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2537(self):
        item = Item("Regular", 0, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2538(self):
        item = Item("Regular", 0, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2539(self):
        item = Item("Regular", 0, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2540(self):
        item = Item("Regular", 0, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2541(self):
        item = Item("Regular", 0, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2542(self):
        item = Item("Regular", 0, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2543(self):
        item = Item("Regular", 0, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2544(self):
        item = Item("Regular", 0, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2545(self):
        item = Item("Regular", 0, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2546(self):
        item = Item("Regular", 0, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2547(self):
        item = Item("Regular", 0, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2548(self):
        item = Item("Regular", 0, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2549(self):
        item = Item("Regular", 0, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2550(self):
        item = Item("Regular", 0, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2551(self):
        item = Item("Regular", 1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2552(self):
        item = Item("Regular", 1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2553(self):
        item = Item("Regular", 1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2554(self):
        item = Item("Regular", 1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2555(self):
        item = Item("Regular", 1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2556(self):
        item = Item("Regular", 1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2557(self):
        item = Item("Regular", 1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2558(self):
        item = Item("Regular", 1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2559(self):
        item = Item("Regular", 1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2560(self):
        item = Item("Regular", 1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2561(self):
        item = Item("Regular", 1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2562(self):
        item = Item("Regular", 1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2563(self):
        item = Item("Regular", 1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2564(self):
        item = Item("Regular", 1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2565(self):
        item = Item("Regular", 1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2566(self):
        item = Item("Regular", 1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2567(self):
        item = Item("Regular", 1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2568(self):
        item = Item("Regular", 1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2569(self):
        item = Item("Regular", 1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2570(self):
        item = Item("Regular", 1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2571(self):
        item = Item("Regular", 1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2572(self):
        item = Item("Regular", 1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2573(self):
        item = Item("Regular", 1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2574(self):
        item = Item("Regular", 1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2575(self):
        item = Item("Regular", 1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2576(self):
        item = Item("Regular", 1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2577(self):
        item = Item("Regular", 1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2578(self):
        item = Item("Regular", 1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2579(self):
        item = Item("Regular", 1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2580(self):
        item = Item("Regular", 1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2581(self):
        item = Item("Regular", 1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2582(self):
        item = Item("Regular", 1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2583(self):
        item = Item("Regular", 1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2584(self):
        item = Item("Regular", 1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2585(self):
        item = Item("Regular", 1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2586(self):
        item = Item("Regular", 1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2587(self):
        item = Item("Regular", 1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2588(self):
        item = Item("Regular", 1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2589(self):
        item = Item("Regular", 1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2590(self):
        item = Item("Regular", 1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2591(self):
        item = Item("Regular", 1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2592(self):
        item = Item("Regular", 1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2593(self):
        item = Item("Regular", 1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2594(self):
        item = Item("Regular", 1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2595(self):
        item = Item("Regular", 1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2596(self):
        item = Item("Regular", 1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2597(self):
        item = Item("Regular", 1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2598(self):
        item = Item("Regular", 1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2599(self):
        item = Item("Regular", 1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2600(self):
        item = Item("Regular", 1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2601(self):
        item = Item("Regular", 2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2602(self):
        item = Item("Regular", 2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2603(self):
        item = Item("Regular", 2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2604(self):
        item = Item("Regular", 2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2605(self):
        item = Item("Regular", 2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2606(self):
        item = Item("Regular", 2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2607(self):
        item = Item("Regular", 2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2608(self):
        item = Item("Regular", 2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2609(self):
        item = Item("Regular", 2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2610(self):
        item = Item("Regular", 2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2611(self):
        item = Item("Regular", 2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2612(self):
        item = Item("Regular", 2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2613(self):
        item = Item("Regular", 2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2614(self):
        item = Item("Regular", 2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2615(self):
        item = Item("Regular", 2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2616(self):
        item = Item("Regular", 2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2617(self):
        item = Item("Regular", 2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2618(self):
        item = Item("Regular", 2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2619(self):
        item = Item("Regular", 2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2620(self):
        item = Item("Regular", 2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2621(self):
        item = Item("Regular", 2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2622(self):
        item = Item("Regular", 2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2623(self):
        item = Item("Regular", 2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2624(self):
        item = Item("Regular", 2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2625(self):
        item = Item("Regular", 2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2626(self):
        item = Item("Regular", 2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2627(self):
        item = Item("Regular", 2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2628(self):
        item = Item("Regular", 2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2629(self):
        item = Item("Regular", 2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2630(self):
        item = Item("Regular", 2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2631(self):
        item = Item("Regular", 2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2632(self):
        item = Item("Regular", 2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2633(self):
        item = Item("Regular", 2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2634(self):
        item = Item("Regular", 2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2635(self):
        item = Item("Regular", 2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2636(self):
        item = Item("Regular", 2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2637(self):
        item = Item("Regular", 2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2638(self):
        item = Item("Regular", 2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2639(self):
        item = Item("Regular", 2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2640(self):
        item = Item("Regular", 2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2641(self):
        item = Item("Regular", 2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2642(self):
        item = Item("Regular", 2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2643(self):
        item = Item("Regular", 2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2644(self):
        item = Item("Regular", 2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2645(self):
        item = Item("Regular", 2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2646(self):
        item = Item("Regular", 2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2647(self):
        item = Item("Regular", 2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2648(self):
        item = Item("Regular", 2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2649(self):
        item = Item("Regular", 2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2650(self):
        item = Item("Regular", 2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2651(self):
        item = Item("Regular", 3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2652(self):
        item = Item("Regular", 3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2653(self):
        item = Item("Regular", 3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2654(self):
        item = Item("Regular", 3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2655(self):
        item = Item("Regular", 3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2656(self):
        item = Item("Regular", 3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2657(self):
        item = Item("Regular", 3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2658(self):
        item = Item("Regular", 3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2659(self):
        item = Item("Regular", 3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2660(self):
        item = Item("Regular", 3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2661(self):
        item = Item("Regular", 3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2662(self):
        item = Item("Regular", 3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2663(self):
        item = Item("Regular", 3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2664(self):
        item = Item("Regular", 3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2665(self):
        item = Item("Regular", 3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2666(self):
        item = Item("Regular", 3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2667(self):
        item = Item("Regular", 3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2668(self):
        item = Item("Regular", 3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2669(self):
        item = Item("Regular", 3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2670(self):
        item = Item("Regular", 3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2671(self):
        item = Item("Regular", 3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2672(self):
        item = Item("Regular", 3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2673(self):
        item = Item("Regular", 3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2674(self):
        item = Item("Regular", 3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2675(self):
        item = Item("Regular", 3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2676(self):
        item = Item("Regular", 3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2677(self):
        item = Item("Regular", 3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2678(self):
        item = Item("Regular", 3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2679(self):
        item = Item("Regular", 3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2680(self):
        item = Item("Regular", 3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2681(self):
        item = Item("Regular", 3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2682(self):
        item = Item("Regular", 3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2683(self):
        item = Item("Regular", 3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2684(self):
        item = Item("Regular", 3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2685(self):
        item = Item("Regular", 3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2686(self):
        item = Item("Regular", 3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2687(self):
        item = Item("Regular", 3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2688(self):
        item = Item("Regular", 3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2689(self):
        item = Item("Regular", 3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2690(self):
        item = Item("Regular", 3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2691(self):
        item = Item("Regular", 3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2692(self):
        item = Item("Regular", 3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2693(self):
        item = Item("Regular", 3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2694(self):
        item = Item("Regular", 3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2695(self):
        item = Item("Regular", 3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2696(self):
        item = Item("Regular", 3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2697(self):
        item = Item("Regular", 3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2698(self):
        item = Item("Regular", 3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2699(self):
        item = Item("Regular", 3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2700(self):
        item = Item("Regular", 3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2701(self):
        item = Item("Regular", 4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2702(self):
        item = Item("Regular", 4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2703(self):
        item = Item("Regular", 4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2704(self):
        item = Item("Regular", 4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2705(self):
        item = Item("Regular", 4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2706(self):
        item = Item("Regular", 4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2707(self):
        item = Item("Regular", 4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2708(self):
        item = Item("Regular", 4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2709(self):
        item = Item("Regular", 4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2710(self):
        item = Item("Regular", 4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2711(self):
        item = Item("Regular", 4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2712(self):
        item = Item("Regular", 4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2713(self):
        item = Item("Regular", 4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2714(self):
        item = Item("Regular", 4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2715(self):
        item = Item("Regular", 4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2716(self):
        item = Item("Regular", 4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2717(self):
        item = Item("Regular", 4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2718(self):
        item = Item("Regular", 4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2719(self):
        item = Item("Regular", 4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2720(self):
        item = Item("Regular", 4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2721(self):
        item = Item("Regular", 4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2722(self):
        item = Item("Regular", 4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2723(self):
        item = Item("Regular", 4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2724(self):
        item = Item("Regular", 4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2725(self):
        item = Item("Regular", 4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2726(self):
        item = Item("Regular", 4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2727(self):
        item = Item("Regular", 4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2728(self):
        item = Item("Regular", 4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2729(self):
        item = Item("Regular", 4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2730(self):
        item = Item("Regular", 4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2731(self):
        item = Item("Regular", 4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2732(self):
        item = Item("Regular", 4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2733(self):
        item = Item("Regular", 4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2734(self):
        item = Item("Regular", 4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2735(self):
        item = Item("Regular", 4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2736(self):
        item = Item("Regular", 4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2737(self):
        item = Item("Regular", 4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2738(self):
        item = Item("Regular", 4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2739(self):
        item = Item("Regular", 4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2740(self):
        item = Item("Regular", 4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2741(self):
        item = Item("Regular", 4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2742(self):
        item = Item("Regular", 4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2743(self):
        item = Item("Regular", 4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2744(self):
        item = Item("Regular", 4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2745(self):
        item = Item("Regular", 4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2746(self):
        item = Item("Regular", 4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2747(self):
        item = Item("Regular", 4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2748(self):
        item = Item("Regular", 4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2749(self):
        item = Item("Regular", 4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2750(self):
        item = Item("Regular", 4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2751(self):
        item = Item("Regular", 5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2752(self):
        item = Item("Regular", 5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2753(self):
        item = Item("Regular", 5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2754(self):
        item = Item("Regular", 5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2755(self):
        item = Item("Regular", 5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2756(self):
        item = Item("Regular", 5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2757(self):
        item = Item("Regular", 5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2758(self):
        item = Item("Regular", 5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2759(self):
        item = Item("Regular", 5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2760(self):
        item = Item("Regular", 5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2761(self):
        item = Item("Regular", 5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2762(self):
        item = Item("Regular", 5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2763(self):
        item = Item("Regular", 5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2764(self):
        item = Item("Regular", 5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2765(self):
        item = Item("Regular", 5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2766(self):
        item = Item("Regular", 5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2767(self):
        item = Item("Regular", 5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2768(self):
        item = Item("Regular", 5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2769(self):
        item = Item("Regular", 5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2770(self):
        item = Item("Regular", 5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2771(self):
        item = Item("Regular", 5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2772(self):
        item = Item("Regular", 5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2773(self):
        item = Item("Regular", 5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2774(self):
        item = Item("Regular", 5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2775(self):
        item = Item("Regular", 5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2776(self):
        item = Item("Regular", 5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2777(self):
        item = Item("Regular", 5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2778(self):
        item = Item("Regular", 5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2779(self):
        item = Item("Regular", 5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2780(self):
        item = Item("Regular", 5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2781(self):
        item = Item("Regular", 5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2782(self):
        item = Item("Regular", 5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2783(self):
        item = Item("Regular", 5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2784(self):
        item = Item("Regular", 5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2785(self):
        item = Item("Regular", 5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2786(self):
        item = Item("Regular", 5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2787(self):
        item = Item("Regular", 5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2788(self):
        item = Item("Regular", 5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2789(self):
        item = Item("Regular", 5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2790(self):
        item = Item("Regular", 5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2791(self):
        item = Item("Regular", 5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2792(self):
        item = Item("Regular", 5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2793(self):
        item = Item("Regular", 5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2794(self):
        item = Item("Regular", 5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2795(self):
        item = Item("Regular", 5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2796(self):
        item = Item("Regular", 5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2797(self):
        item = Item("Regular", 5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2798(self):
        item = Item("Regular", 5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2799(self):
        item = Item("Regular", 5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2800(self):
        item = Item("Regular", 5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2801(self):
        item = Item("Regular", 6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2802(self):
        item = Item("Regular", 6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2803(self):
        item = Item("Regular", 6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2804(self):
        item = Item("Regular", 6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2805(self):
        item = Item("Regular", 6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2806(self):
        item = Item("Regular", 6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2807(self):
        item = Item("Regular", 6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2808(self):
        item = Item("Regular", 6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2809(self):
        item = Item("Regular", 6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2810(self):
        item = Item("Regular", 6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2811(self):
        item = Item("Regular", 6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2812(self):
        item = Item("Regular", 6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2813(self):
        item = Item("Regular", 6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2814(self):
        item = Item("Regular", 6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2815(self):
        item = Item("Regular", 6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2816(self):
        item = Item("Regular", 6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2817(self):
        item = Item("Regular", 6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2818(self):
        item = Item("Regular", 6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2819(self):
        item = Item("Regular", 6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2820(self):
        item = Item("Regular", 6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2821(self):
        item = Item("Regular", 6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2822(self):
        item = Item("Regular", 6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2823(self):
        item = Item("Regular", 6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2824(self):
        item = Item("Regular", 6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2825(self):
        item = Item("Regular", 6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2826(self):
        item = Item("Regular", 6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2827(self):
        item = Item("Regular", 6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2828(self):
        item = Item("Regular", 6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2829(self):
        item = Item("Regular", 6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2830(self):
        item = Item("Regular", 6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2831(self):
        item = Item("Regular", 6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2832(self):
        item = Item("Regular", 6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2833(self):
        item = Item("Regular", 6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2834(self):
        item = Item("Regular", 6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2835(self):
        item = Item("Regular", 6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2836(self):
        item = Item("Regular", 6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2837(self):
        item = Item("Regular", 6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2838(self):
        item = Item("Regular", 6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2839(self):
        item = Item("Regular", 6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2840(self):
        item = Item("Regular", 6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2841(self):
        item = Item("Regular", 6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2842(self):
        item = Item("Regular", 6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2843(self):
        item = Item("Regular", 6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2844(self):
        item = Item("Regular", 6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2845(self):
        item = Item("Regular", 6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2846(self):
        item = Item("Regular", 6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2847(self):
        item = Item("Regular", 6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2848(self):
        item = Item("Regular", 6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2849(self):
        item = Item("Regular", 6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2850(self):
        item = Item("Regular", 6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2851(self):
        item = Item("Regular", 7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2852(self):
        item = Item("Regular", 7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2853(self):
        item = Item("Regular", 7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2854(self):
        item = Item("Regular", 7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2855(self):
        item = Item("Regular", 7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2856(self):
        item = Item("Regular", 7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2857(self):
        item = Item("Regular", 7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2858(self):
        item = Item("Regular", 7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2859(self):
        item = Item("Regular", 7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2860(self):
        item = Item("Regular", 7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2861(self):
        item = Item("Regular", 7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2862(self):
        item = Item("Regular", 7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2863(self):
        item = Item("Regular", 7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2864(self):
        item = Item("Regular", 7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2865(self):
        item = Item("Regular", 7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2866(self):
        item = Item("Regular", 7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2867(self):
        item = Item("Regular", 7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2868(self):
        item = Item("Regular", 7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2869(self):
        item = Item("Regular", 7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2870(self):
        item = Item("Regular", 7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2871(self):
        item = Item("Regular", 7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2872(self):
        item = Item("Regular", 7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2873(self):
        item = Item("Regular", 7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2874(self):
        item = Item("Regular", 7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2875(self):
        item = Item("Regular", 7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2876(self):
        item = Item("Regular", 7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2877(self):
        item = Item("Regular", 7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2878(self):
        item = Item("Regular", 7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2879(self):
        item = Item("Regular", 7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2880(self):
        item = Item("Regular", 7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2881(self):
        item = Item("Regular", 7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2882(self):
        item = Item("Regular", 7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2883(self):
        item = Item("Regular", 7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2884(self):
        item = Item("Regular", 7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2885(self):
        item = Item("Regular", 7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2886(self):
        item = Item("Regular", 7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2887(self):
        item = Item("Regular", 7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2888(self):
        item = Item("Regular", 7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2889(self):
        item = Item("Regular", 7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2890(self):
        item = Item("Regular", 7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2891(self):
        item = Item("Regular", 7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2892(self):
        item = Item("Regular", 7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2893(self):
        item = Item("Regular", 7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2894(self):
        item = Item("Regular", 7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2895(self):
        item = Item("Regular", 7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2896(self):
        item = Item("Regular", 7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2897(self):
        item = Item("Regular", 7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2898(self):
        item = Item("Regular", 7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2899(self):
        item = Item("Regular", 7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2900(self):
        item = Item("Regular", 7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2901(self):
        item = Item("Regular", 8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2902(self):
        item = Item("Regular", 8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2903(self):
        item = Item("Regular", 8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2904(self):
        item = Item("Regular", 8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2905(self):
        item = Item("Regular", 8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2906(self):
        item = Item("Regular", 8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2907(self):
        item = Item("Regular", 8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2908(self):
        item = Item("Regular", 8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2909(self):
        item = Item("Regular", 8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2910(self):
        item = Item("Regular", 8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2911(self):
        item = Item("Regular", 8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2912(self):
        item = Item("Regular", 8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2913(self):
        item = Item("Regular", 8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2914(self):
        item = Item("Regular", 8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2915(self):
        item = Item("Regular", 8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2916(self):
        item = Item("Regular", 8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2917(self):
        item = Item("Regular", 8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2918(self):
        item = Item("Regular", 8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2919(self):
        item = Item("Regular", 8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2920(self):
        item = Item("Regular", 8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2921(self):
        item = Item("Regular", 8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2922(self):
        item = Item("Regular", 8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2923(self):
        item = Item("Regular", 8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2924(self):
        item = Item("Regular", 8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2925(self):
        item = Item("Regular", 8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2926(self):
        item = Item("Regular", 8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2927(self):
        item = Item("Regular", 8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2928(self):
        item = Item("Regular", 8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2929(self):
        item = Item("Regular", 8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2930(self):
        item = Item("Regular", 8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2931(self):
        item = Item("Regular", 8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2932(self):
        item = Item("Regular", 8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2933(self):
        item = Item("Regular", 8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2934(self):
        item = Item("Regular", 8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2935(self):
        item = Item("Regular", 8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2936(self):
        item = Item("Regular", 8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2937(self):
        item = Item("Regular", 8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2938(self):
        item = Item("Regular", 8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2939(self):
        item = Item("Regular", 8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2940(self):
        item = Item("Regular", 8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2941(self):
        item = Item("Regular", 8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2942(self):
        item = Item("Regular", 8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2943(self):
        item = Item("Regular", 8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2944(self):
        item = Item("Regular", 8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2945(self):
        item = Item("Regular", 8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2946(self):
        item = Item("Regular", 8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2947(self):
        item = Item("Regular", 8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2948(self):
        item = Item("Regular", 8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2949(self):
        item = Item("Regular", 8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_2950(self):
        item = Item("Regular", 8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_2951(self):
        item = Item("Regular", 9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2952(self):
        item = Item("Regular", 9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_2953(self):
        item = Item("Regular", 9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(1, item.quality)


    def test_2954(self):
        item = Item("Regular", 9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_2955(self):
        item = Item("Regular", 9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_2956(self):
        item = Item("Regular", 9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_2957(self):
        item = Item("Regular", 9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_2958(self):
        item = Item("Regular", 9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_2959(self):
        item = Item("Regular", 9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_2960(self):
        item = Item("Regular", 9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_2961(self):
        item = Item("Regular", 9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_2962(self):
        item = Item("Regular", 9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_2963(self):
        item = Item("Regular", 9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_2964(self):
        item = Item("Regular", 9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_2965(self):
        item = Item("Regular", 9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_2966(self):
        item = Item("Regular", 9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_2967(self):
        item = Item("Regular", 9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_2968(self):
        item = Item("Regular", 9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_2969(self):
        item = Item("Regular", 9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_2970(self):
        item = Item("Regular", 9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_2971(self):
        item = Item("Regular", 9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_2972(self):
        item = Item("Regular", 9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_2973(self):
        item = Item("Regular", 9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_2974(self):
        item = Item("Regular", 9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_2975(self):
        item = Item("Regular", 9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_2976(self):
        item = Item("Regular", 9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_2977(self):
        item = Item("Regular", 9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_2978(self):
        item = Item("Regular", 9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_2979(self):
        item = Item("Regular", 9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_2980(self):
        item = Item("Regular", 9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_2981(self):
        item = Item("Regular", 9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_2982(self):
        item = Item("Regular", 9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_2983(self):
        item = Item("Regular", 9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_2984(self):
        item = Item("Regular", 9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_2985(self):
        item = Item("Regular", 9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_2986(self):
        item = Item("Regular", 9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_2987(self):
        item = Item("Regular", 9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_2988(self):
        item = Item("Regular", 9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_2989(self):
        item = Item("Regular", 9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_2990(self):
        item = Item("Regular", 9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_2991(self):
        item = Item("Regular", 9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_2992(self):
        item = Item("Regular", 9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_2993(self):
        item = Item("Regular", 9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_2994(self):
        item = Item("Regular", 9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_2995(self):
        item = Item("Regular", 9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_2996(self):
        item = Item("Regular", 9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_2997(self):
        item = Item("Regular", 9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_2998(self):
        item = Item("Regular", 9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_2999(self):
        item = Item("Regular", 9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3000(self):
        item = Item("Regular", 9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3001(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3002(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3003(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3004(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3005(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3006(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3007(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3008(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3009(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3010(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3011(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3012(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3013(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3014(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3015(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3016(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3017(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3018(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3019(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3020(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3021(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3022(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3023(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3024(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3025(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3026(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3027(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3028(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3029(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3030(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3031(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3032(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3033(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3034(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3035(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3036(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3037(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3038(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3039(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3040(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3041(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3042(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3043(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3044(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3045(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3046(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3047(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3048(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3049(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3050(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -10, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-11, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3051(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3052(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3053(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3054(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3055(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3056(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3057(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3058(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3059(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3060(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3061(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3062(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3063(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3064(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3065(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3066(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3067(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3068(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3069(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3070(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3071(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3072(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3073(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3074(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3075(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3076(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3077(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3078(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3079(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3080(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3081(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3082(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3083(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3084(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3085(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3086(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3087(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3088(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3089(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3090(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3091(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3092(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3093(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3094(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3095(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3096(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3097(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3098(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3099(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3100(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-10, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3101(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3102(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3103(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3104(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3105(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3106(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3107(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3108(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3109(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3110(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3111(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3112(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3113(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3114(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3115(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3116(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3117(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3118(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3119(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3120(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3121(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3122(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3123(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3124(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3125(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3126(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3127(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3128(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3129(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3130(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3131(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3132(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3133(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3134(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3135(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3136(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3137(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3138(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3139(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3140(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3141(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3142(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3143(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3144(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3145(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3146(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3147(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3148(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3149(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3150(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-9, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3151(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3152(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3153(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3154(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3155(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3156(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3157(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3158(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3159(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3160(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3161(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3162(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3163(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3164(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3165(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3166(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3167(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3168(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3169(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3170(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3171(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3172(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3173(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3174(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3175(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3176(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3177(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3178(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3179(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3180(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3181(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3182(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3183(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3184(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3185(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3186(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3187(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3188(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3189(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3190(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3191(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3192(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3193(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3194(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3195(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3196(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3197(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3198(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3199(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3200(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-8, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3201(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3202(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3203(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3204(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3205(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3206(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3207(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3208(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3209(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3210(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3211(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3212(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3213(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3214(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3215(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3216(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3217(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3218(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3219(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3220(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3221(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3222(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3223(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3224(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3225(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3226(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3227(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3228(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3229(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3230(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3231(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3232(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3233(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3234(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3235(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3236(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3237(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3238(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3239(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3240(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3241(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3242(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3243(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3244(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3245(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3246(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3247(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3248(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3249(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3250(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-7, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3251(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3252(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3253(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3254(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3255(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3256(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3257(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3258(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3259(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3260(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3261(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3262(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3263(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3264(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3265(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3266(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3267(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3268(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3269(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3270(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3271(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3272(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3273(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3274(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3275(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3276(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3277(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3278(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3279(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3280(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3281(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3282(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3283(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3284(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3285(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3286(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3287(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3288(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3289(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3290(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3291(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3292(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3293(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3294(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3295(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3296(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3297(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3298(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3299(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3300(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3301(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3302(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3303(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3304(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3305(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3306(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3307(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3308(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3309(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3310(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3311(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3312(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3313(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3314(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3315(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3316(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3317(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3318(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3319(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3320(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3321(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3322(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3323(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3324(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3325(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3326(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3327(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3328(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3329(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3330(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3331(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3332(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3333(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3334(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3335(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3336(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3337(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3338(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3339(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3340(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3341(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3342(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3343(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3344(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3345(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3346(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3347(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3348(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3349(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3350(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-5, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3351(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3352(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3353(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3354(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3355(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3356(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3357(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3358(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3359(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3360(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3361(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3362(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3363(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3364(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3365(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3366(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3367(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3368(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3369(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3370(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3371(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3372(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3373(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3374(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3375(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3376(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3377(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3378(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3379(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3380(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3381(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3382(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3383(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3384(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3385(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3386(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3387(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3388(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3389(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3390(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3391(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3392(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3393(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3394(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3395(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3396(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3397(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3398(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3399(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3400(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-4, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3401(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3402(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3403(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3404(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3405(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3406(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3407(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3408(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3409(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3410(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3411(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3412(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3413(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3414(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3415(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3416(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3417(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3418(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3419(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3420(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3421(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3422(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3423(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3424(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3425(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3426(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3427(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3428(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3429(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3430(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3431(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3432(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3433(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3434(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3435(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3436(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3437(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3438(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3439(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3440(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3441(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3442(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3443(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3444(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3445(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3446(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3447(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3448(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3449(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3450(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-3, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3451(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3452(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3453(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3454(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3455(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3456(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3457(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3458(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3459(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3460(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3461(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3462(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3463(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3464(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3465(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3466(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3467(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3468(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3469(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3470(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3471(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3472(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3473(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3474(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3475(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3476(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3477(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3478(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3479(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3480(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3481(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3482(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3483(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3484(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3485(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3486(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3487(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3488(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3489(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3490(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3491(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3492(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3493(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3494(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3495(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3496(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3497(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3498(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3499(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3500(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-2, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3501(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3502(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3503(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3504(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3505(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3506(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3507(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3508(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3509(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3510(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3511(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3512(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3513(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3514(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3515(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3516(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3517(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3518(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3519(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3520(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3521(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3522(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3523(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3524(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3525(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3526(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3527(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3528(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3529(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3530(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3531(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3532(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3533(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3534(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3535(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3536(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3537(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3538(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3539(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3540(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3541(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3542(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3543(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3544(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3545(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3546(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3547(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3548(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3549(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3550(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


    def test_3551(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3552(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3553(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3554(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3555(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3556(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3557(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3558(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3559(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3560(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3561(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3562(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3563(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3564(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3565(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3566(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3567(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3568(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3569(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3570(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3571(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3572(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3573(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3574(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3575(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3576(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3577(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3578(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3579(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3580(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3581(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3582(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3583(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3584(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3585(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3586(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3587(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3588(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3589(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3590(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3591(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3592(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3593(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3594(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3595(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3596(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3597(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3598(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3599(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3600(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3601(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3602(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3603(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3604(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3605(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3606(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3607(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3608(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3609(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3610(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3611(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3612(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3613(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3614(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3615(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3616(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3617(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3618(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3619(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3620(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3621(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3622(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3623(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3624(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3625(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3626(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3627(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3628(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3629(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3630(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3631(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3632(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3633(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3634(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3635(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3636(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3637(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3638(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3639(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3640(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3641(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3642(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3643(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3644(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3645(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3646(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3647(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3648(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3649(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3650(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(1, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3651(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3652(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3653(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3654(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3655(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3656(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3657(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3658(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3659(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3660(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3661(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3662(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3663(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3664(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3665(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3666(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3667(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3668(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3669(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3670(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3671(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3672(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3673(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3674(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3675(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3676(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3677(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3678(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3679(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3680(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3681(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3682(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3683(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3684(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3685(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3686(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3687(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3688(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3689(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3690(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3691(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3692(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3693(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3694(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3695(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3696(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3697(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3698(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3699(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3700(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 3, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(2, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3701(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3702(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3703(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3704(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3705(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3706(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3707(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3708(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3709(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3710(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3711(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3712(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3713(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3714(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3715(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3716(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3717(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3718(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3719(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3720(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3721(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3722(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3723(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3724(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3725(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3726(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3727(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3728(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3729(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3730(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3731(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3732(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3733(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3734(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3735(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3736(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3737(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3738(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3739(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3740(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3741(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3742(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3743(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3744(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3745(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3746(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3747(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3748(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3749(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3750(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(3, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3751(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3752(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3753(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3754(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3755(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3756(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3757(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3758(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3759(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3760(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3761(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3762(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3763(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3764(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3765(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3766(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3767(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3768(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3769(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3770(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3771(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3772(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3773(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3774(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3775(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3776(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3777(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3778(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3779(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3780(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3781(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3782(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3783(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3784(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3785(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3786(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3787(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3788(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3789(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3790(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3791(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3792(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3793(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3794(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3795(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3796(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3797(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3798(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3799(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3800(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(4, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3801(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_3802(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3803(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3804(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3805(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3806(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3807(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3808(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3809(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3810(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3811(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3812(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3813(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3814(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3815(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3816(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3817(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3818(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3819(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3820(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3821(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3822(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3823(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3824(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3825(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3826(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3827(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3828(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3829(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3830(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3831(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3832(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3833(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3834(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3835(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3836(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3837(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3838(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3839(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3840(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3841(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3842(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3843(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3844(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3845(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3846(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3847(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3848(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3849(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3850(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 6, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(5, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3851(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_3852(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3853(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3854(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3855(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3856(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3857(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3858(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3859(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3860(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3861(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3862(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3863(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3864(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3865(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3866(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3867(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3868(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3869(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3870(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3871(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3872(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3873(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3874(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3875(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3876(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3877(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3878(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3879(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3880(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3881(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3882(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3883(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3884(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3885(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3886(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3887(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3888(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3889(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3890(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3891(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3892(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3893(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3894(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3895(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3896(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3897(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3898(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3899(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3900(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 7, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(6, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3901(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_3902(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3903(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3904(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3905(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3906(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3907(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3908(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3909(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3910(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3911(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3912(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3913(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3914(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3915(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3916(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3917(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3918(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3919(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3920(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3921(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3922(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3923(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3924(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3925(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3926(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3927(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3928(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3929(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3930(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3931(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3932(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3933(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3934(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3935(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3936(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3937(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3938(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3939(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3940(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3941(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3942(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3943(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3944(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3945(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3946(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3947(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3948(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3949(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3950(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(7, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_3951(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 0)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(2, item.quality)


    def test_3952(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 1)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(3, item.quality)


    def test_3953(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 2)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(4, item.quality)


    def test_3954(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 3)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(5, item.quality)


    def test_3955(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 4)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(6, item.quality)


    def test_3956(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 5)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(7, item.quality)


    def test_3957(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 6)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(8, item.quality)


    def test_3958(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 7)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(9, item.quality)


    def test_3959(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 8)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(10, item.quality)


    def test_3960(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 9)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(11, item.quality)


    def test_3961(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(12, item.quality)


    def test_3962(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 11)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(13, item.quality)


    def test_3963(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 12)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(14, item.quality)


    def test_3964(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 13)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(15, item.quality)


    def test_3965(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 14)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(16, item.quality)


    def test_3966(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 15)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(17, item.quality)


    def test_3967(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 16)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(18, item.quality)


    def test_3968(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 17)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(19, item.quality)


    def test_3969(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 18)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(20, item.quality)


    def test_3970(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 19)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(21, item.quality)


    def test_3971(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 20)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(22, item.quality)


    def test_3972(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 21)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(23, item.quality)


    def test_3973(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 22)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(24, item.quality)


    def test_3974(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 23)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(25, item.quality)


    def test_3975(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 24)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(26, item.quality)


    def test_3976(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 25)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(27, item.quality)


    def test_3977(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 26)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(28, item.quality)


    def test_3978(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 27)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(29, item.quality)


    def test_3979(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 28)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(30, item.quality)


    def test_3980(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 29)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(31, item.quality)


    def test_3981(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 30)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(32, item.quality)


    def test_3982(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 31)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(33, item.quality)


    def test_3983(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 32)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(34, item.quality)


    def test_3984(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 33)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(35, item.quality)


    def test_3985(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 34)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(36, item.quality)


    def test_3986(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 35)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(37, item.quality)


    def test_3987(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 36)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(38, item.quality)


    def test_3988(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 37)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(39, item.quality)


    def test_3989(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 38)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(40, item.quality)


    def test_3990(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 39)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(41, item.quality)


    def test_3991(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 40)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(42, item.quality)


    def test_3992(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 41)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(43, item.quality)


    def test_3993(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 42)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(44, item.quality)


    def test_3994(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 43)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(45, item.quality)


    def test_3995(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 44)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(46, item.quality)


    def test_3996(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 45)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(47, item.quality)


    def test_3997(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 46)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(48, item.quality)


    def test_3998(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 47)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(49, item.quality)


    def test_3999(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 48)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(50, item.quality)


    def test_4000(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 49)
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals(8, item.sell_in)
        self.assertEquals(50, item.quality)

