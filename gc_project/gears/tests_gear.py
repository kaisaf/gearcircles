from django.test import TestCase
from gears.models import Category, CategoryProperty, Gear, GearProperty, GearAvailability, GearImage
from users.models import User
from datetime import date


class GearTestCase(TestCase):
    def setUp(self):
        self.kaisa = User(name="Kaisa", email="kaisa@kaisa.com", phone="345-435-344", score=10)
        self.kaisa.save()
        self.victor = User(name="Victor", email="victor@victor.com", phone="3443-343", score=9.75)
        self.victor.save()

        self.skiing = Category(name="skiing", description="downhill skiing")
        self.skiing.save()
        Category.objects.create(name="ski boots", description="Downhill skiing boots")
        self.ski_boots = Category.objects.get(name="ski boots")
        self.ski_boots.save()

        self.boot_size = CategoryProperty(
            name="size",
            description="boot size",
            mandatory=True,
            input_type=2 #float
        )
        self.boot_size.save()
        self.boot_size.categories.add(self.ski_boots)

        self.skis = Gear(
            name="telemark skis",
            description="the best skis",
            brand="Black Diamond",
            price="2000",
            preferred_contact=1, #email
            payment=1, #paypal
            expiration_date=date.today(),
            user=self.kaisa
        )
        self.skis.save()
        self.skis.categories.add(self.skiing)

        self.boots = Gear(
            name="telemark boots",
            description="the best boots",
            brand="Scarpa",
            price="2500",
            preferred_contact=1, #email
            payment=1, #paypal
            expiration_date=date.today(),
            user=self.kaisa
        )
        self.boots.save()
        self.boots.categories.add(self.skiing)
        self.boots.categories.add(self.ski_boots)

        self.gear1_size = GearProperty(value=24.5, gear=self.boots, category_property=self.boot_size)
        self.gear1_size.save()


    def test_get_gear(self):
        gear1 = Gear.objects.get(name="telemark boots")
        self.assertEqual(gear1.payment, 1)

    def test_list_all_gear(self):
        self.assertEqual(len(Gear.objects.all()), 2)

    def test_get_gear_category(self):
        gear1 = Gear.objects.get(name="telemark boots")
        self.assertEqual(len(gear1.categories.all()), 2)
        gear2 = Gear.objects.get(name="telemark skis")
        self.assertEqual(gear2.categories.first().name, "skiing")
        
