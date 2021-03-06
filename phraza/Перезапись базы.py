import json

# ЭТОТ ФАЙЛ ЗАПУСКАТЬ ЛИШЬ В ТОМ СЛУЧАЕ, ЕСЛИ ХОТИТЕ СДЕЛАТЬ ПЕРЕЗАПИСЬ ВСЕХ РАНЕЕ ЗАГОТОВЛЕННЫХ ФРАЗЕОЛОГИЗМОВ
# ТЕ ФРАЗЕОЛОГИЗМЫ КОТОРЫЕ ВЫ ЛИЧНО СОЗДАЛИ БУДУТ УДАЛЕНЫ,ФРАЗЕОЛГИЗМЫ КОТОРЫЕ РЕДАКТИРОВАЛИ БУДУТ ВОССТАНОВЛЕНЫ, ФРАЗ. КОТОРЫЕ ВЫ УДАЛЯЛИ БУДУТ ТОЖЕ ВОССТАНОВЛЕНЫ
# ТО ЕСТЬ БАЗА БУДЕТ СОСТОЯТЬ ИЗ ТЕХ ФРАЗ. ЧТО ВЫ ВИДИТЕ НИЖЕ

phrases = {'Абілхаят суы': ['қасиетті су, асыл су, игілікті су, мәңгі өмір дарытатын қасиетті су', 'Абілхаят суы сол жерде өсіп тұрған шыршалар мен қарағайларға шашырады. Олар мәңгілік жап-жасыл болып қалды.', '', ''],
           'Абырой болғанда': ['бақытқа орай,  сәтке орай', 'Абырой болғанда, ешкім зардап шекпейді', '', ''],
           'Абыройы айрандай төгілу': ['масқаралану, абыройсыздану, ұятқа қалу, масқара болу', 'Бір күні абыройым айрандай төгілді.', '', ''],
           'Ағама жеңгем сай': ['мінсіз серіктестер, бір-біріне сәйкес келеді', 'Ағама жеңгем сай , апама жездем сай – мінез – қылығы үйлес', '', ''],
           'Ағаш атқа мінгізу': ['ғайбат айту, өсек айту, өсектеп жамандау', 'Оның жаман әдеті бар - ағаш атқа мінгізу', '', ''],
           'Ағаштан түйін түю': ['нағыз шебер, өз саласының маманы, зергер, өнерлі', 'Оның үстіне өзі ағаштан түйін түйген шебер.', '', ''],
           'Ағыл-тегіл жылау': ['еңіреп жылау, боздау, өкіру, өксіп жылау', 'Басты бет News Назарбаевты қимаған әнші ағыл-тегіл жылап қалды.', '', ''],
           'Ағынан жарылу': ['өтірік айтпау, ішкі сырын бүкпесіз білдіру, өз ойын жасырмай ақтарып салу', 'Aғынан жарылу — адам мінезіндегі ұнамды қасиет.', '', ''],
           'Ағып тұр (тұрған)': ['шешен, тілге бай, сөзге жүйрік,  сөзуар, сөзшең', 'Ол сөзге ағып тұрған шебер, ділмар, топты бастар көсем, дау шешкен шешен болатын ', '', ''],
           'Адам айтқысыз': ['теңдесі жоқ, ақылға сыймайтын, нанғысыз', 'Әлемдегі адам айтқысыз ғылыми тәжірибелер', '', ''],
           'Ажал айдау': ['өлімге қадам жасау, опат болу', 'Тәуелсіз қазақ елім бар деп, паналап келген қазақ әйелін қытайға қайтару - ажалға өз қолымызбен айдау!', '', ''],
           'Ажал аузы': ['өлім халінде, қатер үстінде', 'Ажал аузында жатқан адам, кәлиманы айтуы қажет', '', ''],
           'Айна қатесіз': ['өте ұқсас, бірдей, біркелкі, егіз', '"Алащұбар тілің болады, дүдәмалдау дінің болады" дегені айна қатесіз келіп тұр', '', ''],
           'Айрандай аптап күбідей күптеп': ['үстемдік қылу, қожалық ету, зәулім болу', 'Жаным-ау, айрандай аптап күбідей күптеп болды ғой.', '', ''],
           'Айтқанына көндіріп ұстау': ['бағындыру, мойынсұнып ұстау', 'Ақорда ЕҚЫҰ-на төрағалық етуден бас тартпайды, бірақ айтқанына көндіріп басқаруға тырысады', '', ''],
           'Айылын жимау': ['жасқанбау , сескенбеу', 'Ол ешкімнен айылын жимады', '', ''],
           'Ақ көңіл': ['қайырымды, мейірбан, мейірімді, рақымды, игі, ізгі', 'Ақкөңілдің аты арып, тоны тозбас', 'ақ көңіл <--> ақ жүрек <--> ақ пейілді жұмсақ <--> көңілді', ''],
           'Ақылға сыймау': ['ақыл жетпейтін, мүлде түсініксіз, түсінбеу, түсінбеушілік', 'Америкалық "Ақылға сыймайтын ашылулар шежірешілері"', '', ''],
           'Aла қаптың аузын ашу': ['ортаға салды, бәрін төкті, сырын аитты', 'Ала қаптың аузын аш!', '', ''],
           'Арасынан қыл өтпеу': ['ажыратылмайтын, берік достық, серіктестік', 'Тату арасынан қыл өтпеу ала ауыз.', '', ''],
           'Арқа сүйеу': ['тірек болу', 'Өнеге-үлгіге арқа сүйеу принципінің талаптарының бәрі қарапайым болып келеді.', '', ''],
           'Асығы алшысынан түсу': ['Жолы болды, табысқа жетті', 'Бəріңіздің асықтарыңыз алшысынан түссін!', '', ''],
           'Асығы түгел': ['қалтқысыз бақыт, толық үйлесімділік, жан тыныштығы', 'Оған керек дейсің бе осы, оның асығы түгел.', '', ''],
           'Aт салысу': ['қатысу, жәрдемдесу, көмектесу', 'Келесі жолы міндетті түрде ат салысамын.', '', ''],
           'Аталы сөз': ['дуалы ,салмақты сөз, нақыл сөз, насихат, ғақлия, уағыз', 'Халқымның қадір-қасиеті - аталы сөз', '', ''],
           'Ауыз тию': ['байқап көру, татып көру, татыту', 'Ауыз тигізу - қазақтың ежелден келе жатқан ғұрыптарының бірі', '', ''],
           'Аяқтыға жол ауыздыға сөз бермейтін': ['жылмақай, жылпос, сумақай, сұғанақ', 'Ол жұмыста ауыздыға сөз, аяқтыға жол бермейтін адам болып саналады.', '', ''],
           'Aшуға булығу': ['ашулы,  жынданған,  зығырданы қайнаған, қатты кейіген, ызалы', 'Ашуға булыққандар әкімдікке жиналды.', '', ''],
           'Aяқ астынан': ['кенет, күтпеген жерден, қапыда', 'Бәрі аяқ астынан өзгерді.', '', ''],
           'Бас ию': ['бүгілу, иілу, сыйыну, табыну', 'Жанкүйерлер оның талантына бас иді.', '', ''],
           'Бас қосу': ['бірлестіру, әйел алу, некеге отыру, үйлену', 'Алматыда білікті онкологтар бас қосты.', '', 'жиналысу <--> тұрмысқа шығу'],
           'Бас тарту': ['қабыл алмау, қабылдамау', 'Олар пластикалық пакетті қолданудан бас тартты.', '', ''],
           'Басынан сөз асырмау': ['тиянақты жауап беру, айқын жауап беру', 'Басынан сөз асырмаған, өзгені басындырмаған.', '', ''],
           'Бауы берік болсын': ['берік, денсаулығы күшті, мықты, тың', 'Кішкентайдың бауы берік болсын.', '', ''],
           'Бел буу': ['көңіл тоқтату, тәуекел ету', 'Ол "Дайдидау" әнін орындауға бел буды.', '', ''],
           'Бетке шіркеу болу': ['масқаралап тастау, масқара', 'Жаман жігіт отбасының бетіне шіркеу болады.', '', ''],
           'Бүйректен сирақ шығару': ['қиялдану, қиялдау, ойынан шығару,қиыстыру', 'Бүйректен сирақ шығару-болымсыз нәрседен шатақ шығару,орынсыз жерде сөйлеу.', '', ''],
           'Дайын асқа ие болу': ['аса қиындықсыз, онша қиналмастан', 'Расылхан жұмыстан келіп, дайын асқа қарамастан жатып қалды.', '', ''],
           'Дес бергенде': ['бақытқа орай,бақыт', 'Дес бергенде олай болмай шықты.', '', ''],
           'Дес бермеу': ['аяғын ауыстырып басу,аяққа кезек салмақ салып тұру', 'Ол екінші турда да ешкімге дес бермеді.', '', ''],
           'Дес беру': ['бостандық, еркіндік, ерік', 'Спортшы өзбекстан өкіліне дес берді', '', ''],
           'Дес тию': ['билік, өкім, өкімет, қожалық', 'Дес тиді – ерік берілді, билік тиді.', '', ''],
           'Душар болу': ['бақытсыздық, бәле, қайғы, қырсық', 'Аңшы орман ішінде бір топ қасқырға душар болыпты.', '', ''],
           'Дүние есігін ашу': ['өмірге келу', 'Жыл сайын миллиондаған сәбилер дүние есігін ашады', 'дүниеге есігін ашу <--> дүниеге келу <--> өмірге келу <--> жарыққа келу', ''],
           'Дүние салу': ['қайтыс болу, өліп қалу', 'Бес күн бұрын оның ағасы жол апатынан дүние салған', '', ''],
           'Дінi қатты': ['мейірімсіз, қатыгез', 'Менің өмірімде діні қатты адамдар серек кездескен', '', ''],
           'Дымы құру': ['әбден әлсіреп болу', 'Әрі-бері қарап баланы таппай дымы құрыды.', '', ''],
           'Дірдек қағу': ['дірілдеу, суықтан қалтырау', 'Құлын дірдек қағып тур', '', ''],
           'Жүзіктің көзінен өткендей': ['әдемі, әсем, көрікті, мұнтаздай, мінсіз таза', 'Жүзіктің көзінен өткендей жылпос жас болыс Итбайды губернаторға тапсырды (С.Мұканов).', '', 'қу, жылпос адам <--> пысық <--> мүсінді адамның сипатын береді'],
           'Ебін табу': ['еппен қимылдау', 'Оны ебін тауып ,басқару керек', '', ''],
           'Егіз қозыдай': ['ауыздан түскендей, бір-бірінен аумайды', 'Егіз қозыдай араласқан екі халық', '', ''],
           'Екі дүниеде': ['мәнгі', 'Екі дүниеде де бақытты болудың жолы қандай?', '', ''],
           'Екі қолға бір күрек': ['кез келген жұмыс', 'Екі қолға бір күрек табу қиынға соққан мына заманда қандай жұмысқа болсын жегіле кету – бүгінгінің шындығы.', '', ''],
           'Екі шоқып бір қарау': ['байқау, зейінді', 'Біз сабақта өте құлақ асамыз', '', ''],
           'Ер жүрек': ['батыл, қорықпайтын, жүрек жұтқан', 'Ер жүрек ,батыр қыз ,Әлия!', 'ержүрек <--> жүрек жұтқан <--> жүрегінің түгі бар <--> көкжал', ''],
           'Есі кету': ['қорқып кету, шошыну, абыржу, асып-сасу, әбігерге түсу', 'Ерлі-зайыптының арасына есі кеткен түседі', '', 'қуаныштан дүрлігу <--> қайғыдан абыржу'],
           'Ел аузына іліну': ['атақты болу, айқынды, белгілі болу, даңқы жайылу', 'Оның өлеңдері ел аузына ілікті.', '', ''],
           'Мұрнынан құрты түсу': ['бай болу', 'Біз бәрін ақылды құрақ ұшумыз келді', '', ''],
           'Есін жию': ['өз-өзіне келу,  есіне келу; есі кіру,  ақылға келу; ойлану', 'Ол өзінің ескертуімен оны қытығына тиюды', '', ''],
           'Жалаң аяқ': ['тағдыр, жазмыш', 'Маңдайға жазылған тағдырдан қашып, ешкім ешқайда кете алмайды.', '', ''],
           'Жан ашыр': ['көңіл айту,ниет білдіру', 'Жанымда жан ашитын адам жоқ.', '', ''],
           'Жаны сірі': ['өміршең, ұзақ жасайтын', 'Сонда Шаяхмет деген досым: «Сен жазушы болсаң, мен мұрнымды кесіп берейін» деген.', '', ''],
           'Жеме-жемге келгенде': ['шешуші сәтте, сын сәті, сыни сәт', 'Жеме-жемге келгенде ол әрқашанда жоғалып кетеді.', '', ''],
           'Жерге қарату': ['ұялтқызу, қызарту', 'Сені тағы жерге қараттым.', '', ''],
           'Жоқтың қасы': ['өте аз, кішкене, ептеп, сәл', 'Балалар әні жоқтың қасы!', '', ''],
           'Жол болсын': ['Ақ жол, Сапар оң болсын', 'Жолы болсын әркімнің, орында жол тәртібін!', '', ''],
           'Жол түсу': ['жол ашу, сәттілік', 'Сіз, жол түсіп болса, Алматыға келіңіз.', '', ''],
           'Жұлдыздай ағып өту': ['тез өте шығу , тез өтіп кету', 'Орыс армия офицері Шоқан Шыңғысұлы Уəлиханов шығыстану көгінен құйрықты жұлдыздай ағып өтті.', 'көзді ашып жұмғанша <--> кірпік қаққанша <--> иек кө тергенше <--> қас пен көздің арасында <--> көз ілеспеу <--> ауыз жиғанша <--> тіл қатқанша <--> ә дегенше, әне-міне дегенше <--> әп-сэтте', ''],
           'Жұлдызы оңынан туды': ['дарынды, ақылды, басты', 'Көпшілік елден ерек туған, өнерлі азаматтарға қаратып "сегіз қырлы, бір сырлы" деп айтып жатады.', '', ''],
           'Ит өлген жер': ['тым алыс жер, аулан, алшық', 'Менің туысымның үйі ит өлген жерде орналасқан.', '', ''],
           'Ит жанды': ['берік, көнбіс, көнтерілі, төзімді, шыдамды', 'Ит жанды ит тірілді ғой! - деп қос қабаттаған қамшы бас-көзіме жауып кеп кетті...', 'ит жанды <--> жаны сірі <--> жылқы міңезді <--> ырыққа көнбейтін адам', ''],
           'Көз айырмау': ['үңілу, қадалу, қарау, тесілу, тесірею, шұқшию', 'Ол балық іздеп, судан көзін айырмайды.', '', ''],
           'Көзі жету': ['көзі жету; нану; сену', 'Дәрігер оған көз жетті.', '', ''],
           'Көз қырын салу': ['бағу, бақылау, көздеу, көз салу, қарау', 'Оған көз қырын сал', '', ''],
           'Көз ілмеу (ілінбеу)': ['ұйықтамау, сергек болу', 'Алибек түні бойы көз ілмеді', '', ''],
           'Көзайым болу': ['масаттану, мерейлену, насаттану, шаттану', 'Баласы келіп, апасы көзайым болды.', '', ''],
           'Көзге күйік болу': ['көзіне көріне беру, жынға тию', 'Кет! Көзіме күйік болма!', '', ''],
           'Көзді ашып жұмғанша': ['тез арада, қысқа уақыт ішінде', 'Қыс көзді ашып жұмғанша өтті', '', ''],
           'Көзіне шөп салу': ['алдау, сатып кету', 'Ол өз әйелінің көзіне шөп салып жүр.', '', ''],
           'Көзіңді ашып қарау': ['мұқият қарау, көкірегі өспесін', 'Көзіңді ашып қарамайсың ба?', '', ''],
           'Көңіл бөлу': ['уақытын арнау, көңіл аулау, көңіл бөу', 'Бiз оған көңiл бөлмеймыз.', '', ''],
           'Көңіл қалу': ['кіршік шалу, ойына ақау түсу', 'Сенің істеген жұмысыңа көңілім қалды', '', ''],
           'Көре алмау': ['көре алмау, күндеу, қызғану, қызығу', 'Көре алмау - ең нашар қасиет', '', ''],
           'Көрсе қызар': ['қанағатсыз, тойымсыз ', 'Керекті іспен ғана айналыс, көрсе қызар болма.', '', ''],
           'Қам жеу': ['уайымдау, сары уайымға салыну', 'Қам жемеңіз!', '', ''],
           'Қапы қалу': ['мүмкіндікті пайдалана алмау, қолайлы жағдайды пайдаланбау', 'Наурыз қарсаңында өтетін «Музейдегі түн» акциясынан қапы қалмаңыз!', '', ''],
           'Қапысы жоқ': ['мінсіз, керемет, мұнтаздай', 'Еш қапысы жоқ!', '', ''],
           'Қапысын табу': ['дәл түсу, уақытында болу', 'Дегенмен біздің шығыстың шымыр жігіті қарсыласының қапысын тапты.', '', ''],
           'Қарны ашты': ['үңіреңдеу, ашығу, өзегі талу', 'Менің қарным ашты.', '', ''],
           'Қол қою': ['көну, ырзаласу, қадірін мойындау', 'Келісім-шартқа қол қойдық.', '', ''],
           'Қол қусыру': ['бағыну, көну', 'Мен қол қусырып отыра алмаймын', '', ''],
           'Қол тимеу': ['уақыт жоқ, жұмысбасты болу', 'Қол тимеуді сылтау ету', '', ''],
           'Қол ұшын беру': ['көмектес, көмек қолын беру', 'Көптеген ұйымдар әлеуметтік жағынан осал халыққа қол ұшын береді', '', ''],
           'Қолдан келу': ['мықты болу, меңгеруі керек', 'Әрбір спортшы күштерінде жеңісті қолдан келу', '', ''],
           'Қоясын ашу': ['бөлшектеу,  табу', 'Алаяқтарды қоясын ашу қажет', '', ''],
           'Құдай білсін': ['белгісіз, жұмбақ', 'Бұл жаңбыр қайдан келді Құдай оны біледі', '', ''],
           'Құдай төбеңнен ұрғыр': ['құдай сені көрсетсін, жаза', 'Егер сіз бірдеңе ұрлап алсаңыз, Құдай сізге төбеңнен ұрғыр', '', ''],
           'Құйып қойғандай': ['тура, дәл', 'Бұл көйлек маған құйып қойғандай', '', ''],
           'Құлағым сізде': ['есту, құлақтану, тыңдау', 'Кеңсеге кіріңіз.мен сізде мұқият құлағым.', '', ''],
           'Құлағына алтын сырға': ['ескерту, есте сақтау, назарға', 'Мен жануарлар туралы осы ақпаратты құлағына алтын сырға  аламын', '', ''],
           'Құлақ аспау': ['елемеуге, назар аудармау', 'Мен үй тапсырмасына құлақ аспаймын', '', ''],
           'Құлақ асу': ['байқау, зейінді, абайлау, аңғару, аңдау, аңыстау, бағамдау', 'Біз сабақта өте құлақ асамыз', 'құлақ асу <--> зейін қою <--> құлақ құрышы қану <--> құлағына құю', ''],
           'Құлақ тігу': ['құлақ асу, байқау, зейінді', 'Біз сабақта өте құлақ асамыз', '', ''],
           'Құрақ ұшу': ['жағу, көзге түсу, ұнау', 'Біз бәрін ақылды құрақ ұшумыз келді', '', ''],
           'Қытығына тию': ['өкпелету,ренжіту, жәбірлендіру', 'Ол өзінің ескертуімен оны қытығына тиюды', '', ''],
           'Маңдайға жазылған': ['тағдыр, жазмыш', 'Маңдайға жазылған тағдырдан қашып, ешкім ешқайда кете алмайды.', '', ''],
           'Мойнына алу': ['айып, кінә, кінәні мойындау', 'Біреудің кінәсін өз мойнына алу, айыпты өз мойнынаалу', '', ''],
           'Мұрнымды кесіп берейін': ['дауласу, ерегісу, таластыру', 'Сонда Шаяхмет деген досым: «Сен жазушы болсаң, мен мұрнымды кесіп берейін» деген.', '', ''],
           'Ойда жоқ жерден': ['аңдаусызда, аяқ астынан, байқаусызда', 'Бірақ ойда жоқ жерден саяжайдың қожайыны шыға келді.', '', ''],
           'Оң қарау': ['жақсы ниетті, игі ниетті, тілектес', 'Өткенді мақтан тұту, қазіргі уақытты прагматикалық бағалау және келешекке оң көзқараспен қарау', '', ''],
           'Өкпесі қара қазандай болу': ['өкпелеу, ренжу, жәбірлену', 'Содан бері қос елдің бір біріне өкпесі қара қазандай болған еді.', 'өкпесі қара қазандай болу <--> арасынан мысық өту <--> көңіліне дық ете қалу <--> жүз шайысу', ''],
           'Сары бел': ['жоғарылық, көтеріңкілік', 'Сары даланың бір ұшында – сары бел.', '', ''],
           'Сазайын тартқызу': ['жаза беру, жазалау, сазайын беру', 'Біз оның сазайын береміз!', '', ''],
           'Сегіз қырлы бір сырлы': ['дарынды, ақылды, басты', 'Көпшілік елден ерек туған, өнерлі азаматтарға қаратып "сегіз қырлы, бір сырлы" деп айтып жатады.', '', ''],
           'Сіркесі су көтермеу': ['ештенені көңілі жақтырмайды, долдану, долыру', 'От шықпай түтіндеп, су шалмай шылқылдап отырған кілең сіркесі су көтермейтін наразылар.', '', 'ызылану <--> ренжу <--> ауырып қалу'],
           'Су жүрек': ['қорқақ,батыл емес, жүрексіз, үрейшіл', 'Қоян деген су жүректі білуші ем', '', ''],
           'Суық тию': ['салқын тию, суық өту, суық тию, тұмау', 'Мүмкін маған суық тиіп қалған сияқты', '', ''],
           'Сүттей ұю': ['толық келісімде, тату, бір ауыздан, бір қолдан', 'Олар расымен сүттей ұйып отырған отбасы.', '', ''],
           'Сыр беру': ['әлсіздік көрсету, баяулық, босаңдық', 'Оның денсаулығы сыр беріп жүрген', '', ''],
           'Сыртынан күлу': ['басқа да күледі, келемеждеу, күлу, мазақтау', 'Ол сыртыңнан күлмекші', '', ''],
           'Табанды жалтырату': ['жылдам қашу, тез ағып өту', 'Табаныңды жалтырат осы жерден!', '', ''],
           'Тас жүрек': ['жансыз, сезімсіз безбүйрек, қатал, мейірімсіз', 'Ана мен баланы айырған қайын жұрт тас жүрек пе?', 'тас жүрек <--> діні қатты <--> тас бауыр <--> безбүйрек <--> құдайдан безген <--> жаннан безген', ''],
           'Тақырға отырып қалу': ['адасу, алжасу, жаңылу, қателесу, лағу, теріс кету', 'Бұл жолы азаматтар бар жиған-тергенін «Номад Строй» құрылыс компаниясына салып, тақырға отырып қалған.', 'тақырға отырып қалy <--> cақалын сипап қалу <--> тұзға отырып қалу <--> аузы күю',''],
           'Таяқ жеу': ['желкелен, жазамен қорқыту', 'Менен таяқ жерсің!', '', ''],
           'Тайға таңба басқандай': ['айқын, анық, айқыш', 'Аружан қазақ тілінің ережелерін арнайы дәптерге тайға таңба басқандай ұқыпты етіп жазып жүреді', 'тайға таңба басқандай <--> атқан таңдай <--> соқырға таяқ ұстатқандай', ''],
           'Телегей-теңіз': ['көп, мол, ырғын', 'Телегей теңіз қан төккен батырлықтан гөрі жалғыз тамшы көз жасын құрғатқан батырлық анағұрлым артық.', 'телегей-теңіз <--> көл-көпір <--> көл-көсір <--> ағыл-тегіл <--> ұшан-теңіз <--> ұлан-асыр', ''],
           'Таяқ тастам жер': ['жақын, жақында, жуықта', 'Үйден алыс емес, таяқ тастам жерде.', '', ''],
           'Төбеге ұрғандай болу': ['таңғалған, таңданған', 'Алынған ақпарат тас төбеден ұрғандай болды', '', ''],
           'Түбіне жету ': ['әлсіреу, әлі кету, әлі құру', 'Арамдығың= түбіңе жетеді', '', ''],
           'Тіл үйіру ': ['Өте дәмді, тәтті', 'Тіл үйіру сусын', '', ''],
           'Тірі аруақ': ['ши борбай, азғын, арық, жүдеу, ырғайдай арық', 'Тірі аруаққа айналу', '', ''],
           'Тіс жармау': ['үндемеу, үн қатпау', 'Арман бұл жайлы ешкімге тіс жармады.', 'аузына тас салу <--> иманындай сақтау <--> сөз қайырмау <--> дымын шығармау <--> аузы жұмылу <--> тіс жармау', ''],
           'Тіс қаққан': ['әккі, басалқылы, кәнігі, тәжірибелі', 'Тіс қаққан боксшы', '', ''],
           'Маңдайы ашылған': ['бақытты, оразды, салымды, талайлы, ырысты', 'Қаладағы суреттерде Қара қыздың маңдайы ашылған, алғашқы суреттерден-ақ бойжеткен қыз қадалып қарайды.', 'маңдайы ашылран <--> қыдыр дарыған <--> бақ қонған', ''],
           'Ұлардай шулау ': ['айғайлап жіберу, айқай салу, айқайлап жіберу', 'Ашынған халық ұлардай шулады.', '', ''],
           'Үрерге иті жоқ': ['жасаусыз, түк те жоқ', 'Ол үрерге иті жоқ', '', ''],
           'Үріп ауызға салғандай': ['әдемі, дидарлы, келісті, сүйкімді', 'Ол үріп ауызға салғандай әдемі болатын.', '', ''],
           'Үш қайнаса сорпасы қосылмайды': ['әртүрлі, басқа-басқа, бірдей емес', 'Олардың мінезі тым әр түрлі, үш қайнаса да сорпасықосылмайды.', '', ''],
           'Шаш ал десе бас алу': ['рұқсат етілген шек, ақырғы шек, шектен', 'Ол шаш ал десе бас алу', '', ''],
           'Ши борбай': ['тірі аруақ, азғын, арық, жүдеу, ырғайдай арық', 'Ол  өте ши борбай', '', ''],
           'Шикі өкпе': ['балдырған, бөбек, жас бала, кішкентай бала', 'Ол әлі шикі өкпе', '', ''],
           'Шөп басын сындырмау ': ['әрекетсіздік, қол бостық, іссіздік', 'Ол жаз бойы шөп басын сындырмаған', '', ''],
           'Шынашағына татымайды': ['керегі жоқ, қажеті жоқ', 'Бұл нәрсе жоқ шынашағына татымайды', '', ''],
           'Шыр бітпеу': ['жарлылық, кедейлік, кедейшілік, сорлылық', 'Былтыр оның отбасы шыр бітпеді.', '', ''],
           'Ізін суытпау': ['байқау, бақылау, қадағалап байқау, қадағалау', 'Күдіктіні ізін суытпай ұстады.', '', ''],
           'Іш тарту': ['қабылдау, сезу, сезім, сезіну,толастау, басылу, тыну', 'Мен ғашығыма іш тартамын', '', ''],
           'Іші пысу': ['аңсау, бауырсырау, еңсеу', 'Менің ішім пысып кетті.', '', ''],
           'Ішіне шынашақ айналмайды': ['қанағатсыз, сараң', 'Ішіңе шынашақ айналмайтын Ежірей деген ұлың болады!', '', '']}


keys = ['Абілхаят суы', 'Абырой болғанда', 'Абыройы айрандай төгілу', 'Ағама жеңгем сай', 'Ағаш атқа мінгізу',
        'Ағаштан түйін түю', 'Ағыл-тегіл жылау', 'Ағынан жарылу', 'Ағып тұр (тұрған)', 'Адам айтқысыз', 'Ажал айдау',
        'Ажал аузы', 'Айна қатесіз', 'Айрандай аптап күбідей күптеп', 'Айтқанына көндіріп ұстау', 'Айылын жимау',
        'Ақ көңіл', 'Ақылға сыймау', 'Aла қаптың аузын ашу', 'Арасынан қыл өтпеу', 'Арқа сүйеу', 'Асығы алшысынан түсу',
        'Асығы түгел', 'Aт салысу', 'Аталы сөз', 'Ауыз тию', 'Аяқтыға жол ауыздыға сөз бермейтін', 'Aшуға булығу',
        'Aяқ астынан', 'Бас ию', 'Бас қосу', 'Бас тарту', 'Басынан сөз асырмау', 'Бауы берік болсын', 'Бел буу',
        'Бетке шіркеу болу', 'Бүйректен сирақ шығару', 'Дайын асқа ие болу', 'Дес бергенде', 'Дес бермеу', 'Дес беру',
        'Дес тию', 'Душар болу', 'Дүние есігін ашу', 'Дүние салу', 'Дінi қатты', 'Дымы құру', 'Дірдек қағу',
        'Жүзіктің көзінен өткендей', 'Ебін табу', 'Егіз қозыдай', 'Екі дүниеде', 'Екі қолға бір күрек',
        'Екі шоқып бір қарау', 'Ер жүрек', 'Есі кету', 'Ел аузына іліну', 'Мұрнынан құрты түсу', 'Есін жию',
        'Жалаң аяқ', 'Жан ашыр', 'Жаны сірі', 'Жеме-жемге келгенде', 'Жерге қарату', 'Жоқтың қасы', 'Жол болсын',
        'Жол түсу', 'Жұлдыздай ағып өту', 'Жұлдызы оңынан туды', 'Ит өлген жер', 'Ит жанды', 'Көз айырмау',
        'Көзі жету', 'Көз қырын салу', 'Көз ілмеу (ілінбеу)', 'Көзайым болу', 'Көзге күйік болу', 'Көзді ашып жұмғанша',
        'Көзіне шөп салу', 'Көзіңді ашып қарау', 'Көңіл бөлу', 'Көңіл қалу', 'Көре алмау', 'Көрсе қызар', 'Қам жеу',
        'Қапы қалу', 'Қапысы жоқ', 'Қапысын табу', 'Қарны ашты', 'Қол қою', 'Қол қусыру', 'Қол тимеу', 'Қол ұшын беру',
        'Қолдан келу', 'Қоясын ашу', 'Құдай білсін', 'Құдай төбеңнен ұрғыр', 'Құйып қойғандай', 'Құлағым сізде',
        'Құлағына алтын сырға', 'Құлақ аспау', 'Құлақ асу', 'Құлақ тігу', 'Құрақ ұшу', 'Қытығына тию',
        'Маңдайға жазылған', 'Мойнына алу', 'Мұрнымды кесіп берейін', 'Ойда жоқ жерден', 'Оң қарау',
        'Өкпесі қара қазандай болу', 'Сары бел', 'Сазайын тартқызу', 'Сегіз қырлы бір сырлы', 'Сіркесі су көтермеу',
        'Су жүрек', 'Суық тию', 'Сүттей ұю', 'Сыр беру', 'Сыртынан күлу', 'Табанды жалтырату', 'Тас жүрек',
        'Тақырға отырып қалу', 'Таяқ жеу', 'Тайға таңба басқандай', 'Телегей-теңіз', 'Таяқ тастам жер',
        'Төбеге ұрғандай болу', 'Түбіне жету ', 'Тіл үйіру ', 'Тірі аруақ', 'Тіс жармау', 'Тіс қаққан',
        'Маңдайы ашылған', 'Ұлардай шулау ', 'Үрерге иті жоқ', 'Үріп ауызға салғандай', 'Үш қайнаса сорпасы қосылмайды',
        'Шаш ал десе бас алу', 'Ши борбай', 'Шикі өкпе', 'Шөп басын сындырмау ', 'Шынашағына татымайды', 'Шыр бітпеу',
        'Ізін суытпау', 'Іш тарту', 'Іші пысу', 'Ішіне шынашақ айналмайды']



########################################################
filename = 'Base/idioms.json'
with open(filename, 'w', encoding='utf-8') as f_obj:
    json.dump(phrases, f_obj)


filename = 'Base/idioms_items.json'
with open(filename, 'w', encoding='utf-8') as f_obj:
    json.dump(keys, f_obj)
########################################################