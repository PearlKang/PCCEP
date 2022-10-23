# 24
sub_count=int(input("현재 구독자 수:"))
watch_time=int(input("시청시간:"))

if sub_count>=1000 and watch_time>=4000:
    print("수익 창출 가능")
else:
    print("수익 창출 불가능")