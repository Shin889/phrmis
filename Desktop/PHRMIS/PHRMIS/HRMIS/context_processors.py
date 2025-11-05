from .models import PersonalInformation

def employee_context(request):
    if request.user.is_authenticated:
        try:
            employee = PersonalInformation.objects.get(user=request.user)
            profilepicture = employee.profilepicture.url if employee.profilepicture else None
        except PersonalInformation.DoesNotExist:
            employee = None
            profilepicture = None
    else:
        employee = None
        profilepicture = None

    return {
        'employee': employee,
        'profilepicture': profilepicture,
    }
