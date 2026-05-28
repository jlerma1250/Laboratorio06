from .models import (
    Specialty,
    Doctor,
    Patient,
    Appointment,
    MedicalRecord,
    Treatment,
    Exam,
    Payment
)

admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Treatment)
admin.site.register(Exam)
admin.site.register(Payment)
