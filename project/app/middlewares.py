from django.http import HttpResponse

class MaintainTopSecretMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print('Before view')
        # print(request.path)
        # # print(request.META)
        # print(request.body
        # )
        # print(request.user)

        # print(request.path)

        if request.path == "/secret/":
            if request.user.username == "swift":
                response = self.get_response(request)

                return response

            else:
                return HttpResponse("Not accessible")
            
        else:
            response = self.get_response(request)
            return response
            




        # Code to be executed for each request/response after
        # the view is called.
        # print('After view')
        # print(response)


class SiteUnderMaintainanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print('Before view')
        # print(request.path)
        # # print(request.META)
        # print(request.body
        # )
        # print(request.user)
        return HttpResponse("Site is under maintainance")

