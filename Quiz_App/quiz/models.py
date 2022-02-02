
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"#admin paneldeki isim Categorys değil de bu sayede <categories olacak
        
    def quiz_count(self):#bir categorye ait kaç tane quiz var diye saymak için
        return self.quiz_set.count()#modelin ismi küçük harflerle_set(standart)
class Quiz(models.Model):
    title=models.CharField(max_length=100, )#verbose_name attribute ile adminde title istediğimiz şekilde adlandırabiliriz
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#quiz categorynin altında olacağı için foreignkey ile bağladık
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Updated(models.Model):#Abstract Model Inheritance(modellerde tekrar eden fieldları  tek bir modelde tanımlıyoruz,bu model data base kaydedilmiyor, biziM aBSTACT modelimiz oluyo biz diğer modelleri ondan inherit ediyoruz) 
      updated_date=models.DateTimeField(auto_now=True)
      class Meta:
          abstract=True#database kaydetmemesi için(biryerlerde inheririt edilecek demektir Updated modeli)
      
    
    
    
class Question(Updated):#models.Model yerine Updated dan inherit ettik
    SCALE=(
        (0,"beginner"),
        (1,"intermediate"),
        (2,"advenced")
        
        
    )#ilk değer database,2. kullancının gördüğü
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=300)
    difficulty=models.IntegerField(choices=SCALE)#SCALE deki database kısmına kaydedilen bir integer olarak belirlediğimiz için ıntegerField
    created_date=models.DateTimeField(auto_now_add=True)
    #updated_date=models.DateTimeField(auto_now=True)#Updated modelden inherit ettiğimiz için bu alanı kullanmamıza gerek yok
    
    def __str__(self):
        return self.question
class Answer(Updated):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=250)
    checking=models.BooleanField(default=False)#sorunun doğrulugunu yanlışşlıgını kontrol edebilmek için
    #updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.answer
    

    