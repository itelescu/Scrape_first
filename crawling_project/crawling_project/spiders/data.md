CSS selectors

name_auto = response.xpath('//*/div[1]/h2/a/text()').get()
price_auto = response.xpath('//*/div[4]/div/span/text()').get()
km_auto = response.xpath('//*/div[1]/div/ul/li[2]/text()').get()
fuel_auto = response.xpath('//*/div[1]/div/ul/li[4]/text()').get()
location = response.xpath('//*/div[1]/ul/li[1]/span/span/text()[1]').get()


name_auto = response.css('div.ooa-1mxnix4.e1b25f6f15>h2>a::text').get()
publish_date = response.css('div.ooa-1mxnix4.e1b25f6f15>ul>li::text').get()
link_auto = response.css('div.ooa-1mxnix4.e1b25f6f15>h2>a::attr(href)').get()


class_tip_marca = ooa-1gk8lbw



