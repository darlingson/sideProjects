import json

def convert_data(input_data):
    output_data = {"scorers": []}
    for player, matches in input_data.items():
        for match_day, match_info in matches.items():
            for goal in match_info["goals"]:
                scorer = {
                    "name": player,
                    "day": match_day,
                    "score": match_info["finalScore"],
                    "time": goal["time"],
                    "result": match_info["result"],
                    "venue": match_info["venue"]
                }
                output_data["scorers"].append(scorer)
    return output_data

input_data = json.loads("{\r\n  \"Humphreys Minandi \":{\r\n    \"Wednesday, 01 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Ekwendeni Hammers\",\r\n      \"goals\":[\r\n        {\"time\":\"55\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"M. Paipi\":{\r\n    \"Wednesday, 01 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Chitipa United\",\r\n      \"goals\":[\r\n        {\"time\":\"07\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"R. Saizi\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-4\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Mighty Tigers\",\r\n      \"goals\":[\r\n        {\"time\":\"10\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Wednesday, 18 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"4-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"43\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"K. Ng\'ambi\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-4\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Mighty Tigers\",\r\n      \"goals\":[\r\n        {\"time\":\"66\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"L. Jere\":{\r\n    \"Tuesday, 17 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-3\",\r\n      \"result\":\"lost\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"FCB Nyasa Big Bullets\",\r\n      \"goals\":[\r\n        {\"time\":\"2\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Samuel Adeyemi\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"lost\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Silver Strikers\",\r\n      \"goals\":[\r\n        {\"time\":\"14\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"J. Dambuleni\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"63\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"B. Katinji\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"65\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"C. Batson\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"69\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"P. Chilopi\":{\r\n    \"Sunday, 29 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"0-3\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Bangwe All Stars\",\r\n      \"goals\":[\r\n        {\"time\":\"32\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"P. Macheso\":{\r\n    \"Sunday, 22 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"0-2\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Mighty Tigers\",\r\n      \"goals\":[\r\n        {\"time\":\"71\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Deus Mkutu\":{\r\n    \"Saturday, 21 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Extreme\",\r\n      \"goals\":[\r\n        {\"time\":\"18\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"M. Kaziputa\":{\r\n    \"Saturday, 21 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Extreme\",\r\n      \"goals\":[\r\n        {\"time\":\"47\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"B. Jimu\":{\r\n    \"Saturday, 21 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"lost\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Red Lions\",\r\n      \"goals\":[\r\n        {\"time\":\"91\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Collins Okumu\":{\r\n    \"Saturday, 21 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Chitipa United\",\r\n      \"goals\":[\r\n        {\"time\":\"9\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Emmanuel Saviel\":{\r\n    \"Wednesday, 18 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Bangwe All Stars\",\r\n      \"goals\":[\r\n        {\"time\":\"27\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Emmanuel Kaunga\":{\r\n    \"Sunday, 22 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"0-2\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Mighty Tigers\",\r\n      \"goals\":[\r\n        {\"time\":\"83\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"P. Chipingu\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-0\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"karonga United\",\r\n      \"goals\":[\r\n        {\"time\":\"29\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"C. Kumwembe\":{\r\n    \"Sunday, 29 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"-3\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Bangwe All Stars\",\r\n      \"goals\":[\r\n        {\"time\":\"67\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"W. Mpinganjira\":{\r\n    \"Sunday, 29 October 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"-3\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Bangwe All Stars\",\r\n      \"goals\":[\r\n        {\"time\":\"91\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"G. Soko\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-4\",\r\n      \"result\":\"lost\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Bangwe All Stars\",\r\n      \"goals\":[\r\n        {\"time\":\"16\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"G. Chaomba\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Ekwendeni Hammers\",\r\n      \"goals\":[\r\n        {\"time\":\"89\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"S. Davie\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Ekwendeni Hammers\",\r\n      \"goals\":[\r\n        {\"time\":\"73\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"D. Nyoni\":{\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"win\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Ekwendeni Hammers\",\r\n      \"goals\":[\r\n        {\"time\":\"60\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Ellie Kayombo\":{\r\n    \"Wednesday, 27 September 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"85\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Youngson Mwisho\":{\r\n    \"Wednesday, 27 September 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\" : \"away\",\r\n      \"team\" : \"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"87\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"C. Chipala\":{\r\n    \"Wednesday, 27 September 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"karonga United\",\r\n      \"goals\":[\r\n        {\"time\":\"70\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"C. Nyondo\":{\r\n    \"Sunday, 16 April 2023 CAT (UTC+2)\" :{\r\n      \"finalScore\":\"1-1\",\r\n      \"result\":\"draw\",\r\n      \"venue\" : \"home\",\r\n      \"team\" : \"Bangwe All Stars\",\r\n      \"goals\":[\r\n        {\"time\":\"84\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Sunday, 23 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"won\",\r\n      \"venue\": \"home\",\r\n      \"team\":\"Kamuzu Barracks\",\r\n      \"goals\":[\r\n        {\"time\": \"32\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Saturday, 29 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"lost\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Chitipa United\",\r\n      \"goals\":[\r\n        {\"time\" :\"48\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Saturday, 13 May 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Blue Eagles\",\r\n      \"goals\":[\r\n        {\"time\" :\"25\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Sunday, 28 May 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-1\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"Might Tigers\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"28\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Sunday, 04 June 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"team\":\"Civil Service United\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"60\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Sunday, 02 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"team\":\"MAFCO\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"8\",\"half\":\"1st\"},\r\n        {\"time\" :\"57\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Sunday, 09 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"lost\",\r\n      \"team\":\"karonga United\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"16\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Sunday, 15 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"FCB Nyasa Big Bullets\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"10\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Sunday, 30 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-1\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"Ekwendeni Hammers\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"32\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Sunday, 13 August 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-0\",\r\n      \"result\":\"win\",\r\n      \"team\":\"Chitipa United\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"40\",\"half\":\"1st\",\"penarty\":true}\r\n      ]\r\n    },\r\n    \"Sunday, 27 August 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-0\",\r\n      \"result\":\"win\",\r\n  \"team\":\"Red Lions\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"42\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Wednesday, 27 September 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"karonga United\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"15\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Limbani Phiri\":{\r\n    \"Sunday, 15 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"FCB Nyasa Big Bullets\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"62\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"R. Phiri\":{\r\n    \"Tuesday, 17 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-3\",\r\n      \"result\":\"lost\",\r\n      \"team\":\"FCB Nyasa Big Bullets\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"85\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"M Mgwira\":{\r\n    \"Sunday, 15 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"53\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"H Kajoke\":{\r\n    \"Sunday, 15 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"68\",\"half\":\"2nd\",\"penarty\":true}\r\n      ]\r\n    }\r\n  },\r\n  \"F. Demakude \":{\r\n    \"Sunday, 30 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-1\",\r\n      \"result\":\"draw\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"88\",\"half\":\"2nd\",\"penarty\":true}\r\n      ]\r\n    }\r\n  },\r\n  \"Saulos Moyo\":{\r\n    \"Sunday, 09 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"18\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"J Duwa\":{\r\n    \"Sunday, 09 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"36\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"M Masoatheka\":{\r\n    \"Sunday, 02 July 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"88\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"E Dakalira\":{\r\n    \"Sunday, 04 June 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"win\",\r\n      \"team\":\"Civil Service United\",\r\n      \"venue\":\"home\",\r\n      \"goals\":[\r\n        {\"time\" :\"46\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"M Biason\":{\r\n    \"Sunday, 04 June 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-1\",\r\n      \"result\":\"lost\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"venue\":\"away\",\r\n      \"goals\":[\r\n        {\"time\" :\"10\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"T Kajani\":{\r\n    \"Sunday, 28 May 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-1\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\" :\"47\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Lameck Gamphani\":{\r\n    \"Saturday, 13 May 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Blue Eagles\",\r\n      \"goals\":[\r\n        {\"time\":\"61\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"C. Gototo\":{\r\n    \"Saturday, 13 May 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"8\",\"half\":\"1st\"}\r\n      ]      \r\n    }\r\n  },\r\n  \"M. Mhone\":{\r\n    \"Saturday, 13 May 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"61\",\"half\":\"2nd\"}\r\n      ]      \r\n    },\r\n    \"Saturday, 28 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"0-3\",\r\n      \"result\":\"win\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Extreme\",\r\n      \"goals\":[\r\n        {\"time\":\"53\",\"half\":\"2nd\"}\r\n      ]      \r\n    }    \r\n  },\r\n  \"C. Mpinganjira\":{\r\n    \"Sunday, 23 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Kamuzu Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"55\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"T. Viyuyi\":{\r\n    \"Saturday, 28 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"0-3\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Extreme\",\r\n      \"goals\":[\r\n        {\"time\":\"54\",\"half\":\"2nd\"},\r\n        {\"time\":\"80\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Ephraim Kondowe\":{\r\n    \"Wednesday, 25 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Kamuzu Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"59\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n      \"Tuesday, 17 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-3\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Moyale Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"8\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"M Gasten\":{\r\n    \"Wednesday, 25 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Kamuzu Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"62\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"F Mandinga\":{\r\n    \"Wednesday, 25 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"0-1\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"45\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Olson Kanjira\":{\r\n    \"Wednesday, 25 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"lost\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"FCB Nyasa Big Bullets\",\r\n      \"goals\":[\r\n        {\"time\":\"11\",\"half\":\"1st\"},\r\n        {\"time\":\"65\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"L. Nkhoma\":{\r\n    \"Wednesday, 25 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Kamuzu Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"68\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Saturday, 21 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-0\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Chitipa United\",\r\n      \"goals\":[\r\n        {\"time\":\"21\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Tuesday, 17 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-3\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Moyale Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"21\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Ibrahim Sadick\":{\r\n    \"Sunday, 23 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-2\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Kamuzu Barracks\",\r\n      \"goals\":[\r\n        {\"time\":\"71\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Sunday, 27 August 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"2-0\",\r\n      \"result\":\"win\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Red Lions\",\r\n      \"goals\":[\r\n        {\"time\":\"50\",\"half\":\"2nd\",\"penarty\":true}\r\n      ]\r\n    }\r\n  },\r\n  \"Ramadan Ntafu\":{\r\n    \"Saturday, 29 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Dedza Dynamos Salima\",\r\n      \"goals\":[\r\n        {\"time\":\"13\",\"half\":\"1st\"},\r\n        {\"time\":\"27\",\"half\":\"1st\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Ken Mlenga\":{\r\n    \"Saturday, 29 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-1\",\r\n      \"result\":\"won\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Dedza Dynamos Salima\",\r\n      \"goals\":[\r\n        {\"time\":\"76\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  },\r\n  \"Chikumbutso Salima\":{\r\n    \"Sunday, 16 April 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-1\",\r\n      \"result\":\"draw\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Dedza Dynamos Salima\",\r\n      \"goals\":[\r\n        {\"time\":\"65\",\"half\":\"2nd\"}\r\n      ]\r\n    },\r\n    \"Saturday, 04 November 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"1-4\",\r\n      \"result\":\"win\",\r\n      \"venue\":\"away\",\r\n      \"team\":\"Mighty Tigers\",\r\n      \"goals\":[\r\n        {\"time\":\"1\",\"half\":\"1st\"}\r\n      ]\r\n    },\r\n    \"Wednesday, 18 October 2023 CAT (UTC+2)\":{\r\n      \"finalScore\":\"3-0\",\r\n      \"result\":\"win\",\r\n      \"venue\":\"home\",\r\n      \"team\":\"Dedza Dynamos Salima Sugar\",\r\n      \"goals\":[\r\n        {\"time\":\"71\",\"half\":\"2nd\"}\r\n      ]\r\n    }\r\n  }\r\n}")  # replace with your input data
output_data = convert_data(input_data)
print(json.dumps(output_data, indent=4))