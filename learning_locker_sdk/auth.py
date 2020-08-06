import requests
import base64

class LearningLockerAuth(object):

    basic_token = None
    basic_token_b64 = None
    token = None
    auth_type = "Bearer"

    def __init__(self, base_url, auth_token_path, admin_email, admin_password):
        token = self._make_b64_token(admin_email, admin_password)

        self.base_url = base_url
        self.auth_token_path = auth_token_path

        # Need to convert back to a string to make concatenatable
        self.basic_token = token.decode("utf-8")

        # Store in b64 just in case
        self.basic_token_b64 = token
    
    def _make_b64_token(self, email, password):
        # The user and pwd combo must be passed in b64
        base_string = "{}:{}".format(email, password)
        bytestream = base_string.encode("ascii")
        return base64.b64encode(bytestream)

    
    @property
    def get_bearer_token(self):
        # Construct a token to send to the JWT endpoint
        basic_auth_header_string = "Basic " + self.basic_token
        request_url = self.base_url + self.auth_token_path
        # Make the token generating endpoint
        response = requests.post(
            request_url,
            headers={"Authorization": basic_auth_header_string}
        )
        # Return the token
        # TODO: error handling code
        self.token = "{} {}".format(self.auth_type, response.text) 
        return self.token