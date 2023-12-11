echo "mongo-init.sh is running"
mongoimport --jsonArray --db planet_djanet  --collection posts_1 --file /data/posts_1.json
mongoimport --jsonArray --db planet_djanet  --collection posts --file /data/posts.json
mongoimport --jsonArray --db planet_djanet  --collection followers --file /data/followers.json
mongoimport --jsonArray --db planet_djanet  --collection following --file /data/following.json
mongoimport --db planet_djanet --collection all_content --type=csv --file /data/Tous_les_contenus.csv --headerline
mongoimport --db planet_djanet --collection couverture_insta --type=csv --file /data/Couverture_Insta.csv --headerline
mongoimport --db planet_djanet --collection visitors_insta --type=csv --file /data/Visits_Insta.csv --headerline
mongoimport --db planet_djanet --collection likes_gender_age --type=csv --file /data/likes_gender_age.csv --headerline
mongoimport --db planet_djanet --collection likes_city --type=csv --file /data/likes_ville.csv --headerline
mongoimport --db planet_djanet --collection couverture_fb --type=csv --file /data/Couverture.csv --headerline
mongoimport --db planet_djanet --collection likes_fb --type=csv --file /data/Visits_Fb.csv --headerline
mongoimport --db planet_djanet --collection pub --type=csv --file /data/Tendances_publicitaires.csv --headerline