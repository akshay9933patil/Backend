from datetime import datetime


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.last_activity = None

    def __call__(self, request):
        if request.session.get('last_activity'):
            self.last_activity = request.session['last_activity']

        response = self.get_response(request)

        # Check for inactivity and display a warning if necessary.
        if self.last_activity is not None and (datetime.now() - self.last_activity).seconds > 60:
            # Check if the user has any active windows.
            if len(request.session['window_ids']) > 1:
                response.set_cookie('session_timeout', 'true', max_age=30)
            else:
                # Log the user out.
                response.delete_cookie('sessionid')

        return response

