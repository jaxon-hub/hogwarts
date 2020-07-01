"""
__author__ = 'jaxon'
__time__ = '2020/7/1 4:50 下午'
__desc__ = ''
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


def test_file_upload():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[2]').click()
    driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys("/Users/jaxon/Code/test_code/hogwarts/xueqiu_app/test_case/error.png")
    sleep(10)
    print(driver.title)
    driver.quit()

def test_drop():
    driver = webdriver.Chrome()
    driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
    draggable = driver.find_element_by_id("draggable")
    droppable = driver.find_element_by_id("droppable")
    action = ActionChains
    action.drag_and_drop(draggable,droppable).perform()  # 将元素draggable拖拽至droppable
    sleep(4)
    driver.switch_to.alert().accept()  # 操作alert弹窗，点击确认；dismiss()操作alert弹窗，点击取消
    driver.switch_to.default_content()  # 切换至主frame
    droppable.find_element_by_id("submitBTN").click()

    driver.quit()



if __name__ == '__main__':
    pytest.main()