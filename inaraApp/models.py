from django.db import models

# Create your models here.

class Home (models.Model):
    first = models.CharField(max_length=6, blank=True, null=False)
    second = models.CharField(max_length=18, blank=True, null=False)
    third = models.TextField(max_length=520, blank=True, null=True)
    fourth = models.TextField(max_length=520, blank=True, null=True)
    image = models.ImageField(upload_to='home/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.first


class Hero (models.Model):
    title_one = models.CharField(max_length=30, blank=True, null=False)
    title_one_sub1 = models.CharField(max_length=30, blank=True, null=False)
    title_one_sub2 = models.CharField(max_length=30, blank=True, null=False)
    title_two =  models.TextField(max_length=520, blank=True, null=False)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title_one
class Abt (models.Model):
    t_one = models.CharField(max_length=30, blank=True, null=False)
    t_one_sub1 = models.CharField(max_length=30, blank=True, null=False)
    t_one_sub2 = models.CharField(max_length=30, blank=True, null=False)
    img = models.ImageField(upload_to='home/', blank=True, null=True)
    t_two =  models.TextField(max_length=520, blank=True, null=False)
    t_two_sub1 = models.CharField(max_length=30, blank=True, null=False)
    t_two_sub2 = models.TextField(max_length=520, blank=True, null=False)
    img1 = models.ImageField(upload_to='home/', blank=True, null=True)
    t_three = models.TextField(max_length=520, blank=True, null=False)
    t_three_sub1 = models.CharField(max_length=30, blank=True, null=False)
    t_three_sub2 = models.TextField(max_length=600, blank=True, null=False)
    img2 = models.ImageField(upload_to='home/', blank=True, null=True)
    img3 = models.ImageField(upload_to='home/', blank=True, null=True)
    img4 = models.ImageField(upload_to='home/', blank=True, null=True)

    quality1 = models.CharField(max_length=30, blank=True, null=False)
    quality2 = models.CharField(max_length=30, blank=True, null=False)
    quality3 = models.CharField(max_length=30, blank=True, null=False)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.t_one

class Proc (models.Model):
    t1 = models.CharField(max_length=20, blank=True, null=False)
    d1 = models.TextField(max_length=520, blank=True, null=False)

    p1 = models.TextField(max_length=520, blank=True, null=True)
    p1_d= models.TextField(max_length=520, blank=True, null=True)
    p2 = models.TextField(max_length=520, blank=True, null=True)
    p2_d = models.TextField(max_length=520, blank=True, null=True)
    p3 = models.TextField(max_length=520, blank=True, null=True)
    p3_d = models.TextField(max_length=520, blank=True, null=True)
    p4 = models.TextField(max_length=520, blank=True, null=True)
    p4_d = models.TextField(max_length=520, blank=True, null=True)

    image = models.ImageField(upload_to='home/', blank=True, null=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.t1


class Whyus(models.Model):

    p1 = models.TextField(max_length=520, blank=True, null=True)
    p1_d = models.TextField(max_length=520, blank=True, null=True)
    p2 = models.TextField(max_length=520, blank=True, null=True)
    p2_d = models.TextField(max_length=520, blank=True, null=True)
    p3 = models.TextField(max_length=520, blank=True, null=True)
    p3_d = models.TextField(max_length=520, blank=True, null=True)

    image = models.ImageField(upload_to='home/', blank=True, null=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.p1

class Team(models.Model):
    string= models.TextField(max_length=520, blank=True, null=True)
    team1 = models.ImageField(upload_to='home/', blank=True, null=True)
    team2 = models.ImageField(upload_to='home/', blank=True, null=True)
    team3 = models.ImageField(upload_to='home/', blank=True, null=True)

    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.string
class Works(models.Model):
    string = models.TextField(max_length=520, blank=True, null=True)
    image1 = models.ImageField(upload_to='home/', blank=True, null=True)
    image2 = models.ImageField(upload_to='home/', blank=True, null=True)
    image3 = models.ImageField(upload_to='home/', blank=True, null=True)
    image4 = models.ImageField(upload_to='home/', blank=True, null=True)
    image5 = models.ImageField(upload_to='home/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.string

class Testi(models.Model):
    heading = models.TextField(max_length=520, blank=True, null=True)
    details = models.TextField(max_length=520, blank=True, null=True)
    review1 = models.TextField(max_length=520, blank=True, null=True)
    review2 = models.TextField(max_length=520, blank=True, null=True)
    review3 = models.TextField(max_length=520, blank=True, null=True)
    review4 = models.TextField(max_length=520, blank=True, null=True)
    client1= models.ImageField(upload_to='home/', blank=True, null=True)
    client2= models.ImageField(upload_to='home/', blank=True, null=True)
    client3= models.ImageField(upload_to='home/', blank=True, null=True)
    bgimage=models.ImageField(upload_to='home/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.heading

class Blog(models.Model):
    heading = models.TextField(max_length=520, blank=True, null=True)
    details = models.TextField(max_length=520, blank=True, null=True)

    blog1= models.ImageField(upload_to='home/', blank=True, null=True)
    blog2= models.ImageField(upload_to='home/', blank=True, null=True)
    blog3= models.ImageField(upload_to='home/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.heading

class Callaction(models.Model):
    string = models.TextField(max_length=520, blank=True, null=True)


    background = models.ImageField(upload_to='home/', blank=True, null=True)


    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.string

class ContactU(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return self.name