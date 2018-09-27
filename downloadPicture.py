from google_images_download import google_images_download

#從google下載照片
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"楊洋","output_directory":"pictures","no_directory":True}
response.download(arguments)