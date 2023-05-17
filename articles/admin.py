from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    # Проверка на наличие одного основного раздела для статьи
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_count = is_main_count + 1
        if is_main_count == 0:
            raise ValidationError('Необходимо выбрать основной раздел')
        elif is_main_count > 1:
            raise ValidationError('Можно выбрать только один основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # inlines = [ScopeInline]
    pass
