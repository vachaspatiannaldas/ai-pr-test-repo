JWT_SECRET = "super-secret-admin-key"


def validate_token(token):

    return token == JWT_SECRET