# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DietChange(models.Model):
    changes = models.CharField(max_length=200, blank=True, null=True)
    d_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diet_change'


class DietHistory(models.Model):
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    veg_nonveg = models.CharField(max_length=100, blank=True, null=True)
    food_allergy = models.IntegerField(blank=True, null=True)
    likes_dislikes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diet_history'


class DietInfo(models.Model):
    patient = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    protien_int = models.IntegerField(blank=True, null=True)
    carbs_int = models.IntegerField(blank=True, null=True)
    oil_fat_sugarperday = models.IntegerField(blank=True, null=True)
    alchohol_intake = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diet_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GastrSymptoms(models.Model):
    symptoms = models.CharField(max_length=200, blank=True, null=True)
    g_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gastr_symptoms'


class OtherIllnesses(models.Model):
    metabolic_stress = models.CharField(max_length=100, blank=True, null=True)
    m_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_illnesses'


class PersonalInfo(models.Model):
    patient = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    weight_lost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_info'


class Physical(models.Model):
    phy_illness = models.CharField(max_length=100, blank=True, null=True)
    p_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physical'


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=60, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class WaterInt(models.Model):
    user = models.ForeignKey(PersonalInfo, models.DO_NOTHING, blank=True, null=True)
    water_perday = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'water_int'
