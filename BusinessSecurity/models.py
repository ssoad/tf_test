from django.db import models
from tinymce.models import HTMLField
from Account.models import User
import uuid


# Create your models here.

class NewsSubscriber(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=264, verbose_name='Category Name')
    category_description = models.TextField(max_length=1000, verbose_name='Category Description')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Service Categories'


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='service_category')
    service_icon = models.ImageField(upload_to='service_icon/', verbose_name='Service Icon')
    service_title = models.CharField(max_length=264, verbose_name='Service Title')
    short_description = models.TextField(max_length=1000, verbose_name='Short Description')
    service_header = HTMLField(verbose_name='Service Header', blank=True)
    service_body = HTMLField(verbose_name='Service Body', blank=True)
    service_footer = HTMLField(verbose_name='Service Footer', blank=True)
    has_sub_service = models.BooleanField(default=False, verbose_name='Has Sub Services')
    is_subscription_based = models.BooleanField(default=False, verbose_name='Is Subscription Based')
    total_customer = models.IntegerField(verbose_name='Total Customer', default=0, blank=True)

    def __str__(self):
        return self.service_title

    class Meta:
        verbose_name_plural = 'Services'


input_type = (
    ('text', 'text'),
    ('number', 'number'),
    ('file', 'file'),
    ('select', 'select'),
)


class InputFields(models.Model):
    type = models.CharField(max_length=264, choices=input_type)
    # name = models.CharField(max_length=264, blank=True, null=True)
    placeholder = models.CharField(max_length=264, blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.placeholder}'

    class Meta:
        verbose_name_plural = 'Input Fields'


class SelectChoice(models.Model):
    choices = models.CharField(max_length=255)

    def __str__(self):
        return self.choices


class SelectChoiceRelation(models.Model):
    input_field = models.ForeignKey(InputFields, on_delete=models.CASCADE,
                                    related_name='selectchoicerelation_inputfield')
    choice_field = models.ManyToManyField(SelectChoice, related_name='selectchoicerelation_selectchoice')

    def __str__(self):
        return f'{self.input_field.type} - {self.input_field.placeholder}'


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subservice_service')
    fields = models.ManyToManyField(InputFields, related_name='subservice_inputfields', through='SubServiceInput')
    title = models.CharField(max_length=264, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    total_customer = models.IntegerField(verbose_name='Total Customer', default=0, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub Services'


class SubServiceInput(models.Model):
    subservice = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name='subserviceinput_subservice')
    inputfield = models.ForeignKey(InputFields, on_delete=models.CASCADE, related_name='subserviceinput_inputfield')

    # input_value = models.CharField(max_length=264, blank=True, null=True)

    class Meta:
        db_table = 'BusinessSecurity_subservice_inputfields'


class UserSubserviceInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_subservice_input')
    inputfield = models.ForeignKey(SubServiceInput, on_delete=models.CASCADE, related_name='inputfield_input')
    inputinfo = models.CharField(max_length=255)


duration_type = (
    ('month', 'Month'),
    ('year', 'Year'),
)

order_status = (
    ('new', 'New'),
    ('assigned', 'Assigned'),
    ('attending', 'Attending'),
    ('on_progress', 'On Progress'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
)


class Order(models.Model):
    subserviceinput = models.ManyToManyField(UserSubserviceInput, related_name='order_subservice')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='order_service')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    order_status = models.CharField(max_length=250, choices=order_status, default='new')
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(default=0)


class OrderStaff(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderstaff_order')
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orderstaff_user')


ticket_type = (
    ('bcs', 'BCS'),
    ('pcs', 'PCS'),
)
ticket_status = (
    ('open', 'Open'),
    ('closed', 'Closed'),
)


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_user')
    ticket_type = models.CharField(max_length=255, choices=ticket_type)
    ticket_category = models.CharField(max_length=255, verbose_name='Category')
    ticket_title = models.CharField(max_length=255, verbose_name='Title')
    ticket_description = HTMLField(verbose_name='Description')
    ticket_attachment = models.ImageField(verbose_name='Attachment', upload_to='ticket/')
    ticket_status = models.CharField(max_length=255, choices=ticket_status)
    ticket_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_title


class TicketStaff(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticketstaff_order')
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticketstaff_user')


class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticketcomment_ticket')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticketcomment_user')
    comment = HTMLField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket} - comment - {self.user}'


class SubscriptionBasedPackage(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=264, verbose_name='Package Name')
    servers = models.IntegerField()
    websites = models.IntegerField()
    workstations = models.IntegerField()
    duration = models.IntegerField()
    duration_type = models.CharField(choices=duration_type, max_length=264, default='month')
    price = models.IntegerField()

    def __str__(self):
        return self.package_name

    class Meta:
        verbose_name_plural = 'Subscription Based Packages'


class SubscriptionFeatures(models.Model):
    package = models.ForeignKey(SubscriptionBasedPackage, on_delete=models.CASCADE, related_name='feature_subscription')
    feature_name = models.CharField(max_length=264, verbose_name='Feature Name')

    def __str__(self):
        return self.feature_name

    class Meta:
        verbose_name_plural = 'Package Features'


class UserAllowed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allowed_user')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='allowed_service')

    def __str__(self):
        return f"{self.user.first_name} - {self.service.service_title}"

    class Meta:
        verbose_name_plural = 'Users Allowed'


industry_type = (
    ('software_companies', 'Software Companies'),
    ('government_agencies', 'Government Agencies'),
    ('law_enforcement', 'Law Enforcement'),
    ('financial_institutes', 'Financial Institutes'),
    ('telecommunication_companies', 'Telecommunication Companies'),
    ('wealth_management', 'Wealth Management'),
    ('educational_institutes', 'Educational Institute'),
    ('isp_companies', 'ISP Companies'),
    ('ecommerce_business', 'Ecommerce Business'),
    ('law_farm', 'Law Farm'),
    ('small_and_medium_business', 'Small and Medium Business'),
    ('health_care_institutes', 'Health Care Institutes'),
)

privilege = (
    ('admin', 'Admin'),
    ('member', 'Member'),
)


class Business(models.Model):
    industry_type = models.CharField(max_length=264, choices=industry_type)
    company_name = models.CharField(max_length=264)
    company_logo = models.ImageField(upload_to='company/')
    website = models.URLField(max_length=264, default='https://')
    business_size = models.IntegerField(default=10)
    created_date = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'Businesses'


class UsersBusiness(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_user')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_business')
    position = models.CharField(max_length=264)
    privilege = models.CharField(max_length=264, choices=privilege)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.business} - {self.position}'

    class Meta:
        verbose_name_plural = 'User Businesses'


medium_list = (
    ('online', 'Online'),
    ('offline', 'Offline'),
)
category_list = (
    ('for_business_security', 'For Business CyberSecurity'),
    ('for_personal_security', 'For Personal CyberSecurity'),
)
status_list = (
    ('active', 'Active'),
    ('completed', 'completed'),
    ('canceled', 'canceled'),
)


class Events(models.Model):
    event_name = models.CharField(max_length=264)
    medium = models.CharField(choices=medium_list, max_length=264)
    speaker = models.CharField(max_length=264)
    category = models.CharField(choices=category_list, max_length=264)
    address = models.CharField(max_length=264)
    date_field = models.DateField()
    time_field = models.TimeField()
    status = models.CharField(choices=status_list, max_length=264)
    event_description = HTMLField(max_length=5000)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = 'Events'


class RegisteredEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_event_user')
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='registered_event_event')

    def __str__(self):
        return f'{self.user} - {self.event}'

    class Meta:
        verbose_name_plural = 'Registered Events'
