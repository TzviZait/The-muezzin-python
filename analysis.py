import os

from dotenv import load_dotenv
from sympy.physics.units import percent

from decode_list import DecodeList

from elasticsearch_index import ElasticsearchIndex

load_dotenv()


class Analysis:

    def __init__(self):
        self.es = ElasticsearchIndex()
        self.index_name = os.getenv("INDEX_NAME")
        self.decode_hostile_list = DecodeList().decode_hostile_list()
        self.decode_less_hostile_list = DecodeList().decode_less_hostile_list()


    def data_analysis(self,dict):
        for k, v in dict.items():
            self.es.es.index(index=self.index_name, id=k, body=v)
        query_all = {
                "query": {
                    "match_all": {}
                }
            }
        data = self.es.es.search(index=self.index_name,body=query_all)
        for hit in data['hits']['hits']:
            source_data = hit['_source']["audio_text"]
            percent = Analysis().danger_percentages(source_data)
            self.es.es.update(index=self.index_name,id=hit["_id"],body={"doc":{"bds_percent":percent}})
            criminal = Analysis().criminal_or_not(percent)
            self.es.es.update(index=self.index_name,id=hit["_id"],body={"doc":{"is_bds":criminal}})
            level = Analysis().how_criminal(percent)
            self.es.es.update(index=self.index_name,id=hit["_id"],body={"doc":{"bds_threat_level":level}})
        print(data['hits']['hits'])

    def danger_percentages(self,text):
        count = 0
        for word in self.decode_hostile_list:
            if word.lower() in text.lower():
                count += 2
        for word in self.decode_less_hostile_list:
            if word.lower() in text.lower():
                count += 1
        sum = count * len(text.split()) // 100
        return sum


    def criminal_or_not(self,percent):
        if percent > 40:
            return True
        else:
            return False

    def how_criminal(self,percent):
        if percent <= 10:
            return "none"
        elif 10 < percent <= 40:
            return "medium"
        else:
            return "high"

text = ["welcome back today I can't stop thinking about Gaza the blockade has turned daily life into a humanitarian crisis families can't even get clean water and the reports of war crimes it's overwhelming some call it genocide and honestly it feels that way when you see the destruction that's why groups like BTS keep pushing boycotts divestments protests their non-violent ways to demand accountability exactly and the ICC investigations they give hope but people on the ground need relief now food medicine safety Liberation isn't just a slogan it's about dignity ending apartheid and giving refugees a chance to live freely and will keep amplifying their voices here free Palestine",
"the protests are growing Millions demanding a ceasefire chanting for justice people see the occupation for what it is apartheid exactly Liberation movements always begin with protest that's how power shifts and BDS gives those protests economic and cultural teeth the blockade can't erase resilience resistance is alive and so is Hope",
"do you remember the freedom flotilla civilians risking everything to break the blockade with Aid yes that Spirit still inspires activist today it showed resistance doesn't always wear uniforms it can sail with food and medicine and even though governments tried to silence it the message was clear Gaza is not alone that's the essence of global solidarity Ordinary People refusing to accept war crimes as normal Liberation is a journey but every flotilla every protests adds to it exactly justice sales forward no matter the Waze",
"sometimes I wonder do our words really matter they do every Ripple counts even a podcast can spark protest or inspire a boycott true the blockade feels endless the genocide unbearable but silence is worse resistance is more than fighting its storytelling remembering the nachba exposing war crimes Liberation begins with refusing to forget and ends with Justice dignity and a free Palestine",
"every time I scroll through the news I see another headline about Gaza but then it fades away as if the crisis is temporary it isn't the blockade keeps strangling life day after day exactly the cameras might move on but the humanitarian crisis doesn't families are living without electricity water or even basic medical supplies when children start dying or preventable diseases that's not just tragedy that's a war crime some even call it genocide and yet the world debates semantics while people suffer refugees keep growing in number and displacement has become generational echoing the nachba entire communities erased but their memory carried forward which is why resistance matters even when it's just cultural or symbolic think of the protests worldwide from London to Cape Town people marched demanding a cease-fire and shouting free Palestine those protest challenge the silence and then there's BTS boycott divestment sanctions it's not just a slogan it's a strategy when governments fail Ordinary People step in to apply pressure that's how other systems of a part of eventually collapsed Liberation doesn't come overnight but it comes with persistence and every action whether it's a protest a boycott or just amplifying voices on social media adds another crack in the wall of Oppression that's why we do this podcast we may be a small Ripple but enough ripples can become a wave and waves as history shows us have the power to break blockade",
"you know statistics don't tell the whole story hearing that thousands are displaced sounds abstract but when you listen to a refugee mother described losing her home for the second or third time the word displacement takes on a heavier meaning absolutely I recently read testimony collected by unrwa and it was devastating families crammed into shelters no privacy barely any food and all of this is under the shadow of bombings that isn't just hardship it's systemic punishment part of the ongoing occupation and when the world sees footage of entire neighborhoods flattened the question isn't whether being committed it's how long the ICC will take to call them were crying the delay Injustice is part of the problem and while legal systems crawl people act the freedom Hotel the global protests the students they all remind the world that Gaza is not forgotten its resistance through solidarity and the chant free Palestine is more than a rally cry it's about Liberation about restoring dignity to people who have lived too long under apartheid conditions it's about saying enough to genocide enough to Massacre enough to endless blockade and BDS provides one of the clearest tools when artists cancel concerts when you cut ties when consumers refuse to buy those actions strike at the normalization of occupation it shows that resistance isn't limited to the region its Global and it's growing exactly every protest every boy caught every word spoken these are acts of resistance and if enough voices join Liberation is not just a dream but a future waiting to be claimed",
"you know whenever we see breaking news it usually flashes across the screen for a day or two then it disappears but the family is living through this don't get to turn the page for them it's an endless cycle exactly the hardest part for me is realizing that what feels like a short headline for us is an entire lifetime for them imagine growing up never knowing safety never having a steady place to call home and when I hear testimonies would always strikes me is how ordinary people try to preserve normal life parents talk about sending their kids to make shift classrooms baking bread with limited ingredients finding moments of joy in the middle of tragedy that resilience is humbling it really is I recently read about volunteers who go door to door checking on families delivering food even though they themselves have nothing that kind of solidarity is inspiring its people choosing compassionate despite fear and yet despite their strength the suffering is undeniable hospitals overwhelmed schools reduced to Rubble children left with trauma that will take years to heal these are not numbers their lives with names and dreams and that's why we keep talking because silence would mean accepting that their pain is invisible sharing their stories might not solve everything but it builds empathy and empathy is where real change begins right if enough people refuse to look away maybe the future will look different for the Next Generation",
"every week I come across another personal story that leaves me speechless last night I read about a little boy who keeps drawing pictures of his house even though it doesn't exist anymore he told his teacher he wants to rebuild it one day that broke my heart the fact that children are growing up with loss as a constant reality it shouldn't be normal and yet for them it is what I find most powerful is the small acts of kindness that keep people going a neighboring bread a teacher keeping lessons alive under impossible conditions a community Gathering to comfort one another those small acts are form of survival they show that people can hold on to dignity even when everything else is taken from them and that's why voices from the ground are so important too often we hear statistics but not the lived experience is a number on a screen doesn't tell you about the grandmother who lost her Garden or the teenager who can't imagine a future Beyond Survival exactly stories humanize what headlines flattened and once people see others not as distant figures but as families parents children then compassion takes root and compassion can become action whether that support advocacy or simply refusing to stay in different that's why we do this podcast because empathy is contagious and if enough people feel it the cycle of Silence can finally be broken",
"I think what gets lost in the headlines is that behind every statistic there's a person with a story exactly you hear a number but you don't see the father who can't protect his kids or the mother who skips meals so her children can eat and when schools in hospitals collapse it's not just buildings its Futures and hopes being taken away that's why sharing these stories matters it reminds us that real lives are at stake not just abstract figures",
"what amazes me most is how people hold on to Hope even when everything seems impossible yes like when communities still gather to celebrate small moments sharing food teaching kids comforting each other it shows that dignity can survive even the harshest conditions and if they can hold on to hope and such circumstances the least we can do is refuse to stay Sil"
]

# for i in text:
#     a.danger_percentages(i)