# drf_sparta // DRF 학습 저장소 입니다.


## Information
1. 강의시간 : 월/수/금 (20:00~22:00)
2. 과제 목표
    - 과제는 단순하게 문제를 풀어보는 것에서 끝나는 것이 아닌, 이후 진행 할 프로젝트의 기반을 다지고 활용하는 것을 목표로 진행합니다.
    - 과제는 지금까지 강의했던 내용을 기반으로 내고 있습니다.
    - 과제에 나온 코드를 작성하실 때에는 꼭 과제에 있는 내용만 적으실 필요는 없습니다. 테이블, 권한 등을 자유롭게 추가 / 수정 하셔도 좋습니다.
3. App 설명
    - user: 회원가입 정보, 프로필 정보 등 사용자 리소스 핸들링
    - blog: 게시글 리소스 핸들링
    - product: 이벤트, 상품 리소스 핸들링
    - assignment: DRF 연습 및 과제 
   

<br><br>


* * *
### 🎈1일차 과제 (22.06.07)
1. 포스트맨으로 get 요청 보낼때 success 메시지 출력되게 views.py, urls.py 작성하기
    - 깃헙 코드: https://github.com/GoHeeSeok00/drf_sparta/blob/main/assignment/views.py
2. python mutable, immutable 객체 정리하기 
    - 블로그: https://a-littlecoding.tistory.com/87
    - 코드: https://github.com/GoHeeSeok00/drf_sparta/blob/main/python_script.py

* * *
### 🎈2일차 과제 (22.06.08)
1. one to one, many to many 등 다양한 속성을 가진 필드를 사용해 모델링 해보기
    - user/models.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/user/models.py
    - user/admin.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/user/admin.py
2. CBV를 사용해 views.py 구성해보기
3. custom user psermission을 활용해 내가 원하는 대로 권한 바꿔보기
    - user/views.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/user/views.py


* * *
### 🎈3일차 과제 (22.06.10)
1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.
2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
```
    - createsuperuser admin 계정 생성 시 custom user 반영해서 permission_level, email 저장
```
3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요
4. blog라는 앱을 만든 후 settings.py에 등록해주세요
5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)
```
    - 작성 시간, 수정 시간 필드 추가
```
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요
    - blog/models.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/blog/models.py
```
    - 사용자는 `ForeignKey` 카테고리는 `ManyToManyField` 사용해서 관계 형성
```
8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요
    - blog/admin.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/blog/admin.py
9. admin 페이지에서 사용자, 카테고리, 게시글을 자유롭게 추가해주세요
10. views.py에 username, password를 받아 로그인 할 수 있는 기능을 만들어주세요
    - 로그인 기능 구현이 처음이시라면 3일차 강의자료 5번 항목을 확인해주세요
11. views.py에 로그인 한 사용자의 정보, 게시글을 보여주는 기능을 만들어주세요
    - user/views.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/user/views.py
12. views.py에 <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해주는 기능을 만들어주세요
    - 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정해주세요
    - 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 해주세요
      - blog/views.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/blog/views.py
      - blog/urls.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/blog/urls.py


* * *
### 🎈4일차 과제 (22.06.13)
1. blog 앱에 <게시글, 작성자, 작성 시간, 내용>이 포함된 comment라는 테이블을 추가해주세요
    - 게시글과 작성자는 fk 필드로 생성해주셔야 해요
        - blog/models.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/blog/models.py#L27
2. Django Serializer 기능을 사용해 로그인 한 사용자의 기본 정보들을 response data에 넣어서 return 해주세요
    - user/views.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/user/views.py#L35
3. 사용자가 작성 한 게시글을 로그인 한 (2번)User의 serializer data에 포함시켜서 같이 return해주세요
    - user/serializers.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/user/serializers.py#L64
    - result_image: https://github.com/GoHeeSeok00/drf_sparta/issues/11


* * *
### 🎈5일차 과제 (22.06.15)
1. product라는 앱을 새로 생성해주세요
2. product 앱에서 <제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부>가 포함된 event 테이블을 생성해주세요
    - product/models.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/product/models.py#L4
3. django serializer에서 기본적으로 제공하는 validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요
    - 전달 받은 데이터는 **kwargs를 사용해 입력해주세요
    - postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요
        - product/views.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/product/views.py#L24
4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 활성화 여부가 True인 event 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요
    - product/views.py: https://github.com/GoHeeSeok00/drf_sparta/blob/main/product/views.py#L15


* * *
### 🎈6일차 과제 (22.06.17)
1. product 앱에서 <작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부>가 포함된 product 테이블을 생성해주세요
2. django serializer를 사용해 validate / create / update 하는 기능을 구현해주세요
    1. custom validation 기능을 사용해 노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없도록 해주세요
    2. custom creator 기능을 사용해 상품 설명의 마지막에 “<등록 일자>에 등록된 상품입니다.” 라는 문구를 추가해주세요
    3. custom update 기능을 사용해 상품이 update 됐을 때 상품 설명의 가장 첫줄에 “<수정 일자>에 수정되었습니다.” 라는 문구를 추가해주세요
3. product 앱에서 <작성자, 상품, 내용, 평점, 작성일>을 담고 있는 review 테이블을 만들어주세요
4. 현재 날짜를 기준으로, 노출 종료 날짜가 지나지 않았고 활성화 여부가 True이거나 로그인 한 사용자가 등록 한 상품들의 정보를 serializer를 사용해 리턴해주세요
5. 4번 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
    1. 평균 점수는 (리뷰 평점의 합/리뷰 갯수)로 구해주세요
    2. 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
6. 로그인 하지 않은 사용자는 상품 조회만 가능하고, 회원가입 이후 3일 이상 지난 사용자만 상품을 등록 할 수 있도록 권한을 설정해주세요
