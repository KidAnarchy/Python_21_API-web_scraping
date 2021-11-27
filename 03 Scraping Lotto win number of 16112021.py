#--------------------------------------------------------------------------------------
#                   Scraping Lotto win number of Date: 16/11/2021
#--------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

html = requests.get("https://news.sanook.com/lotto/check/16112564/")

bs = BeautifulSoup(html.content, "html.parser")

#----------Pull data from Span and Strong by Class--------
result_by_class = bs.find_all(['span', 'strong'], {'class': 'lotto__number'})

print(result_by_class)
print('Number of results: ', len(result_by_class))

# [<strong class="lotto__number lotto__number--first">032761</strong>, 
# <strong class="lotto__number">648</strong>, 
# <strong class="lotto__number">471</strong>, <strong class="lotto__number">844</strong>, <strong class="lotto__number">245</strong>, 
# <strong class="lotto__number">57</strong>, 
# <strong class="lotto__number">032760</strong>, 
# <strong class="lotto__number">032762</strong>, 
# <span class="lotto__number">088445</span>, <span class="lotto__number">186581</span>,
# <span class="lotto__number">463393</span>, <span class="lotto__number">795889</span>, <span class="lotto__number">947522</span>, 
# <span class="lotto__number">064734</span>, <span class="lotto__number">141088</span>, <span class="lotto__number">157550</span>, 
# <span class="lotto__number">190830</span>, <span class="lotto__number">255181</span>, <span class="lotto__number">287391</span>, 
# <span class="lotto__number">402692</span>, <span class="lotto__number">646494</span>, <span class="lotto__number">776372</span>, 
# <span class="lotto__number">970336</span>, <span class="lotto__number">010032</span>, <span class="lotto__number">071506</span>, 
# <span class="lotto__number">170411</span>, <span class="lotto__number">253744</span>, <span class="lotto__number">392119</span>, 
# <span class="lotto__number">499342</span>, <span class="lotto__number">610529</span>, <span class="lotto__number">682581</span>, 
# <span class="lotto__number">863748</span>, <span class="lotto__number">920951</span>, <span class="lotto__number">013299</span>, 
# <span class="lotto__number">093175</span>, <span class="lotto__number">172590</span>, <span class="lotto__number">273095</span>, 
# <span class="lotto__number">406661</span>, <span class="lotto__number">503818</span>, <span class="lotto__number">626024</span>, 
# <span class="lotto__number">699247</span>, <span class="lotto__number">878484</span>, <span class="lotto__number">941838</span>, 
# <span class="lotto__number">019427</span>, <span class="lotto__number">097054</span>, <span class="lotto__number">172736</span>, 
# <span class="lotto__number">313936</span>, <span class="lotto__number">426635</span>, <span class="lotto__number">516537</span>, 
# <span class="lotto__number">629357</span>, <span class="lotto__number">712334</span>, <span class="lotto__number">888714</span>, 
# <span class="lotto__number">968045</span>, <span class="lotto__number">042178</span>, <span class="lotto__number">146084</span>, 
# <span class="lotto__number">234661</span>, <span class="lotto__number">355311</span>, <span class="lotto__number">430076</span>, 
# <span class="lotto__number">543000</span>, <span class="lotto__number">641050</span>, <span class="lotto__number">725398</span>, 
# <span class="lotto__number">890452</span>, <span class="lotto__number">971223</span>, <span class="lotto__number">071274</span>, 
# <span class="lotto__number">161103</span>, <span class="lotto__number">238338</span>, <span class="lotto__number">367089</span>, 
# <span class="lotto__number">485132</span>, <span class="lotto__number">565596</span>, <span class="lotto__number">680387</span>, 
# <span class="lotto__number">793861</span>, <span class="lotto__number">896546</span>, <span class="lotto__number">994111</span>, 
# <span class="lotto__number">031949</span>, <span class="lotto__number">100108</span>, <span class="lotto__number">154263</span>, 
# <span class="lotto__number">214805</span>, <span class="lotto__number">336167</span>, <span class="lotto__number">388487</span>, 
# <span class="lotto__number">484965</span>, <span class="lotto__number">588386</span>, <span class="lotto__number">762490</span>, 
# <span class="lotto__number">876348</span>, <span class="lotto__number">040674</span>, <span class="lotto__number">105054</span>, 
# <span class="lotto__number">165331</span>, <span class="lotto__number">223850</span>, <span class="lotto__number">343594</span>, 
# <span class="lotto__number">390960</span>, <span class="lotto__number">498432</span>, <span class="lotto__number">615997</span>, 
# <span class="lotto__number">765989</span>, <span class="lotto__number">882075</span>, <span class="lotto__number">044387</span>, 
# <span class="lotto__number">109430</span>, <span class="lotto__number">165666</span>, <span class="lotto__number">227820</span>, 
# <span class="lotto__number">347580</span>, <span class="lotto__number">392541</span>, <span class="lotto__number">502877</span>, 
# <span class="lotto__number">621169</span>, <span class="lotto__number">770009</span>, <span class="lotto__number">885595</span>, 
# <span class="lotto__number">051572</span>, <span class="lotto__number">121768</span>, <span class="lotto__number">173400</span>, 
# <span class="lotto__number">228139</span>, <span class="lotto__number">351153</span>, <span class="lotto__number">400586</span>, 
# <span class="lotto__number">511923</span>, <span class="lotto__number">649421</span>, <span class="lotto__number">778323</span>, 
# <span class="lotto__number">896434</span>, <span class="lotto__number">052793</span>, <span class="lotto__number">127608</span>, 
# <span class="lotto__number">181158</span>, <span class="lotto__number">243249</span>, <span class="lotto__number">352624</span>, 
# <span class="lotto__number">424704</span>, <span class="lotto__number">527767</span>, <span class="lotto__number">656071</span>, 
# <span class="lotto__number">809294</span>, <span class="lotto__number">896687</span>, <span class="lotto__number">055201</span>, 
# <span class="lotto__number">127874</span>, <span class="lotto__number">184279</span>, <span class="lotto__number">245397</span>, 
# <span class="lotto__number">355822</span>, <span class="lotto__number">451330</span>, <span class="lotto__number">527811</span>, 
# <span class="lotto__number">679441</span>, <span class="lotto__number">823295</span>, <span class="lotto__number">900357</span>, 
# <span class="lotto__number">070806</span>, <span class="lotto__number">133714</span>, <span class="lotto__number">189709</span>, 
# <span class="lotto__number">247908</span>, <span class="lotto__number">369331</span>, <span class="lotto__number">460599</span>, 
# <span class="lotto__number">529127</span>, <span class="lotto__number">681129</span>, <span class="lotto__number">860793</span>, 
# <span class="lotto__number">916776</span>, <span class="lotto__number">074476</span>, <span class="lotto__number">136111</span>, 
# <span class="lotto__number">200319</span>, <span class="lotto__number">285782</span>, <span class="lotto__number">373301</span>, 
# <span class="lotto__number">465361</span>, <span class="lotto__number">539522</span>, <span class="lotto__number">735177</span>, 
# <span class="lotto__number">868193</span>, <span class="lotto__number">945363</span>, <span class="lotto__number">082133</span>, 
# <span class="lotto__number">143098</span>, <span class="lotto__number">208819</span>, <span class="lotto__number">293804</span>, 
# <span class="lotto__number">379437</span>, <span class="lotto__number">469031</span>, <span class="lotto__number">550921</span>, 
# <span class="lotto__number">744318</span>, <span class="lotto__number">869762</span>, <span class="lotto__number">952606</span>, 
# <span class="lotto__number">087472</span>, <span class="lotto__number">151754</span>, <span class="lotto__number">211208</span>, 
# <span class="lotto__number">322558</span>, <span class="lotto__number">381307</span>, <span class="lotto__number">477105</span>, 
# <span class="lotto__number">562066</span>, <span class="lotto__number">759971</span>, <span class="lotto__number">872577</span>, 
# <span class="lotto__number">988109</span>]
# Number of results:  173

#-----------Scrap only Lotto number-------------------
print([text.get_text() for text in result_by_class])
'''['032761', '648', '471', '844', '245', '57', '032760', '032762', '088445', '186581', '463393', '795889', '947522', '064734', 
'141088', '157550', '190830', '255181', '287391', '402692', '646494', '776372', '970336', '010032', '071506', '170411', '253744', 
'392119', '499342', '610529', '682581', '863748', '920951', '013299', '093175', '172590', '273095', '406661', '503818', '626024', 
'699247', '878484', '941838', '019427', '097054', '172736', '313936', '426635', '516537', '629357', '712334', '888714', '968045', 
'042178', '146084', '234661', '355311', '430076', '543000', '641050', '725398', '890452', '971223', '071274', '161103', '238338', 
'367089', '485132', '565596', '680387', '793861', '896546', '994111', '031949', '100108', '154263', '214805', '336167', '388487', 
'484965', '588386', '762490', '876348', '040674', '105054', '165331', '223850', '343594', '390960', '498432', '615997', '765989', 
'882075', '044387', '109430', '165666', '227820', '347580', '392541', '502877', '621169', '770009', '885595', '051572', '121768', 
'173400', '228139', '351153', '400586', '511923', '649421', '778323', '896434', '052793', '127608', '181158', '243249', '352624', 
'424704', '527767', '656071', '809294', '896687', '055201', '127874', '184279', '245397', '355822', '451330', '527811', '679441', 
'823295', '900357', '070806', '133714', '189709', '247908', '369331', '460599', '529127', '681129', '860793', '916776', '074476', 
'136111', '200319', '285782', '373301', '465361', '539522', '735177', '868193', '945363', '082133', '143098', '208819', '293804', 
'379437', '469031', '550921', '744318', '869762', '952606', '087472', '151754', '211208', '322558', '381307', '477105', '562066', 
'759971', '872577', '988109']'''

# -----------------------------------------------------