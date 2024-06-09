from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    data_birth = models.DateField()


class Books(models.Model):
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publish_date = models.DateField()
    description = models.CharField(max_length=255)


class Members(models.Model):
    name = models.CharField(max_length=100)
    join_date = models.DateField(null=False,blank=False)



class BorrowingRecords(models.Model):
    book_id = models.OneToOneField(Books, on_delete=models.CASCADE)
    member_id = models.OneToOneField(Members,on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()



