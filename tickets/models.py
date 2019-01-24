from django.db import models

class Passenger(models.Model):
  userID = models.CharField(primary_key=True, max_length=100)
  displayName = models.CharField(max_length=100)

  def __str__(self):
    return "%s (%s)" % (self.displayName, self.userID)

class Bus(models.Model):
  busID = models.CharField(primary_key=True, max_length=100)

  def __str__(self):
    return self.busID

class Terminal(models.Model):
  terminalID = models.CharField(primary_key=True, max_length=100)
  terminalName = models.CharField(max_length=100)    

  def __str__(self):
    return "%s (%s)" % (self.terminalName, self.terminalID)

class Driver(models.Model):
  driverID = models.CharField(primary_key=True, max_length=100)
  displayName = models.CharField(max_length=100)

  def __str__(self):
    return "%s (%s)" % (self.displayName, self.driverID)

class Trip(models.Model): 
  tripID = models.CharField(primary_key=True, max_length=100)
  departureDate = models.DateField()
  departureTime = models.TimeField()
  sourceTerminal = models.ForeignKey(Terminal, related_name='sourceTerminal', on_delete=models.CASCADE)
  destinationTerminal = models.ForeignKey(Terminal, related_name='destinationTerminal', on_delete=models.CASCADE)
  seatsLeft = models.IntegerField()
  price = models.IntegerField(default=0)

  def __str__(self):
    return "%s -> %s (%s)" % (self.sourceTerminal, self.destinationTerminal, self.tripID)

class Rating(models.Model):
  userID = models.ForeignKey(Passenger, on_delete=models.CASCADE)
  tripID = models.ForeignKey(Trip, on_delete=models.CASCADE)
  rating = models.IntegerField()

  class Meta:
    unique_together = (('userID', 'tripID'),)

  def __str__(self):
    return '%s (%s)' % (self.tripID, self.userID)
 
class Booking(models.Model):
  userID = models.ForeignKey(Passenger, on_delete=models.CASCADE)
  tripID = models.ForeignKey(Trip, on_delete=models.CASCADE)
  class Meta:
    unique_together = (('userID', 'tripID'),)

  def __str__(self):
    return '%s (%s)' % (self.tripID, self.userID)

class Bus_Trip(models.Model):
  busID = models.ForeignKey(Bus, on_delete=models.CASCADE)
  tripID = models.ForeignKey(Trip, on_delete=models.CASCADE)

  class Meta:
    unique_together = (('busID', 'tripID'),)

  def __str__(self):
    return '%s (%s)' % (self.tripID, self.busID)

class Bus_Driver(models.Model):
  busID = models.ForeignKey(Bus, on_delete=models.CASCADE)
  driverID = models.ForeignKey(Driver, on_delete=models.CASCADE)

  class Meta:
    unique_together = (('busID', 'driverID'),)

  def __str__(self):
    return '%s (%s)' % (self.driverID, self.busID)

class CurrentTerminal(models.Model):
  terminalID = models.ForeignKey(Terminal, on_delete=models.CASCADE)
  tripID = models.ForeignKey(Trip, on_delete=models.CASCADE)

  class Meta:
    unique_together = (('terminalID', 'tripID'),)

  def __str__(self):
    return '%s (%s)' % (self.tripID, self.terminalID)