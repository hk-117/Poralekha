from django.db import models
from django.contrib.auth.models import User


class Tutor(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=64)
    institute = models.CharField(max_length=100)
    is_premium = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    preffered_subject = models.CharField(max_length=512)
    preffered_medium = models.CharField(max_length=64)
    preffered_class = models.CharField(max_length=512)
    preffered_time = models.CharField(max_length=512)
    address_covered = models.CharField(max_length=512)
    address_division = models.CharField(max_length=64)
    address_district = models.CharField(max_length=64)
    address_present = models.CharField(max_length=512)
    address_phone = models.CharField(max_length=64)
    expected_salary = models.IntegerField()
    tution_status = models.BooleanField(default=True)
    working_days = models.IntegerField()
    place_of_learning = models.CharField(max_length=64)
    extra_facilities = models.CharField(max_length=512)
    current_tution_number = models.IntegerField(default=0)
    total_tution_so_far = models.IntegerField(default=0)
    ssc_exam_year = models.IntegerField(default=None)
    ssc_institute = models.CharField(max_length=100)
    ssc_subject = models.CharField(max_length=64)
    ssc_result = models.CharField(max_length=25)
    hsc_exam_year = models.IntegerField()
    hsc_institute = models.CharField(max_length=100)
    hsc_subject = models.CharField(max_length=64)
    hsc_result = models.CharField(max_length=25)
    honours_exam_year = models.IntegerField()
    honours_subject = models.CharField(max_length=64)
    honours_result = models.CharField(max_length=25)
    profile_pic= models.ImageField(upload_to='profile',default='profile/default.png')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address_division = models.CharField(max_length=64)
    address_district = models.CharField(max_length=64)
    address_present = models.CharField(max_length=512)
    address_phone = models.CharField(max_length=64)
    info_class = models.CharField(max_length=64)
    info_medium = models.CharField(max_length=64)
    info_gender = models.CharField(max_length=10)
    institute = models.CharField(max_length=100)
    profile_pic= models.ImageField(upload_to='profile',default='profile/default.png')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tution(models.Model):
    posted_by=models.ForeignKey(Student,on_delete=models.CASCADE)
    tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE,blank=True,null=True)
    post_title=models.CharField(max_length=100)
    time_created=models.DateTimeField()
    time_confirmed=models.DateTimeField(blank=True,null=True)
    time_ended=models.DateTimeField(blank=True,null=True)
    rating_given=models.IntegerField(default=0)
    salary=models.IntegerField()
    student_class=models.CharField(max_length=64)
    student_medium=models.CharField(max_length=64)
    student_subjects=models.CharField(max_length=100)
    student_location=models.CharField(max_length=512)
    student_district=models.CharField(max_length=64)
    student_gender=models.CharField(max_length=10)
    student_number=models.IntegerField(default=1)
    requirement_gender=models.CharField(max_length=10)
    requirement_teaching_time=models.CharField(max_length=64)
    requirement_days_per_week=models.IntegerField()
    requirement_others=models.CharField(max_length=512)
    confirmed=models.BooleanField(default=False)
    ended=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.post_title}"

class TutionRequests(models.Model):
    tution=models.ForeignKey(Tution,on_delete=models.CASCADE)
    tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE)
    confirmed=models.BooleanField(default=False)
    cancelled=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.tution.post_title} req- {self.id}"
