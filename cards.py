# =========== Card Contents=============
# card contents to be imported to objects
# store as dictionaries for card name and descriptions 
# name cards for hard coded tiles by tile number to draw the corresponding tile
# other cards to be drawn randomly are numbered arbitrarily
START = {1: {'title': 'Youre from a Ashkenazi Jewish descent',
            'description': 'Jewish women, particularly those of Ashkenazi descent, have a higher risk of carrying specific BRCA gene mutations.',
            'suggestion': 'If you have family history, consider genetic counseling to evaluate your breast cancer risk'},
        2: {'title': 'Two first- or second-degree relatives diagnosed with breast cancer before an average age of 45 (at least one must be a first-degree relative)',
            'description': 'Family history is a significant risk factor in early onset breast cancer. ',
            'suggestion': 'You have a higher chance having an inherited genetic predisposition to breast cancer. Consider genetic counselling/testing to make informed decisions'},
        3: {'title': 'You have one first- or second-degree relative with breast or ovarian cancer and a male relative with breast cancer ',
            'description': 'Breast cancer in male is rare and family history plays a huge role in breast cancer risk.',
            'suggestion': 'You have a higher chance having an inherited genetic predisposition to breast cancer. Consider genetic counselling/testing to make informed decisions'},
        4: {'title': 'You have four relatives diagnosed with breast cancer at any age (one must be a first-degree relative)',
            'description': 'Family history playes a huge role in bresat cnacer risk.',
            'suggestion': 'You have a higher chance having an inherited genetic predisposition to breast cancer. Consider genetic counselling/testing to make informed decisions'},
        5: {'title': 'You have two first- or second-degree relatives diagnosed with ovarian cancer at any age',
            'description': 'Hereditary ovarian cancer is related to breast cancer due to shared genetic links i.e. BRCA gene.',
            'suggestion': 'You have a higher chance having an inherited genetic predisposition to breast cancer. Consider genetic counselling/testing to make informed decisions'},
        6: {'title': 'You have one first- or second-degree relative with both breast and ovarian cancer',
            'description': 'Hereditary ovarian cancer is related to breast cancer due to shared genetic links i.e. BRCA gene.',
            'suggestion': 'You have a higher chance having an inherited genetic predisposition to breast cancer. Consider genetic counselling/testing to make informed decisions'},
        7: {'title': 'You don’t have any relatives who has breast or ovarian cancers.',
            'description': 'Breast cancers is not only hereditary, it could be developed at later stages due to spontaneous gene mutations',
            'suggestion': 'You have may not have family history of breast cancer but don’t ignore the lifestyle risks of breast cancers.'}}

INFO = {1: {'title': 'BRCA is not the only breast cancer related gene!',
            'description': 'Mutations in other genes such as PTEN, TP53, CDH1, and STK11 could also affect the risk of developing breast cancer',
            'suggestion': 'If you have family history, consider genetic counseling to evaluate your breast cancer risk'},
        2: {'title': 'Young girls can also get breast cancer',
            'description': 'The youngest breast cancer patient to-date was diagnosed at 8 years old',
            'suggestion': 'Breast education is never too early, start learning about self-examination to save your life'},
        3: {'title': 'Breast cancer lumps could be painless',
            'description': 'Breast cancer lumps are often hard and painless, although some are painful. However, not all lumps are cancer. Benign cysts can also cause painful lumps.',
            'suggestion': 'Learn about self-examination properly and be alerted. Schedule a mammogram screening with your healthcare provider if there are symtoms'},
        4: {'title': 'Swelling in or around your breast, collarbone, or armpit are also symtoms of breast cancer',
            'description': 'Swelling or lumps around your collarbone or armpits can be caused by breast cancer that has spread to lymph nodes in those areas. The swelling can occur even before you can feel a lump in your breast.',
            'suggestion': 'If you have swelling, be sure to let your health care provider know as soon as possible.'},
        5: {'title': 'Persisted skin dimpling is also a warning flag to look out for',
            'description': 'If the skin of your breast starts to feel thicker and looks a bit like an orange peel, it can be caused by inflammatory breast cancer',
            'suggestion': 'If your symptoms don’t improve after a week or so, you should get checked again'},
        6: {'title': 'Nipple retraction doesn’t just occur with ageing, it is also a symtom of breast cancer',
            'description': 'Breast cancer can sometimes cause your nipple to turn inward',
            'suggestion': 'If you notice a change in your nipple, get checked by your health care team right away. '},
        7: {'title': 'Look out for anything other than milk that comes out of your breasts',
            'description': 'Nipple discharge other than milk is often caused by injury, infection, or a benign tumor. However, breast cancer is a possibility, especially if the fluid is bloody.',
            'suggestion': 'If you notice abnormal discharge in your nipple, get checked by your health care provider right away. '}}

RANDOMEVENT = {1: {'title': 'You think you are too young',
            'description': 'You dismiss your relative’s suggestion to learn about self-checks because you think you’re too young',
            'suggestion': 'This false belief delays awareness. Remember: young women can be affected too.'},
        2: {'title': 'Self-checks feel awkward',
            'description': 'You avoid breast self-exams because it feels uncomfortable or embarrassing',
            'suggestion': 'Learning you body helps normalize it. Awareness starts with comfort and knowledge'},
        3: {'title': 'Nobody talks about it',
            'description': 'You realize your peers never talk about breast health, so you don’t either',
            'suggestion': 'Silence can lead to ignorance. Start the conversation, it might help someone else too.'},
        4: {'title': 'You Google a symptom',
            'description': 'You feel discomfort in your breast and turn to the internet',
            'suggestion': 'Not all online info is reliable. Use trusted sources or talk to health care provider/breast cancer communities.'},
        5: {'title': 'Too much going on',
            'description': 'You’re juggling work and relationships. Breast health is just not a priority.',
            'suggestion': 'It’s easy to overlook prevention, but health habits now can pay off later'},
        6: {'title': 'Empowerment through education',
            'description': 'You attend an awarenes talk conducted by BCF and learnt how to do a proper self-check',
            'suggestion': 'Knowledge gives you control. You feel more confident and informed'},
        7: {'title': 'Community screening',
            'description': 'You saw BCF’s mammobus drove by and considered scheduling a screening',
            'suggestion': 'Early detection saves your life. Get affordable and accessible screening with our community.'},
        8: {'title': 'You discovered symtoms around your breast',
            'description': 'You performed self-examination and discoverd symtoms like lump, skin dimpling and abnormal nipple discharge',
            'suggestion': 'These are warning flags of breast cancer, schedule a mammogram with your healthcare provider for timely diagnosis and treatment'},}

# dict names by tile indices
HEALTHMOMENT = {3: {'title': 'You have reached childhood. Do you consume a lot of ultra processed food?',
            'description': 'Ultra processed food contain high levels of unhealthy components like saturated fats, sugar, and sodium, and may also contain additives, preservatives, and contaminants that could contribute to cancer development',
            'suggestion': ['You have increased risk of breast cancer', 'You have decreased risk of breast cancer'],
            'effect': [1, -1]}, # indices corresponding to choice yes: 0, no: 1
        7: {'title': 'You find yourself going out with peers to drink too often. Do you still have time to keep up with exercising? (alcoholic route) ',
            'description': 'Lack of physical activity increases the risk of breast cancer.',
            'suggestion': ['You have decreased risk of breast cancer', 'You have increased risk of breast cancer'],
            'effect': [-1, 1]},
        10: {'title': 'You started family planning. Are you going to have your first child before 30? (fertility route 1)',
            'description': 'First child after 30 increases breast cancer risk compared to those with early pregnancy',
            'suggestion': ['You have decreased risk of breast cancer', 'You have increased risk of breast cancer'],
            'effect': [-1, 1]},
        12: {'title': 'Your baby is born. Do you breastfeed? (fertility route 2)',
            'description': 'Breast feeding decreases the risk of breast cancer as it reduces women’s lifetime exposure to estrogen.',
            'suggestion': ['You have decreased risk of breast cancer', 'You have increased risk of breast cancer'],
            'effect': [-1, 1]},
        13: {'title': 'Do you use oral contraceptives or birth control shots for contraception? (contraception route)',
            'description': 'Oral contraceptives or birth control shots contain hormones that potentially increases the risk of breast cancer',
            'suggestion': ['You have increased risk of breast cancer', 'You have decreased risk of breast cancer'],
            'effect': [1, -1]},
        16: {'title': 'You have reached the age of menopause. Do you use hormonal therapies to relieve the symtoms? (late adulthood)',
            'description': '(Combination) hormonal therapies to relieve symtoms of menopause contains estrogen that increases the risk of breast cancer',
            'suggestion': ['You have increased risk of breast cancer', 'You have decreased risk of breast cancer'],
            'effect': [1, -1]},
        18: {'title': 'You have become more concerned with health at this age. Do you still keep up with physical activity? (old age)',
            'description': 'Lack of physical activity increases the risk of breast cancer.',
            'suggestion': ['You have decreased risk of breast cancer', 'You have increased risk of breast cancer'],
            'effect': [-1, 1]},
        }

DECISIONPOINT = {4: {'title': 'You are going into the social scene as a young adult. Do you drink regularly?',
            'description': 'Alcohol consumption is a significant risk factor for breast cancer. Even light drinking could increase the likelihood of getting breast cancer, the more you drink the higher the risk.',
            'suggestion': ['You have increased risk of breast cancer', 'You have decreased risk of breast cancer'],
            'effect': [1, -1]}, # indices corresponding to choice yes: 0, no: 1
        9: {'title': 'You are thinking whether to start a family or not. Would you like to have kids?',
            'description': 'Having children reduces your risk of developing breast cancer as you have reduced lifetime exposure to estrogen',
            'suggestion': ['You have decreased risk of breast cancer', 'You have increased risk of breast cancer'],
            'effect': [-1, 1]},
        }

FINISH = {1: {'title': 'High (HBOC family history)',
            'description': 'You are at high risk of developing breast cancer because of your family history.',
            'suggestion': 'High surveillence or consider preventive surgical procedures.'}, # indices corresponding to choice yes: 0, no: 1
        2: {'title': 'Moderate (risk score > threshold)',
            'description': 'You have moderate risk of developing breast cancer as you have some risk increasing lifestyle habits.',
            'suggestion': 'Lifestyle is also an important factor affect breast cancer risk. Try to shift to a healthier lifestyle '},
        3: {'title': 'Low (risk score <= threshold)',
            'description': 'Good job with being conscious of lifestyle choices that could affect breast health. You have low risk of developing breast cancer.',
            'suggestion': 'Keep up with the healthy lifestyle and the awareness of your breast health. Of course, don’t forget to self-check regularly!'},
        }