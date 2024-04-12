from django.db import models

from library_app.utils import CirculationType, ReservationStatus


class Book(models.Model):
    book_id = models.IntegerField(db_column='BookID')
    book_name = models.CharField(max_length=150, db_column='BookName')
    number_of_copies = models.IntegerField(db_column='NumberOfCopies')


class Member(models.Model):
    member_id = models.IntegerField(db_column='MemberID')
    member_name = models.CharField(max_length=150, db_column='MemberName')


class Circulation(models.Model):
    type = models.IntegerField(choices=CirculationType.choices())
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class Reservation(models.Model):
    reservation_id = models.CharField(max_length=150)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ReservationStatus.choices(), default=ReservationStatus.NOT_FULFILLED)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
