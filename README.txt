Scripts consisting of two functions.


The first function  'download_image' is responsible for downloading the single image from google chrome.

parameters:

download_path - full path to the directory where the image will be stored

source - full url to the single image

file_name - name of the downloaded photo


The Second function 'download_multiple_images' is responsible for collecting multiple imagesand then the transfer of their "download photos" function
which will save them to disk

parameters:

driver - webdriver defined

max_img - maximum number of photos to download

delay - delay with which the function will start downloading the next photo