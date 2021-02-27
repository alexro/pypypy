def solve(N):
    R = 0
    k = 0
    L = 10
    while k < 9:
        m = 0
        s = 0
        t = 0
        while s < 9:
            z = (N // (10 ** s)) % 10
            if z > m and z < L:
                m = z
                t = s
            s += 1
        if m > 0:
            R = R * 10 + t
            k += 1
            L = m

    return R == 285197364


for k in range(1000000000):
    res = solve(k)
    if res:
        print(k)
        break

# # # n = 5
# # # for mask in range(1 << n):
# # #     for i in range(n):
# # #         # if mask & (1 << i):
# # #         #     print(i + 1)
# # #         print(mask, bin(mask), i, bin(i), 1 << i, bin(1 << i), mask & (1 << i) > 0)
# #
# # import random
# # import os
# #
# # random.seed(os.urandom(128))
# #
# # dt = {
# #     0: [1, 2],
# #     1: [3]
# # }
# #
# # t = {
# #     0: (0, 0, 0, 0)
# # }
# #
# # ROOT = PRIORITY = 0
# # LEFT_CHILD = 1
# # RIGHT_CHILD = 2
# # VALUE = 3
# #
# #
# # def rnd():
# #     r = random.randint(0, 10000000000)
# #     while r in t:
# #         r = random.randint(0, 10000000000)
# #     return r
# #
# #
# # def add(parent, node):
# #     print('add', parent, node)
# #     left_child = parent[LEFT_CHILD]
# #     right_child = parent[RIGHT_CHILD]
# #
# #     if left_child == 0:
# #         t[parent[PRIORITY]] = (node[PRIORITY], left_child[PRIORITY], 0, node[VALUE])
# #
# #
# # def insert(x):
# #     priority = rnd()
# #     node = (priority, 0, 0, x)
# #     t[priority] = node
# #
# #     if t[ROOT][PRIORITY] == 0:
# #         t[ROOT] = node
# #     elif t[ROOT][PRIORITY] < priority:
# #         node = (priority, t[ROOT][PRIORITY], 0, x)
# #         t[ROOT] = node
# #     else:
# #         add(t[ROOT], node)
# #
# #
# # def go(dt, n):
# #     if n in dt:
# #         for c in dt[n]:
# #             go(dt, c)
# #     print(n)
# #
# #
# # insert(12)
# # insert(15)
# #
# # print(t)
#
# import xml.dom.minidom
#
# document = """\
# <slideshow>
# <title>Demo slideshow</title>
# <slide><title>Slide title</title>
# <point>This is a demo</point>
# <point>Of a program for processing slides</point>
# </slide>
#
# <slide><title>Another demo slide</title>
# <point>It is important</point>
# <point>To have more than</point>
# <point>one slide</point>
# </slide>
# </slideshow>
# """
#
# dom = xml.dom.minidom.parseString(document)
#
#
# def getText(nodelist):
#     rc = []
#     for node in nodelist:
#         if node.nodeType == node.TEXT_NODE:
#             rc.append(node.data)
#     return ''.join(rc)
#
#
# def handleSlideshow(slideshow):
#     print("<html>")
#     handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
#     slides = slideshow.getElementsByTagName("slide")
#     handleToc(slides)
#     handleSlides(slides)
#     print("</html>")
#
#
# def handleSlides(slides):
#     for slide in slides:
#         handleSlide(slide)
#
#
# def handleSlide(slide):
#     handleSlideTitle(slide.getElementsByTagName("title")[0])
#     handlePoints(slide.getElementsByTagName("point"))
#
#
# def handleSlideshowTitle(title):
#     print("<title>%s</title>" % getText(title.childNodes))
#
#
# def handleSlideTitle(title):
#     print("<h2>%s</h2>" % getText(title.childNodes))
#
#
# def handlePoints(points):
#     print("<ul>")
#     for point in points:
#         handlePoint(point)
#     print("</ul>")
#
#
# def handlePoint(point):
#     print("<li>%s</li>" % getText(point.childNodes))
#
#
# def handleToc(slides):
#     for slide in slides:
#         title = slide.getElementsByTagName("title")[0]
#         print("<p>%s</p>" % getText(title.childNodes))
#
#
# handleSlideshow(dom)
