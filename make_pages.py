contents = open("Blog_text.txt","r")
with open("blog_text.html", "w") as e:
    e.write("<table>\n")
    for lines in contents.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")
