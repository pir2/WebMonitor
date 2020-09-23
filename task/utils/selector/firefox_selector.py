import ast
import warnings

from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from task.utils.selector.selector import Selector as FatherSelector

warnings.filterwarnings("ignore")

class FirefoxSelector(FatherSelector):
    def __init__(self, debug=False):
        self.debug = debug

    def get_html(self, url, headers):
        # if headers:
        #     header_dict = ast.literal_eval(headers)
        #     if type(header_dict) != dict:
        #         raise Exception('必须是字典格式')

        #     for key, value in header_dict.items():
        #         if key.lower() == 'User-Agent':
        #             webdriver.DesiredCapabilities.PHANTOMJS[
        #                 'phantomjs.page.settings.userAgent'] = value
        #         else:
        #             webdriver.DesiredCapabilities.PHANTOMJS[
        #                 'phantomjs.page.customHeaders.{}'.format(key)] = value
        options = Options()
        # 默认userAgent
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        if self.debug:
            import os
            basepath = os.path.dirname(os.path.dirname(__file__))
            save_path = os.path.join(basepath, '..', 'static', 'error')
            os.makedirs(save_path, exist_ok=True)
            driver.save_screenshot(os.path.join(save_path, 'screenshot.png'))
        html = driver.page_source
        driver.quit()
        return html

    def get_by_xpath(self, url, xpath, headers=None):
        html = self.get_html(url, headers)
        if 'string()' in xpath:
            xpath = xpath.split('/')
            xpath = '/'.join(xpath[:-1])
            res = Selector(
                text=html).xpath(xpath)[0].xpath('string(.)').extract()
        else:
            res = Selector(text=html).xpath(xpath).extract()

        if len(res) != 0:
            return res[0]
        else:
            raise Exception('无法获取文本信息')# - {} - {}'.format(res,html))

    def get_by_css(self, url, xpath, headers=None):
        html = self.get_html(url, headers)
        res = Selector(text=html).css(xpath).extract()

        if len(res) != 0:
            return res[0]
        else:
            raise Exception('无法获取文本信息')
