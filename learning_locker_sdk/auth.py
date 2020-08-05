import requests
import base64

class LearningLockerAuth(object):

    basic_token = None
    token = None
    auth_type = "Bearer"

    def __init__(self, base_url, auth_token_path, admin_email, admin_password):
        self.basic_token = self._make_b64_token(admin_email, admin_password)

    def _make_b64_token(self, email, password):
        base_string =  "{}:{}".format(email, password)
        bytestream = base_string.encode("ascii")
        return base64.b64encode(bytestream)
    
    @property
    def get_bearer_token(self):
        basic_auth_header_string = "Basic " + self.basic_token
        request_url = self.base_url + self.auth_token_path
        response = requests.post(
            request_url,
            headers={"Authorization": basic_auth_header_string}
        )
        self.token = "{} {}".format(self.auth_type, response.text) 
        return self.token