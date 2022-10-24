# 문자 합치기
text=["Monday","Friday","Saterday"]
print("".join(text))
print(" ".join(text))
print(":".join(text))

# 공백문자 제거
text="        아따 날씨 좋구마이!         "
print(text.strip())
print(text.lstrip())
print(text.rstrip())