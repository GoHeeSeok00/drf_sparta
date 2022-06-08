# ★★★ mutable immutable 자료구조 정리 ★★★

immutable_str   = "String is immutable!!"
immutable_int   = 10
immutable_float = 10.0
immutable_tuple = ("Tuple is immutable!!")
immutable_frozenset = frozenset({"Frozenset is immutable!!"})

mutable_list    = ["list is mutable!!"]
mutable_dict    = {"dict": "is mutavle!!"}
mutable_set     = {"set is mutable!!"}

# mutable, immutable 성격을 가진 자료구조를 각각의 변수에 저장
str_ = immutable_str
int_ = immutable_int
float_ = immutable_float
tuple_ = immutable_tuple
frozenset_ = immutable_frozenset

list_ = mutable_list
dict_ = mutable_dict
set_ = mutable_set

# 각각의 변수에 data 추가하기
str_ += " immutable string!!"
int_ += 10
float_ += 10
tuple_ += (" immutable tuple!!")
frozenset_ |= frozenset({"immutable frozenset!!"})


list_.append("mutable list!!")
dict_["add"] = "mutable dict!!"
set_ |= {"mutable set!!"}

# 기존의 데이터와 변수를 수정한 데이터간 자료 비교하기
print("★★  immutable ★★")
print(f"immutable_str:       {immutable_str}")
print(f"str_:                {str_}")
print(f"immutable_int:       {immutable_int}")
print(f"int_:                {int_}")
print(f"immutable_float:     {immutable_float}")
print(f"float_:              {float_}")
print(f"immutable_tuple:     {immutable_tuple}")
print(f"tuple_:              {tuple_}")
print(f"immutable_frozenset: {immutable_frozenset}")
print(f"frozenset_:          {frozenset_}")

print("")
print("★★  mutable ★★")
print(f"mutable_list:  {mutable_list}")
print(f"list_:         {list_}")
print(f"mutable_dict:  {mutable_dict}")
print(f"dict_:         {dict_}")
print(f"mutable_set:   {mutable_set}")
print(f"set_:          {set_}")


# 해당 코드를 실행했을 때 나오는 결과를 유추하고
# mutable 자료형과 immutable 자료형은 어떤 게 있는지 알아야 함