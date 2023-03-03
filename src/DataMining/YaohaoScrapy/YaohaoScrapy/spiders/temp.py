# 拦截请求
def process_request(self, request, spider):
    # return None
    driver = webdriver.Chrome(
        executable_path=r'E:\Python_Project\Scrapy\chromedriver.exe')
    if request.url == 'https://www.jianshu.com/' or request.url.split(
            '/')[-2] == 'u':
        # 打开一个指定网址
        driver.get(request.url)
        time.sleep(0.5)
        while True:
            # 获取当前网页正文全文高度
            check_height = driver.execute_script(
                "return document.body.scrollHeight;")
            try:
                # 如果获取到网页上有 阅读更多 则进行点击加载
                load = driver.find_element_by_class_name('load-more')
                print('已点击>阅读更多')
                load.click()
            except:
                pass
            # 移动一个网页正文全文高度，也就等于下拉一次到底部
            driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(0.5)
            # 计算最新的网页正文全文高度
            check_height1 = driver.execute_script(
                "return document.body.scrollHeight;")
            # 如果滑动一次，前后两次的高度都没有变的话，说明已经滑倒底部了
            if check_height == check_height1:
                break

    else:  # else 打开的都是文章内容, .../p/...
        # print(request.url)
        # 打开一个指定网址
        driver.get(request.url)
        time.sleep(0.5)
        try:
            i = 1
            while True:
                # 定位到专题 展开更多
                unfold = driver.find_element_by_class_name('H7E3vT')
                if i == 1:
                    # 注意找到了该元素，并不等于可以进行操作，需要在屏幕可视范围内进行操作；
                    # 注意如果没有找到该元素，会抛出异常。
                    driver.execute_script("arguments[0].scrollIntoView();",
                                          unfold)  # 拖动到可见的元素去
                    print('已将元素拖动到屏幕内')
                    # 以下需要注意，文章模块有两种，一种底部有推荐阅读，一种个人文章，底部没有推荐阅读。
                    try:
                        # 定位 “更多精彩内容” ， 如果定位到，说明有推荐阅读；如果没有定位到，则抛出异常，并被捕捉处理。
                        recom = driver.find_element_by_class_name('_29KFEa')
                        print('查找到该篇文章有 “推荐阅读”')
                        # 这里有坑，因为 在简书的文章中，头部跟底部都是固定定位（fixed）的，也就是说，当你定位到指定元素时，虽说是在屏幕内，但是不在可视范围内，需要格外做处理，进行上下拖动。
                        driver.execute_script('window.scrollBy(0,-100)')
                        # scrollBy(xnum,ynum) 是从当前位置滚动到某个相对位置，从当前位置起向右和向下滚动多少像素。
                        # scrollTo(xpos,ypos) 是滚动到某个绝对位置，即滚动到坐标为xpos,ypos的位置。
                        print('向上滑动100像素')
                    except:
                        print('查找到该篇文章没有 “推荐阅读”')
                        # 直接滑到底部即可，即屏幕的可视范围了
                        driver.execute_script(
                            'window.scrollTo(0,document.body.scrollHeight)')
                i += 1
                unfold.click()
                print('已点击>展开更多')
                time.sleep(0.5)

        except:
            print('本篇可能没有专题收入或者已经获取完了')

    source = driver.page_source  # 获取所有网页内容
    response = HtmlResponse(url=driver.current_url,
                            body=source,
                            request=request,
                            encoding='utf-8')
    driver.quit()  # 这里要注意的是，要先获取内容，在关闭浏览器
    return response
