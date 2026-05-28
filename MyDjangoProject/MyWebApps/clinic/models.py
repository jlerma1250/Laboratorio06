from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)

    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    full_name = models.CharField(max_length=150)
    dni = models.CharField(max_length=8, unique=True)

    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['full_name']

    def save(self, *args, **kwargs):
        self.full_name = self.full_name.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateTimeField()
    reason = models.TextField()

    status = models.CharField(max_length=20, default='pending')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date']

    def __str__(self):
        return f"{self.patient} - {self.doctor}"


class MedicalRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)

    diagnosis = models.TextField()
    observations = models.TextField(null=True, blank=True)
    treatment_plan = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Record {self.appointment}"


class Treatment(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Exam(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)

    exam_name = models.CharField(max_length=100)
    result = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exam_name


class Payment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    status = models.CharField(max_length=20, default='pending')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Payment {self.amount}"