from django.test import TestCase
from users.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.kaisa = User(email="kaisa@kaisa.com", phone="345-435-344", score=10)
        self.kaisa.save()
        User.objects.create(email="victor@victor.com", phone="3443-343", score=9.75)

    def test_query_user(self):
        self.assertEqual(len(User.objects.all()), 2)
        self.assertEqual(self.kaisa.score, 10)
        victor = User.objects.get(email="victor@victor.com")
        self.assertEqual(victor.phone, "3443-343")
