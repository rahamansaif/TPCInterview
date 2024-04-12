import uuid
from django.shortcuts import get_object_or_404

from library_app.models import Book, Member, Circulation, Reservation
from library_app.utils import CirculationType, ReservationStatus


def handle_checkout_request(book_id, member_id):
    book = get_object_or_404(Book, book_id=book_id)
    member = get_object_or_404(Member, member_id=member_id)
    if book.number_of_copies == 0:
        reservation = make_reservation()
        return {'reservation': reservation}
    circulation = checkout_book()
    return {'checkout': circulation}


def checkout_book(book, member):
    circulation = Circulation.objects.create(
        circulation_type=CirculationType.CHECKOUT, book=book, member=member,
    )
    book.number_of_copies = book.number_of_copies - 1
    book.save()
    return circulation


def make_reservation(book, member):
    return Reservation.objects.create(
        reservation_id=str(uuid.uuid4()), status=ReservationStatus.NOT_FULFILLED, book=book, member=member,
    )


def handle_return_request(book_id, member_id):
    book = get_object_or_404(Book, book_id=book_id)
    member = get_object_or_404(Member, member_id=member_id)
    circulation = Circulation.objects.create(
        circulation_type=CirculationType.RETURN, book=book, member=member,
    )
    pending_reservation = Reservation.objects.filter(book=book, status=ReservationStatus.NOT_FULFILLED).first()
    if not pending_reservation:
        book.number_of_copies = book.number_of_copies - 1
        book.save()
    else:
        pending_reservation.status = ReservationStatus.CAN_BE_FULFILLED
        pending_reservation.save()
    return {'return': circulation}


def fulfill_reservation(reservation_id):
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id, status=ReservationStatus.CAN_BE_FULFILLED)
    circulation = Circulation.objects.create(
        circulation_type=CirculationType.CHECKOUT, book=reservation.book, member=reservation.member,
    )
    reservation.status = ReservationStatus.FULFILLED
    reservation.save()
    return {
        'checkout': circulation,
        'reservation': reservation,
    }
