import scrapy
from asia_teachers.items import AsiaTeachersItem

class TeachersSpider(scrapy.Spider):
    name = "teachers"
    start_urls = ["https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty"]

    def parse(self, response):
        profiles = response.css('.i-member-profile-data-wrap')
        for profile in profiles:
            name = profile.css('.member-data-value-name a::text').get()
            expertise = profile.css('.member-data-value-7::text').get()
            if not expertise:
                expertise = "無"
            item = AsiaTeachersItem(name=name, expertise=expertise)
            yield item
