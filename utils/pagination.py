from django.utils.safestring import mark_safe

class Pagination(object):
    def __init__(self, current_page, data_count, per_page_count=10, pager_num=10):
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.pager_num = pager_num

    @property
    def start(self):
        """
        数据库分片的开始
        :return:
        """
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        """
        数据库分片的结束
        :return:
        """
        return self.current_page * self.per_page_count

    @property
    def total_count(self):
        """
        分页的个数
        :return: 总共分多少页
        """
        v, y = divmod(self.data_count, self.per_page_count)
        if y:
            v += 1
        return v

    def page_str(self,base_url):
        page_list = []
        if self.total_count < self.pager_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.pager_num +1)/2:
                start_index = 1
                end_index = self.pager_num + 1
            else:
                start_index = self.current_page - (self.pager_num - 1) / 2
                end_index = self.current_page + (self.pager_num + 1) / 2
                if (self.current_page + (self.pager_num - 1) / 2) > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - self.pager_num + 1

        if self.current_page == 1:
            # prev = '<li><a href="javascript:void(0);"> « </a></li>'
            prev = ''
        else:
            prev = '<li><a href="%s?p=%s"> « </a></li>' %(base_url,self.current_page - 1)
        page_list.append(prev)

        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<li class="active"><a href="%s?p=%s">%s</a></li>' % (base_url, i, i)
            else:
                temp = '<li><a href="%s?p=%s">%s</a></li>' % (base_url, i, i)
            page_list.append(temp)

        if self.current_page == self.total_count:
            # prev = '<li><a href="javascript:void(0);"> » </a></li>'
            prev = ''
        else:
            prev = '<li><a href="%s?p=%s"> » </a></li>' % (base_url, self.current_page + 1)
        page_list.append(prev)
        return mark_safe("".join(page_list))