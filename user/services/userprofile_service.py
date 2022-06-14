from user.models import UserProfile as UserProfileModel




# 사용자 프로필 create
def create_user_profile(user, introduction, age, birthday):
    return UserProfileModel.objects.create(
        user=user,
        introduction=introduction,
        age=age,
        birthday=birthday
    )
