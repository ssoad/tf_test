import base64
import itertools

import requests
from django.shortcuts import render
from Api import serializer
from rest_framework import generics
from Blog import models
from Account import models as accountmodel
from BusinessSecurity import models as bcsmodels
from Academy import models as coursemodels
from rest_framework import permissions, pagination, filters
from datetime import date
from django.db.models import Q
from rest_framework.response import Response
from Api import apipermissions


# Create your views here.

class PostApi(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializer.PostSerializer


class CategoryApi(generics.ListAPIView):
    permission_classes = [apipermissions.IsBlogAdmin]
    queryset = models.BlogCategory.objects.all()
    serializer_class = serializer.CategorySerializer


class SubCategoryApi(generics.ListAPIView):
    # queryset = models.BlogSubCategory.objects.all()
    permission_classes = [apipermissions.IsBlogAdmin]
    serializer_class = serializer.SubCategorySerializer

    def get_queryset(self):
        category = self.kwargs['id']
        return models.BlogSubCategory.objects.filter(category=category)


class FilterApi(generics.ListAPIView):
    # queryset = models.FilterOption.objects.all()
    permission_classes = [apipermissions.IsBlogAdmin]
    serializer_class = serializer.FilterSerializer

    def get_queryset(self):
        category = self.kwargs['id']
        subcategory = self.kwargs['sub_id']
        return models.FilterOption.objects.filter(sub_category=subcategory, sub_category__category=category)


class Page(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 5


class AllCommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['comment_date']


class CommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page

    def get_queryset(self):
        post = self.kwargs['post_id']
        return models.Comment.objects.filter(post=post)


class BlogFilterApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        return models.Post.objects.filter(
            Q(category__category__iexact=category, title__icontains=text) | Q(category__category__iexact=category,
                                                                              short_description__icontains=text))


class BlogFilterDateApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer
    today = date.today()

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        if text == 'month':
            return models.Post.objects.filter(category__category__iexact=category, date__month=self.today.month)
        elif text == 'year':
            return models.Post.objects.filter(category__category__iexact=category, date__year=self.today.year)


class PackageListViewApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.PackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionBasedPackage.objects.filter(service_id=service_id)


class SubscriptionServiceApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.SubscriptionServiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionServices.objects.filter(id=service_id)


class ServiceListApiView(generics.ListAPIView):
    serializer_class = serializer.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    # queryset = bcsmodels.Service.objects.all()

    def get_queryset(self):
        cat_type = self.kwargs['cat']
        return bcsmodels.Service.objects.filter(category_choice=cat_type)


class SubServiceApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubService.objects.filter(service_id=service_id)


class SubServiceInputApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceInputSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubServiceInput.objects.filter(subservice_id=service_id)


class ChoiceApiView(generics.ListAPIView):
    serializer_class = serializer.ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']
        return bcsmodels.SelectChoiceRelation.objects.filter(input_field_id=id)


class UserSubServiceOrderApiView(generics.ListAPIView):
    serializer_class = serializer.UserSubServiceOrderSerializer

    def get_queryset(self):
        subservice_id = self.kwargs['id']
        return bcsmodels.Order.objects.filter(id=subservice_id)


class TeamPermissionApiView(generics.RetrieveUpdateAPIView):
    serializer_class = serializer.TeamPermissionSerializer
    permission_classes = [apipermissions.IsTeamAdmin]
    lookup_field = 'id'
    queryset = bcsmodels.UsersBusiness


class BCSAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()
    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')

        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_years,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class BCSAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = date.today().month
        # print(end_date)
        all_months = list(range(start_date, end_date + 1))
        # print(all_months)
        current_year = date.today().year

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')

        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year,
                                 service__is_subscription_based=False).count()
            subscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year,
                                 service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year, ).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_months,
            'datas': datas
        })


class BCSAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = date.today().day
        # print(end_date)
        all_dates = list(range(start_date, end_date + 1))
        # print(all_dates)
        current_month = date.today().month

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month,
                                 service__is_subscription_based=False).count()
            subscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month,
                                 service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class PCSAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):
        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')

        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class PCSAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))
        current_year = date.today().year

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')

        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year,
                                 service__is_subscription_based=False).count()
            subscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year,
                                 service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year, ).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_months,
            'datas': datas
        })


class PCSAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().day

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []
        current_month = date.today().month

        query = bcsmodels.Order.objects.filter(category_choice='pcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month,
                                 service__is_subscription_based=False).count()
            subscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month,
                                 service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class MainAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.all()

        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=False).count()
            subscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year, service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = query.filter(order_date__year=year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class MainAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))
        current_year = date.today().year

        subscription_count = []
        unsubscription_count = []
        total_count = []

        query = bcsmodels.Order.objects.all()

        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year,
                                 service__is_subscription_based=False).count()
            subscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year,
                                 service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_months,
            'datas': datas
        })


class MainAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().day

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []
        total_count = []
        current_month = date.today().month

        query = bcsmodels.Order.objects.all()

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month,
                                 service__is_subscription_based=False).count()
            subscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month,
                                 service__is_subscription_based=True).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            total_count.append(order)

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class SubscriptionApiView(generics.ListAPIView):
    serializer_class = serializer.SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'service'

    def get_queryset(self):
        service_id = self.kwargs['service']
        return bcsmodels.Order.objects.filter(service__id=service_id, user=self.request.user,
                                              service__is_subscription_based=True).order_by('-order_date')

    # def list(self, request, *args, **kwargs):
    #     ser = self.get_serializer(self.get_queryset(), many=True)
    #     responseData = ser.data
    #     print(self.get_queryset())
    #     responseData.append({
    #         'price': '1223'
    #     })
    #     return Response(responseData)


class SubscriptionOrderView(generics.CreateAPIView):
    serializer_class = serializer.SubscriptionOrderSerializer
    queryset = bcsmodels.SubscriptionOrder
    permission_classes = [permissions.IsAuthenticated]

    def cancelSubscriptions(self, subscription_service, category_choice):
        """
        Cancelling Previous Subscriptions
        """
        username = 'AfTmv1E8P0HbJCkRMtm7s_07rqkJCGvp4WufOBxLWUl5AFujlsqmn6WdpMZo-nQr-yKVTnogZOQYgLnl'
        password = 'EOsLHpTI748BbKSwcWlQpgmuJZXyudRnJP50Gc8H5Anf8VnDfk8FtEtRYwJ_iU1T9sgH5DOv53BuqeyH'
        busername = str(base64.b64encode(bytes(username, 'utf-8')))[1:].replace("'", "").replace("=", '')
        bpassword = str(base64.b64encode(bytes(password, 'utf-8')))[1:].replace("'", "")
        bearer = f"Basic {busername}6{bpassword}"

        packages = bcsmodels.SubscriptionBasedPackage.objects.filter(
            service_id__category_choice=category_choice).values_list(
            'id')
        if category_choice == 'pcs':
            user_orders = bcsmodels.SubscriptionOrder.objects.filter(
                # user__business_user__business=self.request.user.business_user.business,
                user=self.request.user,
                subscription_package__in=packages,
                subscription_service=subscription_service,
                is_active=True
            )
            for current_order in user_orders:
                current_order.is_active = False
                current_order.save()
                url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{current_order.paypal_subscription_id}/cancel'
                headers = {
                    'Content-type': 'application/json',
                    'Authorization': bearer
                }
                r = requests.post(url, headers=headers)
                print(r.status_code)
            notification = bcsmodels.AdminNotification.objects.create(category_choice='pcs',
                                                                      user=self.request.user,
                                                                      notification=f'User has cancelled the '
                                                                                   f'subs'
                                                                                   f'cription for '
                                                                                   f'{current_order.subscription_service.service_title}')
            notification.save()
        elif category_choice == 'bcs':
            user_orders = bcsmodels.SubscriptionOrder.objects.filter(
                user__business_user__business=self.request.user.business_user.business,
                # user=self.request.user,
                subscription_package__in=packages,
                subscription_service=subscription_service,
                is_active=True
            )
            for current_order in user_orders:
                current_order.is_active = False
                current_order.save()
                url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{current_order.paypal_subscription_id}/cancel'
                headers = {
                    'Content-type': 'application/json',
                    'Authorization': bearer
                }
                r = requests.post(url, headers=headers)
                print(r.status_code)
            notification = bcsmodels.AdminNotification.objects.create(category_choice='bcs',
                                                                      business=self.request.user.business_user.business,
                                                                      notification=f'User has cancelled the '
                                                                                   f'subs'
                                                                                   f'cription for '
                                                                                   f'{current_order.subscription_service.service_title}')
            notification.save()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_active=True)

    def create(self, request, *args, **kwargs):
        subscription_service = request.data['subscription_service']
        subscription_package = request.data['subscription_package']
        category_choice = request.data['category_choice']
        if category_choice == 'pcs':
            try:
                check_existing_order = bcsmodels.SubscriptionOrder.objects.get(user=self.request.user,
                                                                               subscription_service=subscription_service,
                                                                               subscription_package=subscription_package,
                                                                               is_active=True)
                return Response({'response': 'You have already Subscribed to this Package'})
            except:
                self.cancelSubscriptions(subscription_service, 'pcs')
                """
                Creating new Subscription
                """
                ser = self.get_serializer(data=request.data)
                ser.is_valid(raise_exception=True)
                self.perform_create(ser)
                subscription_id = request.data['paypal_subscription_id']
                user_subscribed = bcsmodels.SubscriptionOrder.objects.get(paypal_subscription_id=subscription_id)

                notification = bcsmodels.AdminNotification.objects.create(category_choice='pcs',
                                                                          user=self.request.user,
                                                                          notification=f'New Subscription. '
                                                                                       f'<a href="https://pcs.techforing.com/pcs_admin_subscription_detail/{user_subscribed.id}/" target="_blank" class="btn btn-success">Visit Now</a>')
                notification.save()
                return Response(ser.data)
        elif category_choice == 'bcs':
            try:
                check_existing_order = bcsmodels.SubscriptionOrder.objects.get(
                    user__business_user__business=self.request.user.business_user.business,
                    subscription_service=subscription_service,
                    subscription_package=subscription_package,
                    is_active=True)
                return Response({'response': 'You have already Subscribed to this Package'})
            except:
                self.cancelSubscriptions(subscription_service, 'bcs')
                """
                Creating new Subscription
                """
                ser = self.get_serializer(data=request.data)
                ser.is_valid(raise_exception=True)
                self.perform_create(ser)
                subscription_id = request.data['paypal_subscription_id']
                user_subscribed = bcsmodels.SubscriptionOrder.objects.get(paypal_subscription_id=subscription_id)

                notification = bcsmodels.AdminNotification.objects.create(category_choice='bcs',
                                                                          business=self.request.user.business_user.business,
                                                                          notification=f'New Subscription. '
                                                                                       f'<a href="https://main.techforing.com/bcs_admin_subscription_detail/{user_subscribed.id}/" target="_blank" class="btn btn-success">Visit Now</a>')
                notification.save()
                return Response(ser.data)


class SubscriptionPurchaseCheckApiView(generics.ListAPIView):
    queryset = bcsmodels.SubscriptionOrder
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        purchased_list = bcsmodels.SubscriptionOrder.objects.filter(user=self.request.user, is_active=True).values_list(
            'subscription_package_id',
            flat=True)
        # print(purchased_list)
        return Response({'result': purchased_list})


class PCSCoursePurchaseCheckApiView(generics.ListAPIView):
    queryset = coursemodels.CoursePurchase
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        purchased_list = coursemodels.CoursePurchase.objects.filter(user=self.request.user).values_list('course_id',
                                                                                                        flat=True)
        print(purchased_list)
        return Response({'result': purchased_list})


class PCSCoursePurchaseApiView(generics.CreateAPIView):
    serializer_class = serializer.PCSCoursePurchaseSerializer
    queryset = coursemodels.CoursePurchase.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        course = request.data['course']
        try:
            check_existing_order = coursemodels.CoursePurchase.objects.get(user=self.request.user, course_id=course)
            return Response({'response': 'You have already purchased this course'})
        except:
            ser = self.get_serializer(data=request.data)
            ser.is_valid(raise_exception=True)
            self.perform_create(ser)
            return Response(ser.data)


class BCSCourseApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.BCSCourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        service_id = self.kwargs['id']
        return coursemodels.BCSCourse.objects.filter(id=service_id)


class BCSCoursePackageListViewApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.BCSCoursePackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return coursemodels.CoursePackage.objects.filter(service_id=service_id)


class CollectiveNotificationApiView(generics.CreateAPIView):
    permission_classes = [apipermissions.IsMainAdmin]
    serializer_class = serializer.CollectiveNotificationSerializer
    queryset = bcsmodels.Notification


class CollectiveApiView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        return Response({
            'response': ['PCS', 'BCS']
        })


class IndividualApiView(generics.ListAPIView):
    permission_classes = [apipermissions.IsMainAdmin]
    serializer_class = serializer.IndividualSerializer

    def list(self, request, *args, **kwargs):
        emails = models.User.objects.all()
        ser = self.get_serializer(emails, many=True)
        datas = []
        for email in ser.data:
            datas.append(email['email'])
        return Response({
            'response': datas
        })


class BusinessApiView(generics.ListAPIView):
    permission_classes = [apipermissions.IsMainAdmin]
    serializer_class = serializer.BusinessSerializer

    def list(self, request, *args, **kwargs):
        company_name = bcsmodels.Business.objects.all()
        ser = self.get_serializer(company_name, many=True)
        datas = []
        for email in ser.data:
            datas.append(email['company_name'])
        return Response({
            'response': datas
        })


class InterestApiView(generics.ListAPIView):
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        return Response({
            'response': [field.name for field in accountmodel.Interest._meta.get_fields() if
                         field.name != 'id' and field.name != 'user']
        })
