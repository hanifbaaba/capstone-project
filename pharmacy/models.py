from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient_name = models.CharField(max_length=100)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_issued = models.DateField()

    def __str__(self):
        return f'{self.patient_name} - {self.medicine.name}'
