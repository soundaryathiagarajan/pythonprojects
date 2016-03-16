__author__ = 'soundarya'

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


kafka =  KafkaClient("localhost:9092")

producer = SimpleProducer(kafka)

#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        producer.send_messages("tweetsa", data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['Hillary Clinton', '@hillaryclinton', '@ClintonNews', '@HRClinton', '@voteHillary2016', '@AllThingsHill', '@hillaryRussia', '@danmericaCNN', '@KThomasDC', '@anniekarni', '@AndrewStilesUSA', '@Madam_President', '@hillarynews1', '@FaithVotersPAC', '@HillDawgClinton', '@ABCLiz', '@NICKWALSH', '#Hillary2016', '@HillaryIn2016', 'Bernie Sanders', '@SenSanders', '@BernieSanders', '@ajbends', '@Bobby_Budds', '@Sanders4Potus', '@VoteBernie2016', 'Jeb Bush', '@JebBush', '@TeamJebBush', '@EliStokols', '@TomBeaumont', '@JBushNews', '@JBushNews', '@jebbushnews', '@VoteJeb', '@Bush', '@r2rusa', '@JebBushforPres', '@JebHillary2016', 'Donald Trump', '@realDonaldTrump', '@Writeintrump', '@Vote_For_Trump', '@NoahGrayCNN', '@DanScavino', 'John Kasich', '@JohnKasich', '@JohnKasichNews', '@TeamJohnKasich', '@GovernorKasich', 'Marco Rubio', '@marcorubio', '@TeamMarco', '@PoliticsTBTimes', '@MarcoRubioNews', 'Scott Walker', '@ScottWalker', '@GovWalker', '@wpjenna', '@ScottWalkerHQ'])

