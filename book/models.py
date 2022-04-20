from django.db import models


class Book(models.Model):
    GENRE = (
        ('РОМАНТИКА',"романтика"),
        ("ФЭНТЕЗИ","фентези"),
        ("ДЕТЕКТИВ", "детектив"),
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    createa_data= models.DateField(auto_now_add=True)
    updeted_data = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='')
    pages = models.PositiveIntegerField()
    author = models.CharField(max_length=25, null=True)
    genre = models.CharField(max_length=90, choices=GENRE)

    def __str__(self):
        return self.title

class BookFreedBack(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    books = models.ForeignKey(Book,
                              on_delete=models.CASCADE,
                              related_name="book_freed")

    def __str__(self):
        return self.book.title