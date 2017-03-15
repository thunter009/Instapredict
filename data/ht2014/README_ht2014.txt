
######################################################
### Instagram datasets (HYPERTEXT-2014)
###
### Crawled: Jan 20 - Feb 17, 2014
### Source:  http://uweb.dimes.unical.it/tagarelli/data/ 
###
### TERMS OF USAGE:
### 1. The following paper is to be cited in any research product whose 
### findings are based on the data here distributed:
### 
### Emilio Ferrara, Roberto Interdonato, Andrea Tagarelli. 
### Online Popularity and Topical Interests through the lens of Instagram. 
### In Proc. 25th ACM Conference on Hypertext and Social Media, 
### September 1-4, 2014, Santiago, Chile.
###
### 2. The datasets cannot be redistributed.
######################################################


_________________________________________________

TABLE-OF-CONTENTS

1. Summary of the data crawling process
2. Data files and attributes
3. Basic statistics 
4. List of selected #whp contests


================================
1. Summary of the data crawling process
================================

This is an Instagram dump based on the Instagram weekend hashtag project (WHP) promoted by the Instagram's official blog (http://blog.instagram.com/tagged/weekend-hashtag-project). Every Friday, the Instagram team runs a photographic contest, which  is assigned a specific topic expressed by a unique hashtag prefixed with #whp.
 
We selected 72 popular contest #whp-tags and randomly picked up about 2,100 users who participated in at least one of those contests. All media uploaded by these users (including media that were not tagged with #whp-tags) were retrieved. 

The users selected to build the media dataset were used as seed nodes for the construction of the user network. This models asymmetric relationships that hold strictly among the participants in the contests. A breadth-first search process was started from the set of seed nodes, filtering out any user who did not participate in at least a whp contest.



=====================
2. Data files and attributes
=====================

media (csv)
	* mediaID: anonymized media ID.
	* authorID: anonymized ID of the user who created the media.
	* TS_upload: timestamp of media upload.
	* tagset: set of tags assigned to the media.
	* likes: number of likes received by the media.
	* comments: number of comments received by the media.

users (csv)
	* follower: anonymized follower ID.
	* followee: anonymized followee ID.
	* likes: number of likes that "follower" posted to media created by "followee".
	* comments: number of comments that "follower" posted to media created by "followee".
	* timestamps: comma-separated list of timestamps of the comments.


==============
3. Basic statistics
==============

media (csv)
	No. Media:		1,686,349
	No. Distinct users:	2,081
	No. Tags:			8,919,630
	No. Distinct tags:	269,359
	No. Likes:		1,242,923,022
	No. Comments:	41,341,783

users (csv):
	No. Nodes: 			44,766
	No. Links:			677,686
	Avg. In-degree:		15.14
	Avg. path length:		3.16			
	Clustering coefficient:	4.1E-2
	Diameter:			11
	Assortativity index:	-0.097 
	No. communities:		151
	Network modularity:	0.578


=========================
4. List of selected #whp contests
=========================

whpumbrellas
whpaquarium
whpstoryinmotion
whpmovingphotos
whpbirdsonawire
whppetportraits
whpmovingportrait
whpexplore
whpdoortodoor
whpgratefulfor
whpstilllife
whpjumpstagram
whpstoryportrait
whpfoggy
whpemptyspaces
whpshiftingseasons
whpfiftyfifty
whpgreatheights
whpmovingshadows
whpstrideby
whptakeahike
whpslowmotion
whpdearphotograph
whpsidewayscity
whpreplacemyface
whpmylibrary
whpunderoverpass
whpgoldenhour
whpleanwithit
whpsolocolor
whpputaplaneonit
whpmotherlylove
whpfilmedfromabove
whpneonsigns
whpartwatching
whpresolutions
whpbigreveal
whp100
whpuniqueportraitsoflove
whptruecalling
whphowicook
whplookingup
whpovergrown
whphideandseek
whpsuperpower
whpmotels
whpwaterdrops
whpfamilyportrait
whpmindtheclouds
whpsilhouettes
whpwhatmovesme
whpmyfavoriteplace
whpbehindthelens
whpreflectagram
whpnotquitea
whpbuildingpatterns
whpwaiting
whpthanksdad
whpthroughthetrees
whplighthouse
whpcaughtgramming
whpsignsoftheseason
whpflowerpower
whpchameleoncar
whpportraitofahome
whpfirstphotoredo
whpmyhometown
whpselfportrait
whpliquidlandscape
whpfromwhereistand
whpbluronpurpose
whpstraightfacades