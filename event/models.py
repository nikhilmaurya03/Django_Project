from django.db import models

# Create your models here.

class Event_Table(models.Model):
  #event_id = models.IntegerField(null =True)
  event_name = models.CharField(max_length=255) 
  event_date = models.DateField()
  event_duration = models.IntegerField()
  event_guest = models.CharField(max_length=255)
  event_participation_count = models.IntegerField(null=True) 
  event_cost = models.IntegerField(null=True)
  event_type = models.CharField(max_length=255)
  event_winner_id = models.IntegerField(null=True)
  event_image_location = models.CharField(max_length=255)
  
  def __str__(self):
      return f"{self.event_name} {self.event_date} {self.event_duration} {self.event_guest} {self.event_participation_count} {self.event_cost} {self.event_type} {self.event_winner_id} {self.event_image_location}"