# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added models

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: models / entities for the database

from django.db import models

# building entity
class Building(models.Model):
  buildID = models.CharField(primary_key = True, max_length = 100)
  buildName = models.CharField(max_length = 100)

  def __str__(self):
    return "%s (%s)" % (self.buildID, self.buildName)

# floor entity
class Floor(models.Model):
	buildID = models.ForeignKey(Building, on_delete = models.CASCADE)
	floorID = models.CharField(primary_key = True, max_length = 100)
	floorNo = models.IntegerField()	
	floorImageLink = models.URLField()	

	class Meta:
		unique_together = (('buildID', 'floorID'),)

	def __str__(self):
		return '%s (%s)' % (self.buildID, self.floorID)