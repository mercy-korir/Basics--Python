Courses= ['History','Math','Physics','Compsci']
print(Courses)
print(len(Courses))
print(Courses[0])
print(Courses[-1])
print(Courses[0:2])
"Modifying Lists"
"1) Append methods"
Courses.append('Geography')
print(Courses)
"2) Insert method"
Courses.insert(0,'Geography')
print(Courses)
"3) Extend method"
Courses_2= ['Art','Education']
Courses.insert(0,Courses_2)
print(Courses[0])
Courses.extend(Courses_2)
"Removing Value from the list"
"1) Remove method"
Courses.remove('Math')
"2) Pop method"
Courses.pop()
print('popped')
print(Courses)
"Sorting the list"
"1)  Reverse method"
Courses.reverse()
print(Courses)
"2) Sort Method"
Courses.sort()
"Sorted version in alphabetic and ascending order"
nums=[1,5,2,4,3]
Courses.sort()
nums.sort()
print(Courses)
print(nums)
"Sorted version in desceding order"
Courses.sort(reverse=True)
nums.sort(reverse=True)
print(Courses)
print(nums)
"Sorted version without alteration of original list"
sorted_courses=sorted(Courses)
print(sorted_courses)
"Min, max and sum"
print(sum(nums))
print(min(nums))
print(max(nums))
