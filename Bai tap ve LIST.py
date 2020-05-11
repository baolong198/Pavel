A=[2,3,4,5,6,7,8,9,5]
B=[-1,2,3,-2,4,5,-6,-7]
C=A+B #Ghép A và B thành List C
print(A) # In ra list A
print(B) # In ra list B
print(C) # In ra list C
C.sort() # Sắp xếp List C tăng dần
print(C.count(7)) # số lần xuất hiện
print(C.index(7)) # trả về vị trí xuất hiện
C=list(set(C)) #- Xóa các phần tử trùng nhau của List C
print(C) #in ra List C mới.