from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import io
from PIL import Image
import requests
import time


service = Service('C:/driver/chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=service, options=options)


#source = "put/full/url/to/single/image/source"

#download_path = "put/full/path/to/directory"


def download_multiple_images(driver, max_img, delay):

	def scroll_to_end(driver):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = """https://www.google.com/search?q=forest&rlz=1C1BNSD_plPL998PL998&source=lnms&tbm=
		isch&sa=X&ved=2ahUKEwiVoOSfoeH2AhVGAxAIHQp4BTwQ_AUoAXoECAEQAw&biw=1920&bih=947&dpr=1"""

	driver.get(url)

	image_urls = set()

	while len(image_urls) < max_img:
		scroll_to_end(driver)
		thumbnails = driver.find_elements(By.CLASS_NAME,"Q4LuWd")

		for img in thumbnails[len(image_urls):max_img]:
			try:
				img.click()
				time.sleep(delay)
			except Exception as e:
				print(f"something went wrong - {e!r}")
				continue
			
			images = driver.find_elements(By.CLASS_NAME,"n3VNCb")

			for image in images:
				if image.get_attribute("src").startswith("http"):
					image_urls.add(image.get_attribute("src"))
					print(f"file nr {len(image_urls)} collected")
	
	return image_urls


def download_image(download_path, source, file_name):

	try:
		image_content = requests.get(source).content
		image_bytes = io.BytesIO(image_content)
		image = Image.open(image_bytes)
		file_path = download_path + "/" + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")
			print("successfully downloaded")

	except Exception as e:
		print(f"something went wrong - {e!r}")


urls = download_multiple_images(driver,10,2)

for i, url in enumerate(urls):
	download_image(download_path, url, str(i) + ".jpg")