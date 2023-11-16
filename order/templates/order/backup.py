
@login_required
def profile(request):
    try:
        user_profile = User.objects.get(user=request.user)
        return render(request, 'order/profile.html', {'user_profile': user_profile})
    except User.DoesNotExist:
        # Render a template indicating that the profile doesn't exist
        return render(request, 'order/profile.html')