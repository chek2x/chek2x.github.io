from Classification import NaiveBayes
from TextCleaner import TextCleaner
import sqlite3

# Connect to MySQL Database
conn = sqlite3.connect("./server/db_fakechekr.db")
cursor = conn.cursor()

# Initiate NaiveBayes local class
nb = NaiveBayes()
tc = TextCleaner()

# Test Case 1
information = {
    "link" : "https://www.theonion.com/elon-musk-fans-explain-why-they-love-cybertrucks-1850991183",
    "website" : "the onion",
    "headline" : "elon musk fans explain why they love cybertrucks.",
    "author" : "unknown",
    "body" : "aside from killing monkeys and destroying twitter elon musk has also had his sights set on something else building teslas futuristic cybertruck the onion asked musks fans why they want to spend tens of thousands of dollars on a blade runner ripoff and this is what they said",
    "pub_date" : "2023-11-07"
}

information['body'] = tc.clean_text(information['body'])
result = nb.classify(information)
print("Test Case 1:", result, "\nCleaned text:", information['body'])

# Inserts information to the articles table in db_fakechekr
# cursor.execute("INSERT INTO articles (link, website, headline, authors, body, pub_date, legit) VALUES (\""
#                + information['link'] + "\", \""
#                + information['website'] + "\", \""
#                + information['headline'] + "\", \""
#                + information['author'] + "\", \""
#                + information['body'] + "\", \""
#                + information['pub_date'] + "\", \""
#                + result + "\")")
# conn.commit()

# Test Case 2
information = {
    "link" : "https://edition.cnn.com/2023/11/07/politics/virginia-elections-glenn-youngkin/index.html",
    "website" : "cnn",
    "headline" : "in virginia youngkin looks to prove that nonmaga politics can be a winning republican strategy",
    "author" : "jake tapper arit john",
    "body" : "virginia gov glenn youngkin isnt on the ballot this year but his push for a new conservative direction for the republican party is tuesday nights results of virginias legislative elections will be viewed for better or for worse as a referendum on youngkins nonmaga brand of conservative politics and the state house of delegates and state senate candidates who subscribe to it hes made sure of it youngkin elected two years ago in a state that has swung blue in the last four presidential cycles is hoping to flip the state senate and hold control of the house of delegates and has endorsed in key primaries spent weeks campaigning with republicans across the commonwealth urged his partys voters to cast their ballots early and raised millions to help compete with democratic fundraising all 140 seats in the democratcontrolled senate and republicancontrolled house of delegates are up for election and candidates are running on new maps following a dramatic redistricting cycle youngkins investment of time on the trail messaging training and financial resources reflects the high stakes for both his party and his own political future virginia governors arent allowed to run for consecutive terms making this the only chance youngkin will have to govern with republicans majorities and enact a conservative agenda after two years of sharing power with democrats gop victories on tuesday would also boost his profile before he embarks on the next stage of his political career whether thats a late entry into the republican presidential primary or a run for the us senate in 2024 or 2026 privately the governor and his political team have been deeply involved in recruiting candidates he felt best reflected his particular brand of more traditional gop conservativism ones whom the youngkin team hope can win both trump supporters and the suburban voters former president donald trump lost in 2016 and 2020 the focus here was getting candidates that reflect their community and the commonwealth a knowledgeable gop source told cnn thats why gov youngkin leaned in during the nomination contests and went 10 for 10 in the ones that were contested when your goal is winning to further a commonsense conservative agenda you have to put the best team on the field about 20 battleground district candidates competing in both delegate and state senate races attended several bootcamp meetings and messaging sessions with a debate coach starting in the spring according to a second source his team also discouraged campaigns from denying the results of the 2020 presidential election make it clear they needed to look forward was how it was conveyed ive consistently said that joe biden was legitimately elected president youngkin told abcs george stephanopoulos on sunday candidates were encouraged to rally around youngkins proposed 15week abortion ban with exceptions for rape incest and life of the mother and not to support a wider ban the discipline extended beyond the 10 candidates youngkin endorsed in competitive primaries so as to keep distractions at bay at one point sources say one delegate candidate posted something rather incendiary on abortion within 25 minutes the post was taken down virginia democrats who would normally use such a post to put the entire gop in an awkward position did not apparently even notice youngkin is eager to argue that he was successfully able to chart a sane conservative path for legislative candidates in 2021 a state that was lost a state that was completely blue has systematically taken a right turn and demonstrated that common sense conservative policies work youngkin said during a getoutthevote campaign stop monday in fredericksburg we have got to finish the job its not clear youngkins strategy will work democrats are projecting that they only need to keep control of the senate tuesday which would allow them to continue blocking the governors policies anything short of control of both chambers would likely be a huge disappointment for youngkin said mark j rozell the dean of the schar school of policy and government at george mason university virginia has been trending democratic for years and the dobbs supreme court decision overturning roe v wade has many democrats running ads focused entirely on the issue of abortion rights which could very well work in some of these districts it was something of a gamble on his part to stake so much of his political capital on races that he doesnt have complete control over rozell said there are local candidates and personalities and issues that drive some of these competitive races that have little to do with the governors intervention or efforts youngkins strategy youngkins political apparatus took advantage of virginias loose campaign finance laws to work closely with campaigns to advise on message spending and campaign operations the source said on abortion youngkins team shared their messaging which has been to argue that a 15week limit with exceptions for rape incest and to protect the life of the mother is a consensus opinion his team also discouraged campaigns from denying the results of the 2020 presidential election were fighting some tough fights on messaging and as a party trying to navigate the waters on certain issues said taylor keeney a former press secretary for republican gov bob mcdonnell but youngkins positioned himself and positioned our party here in virginia in the right spot especially when youre looking at issues like abortion youngkins spirit of virginia pac has raised more than 1878 million since march according to the virginia public access project including 3 million from billionaire donor thomas peterffy who has urged youngkin to consider a lastminute entry into the 2024 presidential race the biggest contribution about 13 million has gone to state sen siobhan dunnavant an obgyn running for reelection in a competitive district outside richmond dunnavant has backed youngkins 15week limit rejecting democrats characterization of it as a ban a key part of the governors strategy was helping his preferred candidates win competitive primaries against more extreme or less experienced opponents he endorsed in 10 competitive house and senate primaries in which all of his preferred candidates won in senate district 27 a fredericksburgarea senate seat he endorsed state del tara durant over matt strickland a restaurant owner who clashed with state government over his refusal to comply with covid19 safety measures in senate district 17 youngkinbacked del emily brewer beat hermie sadler a former nascar driver who ran as a political outsider in september youngkin launched a bus tour to promote early voting hes also made nearly 100 campaign stops since mid summer many of these events have also sought to appeal to diverse groups within virginia he campaigned with durant at a hispanic heritage festival in fredericksburg and attended a diwali event at the heritage indian festival in chantilly with juan pablo segura who is running in senate district 31 a competitive seat in northern virginia the embracing of virginias diversity seems to underline a gop of yore not the maga of a president who once told four congresswomen of color to go back to where they came from the other candidates in the youngkin ten include senate candidates jason ballard john mcguire bryce reeves and bill woolf and delegate candidates buddy fowler john stirrup lee peters and mike dillender mcguire reeves and ballard were nominated through conventions not primaries a possible sign of youngkins strength with the partys conservative base again and again conservative leaders understand that power and the countrys future start in state legislatures said daniel squadron the founding partner of the states project a democratic group focused on state legislative races on our side that seems to be a lesson thats never learned the states project announced last month it would spend more than 45 million in virginia other democratic groups have jumped in as well alarmed by youngkins fundraising and the high stakes of the race the democratic national committee directed 12 million to the state at the urging of us sens tim kaine who is up for reelection next year and mark warner bringing their total to 15 million democrats in the state have warned that if youngkin succeeds in securing republican control of the legislature republicans could roll back progressive voting laws enacted by democrats in 2020 democrats lost full control in 2021 when youngkin was elected and republicans flipped the house of delegates at the time democrats tried to tie him to former president donald trump but the former private equity firm chief executive managed to come across as more personable and moderate while still appealing to the former presidents supporters two years later democrats are pointing to legislation he and republicans have backed on voting rights abortion and gun control to argue hes not as moderate as he seems still there isnt a lot of evidence that the virginia democratic party sees youngkin as any sort of liability for the gop he isnt featured negatively in any of their ads for example what we have found out over the last two years is that that vestwearing affable basketball playing dad is really a maga extremist said virginia democratic party chair susan swecker i am confident from going around the commonwealth campaigning for our candidates and out talking to voters that theres a lot of buyers remorse",
    "pub_date" : "0001-01-01"
}

information['body'] = tc.clean_text(information['body'])
result = nb.classify(information)
print("Test Case 2:", result, "\nCleaned text:", information['body'])

# Inserts information to the articles table in db_fakechekr
# cursor.execute("INSERT INTO articles (link, website, headline, authors, body, pub_date, legit) VALUES (\""
#                + information['link'] + "\", \""
#                + information['website'] + "\", \""
#                + information['headline'] + "\", \""
#                + information['author'] + "\", \""
#                + information['body'] + "\", \""
#                + information['pub_date'] + "\", \""
#                + result + "\")")
# conn.commit()

cursor.close()