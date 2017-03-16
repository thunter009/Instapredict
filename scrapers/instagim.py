from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import time
import csv

driver = webdriver.Chrome()
#open up the page
driver.get('http://www.instagim.com/tag/nature')

#create the csv
csv_file = open('instagim.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['index','image','hashtags', 'comments', 'caption','user','filter','time', 'likes'])

#click the load more photos button on the bottom as many times as you like 
#for i in range(0,75):
#    button = driver.find_element_by_xpath('/html/body/div/div[@class="content"]/div[@class="load-more-wrap ims"]/button')
#    button.click()
#    time.sleep(3)

#define it as a function
def get_photos(num):
    index = 0
    #at the moment don't need this while loop, will probably remove
    while index < num:
        try:
        	photos = driver.find_elements_by_xpath('/html/body/div/div[@class="content"]/div[@class="box-photos clearfix"]/div[@class="box-photo"]')
        	print len(photos)
        	index = index + 1
        	counter = 0
        	for photo in photos:
        		print "Photo" + str(counter)
        		counter += 1
                        dic = {}

                        user = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="user-info-wrap"]/div[@class="user-info"]/div[@class="username"]/a').text
                        print 'user ok'

                        image = photo.find_element_by_xpath('./div[@class="photo"]/a/img')
                        src = image.get_attribute('src')
                        print 'image ok'
                        
                        time_post = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="user-info-wrap"]/div[@class="user-info"]/div[@class="upload-time"]').text
                        print 'time post ok'
                        
                        caption = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="photo-description"]')
                        caption = caption.text.encode('ascii', 'ignore')
                        print 'caption ok'
 
                        hashtags = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="photo-tags"]').text
                        print 'hashtags ok'
                        
                        filters = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="photo-footer clearfix"]/div[@class="filter-text"]').text
                        print 'filters ok'
                        
                        comments = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="photo-footer clearfix"]/div[@class="soc-wrap"]/a[@class="photo-comments"]/span[@class="icon-chat"]').text
                        print 'comments ok'
                        
                        likes = photo.find_element_by_xpath('./div[@class="photo-info"]/div[@class="photo-footer clearfix"]/div[@class="soc-wrap"]/a[@class="photo-likes"]/span[@class="icon-thumbs-up-alt"]').text
                        print 'likes ok'

                        dic['index'] = index
                        dic['image'] = src
                        print 'img good'
                        dic['user'] = user.encode('ascii', 'ignore')
                        print 'user good'
                        dic['time'] = time_post.encode('ascii', 'ignore')
                        print 'time good'
                        dic['caption'] = caption
                        dic['hashtags'] = hashtags.encode('ascii', 'ignore')
                        print 'hash good'
                        dic['filters'] = filters.encode('ascii', 'ignore')
                        print 'filt good'
                        dic['comments'] = comments.encode('ascii', 'ignore')
                        print 'comm good'
                        dic['likes'] = likes.encode('ascii', 'ignore')
                        print 'likes good'

                        #problems with an encoding error when writing a row here
                        try:
                            writer.writerow(dic.values())
                            urllib.urlretrieve(src, str(index) + ".jpg") #I'll do more with this later
                            print 'write good'
                        except:
                            print 'nah'
                            
                        time.sleep(2)
        except Exception as e:
            print e
            csv_file.close()
            driver.close()
            break

#call the function
get_photos(1)


