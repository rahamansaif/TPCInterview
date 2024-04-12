from rest_framework.decorators import api_view
from rest_framework.response import Response

from library_app.service import handle_checkout_request, handle_return_request, fulfill_reservation


@api_view(['POST'])
def checkout(request):
    book_id = request.POST.get('book_id')
    member_id = request.POST.get('member_id')
    resp = handle_checkout_request(book_id, member_id)
    data = {}
    if 'checkout' in resp.keys():
        data['message'] =  'Book issued'
    else:
        data['message'] = 'Book reserved'
        data['reservation_id'] = resp['reservation'].reservation_id
    return Response(data)


@api_view(['POST'])
def return_book(request):
    book_id = request.POST.get('book_id')
    member_id = request.POST.get('member_id')
    resp = handle_return_request(book_id, member_id)
    return Response({'message': 'Book Returned'})


@api_view(['POST'])
def fulfill(request):
    reservation_id = request.POST.get('reservation_id')
    resp = fulfill_reservation(reservation_id)
    return Response({'message': 'Book Issued'})
