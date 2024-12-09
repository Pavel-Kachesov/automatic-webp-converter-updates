import shutil
from PIL import Image
import os
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import subprocess
from pynput.keyboard import Controller, Key

def wait_for_element(driver):
    # Устанавливаем явное ожидание
    wait = WebDriverWait(driver, 15)  # ожидание 30 секунд
    while True:
        try:
            # Перемещаем курсор в точку (x=100, y=200)
            pyautogui.moveTo(412, 454)
            time.sleep(1)

            pyautogui.click(412, 454)

            # Проверяем, появился ли элемент с id 'artificial-flash'
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#artificial-flash')))
            print('Элемент #artificial-flash появился на странице!')
            pyautogui.moveTo(1865, 224)

            time.sleep(1)
            pyautogui.click(1865, 224)
            time.sleep(5)
            break  # Выход из цикла, если элемент найден
        except:
            print('Элемент #artificial-flash не найден, продолжаем ожидать...')
            # Можно добавить задержку перед следующей проверкой, чтобы уменьшить нагрузку
            time.sleep(2)  # Задержка в 2 секунды перед следующей проверкой





def klikCSS(css):
    menu_itemcss = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, css)))
    # Клик по нужному элементу меню
    menu_itemcss.click()


def convert_to_webp(input_dir, output_dir, quality=80):
    # Создаём выходную директорию, если её нет
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # Удаляем содержимое директории
    os.makedirs(output_dir, exist_ok=True)  # Создаём пустую директорию

    # Перебираем все файлы в директории
    for file_name_to_convert in os.listdir(input_dir):
        input_path_to_convert = os.path.join(input_dir, file_name_to_convert)

        # Проверяем, является ли файл изображением
        if os.path.isfile(input_path_to_convert) and file_name_to_convert.lower().endswith(
                ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            output_path_to_convert = os.path.join(output_dir, os.path.splitext(file_name_to_convert)[0] + ".webp")
            try:
                with Image.open(input_path_to_convert) as img:
                    img.save(output_path_to_convert, format='WEBP', quality=quality)
                    print(f"Обработан файл: {input_path_to_convert} -> {output_path_to_convert}")
                    return output_path_to_convert
            except Exception as e:
                print(f"Ошибка обработки файла {input_path_to_convert}: {e}")


# Путь к папке "images" на рабочем столе
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
save_folder = os.path.join(desktop, "images")

# Убедимся, что папка существует, если нет — создаём её
if os.path.exists(save_folder):
    # Удаляем все файлы и папки внутри
    shutil.rmtree(save_folder)
os.makedirs(save_folder)

# Cesta k Chromedriveru
chromedriver_path = ""
pocetstran = 3

# Otevřeme Chrome pomocí Selenium
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Ссылка, которую нужно открыть
url = ''
# Перейти по ссылке


driver.get(url)

# Ожидание появления полей ввода логина и пароля
wait = WebDriverWait(driver, 10)

# Ввод логина
login_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#frmloginForm-email')))
login_field.send_keys("")

# Ввод пароля
password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#frmloginForm-password')))
password_field.send_keys("")

# Нажатие на кнопку входа
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#frmloginForm-login')))
login_button.click()

# Открываем новую вкладку
driver.execute_script("window.open('https://canntropy.admin.s19.upgates.com/manager/files/?filesPaginator-page=1"
                      "#openSubMenu', '_blank');")
print("Окно 2: ", driver.current_url)

# Получаем список всех открытых окон/вкладок
windows = driver.window_handles
print("Все окна:", windows)
driver.switch_to.window(windows[0])

# Ожидание загрузки после входа и поиск элемента для клика
menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#slide-out > div > div > ul > '
                                                                    'li.d-flex.flex-column > ul > li:nth-child(4) > '
                                                                    'a.collapsible-header.sm-link.arrow-r > '
                                                                    'span.menu-close-hide')))

# Клик по нужному элементу меню
menu_item.click()

# Ожидание загрузки после входа и поиск элемента для клика
menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > main > div.main-in.MenuToggleTop > div > '
                                                                    'div.container.fluid.d-flex.flex-nowrap.align'
                                                                    '-items-start.align-items-xl-center.justify'
                                                                    '-content-between.header-main > '
                                                                    'div.buttons.MainButtonsDesktop > '
                                                                    'a.btn.btn-default.ShowDataGridFilters')))

# Клик по нужному элементу меню
menu_item.click()
# Ожидание загрузки после входа и поиск элемента для клика
menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#frmform-filter-image_column')))

# Клик по нужному элементу меню
menu_item.click()
# Находим элемент <select> с помощью его CSS-селектора
select_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#frmform-filter-image_column')))

# Создаем объект Select, чтобы работать с выпадающим списком
select = Select(select_element)

# Выбираем значение, по-видимому, тексту
select.select_by_visible_text('Ano')

menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid-productsGrid-FiltersContainer > '
                                                                    'div.py-2.w-100.datagrid-filters-button > a')))

# Клик по нужному элементу меню
menu_item.click()
# Разворачиваем окно браузера на весь экран
driver.maximize_window()

# Подождем, чтобы увидеть результат поиска
time.sleep(5)
first = True
# Цикл на 20 повторений
for i in range(pocetstran):
    print("stranka " + str(i + 1))
    # Цикл на 20 повторений
    for index in range(25):
        # Форматирование селектора с использованием текущего языка
        xpath = f'//*[@id="frm-productsGrid-form"]/div[4]/table/tbody/tr[{index + 1}]/td[4]/a'
        print("product " + str(index + 1))

        # Теперь находим элемент, который становится видимым
        sitem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # Кликаем на элемент
        sitem.click()
        if first:
            first = False
            # Ожидание загрузки после входа и поиск элемента для клика
            menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                               '#editProductForm > div.ProductEdit > '
                                                               'div.fieldset-hidding.mt-0.IconTabsFielsetsSource > '
                                                               'fieldset.first.fieldset-open > legend > a')))

            # Клик по нужному элементу меню
            menu_item.click()
            time.sleep(1)
            # Ожидание загрузки после входа и поиск элемента для клика
            menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                               '#editProductForm > div.ProductEdit > '
                                                               'div.fieldset-hidding.mt-0.IconTabsFielsetsSource > '
                                                               'fieldset:nth-child(5) > legend > a')))

            # Клик по нужному элементу меню
            menu_item.click()
        # Ожидаем и находим элемент
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#editProductForm > div.ProductEdit > '
                                                                              'div.fieldset-hidding.mt-0'
                                                                              '.IconTabsFielsetsSource > '
                                                                              'fieldset.ButtonSaveHide.fieldset-open '
                                                                              '> legend > a > small')))

        # Получаем текст элемента
        text = element.text

        # Выводим его в консоль
        print("number of img = " + text)
        number = int(text)
        # Явное ожидание элементов на странице
        wait = WebDriverWait(driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#sortable-items > div > i')))

        # Создание объекта ActionChains
        actions = ActionChains(driver)
        indexx = 1

        # Поочередно наводим мышь на каждый элемент
        while indexx < len(elements)+1:
            # Найдите элемент с помощью CSS-селектора
            elementatribut = driver.find_element(By.CSS_SELECTOR, f'#sortable-items > div:nth-child({indexx})')

            data_item_file_id = elementatribut.get_attribute('data-item-file-id')
            actions.move_to_element(elements[indexx-1]).perform()
            # Получаем атрибут 'data-item-file-id' для текущего элемента

            # Выводим атрибут и индекс
            print(f"Индекс: {indexx}, data-item-file-id: {data_item_file_id}")
            # Здесь можно добавить дополнительные действия, если необходимо
            print(f"Навели мышь на элемент: {elements[indexx-1]}")
            time.sleep(1)
            actions.move_to_element(elements[indexx-1]).click().perform()  # Наведение и клик
            time.sleep(1)
            print(indexx)
            # Ожидаем появления элемента
            # Найдем элемент с помощью XPath и получим его текст
            element = driver.find_element(By.XPATH, f'//*[@id="sortable-items"]/div[{indexx}]/div[1]/div[1]/div')
            text = element.text

            # Выведем текст элемента
            print(text)

            # Проверяем, если последние 4 символа текста - 'webp'
            if not text.endswith('webp'):
                # Теперь найдем соответствующие чекбоксы для этого элемента
                checkbox_main = driver.find_element(By.CSS_SELECTOR, f'#image_main_yn_{data_item_file_id}')
                checkbox_list = driver.find_element(By.CSS_SELECTOR, f'#image_list_yn_{data_item_file_id}')
                # Проверяем, отмечен ли чекбокс
                if checkbox_main.is_selected():
                    checkbox_main = True
                    print("Чекбокс отмечен!")
                else:
                    checkbox_main = False
                    print("Чекбокс не отмечен.")

                if checkbox_list.is_selected():
                    checkbox_list = True
                    print("Чекбокс отмечен!")
                else:
                    checkbox_list = False
                    print("Чекбокс не отмечен.")

                # Убедитесь, что элемент видим и доступен для клика
                klikCSS(f'#sortable-items > div:nth-child({indexx}) > div.card-body.card-action.d'
                        f'-flex.flex-column.justify-content-center.align-items-center.CardBody > '
                        f'div.text-center.cb-btns > a.btn-floating.btn-dark.edit.ml-1')
                link_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#editTitleDialog > '
                                                                                           'div.form-group.form-group'
                                                                                           '-text > a')))

                # Получение значения атрибута href
                image_url = link_element.get_attribute("href")
                print(f"Ссылка: {image_url}")

                # Скачать изображение
                response = requests.get(image_url, stream=True)
                if response.status_code == 200:
                    # Извлечение имени файла из URL
                    # Убедимся, что папка существует, если нет — создаём её
                    if os.path.exists(save_folder):
                        # Удаляем все файлы и папки внутри
                        shutil.rmtree(save_folder)
                    os.makedirs(save_folder)
                    file_name = os.path.join(save_folder, os.path.basename(image_url))

                    # Сохраняем файл
                    with open(file_name, "wb") as file:
                        shutil.copyfileobj(response.raw, file)
                    print(f"Изображение сохранено в {file_name}")
                    path = convert_to_webp("/Users/Kachesov/Desktop/images", "/Users/Kachesov/Desktop/vystup", 100)
                    klikCSS('body > div.ui-dialog-container.opened > div > '
                            'div.ui-dialog-titlebar.ui-widget-header.ui-corner-all.ui-helper-clearfix > a')
                    # крестик закрыть
                    klikCSS(f'#sortable-items > div:nth-child({indexx}) > i')
                    klikCSS(f'#sortable-items > div:nth-child({indexx}) > '
                            'div.card-body.card-action.d-flex.flex-column.justify-content-center.align-items-center'
                            '.CardBody > div.text-center.cb-btns > a.btn-floating.btn-danger.unlink.ml-1')

                    # Получаем список всех окон
                    windows = driver.window_handles

                    # Переключаемся на новое всплывающее окно (например, оно будет вторым)
                    driver.switch_to.window(windows[1])

                    time.sleep(1)
                    try:
                        klikCSS('#snippet--folders > ul > li > div.collapsible-body > ul > li.droppable.open > div > a > small')
                        search_box = wait.until(
                            EC.visibility_of_element_located((By.XPATH, '//*[@id="frmsearchForm-search"]')))
                        # Очищаем поле ввода
                        search_box.clear()

                        # Вставляем текст в поле поиска
                        search_box.send_keys(text)

                        # Нажимаем Enter, чтобы отправить форму
                        search_box.send_keys(Keys.RETURN)
                        time.sleep(3)

                        element = wait.until(EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '#snippet--managerFiles > div.manager-files.FilesCardContainer.card-item'
                                              '-group.no-crosshair > div > i')))
                        # Наводим курсор на элемент
                        actions.move_to_element(element).perform()  # Наведение и клик
                        klikCSS("#snippet--managerFiles > div.manager-files.FilesCardContainer.card-item-group.no"
                                "-crosshair > div > "
                                "div.card-body.card-action.d-flex.flex-column.justify-content-center.align-items-center"
                                ".CardBody > div.text-center.cb-btns > a.btn-floating.btn-dark.ml-1.FileEdit")
                        time.sleep(1)
                        klikCSS('#frm-editNameForm > div:nth-child(3) > a')
                        time.sleep(3)
                        # Найдем элемент <input type="file"> с помощью его селектора
                        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                        # Вставляем путь к файлу в поле ввода
                        print(path)
                        file_input.send_keys(path)

                        time.sleep(5)
                    except:
                        search_box = wait.until(
                            EC.visibility_of_element_located((By.XPATH, '//*[@id="frmsearchForm-search"]')))
                        # Очищаем поле ввода
                        search_box.clear()
                        driver.refresh()
                        time.sleep(5)
                        klikCSS(
                            '#snippet--folders > ul > li > div.collapsible-body > ul > li.droppable.open > div > a > small')
                        time.sleep(3)
                        # Найдем элемент <input type="file"> с помощью его селектора
                        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                        # Вставляем путь к файлу в поле ввода
                        print(path)
                        file_input.send_keys(path)

                        time.sleep(5)

                    driver.switch_to.window(windows[0])
                    driver.refresh()
                    time.sleep(5)

                    # Сдвигаем курсор на 15 пикселей вниз

                    # Наводим мышь на кнопку меню
                    menu_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "#images > div.buttons.MainButtonsDesktop > "
                                                                         "div > a"))
                    )
                    actions.move_to_element(menu_button).perform()
                    # Кликаем на элемент по индексу в меню
                    actions.move_by_offset(0, 50).click().perform()
                    # Ожидаем, чтобы увидеть результат
                    time.sleep(5)

                    wait_for_element(driver)

                    if number > 1:
                        elementss = wait.until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#sortable-items > div > i')))

                        first_element = elementss[1]
                        print(first_element)

                        # Получаем ID текущего элемента (например, через атрибут)
                        data_item_file_id = first_element.get_attribute("data-item-file-id")  # Укажите точный атрибут

                        # Устанавливаем галочку, если не отмечено
                        if checkbox_main:
                            klikCSS(
                                f'#sortable-items > div:nth-child(1) > div.card-footer.flex-nowrap.justify-content-between.px-25.pb-2 > div.form-group.td_main_yn > label')
                            print("Чекбокс Main отмечен!")

                        if checkbox_list:
                            klikCSS(
                                f'#sortable-items > div:nth-child(1) > div.card-footer.flex-nowrap.justify-content-between.px-25.pb-2 > div.form-group.td_list_yn > label')
                            print("Чекбокс List отмечен!")
                    elements = wait.until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#sortable-items > div > i')))

                    # Предположим, вы уже переключились на нужное окно
                    driver.switch_to.window(windows[1])

                    # Перезагрузка текущей вкладки
                    driver.refresh()

                    time.sleep(5)
                    driver.switch_to.window(windows[0])

                else:
                    print(f"Ошибка загрузки изображения: {response.status_code}")
            else:
                print("Пропуск: текст заканчивается на 'webp'")
            indexx += 1
        # Ожидание загрузки после входа и поиск элемента для клика
        menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > main > div.main-in.MenuToggleTop '
                                                                            '> div > '
                                                                            'div.header-top-page.body-color-dark'
                                                                            '.header-top.short > div > '
                                                                            'div.header-top-left > a')))

        # Клик по нужному элементу меню
        menu_item.click()

    # Ожидание загрузки после входа и поиск элемента для клика
    menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#frm-productsGrid-form > '
                                                                        'div.row.grid-under.no-gutters.footer > '
                                                                        'div.col-md.paginator.text-center.form-sm'
                                                                        '.text-xl-center.text-md-left > '
                                                                        'a.icon.px-3.ajax.paginator-next')))

    # Клик по нужному элементу меню
    menu_item.click()
# Завершение работы драйвера
driver.quit()
