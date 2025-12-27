from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin #=== この行を追加 ===

from recipe.models import Recipe
from recipe.forms import RecipeForm


class StaffroomMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")

class StaffroomTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "staffroom/index.html"

    # ▼▼▼ 追加 ▼▼▼
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['recipe_list'] = Recipe.objects.all()
        # ▼▼▼ ここから修正 ▼▼▼
        if self.request.user.is_authenticated:
            # context['recipe_list'] = Recipe.objects.filter(user=self.request.user)
            context['recipe_list'] = Recipe.objects.filter(user=self.request.user).prefetch_related("comment_set")
        else:
            context['recipe_list'] = None
        # ▲▲▲ ここまで修正 ▲▲▲

        return context
    # ▲▲▲ 追加 ▲▲▲

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    # login_url = "login"
    form_class = RecipeForm
    # fields = ["title", "content", "description", "image"]
    success_url = reverse_lazy("recipe:index")

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.POST.dict()
        data['user'] = user.id
        form = RecipeForm(data=data, files=request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ["title", "content", "description", "image"]

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("recipe:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)
