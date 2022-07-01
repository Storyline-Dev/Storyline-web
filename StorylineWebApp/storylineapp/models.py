from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Address(models.Model):
    street =  models.CharField(max_length=200)
    unitNumber = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

# class User(models.Model):
    
#     firstName = models.CharField(max_length=200)
#     lastName = models.CharField(max_length=200)
#     rememberMe = models.BooleanField()
#     username = models.CharField(max_length=200)
#     userType = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     activityStatus = models.BooleanField()
#     address = Address()
#     billingAddress = Address()

class Practice(models.Model):
    name = models.CharField(max_length=200)
    address = Address()
    country = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    numberOfLocations = models.IntegerField()
    percentageOfLicensed = models.FloatField()

class Clinician(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    practice = Practice()
    storylineNetwork = models.CharField(max_length=200)
    activityStatus = models.BooleanField()
    currentlyTakeClients = models.BooleanField()
    licensure = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class PracticeList(models.Model):
    sessionNumber = models.IntegerField()
    title = models.CharField(max_length=200)
    timesPerDay = models.IntegerField()
    timesPerWeek = models.IntegerField()
    practiceTool = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class CounselingNotes(models.Model):
    sessionNumber = models.IntegerField()
    title = models.CharField(max_length=200)
    dateOfSession = models.DateField()
    lastEdited = models.DateTimeField(default=timezone.now)
    summaryPoints = models.CharField(max_length=200)
    additionalDescription = models.CharField(max_length=200)
    visibility = models.BooleanField()

class HealthAssessment(models.Model):
    dateTime = models.DateTimeField()

class Pathways(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField()
    startDate = models.DateField()
    endDate = models.DateField()

class Journal(models.Model):
    sessionNumber = models.IntegerField()
    title = models.CharField(max_length=200)
    sessionType = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    journalPoints = models.CharField(max_length=200)
    additionalDescription = models.CharField(max_length=200)

class Memory(models.Model):
    title = models.CharField(max_length=200)
    month = models.IntegerField()
    year = models.IntegerField()
    people = models.JSONField()
    coreBeliefs = models.JSONField()
    emotions = models.JSONField()
    polarity = models.CharField(max_length=200)
    impactLevel = models.IntegerField()
    storyDescription = models.CharField(max_length=200)
    reauthoredStory = models.CharField(max_length=200)

class BodyScan(models.Model):
    location = models.CharField(max_length=200)
    sensation = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    intensity = models.IntegerField()
    frontOrBack = models.CharField(max_length=200)

class EmotionWheel(models.Model):
    emotion = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    emotionDescriptorOne = models.CharField(max_length=200)
    emotionDescriptorTwo = models.CharField(max_length=200)

class PreSessionCheckIns(models.Model):
    sessionDate = models.DateField()
    feeling = models.CharField(max_length=200)
    progressRating = models.IntegerField()
    bodyScan = models.CharField(max_length=200)
    importantDescription = models.CharField(max_length=200)

class Exercise(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField()
    description = models.CharField(max_length=200)

# class GroundingExercises(models.Model):
# class Genogram(models.Model):
# class Goals(models.Model):
class SafetyProtocol(models.Model):
    safePeople = models.JSONField()
    biggestTrigger = models.JSONField()
    calmDown = models.JSONField()

class Patient(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField('Date of Birth')
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    startDate = models.DateField('Start Date')
    lastSession = models.DateField('Last Session Date')
    numOfSessions = models.IntegerField()
    activityStatus = models.BooleanField()
    groundingNumber = models.IntegerField()
    messaging = models.BooleanField()
    resources = models.JSONField()
    therapist = models.CharField(max_length=200)
    practiceList = PracticeList()
    counselingNotes = CounselingNotes()
    healthAssessment = HealthAssessment()
    pathways = Pathways()
    journal = Journal()
    storyline = models.JSONField()
    bodyScan = BodyScan()
    emotionWheel = EmotionWheel()
    preSessionCheckIns = PreSessionCheckIns()
    personalityAssessments = models.CharField(max_length=200)
    groundingExercises = models.CharField(max_length=200)
    storylineToolkit = models.CharField(max_length=200)
    genogram = models.CharField(max_length=200)
    goals = models.CharField(max_length=200)
    safetyProtocol = SafetyProtocol()

