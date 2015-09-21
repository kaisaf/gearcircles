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

        self.category1 = Category(name="skiing", description="downhill skiing")
        self.category1.save()
        Category.objects.create(name="ski boots", description="Downhill skiing boots")
        self.category2 = Category.objects.get(name="ski boots")
        self.category2.save()

        self.category2_size = CategoryProperty(
            name="size",
            description="boot size",
            mandatory=True,
            input_type=2 #float
        )
        self.category2_size.save()
        self.category2_size.categories.add(self.category2)

        self.gear1 = Gear(
            name="telemark skis",
            description="the best skis",
            brand="Black Diamond",
            price="2000",
            preferred_contact=1, #email
            payment=1, #paypal
            expiration_date=date.today(),
            user=self.kaisa
        )
        self.gear1.save()
        self.gear1.categories.add(self.category1)

        self.gear2 = Gear(
            name="telemark boots",
            description="the best boots",
            brand="Scarpa",
            price="2500",
            preferred_contact=1, #email
            payment=1, #paypal
            expiration_date=date.today(),
            user=self.kaisa
        )
        self.gear2.save()
        self.gear2.categories.add(self.category1)
        self.gear2.categories.add(self.category2)

        self.gear2_size = GearProperty(value=24.5, gear=self.gear2, category_property=self.category2_size)
        self.gear2_size.save()


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
