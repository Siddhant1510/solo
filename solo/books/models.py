from django.db import models

class book_info(models.Model):
    book_id = models.IntegerField()
    book_title = models.CharField(max_length=60)
    book_author = models.CharField(max_length=50)
    book_size = models.SmallIntegerField()
    book_pub_date = models.DateField('date published')
    no_of_copies = models.SmallIntegerField()

    def __str__(self):
        return str(self.book_id) + "-" + self.book_title

class issued(models.Model):
    book_id = models.IntegerField()
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.book_id) + "-" + self.user_name

class book_request(models.Model):
    user = models.CharField(max_length = 50)
    book_name = models.CharField(max_length = 80)
    book_author = models.CharField(max_length = 60)
    comment = models.TextField()

    def __str__(self):
        return self.user + "-" + self.book_name
