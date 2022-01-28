# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import utils as bkash_utils
from .models import BkashPayment, BkashTransaction


class PaymentCreateApiView(APIView):
    '''
    A class creating payment creating APIVIEW

    '''
    def post(self, request):
        '''
        A method which is post

        Parameters
        ----------
        :param self:APIVIEW
        :param request:url

        Return
        ------
        if payment id is valid show HTTP_200_OK
        else it returns HTTP_500_INTERNAL_SERVER_ERROR
        
        '''
        try:
            auth_body, auth_headers = bkash_utils.get_header_body_for_token_auth()
            auth_response = requests.post(
                bkash_utils.get_bkash_app_payment_token_grant_url(),
                json=auth_body,
                headers=auth_headers
            )
            response = requests.post(
                bkash_utils.get_bkash_app_payment_create_url(),
                json=dict(request.data, **dict(currency='BDT', merchantInvoiceNumber=bkash_utils.generate_unique_id())),
                headers=bkash_utils.get_header_for_payment_create(auth_response.json().get('id_token'))
            )
            if response.status_code == 200 and response.json() and 'paymentID' in response.json():
                try:
                    payment = BkashPayment(user=request.user, **response.json())
                    payment.save()
                except Exception as exc:
                    print(exc)
            return Response(response.json(), status=status.HTTP_200_OK)
        except Exception as exc:
            return Response(dict(
                status=500,
                message=exc.args[0]
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentExecuteApiView(APIView):
    '''
    A class creating payment executing APIVIEW
    '''
    def post(self, request):
        '''
        A method which is post

        Parameters
        ----------
        :param self:APIVIEW
        :param request:url

        Return
        ------
        if payment id is valid show HTTP_200_OK
        else it returns HTTP_500_INTERNAL_SERVER_ERROR

        '''
        try:
            if 'paymentID' not in request.data:
                return Response(
                    dict(
                        status=500,
                        message='PaymentID is required'
                    ),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            auth_body, auth_headers = bkash_utils.get_header_body_for_token_auth()
            auth_response = requests.post(
                bkash_utils.get_bkash_app_payment_token_grant_url(),
                json=auth_body,
                headers=auth_headers
            )
            response = requests.post(
                '%s/%s'%(bkash_utils.get_bkash_app_payment_execute_url(), request.data.get('paymentID')),
                headers=bkash_utils.get_header_for_payment_create(auth_response.json().get('id_token'))
            )
            if response.status_code == 200 and response.json() and ('paymentID' in response.json() and 'trxID' in response.json()):
                try:
                    transaction = BkashTransaction(user=request.user, **response.json())
                    transaction.save()
                except Exception as exc:
                    print(exc)

            return Response(response.json(), status=status.HTTP_200_OK)
        except Exception as exc:
            return Response(dict(
                status=500,
                message=exc.args[0]
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
