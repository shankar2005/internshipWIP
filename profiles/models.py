from django.db import models
from .choices import *
from django.contrib.auth.models import User

# Create your models here.


class Work(models.Model):
    name = models.CharField(max_length=100, default='')
    weblink = models.URLField(max_length=100, default='')
    is_demo = models.BooleanField(default=False)
    from_client = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    details = models.TextField(default='', blank=True)

    # Login details
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(
        'Project', default='', blank=True, related_name='client_projects')

    # Gray   Man
    client_previous_payout = models.IntegerField(default=0, blank=True)
    production_suggested_project_advance = models.FloatField(
        default=0, blank=True)  # in percent
    latest_project_advance = models.FloatField(
        default=0, blank=True)  # in percent
    latest_client_payout_status = models.CharField(
        max_length=100, default='', blank=True, choices=CLIENT_PAYOUT_STATUS)
    total_client_payout = models.FloatField(default=0, blank=True)

    contract_document_signing_status = models.CharField(
        max_length=100, default='', blank=True,  # options=CONTRACT_SIGNING_STATUS
    )


class Artist(models.Model):
    # Base
    name = models.CharField(max_length=100, default='', blank=True)
    skill = models.CharField(
        choices=SKILLS, max_length=100, default='', blank=True)
    profile_pic = models.ImageField(
        upload_to='artist_pics', default='avatar.png', blank=True)
    location = models.CharField(
        max_length=100, default='', choices=LOCATION, blank=True)
    languages = models.CharField(default='', blank=True, max_length=100)
    age = models.IntegerField(default=0)
    genre = models.CharField(max_length=100, default='', blank=True)
    email = models.EmailField(max_length=100, default='', blank=True)
    phone = models.IntegerField(default=0, blank=True)

    # Conditional only on  skill = 'Actor'

    other_arts = models.CharField(max_length=100, default='', blank=True)
    works_links = models.ManyToManyField(Work, default='', blank=True)
    social_links = models.CharField(default='', blank=True, max_length=200)

    has_manager = models.BooleanField(default=False, blank=True)
    manager = models.ForeignKey(
        'Manager', on_delete=models.CASCADE, default='', blank=True, null=True, related_name='%(class)s_to_Manager_relation')
    budget_range = models.CharField(max_length=100, default='', blank=True)
    budget_idea = models.TextField(default='', blank=True)
    am_notes = models.TextField(default='', blank=True)
    pm_notes = models.TextField(default='', blank=True)
    professional_rating = models.IntegerField(default=0, blank=True)  # 1-10
    attitude_rating = models.IntegerField(default=0, blank=True)  # 1 - 10
    agreement = models.URLField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name


class ArtistFeedback (models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, default='', blank=True, null=True,      related_name='%(class)s_Artist')
    pre_project_feedbace = models.TextField(default='', blank=True)
    on_project_feedback = models.TextField(default='', blank=True)
    post_project_feedback = models.TextField(default='', blank=True)

    def __str__(self):
        return self.artist.name + "--" + " Feedback"


class ProjectDemo (models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, default='', blank=True, null=True,   related_name='%(class)s_Artist')
    demo_work = models.ForeignKey(
        Work, on_delete=models.CASCADE, default='', blank=True, null=True, related_name='%(class)s_DemoWork')
    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, default='', blank=True, null=True,   related_name='%(class)s_Project')

    comment = models.TextField(default='', blank=True)
    status = models.CharField(
        max_length=100, default='', blank=True,       choices=PROJECT_DEMO_STATUS)

    def __str__(self):
        return self.artist.name + "--" + self.project.name + "--" + " Demo"


class Project(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, default='', blank=True, null=True,   related_name='%(class)s_Artist')
    stage = models.CharField(
        max_length=100, default='', blank=True,  choices=PROJECT_STAGE)

    brief = models.TextField(default='', blank=True)
    production_solution = models.TextField(default='', blank=True)
    comments = models.TextField(default='', blank=True)

    shortlisted_artists = models.ManyToManyField(
        Artist, default='', blank=True, related_name='%(class)s_shortlistedArtist')
    assigned_artists = models.ManyToManyField(
        Artist, default='', blank=True, related_name='%(class)s_AssignedArtist')
    showcase_demos = models.ManyToManyField(
        Work, default='', blank=True)

    project_demos = models.ManyToManyField(
        ProjectDemo, default='', blank=True, related_name='%(class)s_ProjectDemo')

    post_project_client_feedback = models.TextField(default='', blank=True)
    project_fee_Status = models.CharField(
        max_length=100, default='', blank=True, choices=PROJECT_FEE_STATUS)

    contract_status = models.BooleanField(default=False, blank=True)
    # project tracking stuff here


class ProjectFee(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, default='', blank=True, null=True, related_name='ProjectFee_to_Project_relation')

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, default='', blank=True, null=True,  related_name='ProjectFee_to_client_relation')

    solution_fee = models .FloatField(default=0, blank=True)

    production_advance = models.FloatField(default=0, blank=True)
    negotiated_advance = models.FloatField(default=0, blank=True)
    final_advance = models.FloatField(default=0, blank=True)

    advance_status = models.CharField(
        max_length=100, default='', blank=True, choices=PROJECT_ADVANCE_STATUS)

    assigned_artist_payouts = models.ManyToManyField(
        Artist, default='')
    artist_payout_status = models.CharField(
        max_length=100, default='', choices=ARTIST_PAYOUT_STATUS)

    final_fee_settlement_status = models.BooleanField(
        default=False, blank=True
    )

    post_project_client_total_payout = models.FloatField(default=0, blank=True)

    project_fee_Status = models.CharField(
        max_length=100, default='', blank=True, choices=PROJECT_FEE_STATUS)


class ArtistRequest(models.Model):
    skill = models.  CharField(
        max_length=100, default='', blank=True, choices=SKILLS)

    location = models.CharField(max_length=100, default='', blank=True)
    genre = models.CharField(max_length=100, default='', blank=True)
    language = models.CharField(max_length=100, default='', blank=True)
    other_performin_arts = models.TextField(default='', blank=True)

    budget_range = models.CharField(max_length=100, default='', blank=True)
    budget_idea = models.TextField(default='', blank=True)

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, default='', blank=True, null=True, related_name='ArtistRequest_to_Project_relation')

    production_hiring = models.IntegerField(default=0, blank=True)
    service_hiring = models.IntegerField(default=0, blank=True)
    shortlisted_artists = models.ManyToManyField(
        Artist, default='',  related_name='%(class)s_ShortlistedArtist'
    )

    rejected_artists = models.ManyToManyField(
        Artist, default='',  related_name='%(class)s_RejectedArtist')

    target = models.IntegerField(default=0, blank=True)
    comments = models.TextField(default='', blank=True)
    hiring_status = models.CharField(
        max_length=100, default='', blank=True, choices=HIRING_STATUS)


class Manager (models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name
