from django.contrib import admin
import nested_admin
from .models import Category,Quiz,Question,Answer


#tabularline admin dashbordda iki veriyi içiçe görmemizi sağlar
#Ben quiz tablosun gittiğimde admindasbordda quizlerin sorularını ve cavaplarını yazabileyim istiyorum.Yani admin dashbordda üç tabloyu(quiz>question>answer) düzenleyebileyim istiyorum
#bunun için nested admin paketini yüklememiz gerekiyor.pip install django-nested-admin, ve installapp e 'nested_admin ile main klasöründeki urls.py a  path('nested_admin/', include('nested_admin.urls') ifadesini eklememiz gerekiyor

class AnswerInline(nested_admin.NestedTabularInline):#nested_adminde inherit ediyoruz
    model=Answer
class QuestionInline(nested_admin.NestedTabularInline):
    model=Question
    inlines=[AnswerInline]
class QuizAdmin(nested_admin.NestedModelAdmin):#.Aslında biz admin modeli overright ettik .Oluşturdugumuz diğer inlinlar QuizAdmin modeline yerleştirmek için
    model=Quiz
    inlines=[QuestionInline]

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)


