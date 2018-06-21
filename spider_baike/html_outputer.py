# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 代表着以utf-8的格式读取文件
        fout = open('output.html', 'w', encoding="utf-8")
        fout.write("<html>")
        fout.write("<head><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />\
        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /></head>")
        fout.write("<body>")
        fout.write("<div>")
        fout.write("<table id = \"customers\">")
        fout.write("<tr>")
        fout.write("<th>%s</th>" % '序号')
        fout.write("<th>%s</th>" % '标题')
        fout.write("<th>%s</th>" % '简介')
        fout.write("</tr>")
        #用sum来循环判断输出不同的样式
        sum  = 1
        for data in self.datas:
            if sum % 2 == 0:
                fout.write("<tr class = \"alt\">")
            else:
                fout.write("<tr>")
            fout.write("<td>%s</td>" % sum)
            sum = sum + 1
            fout.write("<td>%s</td>" % data['title'])
            # 错误记录：当加了meta之后，就不能再encoding了，都否还是乱码，原因不详
            # fout.write("<td>%s</td>" % data['title'].encoding('utf-8'))
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</div>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()