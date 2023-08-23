# member1 = input(name, username, password)


class Member():
    'A Member class'
    mem_count = 0

    def __init__(self):
        self.name = input('name: ')
        self.username = input('id: ')
        self.password = input('password: ')
        Member.mem_count += 1

    def display(self):
        print(
            """
        이름:  {}
        아이디: {}
        """.format(self.name, self.username)
        )
        # print(self.name, self.username)


mem_1 = Member()
mem_2 = Member()
mem_3 = Member()

mem_1.display()
mem_2.display()
mem_3.display()

members = []

for i in range(Member.mem_count+1):
    members.append(Member())


print(members[Member.__name__])


#         mem_i.display()
#
#
# else:
#     print('최소 회원 수는 3명입니다. 회원을 더 만들어주세요.')

# 회원 인스턴스를 세 개 이상 만들고 (a~f라는 6개의 객체(인스턴스) 생성)
# a = Member('유기현', 'bongsook', '1122')
# b = Member('이민혁', 'potato', '1103')
# c = Member('손현우', 'shunuayo', '0618')
# d = Member('임창균', 'rose', '0126')
# e = Member('이주헌', 'honey', '1006')
# f = Member('채형원', 'coenffl', '0115')

# a.display()
# b.display()
# c.display()
# input으로 Member 인스턴스 생성

# members 라는 빈 리스트에 append를 써서 저장
# members 리스트를 돌면서 회원들의 이름을 모두 프린트


# for mem in [a, b, c, d, e, f]:
#     members.append(mem)
#     print(mem.name)


# for print in members:
#     members.append(Member)
#     return


class Post(Member):
    def __init__(self, title, content, author):
        posts = []
        self.title = title
        self.content = content
        Member.username = author
        # 작성자 (author) : 회원의 username 이 저장되어야 함!
        # Member.username = author
        # author = username

    # 게시글을 세 개 이상 작성하는 코드1(메소드 정의.ver)
    post_count = 0

    def posting(self):
        self.title = title
        self.content = content
        Member.username = author
        # 게시글을 세 개 이상 작성하기 위한 조건문 걸기
        # if post_count < 3:
        #     posting 레고


# 게시글을 세 개 이상 작성하는 코드2_Post 인스턴스 집어넣기(post 인스턴스 직접 생성.ver)
x = Post('배고프다', '빠빠이', '유기현')
y = Post('똑똑해', '너 정말', '이민혁')
z = Post('안녕', '안녕하세요', '손현우')
# posts 리스트에 append 저장

# 1)특정 유저의 작성 게시글 제목 프린트
# 하단 코드는 posts 리스트에 저장된 모든 객체의 title을 출력함
for i in [x, y, z]:
    posts.append(i)
    print(i.title)
# 2) 특정단어가 content에 포함된 게시글의 제목 프린트
    for a in [posts.title]:
        if '특정 단어' in a.content:
            print(a.title)


# # print

# # # for a in Post.title:
# # #     print()
