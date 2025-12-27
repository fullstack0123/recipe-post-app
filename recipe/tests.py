from django.test import TestCase
from django.urls import reverse_lazy
from recipe.models import Recipe
# from django.contrib.auth.models import User

# Create your tests here.

# ▼▼▼ 追加 ▼▼▼
class TestRecipe(TestCase):

    fixtures = ["recipe.json", "user.json", ]  # === 追加 ===
    # fixtures = ["recipe_utf8.json", "user_utf8.json"]

    def setUp(self):
        self.recipe_list = Recipe.objects.all()

    def test_top_page(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_recipe_top(self):
        res = self.client.get("/recipe/")
        self.assertEqual(res.status_code, 200)

    def test_recipe_detail(self):
        for recipe in self.recipe_list:
            res = self.client.get(reverse_lazy("recipe:detail", kwargs={"pk": recipe.id}))
            self.assertEqual(res.status_code, 200)
