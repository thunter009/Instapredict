CREATE TABLE photo_info
	(
    caption char(255), 
    comments float, 
    filters char(255), 
    hashtags char(255), 
	image char(255), 
    key char(255), 
    likes float, 
    photo_id float, 
    post_time char(255), 
	scrape_time char(255), 
    tag char(255), 
    scrape_time char(255), 
    user char(255)
    );

CREATE TABLE user_info
	(
    full_name char(255), 
    posts float, 
    followers float, 
    user char(255), 
    bio char(255),
	following float, 
    scrape_time char(255)
    );