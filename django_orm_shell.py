from blog.models import *

nursultan = Author.objects.create(name="Нурсултан Бердиев",email="nursultanberdiev@gmail.com",username="nursultanberdiev",date_register="2021-01-04")
veronika = Author.objects.create(name="Лю Вероника",email="ronilyu@gmail.com",username="ronik",date_register="2023-03-12")
chynara = Author.objects.create(name="Токтосунова Чынара",email="chynara0409@gmail.com",username="chynara",date_register="2023-03-12")

art1_nurs=Article.objects.create(title="Что нужно для разработки мобильных приложений: языки и тренды")
art2_nurs=Article.objects.create(title="Зачем нужно использовать кроссплатформенную систему")
art3_nurs=Article.objects.create(title="Сравниваем Java и Python или с чего лучше начать")

art4_ver=Article.objects.create(title="Новый ChatGPT-4: в чем его особенность")
art5_chyn=Article.objects.create(title="История компании Boston Dynamics. Как появлялись их роботы")

pub_1_nusrultan=Publication.objects.create(author=nursultan,article=art1_nurs,date_published="2021-01-04")
pub_2_nusrultan=Publication.objects.create(author=nursultan,article=art2_nurs,date_published="2021-01-04")
pub_3_nusrultan=Publication.objects.create(author=nursultan,article=art3_nurs,date_published="2021-01-04")

pub_4_veronika=Publication.objects.create(author=veronika,article=art4_ver,date_published="2023-03-12")
pub_5_chynara=Publication.objects.create(author=chynara,article=art5_chyn,date_published="2021-01-04")

Article.objects.all()   
author=Author.objects.all()                     
author
authors = author.order_by("date_register") 
authors
nursultan_pub=Publication.objects.filter(author=nursultan)           
nursultan_pub
authors_gt=author.filter(date_register__gt="2022-10-10") 
authors_gt
all_pub_dict=all_pub.values("author__username", "article__title") 
all_pub_dict
all_pub_tuple = [(t['author__username'], t['article__title']) for t in all_pub_dict]
all_pub_tuple
a_author_pub=Publication.objects.filter(author__name__startswith='Л') 
a_author_pub
