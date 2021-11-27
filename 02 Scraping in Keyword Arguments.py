#-------------------------------------------------------
#                    Keyword Arguments
#-------------------------------------------------------
import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.content, "html.parser")

#-----------Scrap Green and Red text-------------------
result_by_class = bs.find_all('span', {'class':{'green', 'red'}})
print([text for text in result_by_class])


# -----------Scrap only Red text-----------------------
result_by_class = bs.find_all('span', {'class':{'red'}})
print([text for text in result_by_class])
'''[<span class="red">Well, Prince, so Genoa and Lucca are now just family estates of the
Buonapartes. But I warn you, if you don't tell me that this means war,
if you still try to defend the infamies and horrors perpetrated by
that Antichrist- I really believe he is Antichrist- I will have
nothing more to do with you and you are no longer my friend, no longer
my 'faithful slave,' as you call yourself! But how do you do? I see
I have frightened you- sit down and tell me all the news.</span>, <span class="red">If you have nothing better to do, Count [or Prince], and if the
prospect of spending an evening with a poor invalid is not too
terrible, I shall be very charmed to see you tonight between 7 and 10-
Annette Scherer.</span>, <span class="red">Heavens! what a virulent attack!</span>, <span class="red">First of all, dear friend, tell me how you are. Set your friend's
mind at rest,</span>, <span class="red">Can one be well while suffering morally? Can one be calm in times
like these if one has any feeling?</span>, <span class="red">You are
staying the whole evening, I hope?</span>, <span class="red">And the fete at the English ambassador's? Today is Wednesday. I
must put in an appearance there,</span>, <span class="red">My daughter is
coming for me to take me there.</span>, <span class="red">I thought today's fete had been canceled. I confess all these
festivities and fireworks are becoming wearisome.</span>, <span class="red">If they had known that you wished it, the entertainment would
have been put off,</span>, <span class="red">Don't tease! Well, and what has been decided about Novosiltsev's
dispatch? You know everything.</span>, <span class="red">What can one say about it?</span>, <span class="red">What has been decided? They have decided that
Buonaparte has burnt his boats, and I believe that we are ready to
burn ours.</span>, <span class="red">Oh, don't speak to me of Austria. Perhaps I don't understand
things, but Austria never has wished, and does not wish, for war.
She is betraying us! Russia alone must save Europe. Our gracious
sovereign recognizes his high vocation and will be true to it. That is
the one thing I have faith in! Our good and wonderful sovereign has to
perform the noblest role on earth, and he is so virtuous and noble
that God will not forsake him. He will fulfill his vocation and
crush the hydra of revolution, which has become more terrible than
ever in the person of this murderer and villain! We alone must
avenge the blood of the just one.... Whom, I ask you, can we rely
on?... England with her commercial spirit will not and cannot
understand the Emperor Alexander's loftiness of soul. She has
refused to evacuate Malta. She wanted to find, and still seeks, some
secret motive in our actions. What answer did Novosiltsev get? None.
The English have not understood and cannot understand the
self-abnegation of our Emperor who wants nothing for himself, but only
desires the good of mankind. And what have they promised? Nothing! And
what little they have promised they will not perform! Prussia has
always declared that Buonaparte is invincible, and that all Europe
is powerless before him.... And I don't believe a word that Hardenburg
says, or Haugwitz either. This famous Prussian neutrality is just a
trap. I have faith only in God and the lofty destiny of our adored
monarch. He will save Europe!</span>, <span class="red">I think,</span>, <span class="red">that if you had been
sent instead of our dear <span class="green">Wintzingerode</span> you would have captured the
<span class="green">King of Prussia</span>'s consent by assault. You are so eloquent. Will you
give me a cup of tea?</span>, <span class="red">In a moment. A propos,</span>, <span class="red">I am
expecting two very interesting men tonight, <span class="green">le Vicomte de Mortemart</span>,
who is connected with the <span class="green">Montmorencys</span> through the <span class="green">Rohans</span>, one of
the best French families. He is one of the genuine emigres, the good
ones. And also the <span class="green">Abbe Morio</span>. Do you know that profound thinker? He
has been received by <span class="green">the Emperor</span>. Had you heard?</span>, <span class="red">I shall be delighted to meet them,</span>, <span class="red">But tell me,</span>, <span class="red">is it true that the Dowager Empress wants Baron Funke
to be appointed first secretary at Vienna? The baron by all accounts
is a poor creature.</span>, <span class="red">Baron Funke has been recommended to the Dowager Empress by her
sister,</span>, <span class="red">Now about your family. Do you know that since your daughter came
out everyone has been enraptured by her? They say she is amazingly
beautiful.</span>, <span class="red">I often think,</span>, <span class="red">I often think how unfairly sometimes the
joys of life are distributed. Why has fate given you two such splendid
children? I don't speak of <span class="green">Anatole</span>, your youngest. I don't like
him,</span>, <span class="red">Two such charming children. And really you appreciate
them less than anyone, and so you don't deserve to have them.</span>, <span class="red">I can't help it,</span>, <span class="red">Lavater would have said I
lack the bump of paternity.</span>, <span class="red">Don't joke; I mean to have a serious talk with you. Do you know I
am dissatisfied with your younger son? Between ourselves</span>, <span class="red">he was mentioned at Her
Majesty's and you were pitied....</span>, <span class="red">What would you have me do?</span>, <span class="red">You know I did all
a father could for their education, and they have both turned out
fools. Hippolyte is at least a quiet fool, but Anatole is an active
one. That is the only difference between them.</span>, <span class="red">And why are children born to such men as you? If you were not a
father there would be nothing I could reproach you with,</span>, <span class="red">I am your faithful slave and to you alone I can confess that my
children are the bane of my life. It is the cross I have to bear. That
is how I explain it to myself. It can't be helped!</span>]'''

#-----Scrap Red Text in shape of sentence-------------
print('------------------')
print([text.get_text() for text in result_by_class])
------------------
# ["Well, Prince, so Genoa and Lucca are now just family estates of the\nBuonapartes. But I warn you, if you don't tell me that this means war,\nif you still try to defend the infamies and horrors perpetrated by\nthat Antichrist- I really believe he is Antichrist- I will have\nnothing more to do with you and you are no longer my friend, no longer\nmy 'faithful slave,' as you call yourself! But how do you do? I see\nI have frightened you- sit down and tell me all the news.", 
# 'If you have nothing better to do, Count [or Prince], and if the\nprospect of spending an evening with a poor invalid is not too\nterrible, I shall be very charmed to see you tonight between 7 and 10-\nAnnette Scherer.', 
# 'Heavens! what a virulent attack!', 
# "First of all, dear friend, tell me how you are. Set your friend's\nmind at rest,", 'Can one be well while suffering morally? Can one be calm in times\nlike these if one has any feeling?', 'You are\nstaying the whole evening, I hope?', "And the fete at the English ambassador's? Today is Wednesday. I\nmust put in an appearance there,", 'My daughter is\ncoming for me to take me there.', "I thought today's fete had been canceled. I confess all these\nfestivities and fireworks are becoming wearisome.", 'If they had known that you wished it, the entertainment would\nhave been put off,', "Don't tease! Well, and what has been decided about Novosiltsev's\ndispatch? You know everything.", 'What can one say about it?', 'What has been decided? They have decided that\nBuonaparte has burnt his boats, and I believe that we are ready to\nburn ours.', "Oh, don't speak to me of Austria. Perhaps I don't understand\nthings, but Austria never has wished, and does not wish, for war.\nShe is betraying us! Russia alone must save Europe. Our gracious\nsovereign recognizes his high vocation and will be true to it. That is\nthe one thing I have faith in! Our good and wonderful sovereign has to\nperform the noblest role on earth, and he is so virtuous and noble\nthat God will not forsake him. He will fulfill his vocation and\ncrush the hydra of revolution, which has become more terrible than\never in the person of this murderer and villain! We alone must\navenge the blood of the just one.... Whom, I ask you, can we rely\non?... England with her commercial spirit will not and cannot\nunderstand the Emperor Alexander's loftiness of soul. She has\nrefused to evacuate Malta. She wanted to find, and still seeks, some\nsecret motive in our actions. What answer did Novosiltsev get? None.\nThe English have not understood and cannot understand the\nself-abnegation of our Emperor who wants nothing for himself, but only\ndesires the good of mankind. And what have they promised? Nothing! And\nwhat little they have promised they will not perform! Prussia has\nalways declared that Buonaparte is invincible, and that all Europe\nis powerless before him.... And I don't believe a word that Hardenburg\nsays, or Haugwitz either. This famous Prussian neutrality is just a\ntrap. I have faith only in God and the lofty destiny of our adored\nmonarch. He will save Europe!", 'I think,', "that if you had been\nsent instead of our dear Wintzingerode you would have captured the\nKing of Prussia's consent by assault. You are so eloquent. Will you\ngive me a cup of tea?", 'In a moment. A propos,', 'I am\nexpecting two very interesting men tonight, le Vicomte de Mortemart,\nwho is connected with the Montmorencys through the Rohans, one of\nthe best French families. He is one of the genuine emigres, the good\nones. And also the Abbe Morio. Do you know that profound thinker? He\nhas been received by the Emperor. Had you heard?', 'I shall be delighted to meet them,', 'But tell me,', 'is it true that the Dowager Empress wants Baron Funke\nto be appointed first secretary at Vienna? The baron by all accounts\nis a poor creature.', 'Baron Funke has been recommended to the Dowager Empress by her\nsister,', 'Now about your family. Do you know that since your daughter came\nout everyone has been enraptured by her? They say she is amazingly\nbeautiful.', 'I often think,', "I often think how unfairly sometimes the\njoys of life are distributed. Why has fate given you two such splendid\nchildren? I don't speak of Anatole, your youngest. I don't like\nhim,", "Two such charming children. And really you appreciate\nthem less than anyone, and so you don't deserve to have them.", "I can't help it,", 'Lavater would have said I\nlack the bump of paternity.', "Don't joke; I mean to have a serious talk with you. Do you know I\nam dissatisfied with your younger son? Between ourselves", "he was mentioned at Her\nMajesty's and you were pitied....", 'What would you have me do?', 'You know I did all\na father could for their education, and they have both turned out\nfools. Hippolyte is at least a quiet fool, but Anatole is an active\none. That is the only difference between them.', 'And why are children born to such men as you? If you were not a\nfather there would be nothing I could reproach you with,', "I am your faithful slave and to you alone I can confess that my\nchildren are the bane of my life. It is the cross I have to bear. That\nis how I explain it to myself. It can't be helped!"]

#------------------------------------------------------------------------------