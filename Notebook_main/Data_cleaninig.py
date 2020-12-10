This note book does exploratory data analysis and data cleaning.
File descriptions:
. sales_train.csv - the training set. Daily historical data from January 2013 to October 2015 for different products and shops.
. test.csv - the test set. You need to forecast the sales for these shops and products for November 2015.
. items.csv - supplemental information about the items/products.
. item_categories.csv - supplemental information about the items categories.
. shops.csv- supplemental information about the shops.
. sample_submission.csv - a sample submission file in the correct format.
Data Fields:
.shop_id - unique identity of a shop
. item_id - unique identity of a product
. item_category_id - unique identity of the category of a item
. item_cnt_day - It is number of products sold each day. You are predicting a monthly amount of this measure
. item_price - current price of an item.
. date - date in format dd/mm/yyyy
. date_block_num - It represents a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
. item_name - name of the item
. shop_name - name of the shop
. item_category_name - name of item category
Exploratory Data Analysis
## Check versions
import lighgbm as lgb
import numpy as np
import pandas pd
import sklearn
import dateutil
import xgboost
import catboost
