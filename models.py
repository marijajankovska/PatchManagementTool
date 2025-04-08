from datetime import timedelta, timezone, datetime, date

from django.db import models
from django.urls import include


# Create your models here.
class Application_Admin(models.Model):
    name = models.CharField(max_length=255)
    domain_username = models.CharField(max_length=255)
    email= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class System(models.Model):
    name = models.CharField(max_length=255)
    admins = models.ManyToManyField(Application_Admin)
    def __str__(self):
         return self.name
class Patching(models.Model):
    machine = models.CharField(max_length=255)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    OS_Name = models.CharField(max_length=255)
    OS_major_version = models.CharField(max_length=255)
    OS_admin_choices = [
        ("Linux admins Asseco", "Linux admins Asseco"),
        ("Linux admins MKT", "Linux admins MKT"),
        ("Windows Admins Asseco", "Windows Admins Asseco"),
        ("Vendor", "Vendor"),
        ("Orphan", "Orphan"),
        ("Cyber Security", "Cyber Security"),
        ("IST/ICT Delivery Stream", "IST/ICT Delivery Stream")
    ]
    deployment_stage_choices = [
        ("Production", "Production"),
        ("Development", "Development"),
        ("Test", "Test")
    ]

    OS_admin = models.CharField(max_length=255, choices=OS_admin_choices)
    deployment_stage = models.CharField(max_length=255, choices=deployment_stage_choices)
    OS_support = models.CharField(max_length=255, blank=True, null=True)
    eol_date = models.DateField()
    in_tos = models.BooleanField()
    point_of_contact = models.CharField(max_length=1024, blank=True, null=True)

    patch_plan_jan = models.DateField(null=True, blank=True)
    patch_exec_jan = models.DateField(null=True, blank=True)

    patch_plan_feb = models.DateField(null=True, blank=True)
    patch_exec_feb = models.DateField(null=True, blank=True)

    patch_plan_mar = models.DateField(null=True, blank=True)
    patch_exec_mar = models.DateField(null=True, blank=True)

    patch_plan_apr = models.DateField(null=True, blank=True)
    patch_exec_apr = models.DateField(null=True, blank=True)

    patch_plan_may = models.DateField(null=True, blank=True)
    patch_exec_may = models.DateField(null=True, blank=True)

    patch_plan_jun = models.DateField(null=True, blank=True)
    patch_exec_jun = models.DateField(null=True, blank=True)

    patch_plan_jul = models.DateField(null=True, blank=True)
    patch_exec_jul = models.DateField(null=True, blank=True)

    patch_plan_aug = models.DateField(null=True, blank=True)
    patch_exec_aug = models.DateField(null=True, blank=True)

    patch_plan_sep = models.DateField(null=True, blank=True)
    patch_exec_sep = models.DateField(null=True, blank=True)

    patch_plan_oct = models.DateField(null=True, blank=True)
    patch_exec_oct = models.DateField(null=True, blank=True)

    patch_plan_nov = models.DateField(null=True, blank=True)
    patch_exec_nov = models.DateField(null=True, blank=True)

    patch_plan_dec = models.DateField(null=True, blank=True)
    patch_exec_dec = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.system:
            # Get the names of all admins related to this system and join them with commas
            self.point_of_contact = ", ".join([admin.name for admin in self.system.admins.all()])

        if self.patch_plan_jan:
            # Add 12 weeks (84 days) to the patch plan date for the subsequent months
            if not self.patch_plan_feb:
                self.patch_plan_feb = self.patch_plan_jan + timedelta(weeks=4)
            if not self.patch_plan_mar:
                self.patch_plan_mar = self.patch_plan_feb + timedelta(weeks=4)
            if not self.patch_plan_apr:
                self.patch_plan_apr = self.patch_plan_mar + timedelta(weeks=4)
            if not self.patch_plan_may:
                self.patch_plan_may = self.patch_plan_apr + timedelta(weeks=4)
            if not self.patch_plan_jun:
                self.patch_plan_jun = self.patch_plan_may + timedelta(weeks=4)
            if not self.patch_plan_jul:
                self.patch_plan_jul = self.patch_plan_jun + timedelta(weeks=4)
            if not self.patch_plan_aug:
                self.patch_plan_aug = self.patch_plan_jul + timedelta(weeks=4)
            if not self.patch_plan_sep:
                self.patch_plan_sep = self.patch_plan_aug + timedelta(weeks=4)
            if not self.patch_plan_oct:
                self.patch_plan_oct = self.patch_plan_sep + timedelta(weeks=4)
            if not self.patch_plan_nov:
                self.patch_plan_nov = self.patch_plan_oct + timedelta(weeks=4)
            if not self.patch_plan_dec:
                self.patch_plan_dec = self.patch_plan_nov + timedelta(weeks=4)

        if self.eol_date <= date.today():
            self.OS_support = "END OF LIFE"
        else:
            self.OS_support = "SUPPORTED"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.machine
