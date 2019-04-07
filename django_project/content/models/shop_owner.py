import os
from django.db import models
from django.contrib.auth.models import User
from django.conf.global_settings import MEDIA_ROOT
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import datetime


class ApprovedShopManager(models.Manager):
    """Custom shop manager that shows only approved records."""

    def get_queryset(self):
        """Query set generator."""
        return super(
            ApprovedShopManager, self).get_queryset().filter(
                approved=True)


class UnapprovedShopManager(models.Manager):
    """Custom shop manager that shows only unapproved records."""

    def get_queryset(self):
        """Query set generator."""
        return super(
            UnapprovedShopManager, self).get_queryset().filter(
                approved=False)


class ShopOwner(models.Model):
    """Shop owner definition, (our client)."""

    name = models.CharField(
        _('Shop Name'),
        max_length=255,
        null=False,
        blank=False
    )
    email = models.EmailField(
        _('Email Address'),
        blank=True,
        null=True
    )
    phone = models.CharField(
        _('Phone Number'),
        max_length=255,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        _("Vendor Picture"),
        blank=True,
        null=True,
        upload_to=os.path.join(MEDIA_ROOT, 'photos/vendors/%Y/%m/%d/')
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        _('Is Shop approved?'),
        default=False
    )
    shop_managers = models.ManyToManyField(
        User,
        related_name='shop_managers',
        blank=True,
        # null=True, null has no effect on ManyToManyField.
        help_text=_(
            'Managers of the shop in this project. '
            'They will be allowed to create or remove '
            'products in their shop.')
    )
    product_managers = models.ManyToManyField(
        User,
        related_name='product_managers',
        blank=True,
        # null=True, null has no effect on ManyToManyField.
        help_text=_(
            'Managers of the shop products in this project. '
            'They will be allowed to approve products for publishing')
    )

    created = models.DateTimeField(default=datetime.now)

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    # slug = models.SlugField(unique=True)
    objects = models.Manager()
    approved_objects = ApprovedShopManager()
    unapproved_objects = UnapprovedShopManager()

    class Meta:
        verbose_name = 'Vendor Name'
        verbose_name_plural = 'Vendor Names'
        ordering = ['id', 'created']
        # permissions = (
        #     ('can_manage_own_shop', 'Can Manage Own Shop'),
        # )

    def __str__(self):
        return self.name
