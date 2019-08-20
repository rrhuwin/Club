# coding=gbk
# 人生苦短，我用python
__auther__ = 'Mr.Hu'

class Pageinfo(object):
    #                  当前页  总数据量    每页显示数量  展现页面数量
    def __init__(self, page, all_count, par_page, url,tp, showpage=11):
        try:
            self.page =int(page)
        except Exception as e:
            self.page=1
        self.par_page = par_page
        self.tp=tp
        # 计算总页码数
        a, b = divmod(all_count, par_page)
        if b:
            a = a + 1
        self.all_page = a  # 总页数
        self.showpage = showpage
        self.url = url

    # 取值开始
    def start(self):
        return (self.page - 1) * self.par_page

    #     取值结束
    def end(self):
        return self.page * self.par_page

    def a_page(self):
        if self.all_page <= self.showpage:
            begin = 1
            sotp = self.all_page + 1
        else:
            if self.page <= 5:
                begin = 1
                sotp = self.showpage
            else:
                if self.page + 5 >= self.all_page:
                    begin = self.all_page - self.showpage
                    sotp = self.all_page + 1
                else:
                    begin = self.page - 5
                    sotp = self.page + 5 + 1
        if self.page <= 1:
            # prev = f"<a class='page-link' href='' aria-label='Previous'><< 上一页</a>"
            prev = f'<li class="page-item "><a class="page-link" href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span><span class="sr-only">Previous</span></a></li>'
        else:
            # prev = f"<a class='page-link' href='{self.url}?page={self.page - 1}' aria-label='Previous'><< 上一页</a>"
            prev = f'<li class="page-item "><a class="page-link" href="{self.url}{self.tp}/{self.page - 1}" aria-label="Previous"><span aria-hidden="true">&laquo;</span><span class="sr-only">Previous</span></a></li>'
        if self.page >= self.all_page:
            next = f"<a class='page-link' href='' aria-label='Next'>下一页>></a>"
            next = f'<li class="page-item"><a class="page-link" href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span><span class="sr-only">Next</span></a></li>'
        else:
            next = f'<li class="page-item"><a class="page-link" href="{self.url}{self.tp}/{self.page + 1}" aria-label="Next"><span aria-hidden="true">&raquo;</span><span class="sr-only">Next</span></a></li>'
            # next = f"<a class='page-link' href='{self.url}?page={self.page + 1}' aria-label='Previous'>下一页>></a>"

        pagelist = []
        pagelist.append(prev)
        for i in range(begin, sotp):
            if i == self.page:
                # v = f"<a  class='page-item active' href='{self.url}?page={i}'>{i}</a>"
                v= f'<li class="page-item active"><a class="page-link" href="{self.url}{self.tp}/{i}">{i}</a></li>'
            else:
                # v = f"<a  class='page-item active' href='{self.url}?page={i}'>{i}</a>"
                v= f'<li class="page-item "><a class="page-link" href="{self.url}{self.tp}/{i}">{i}</a></li>'

            pagelist.append(v)
        pagelist.append(next)
        # print(v)
        return ''.join(pagelist)
