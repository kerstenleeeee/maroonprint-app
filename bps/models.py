from django.db import models

# Create your models here.

class Building(models.Model):
  buildID = models.CharField(primary_key = True, max_length = 100)
  buildName = models.CharField(max_length = 100)

  def __str__(self):
    return "%s (%s)" % (self.buildID, self.buildName)

class Floor(models.Model):
	buildID = models.ForeignKey(Building, on_delete = models.CASCADE)
	floorID = models.CharField(primary_key = True, max_length = 100)
	floorNo = models.IntegerField()	

	class Meta:
		unique_together = (('buildID', 'floorID'),)

	def __str__(self):
		return '%s (%s)' % (self.buildID, self.floorID)