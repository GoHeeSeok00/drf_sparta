# drf_sparta // DRF 학습 저장소 입니다.


### 🎈1일차 과제
1. 포스트맨으로 get 요청 보낼때 success 메시지 출력되게 views.py, urls.py 작성하기
  - 깃헙 코드 : https://github.com/GoHeeSeok00/drf_sparta/blob/main/assignment/views.py
2. python mutable, immutable 객체 정리하기 
  - 블로그 : https://a-littlecoding.tistory.com/87
  - 깃헙 코드 : https://github.com/GoHeeSeok00/drf_sparta/commit/d387696f080ddb2b9d59749c205c25dfe3ab6dfd

* * *
### 🎈2일차 과제
1. one to one, many to many 등 다양한 속성을 가진 필드를 사용해 모델링 해보기
  - models.py : https://github.com/GoHeeSeok00/drf_sparta/blob/main/members/models.py
  - admin.py : https://github.com/GoHeeSeok00/drf_sparta/blob/main/members/admin.py
2. CBV를 사용해 views.py 구성해보기
3. custom user psermission을 활용해 내가 원하는 대로 권한 바꿔보기
  - views.py : https://github.com/GoHeeSeok00/drf_sparta/blob/main/members/views.py

* * *
### 🎈4일차 과제
1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.
2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요
4. blog라는 앱을 만든 후 settings.py에 등록해주세요
5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요
8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요
9. admin 페이지에서 사용자, 카테고리, 게시글을 자유롭게 추가해주세요
10. views.py에 username, password를 받아 로그인 할 수 있는 기능을 만들어주세요
    - 로그인 기능 구현이 처음이시라면 3일차 강의자료 5번 항목을 확인해주세요
11. views.py에 로그인 한 사용자의 정보, 게시글을 보여주는 기능을 만들어주세요
12. views.py에 <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해주는 기능을 만들어주세요
    - 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정해주세요
    - 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 해주세요
