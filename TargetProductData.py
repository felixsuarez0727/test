import requests

class TargetProductData():
    
    #API KEY FOR PRODUCT DATA
    key_product='ff457966e64d5e877fdbad070f276d18ecec4a01'
    #API KEY FOR QUESTIONS API
    key_question='c6b68aaef0eac4df4931aae70500b7056531cb37'

        
    def getJson(self, product_id):
        purl='https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key='+self.key_product+'&tcin='+product_id+'&store_id=2332&pricing_store_id=2332'
        qurl='https://r2d2.target.com/ggc/Q&A/v1/question-answer?type=product&questionedId='+product_id+'&key='+self.key_question

        try: 
            r_prod = requests.get(url=purl)
            prod = r_prod.json()
            print('ID: '+prod['data']['product']['tcin'])
            print('Title: '+prod['data']['product']['item']['product_description']['title'])
            
            if 'children' in prod['data']['product']:                
                print('Price: '+str(prod['data']['product']['children'][0]['price']['current_retail']))
                print('Description: '+prod['data']['product']['children'][0]['item']['product_description']['downstream_description'])
                print('Highlights: '+prod['data']['product']['children'][0]['item']['product_description']['soft_bullet_description'])
                print('Pictures: ')
                for pic in prod['data']['product']['children'][0]['item']['enrichment']['images']['alternate_image_urls']:
                    print('Image Link: '+pic)
            else:            
                print('Price: '+str(prod['data']['product']['price']['current_retail']))
                print('Description: '+prod['data']['product']['item']['product_description']['downstream_description'])
                print('Highlights: '+prod['data']['product']['item']['product_description']['soft_bullet_description'])
                print('Pictures: ')
                for pic in prod['data']['product']['item']['enrichment']['images']['alternate_image_urls']:
                    print('Image Link: '+pic)

            print('Specifications: ')
            for spec in prod['data']['product']['item']['product_description']['bullet_descriptions']:
                print('Spec: '+spec)
            
            r_quest = requests.get(url=qurl)
            questions = r_quest.json()

            print('Questions: ')
            if len(questions['results']) > 0:
                for question in questions['results']:
                    print('--Questions Says: '+question['text'])
                    if(len(question['answers'])>0):
                        for answer in question['answers']:
                            print('----Answer Says: '+answer['text'])
                    else:
                        print('----There are not answers')
            else:
                print('--There are not questions')
        except Exception:
            print ('Something went wrong!')


        
#https://www.target.com/p/apple-iphone-13-pro-max/-/A-84616123
#LINK WITH PRODUCT ID
item = TargetProductData()
item.getJson('84616123')
