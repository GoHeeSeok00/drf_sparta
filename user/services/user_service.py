from user.models import User as UserModel



# 사용자 create
def create_user(username, password, email, fullname):
    return UserModel.objects.create(
        username=username,
        password=password,
        email=email,
        fullname=fullname
    )