# ★★★ mutable immutable 자료구조 정리 ★★★

immutable_str   = "String is immutable!!"
immutable_int   = 10
immutable_float = 10.0
immutable_tuple = ("Tuple is immutable!!")
immutable_frozenset = frozenset({"Frozenset is immutable!!"})

mutable_list    = ["list is mutable!!"]
mutable_dict    = {"dict": "is mutavle!!"}
mutable_set     = {"set is mutable!!"}

# mutable, immutable 성격을 가진 객체를 변수에 저장
str_ = immutable_str
int_ = immutable_int
float_ = immutable_float
tuple_ = immutable_tuple
frozenset_ = immutable_frozenset

list_ = mutable_list
dict_ = mutable_dict
set_ = mutable_set

# 변수에 data 추가하기
str_ += " immutable string!!"
int_ += 10
float_ += 10
tuple_ += (" immutable tuple!!")
frozenset_ |= frozenset({"immutable frozenset!!"})


list_.append("mutable list!!")
dict_["add"] = "mutable dict!!"
set_ |= {"mutable set!!"}

# 처음 만든 객체와 데이터를 추가한 변수의 좌표값과 데이터 비교하기
print("★★  immutable ★★")
print(f"hex_id: {hex(id(immutable_str))}        immutable_str: {immutable_str}")
print(f"hex_id: {hex(id(str_))}                 str_: {str_}")
print(f"hex_id: {hex(id(immutable_int))}        immutable_int: {immutable_int}")
print(f"hex_id: {hex(id(int_))}                 int_: {int_}")
print(f"hex_id: {hex(id(immutable_float))}      immutable_float: {immutable_float}")
print(f"hex_id: {hex(id(float_))}               float_: {float_}")
print(f"hex_id: {hex(id(immutable_tuple))}      immutable_tuple: {immutable_tuple}")
print(f"hex_id: {hex(id(tuple_))}               tuple_: {tuple_}")
print(f"hex_id: {hex(id(immutable_frozenset))}  immutable_frozenset: {immutable_frozenset}")
print(f"hex_id: {hex(id(frozenset_))}           frozenset_: {frozenset_}")

print("")
print("★★  mutable ★★")
print(f"hex_id: {hex(id(mutable_list))}         mutable_list: {mutable_list}")
print(f"hex_id: {hex(id(list_))}                list_: {list_}")
print(f"hex_id: {hex(id(mutable_dict))}         mutable_dict: {mutable_dict}")
print(f"hex_id: {hex(id(dict_))}                dict_: {dict_}")
print(f"hex_id: {hex(id(mutable_set))}          mutable_set: {mutable_set}")
print(f"hex_id: {hex(id(set_))}                 set_: {set_}")


# 해당 코드를 실행했을 때 나오는 결과를 유추하고
# mutable 자료형과 immutable 자료형은 어떤 게 있는지 알아야 함