.\" $Revision$
.TH INND 8
.SH NAZWA
innd, inndstart \- InterNetNews daemon
.SH SK£ADNIA
.B innd
[
.B \-a
]
[
.BI \-c " dni"
]
[
.B \-C
]
[
.B \-d
]
[
.B \-f
]
[
.BI \-H " licznik"
]
[
.BI \-i " licznik"
]
[
.BI \-I "adres_IP"
]
[
.BI \-l " rozmiar"
]
[
.B \-L
]
[
.BI \-m " tryb"
]
[
.BI \-n " flaga"
]
[
.BI \-o " licznik"
]
[
.BI \-p "fd_des"
]
[
.BI \-P "port"
]
[
.B \-r
]
[
.B \-s
]
[
.BI \-t " opó¼nienie"
]
[
.BI \-T " licznik"
]
[
.B \-u
]
[
.BI \-X " sekundy"
]
[
.B \-Z
]

.B inndstart
[
.B flagi
]
.SH OPIS
.IR Innd ,
który jest demonem news (InterNetNews), obs³uguje wszystkie nadchodz±ce
feedy. Najpierw wczytuje do pamiêci pliki
.IR active (5),
.IR newsfeeds (5)
i
.IR incoming.conf (5).
Potem otwiera port NNTP do odbierania artyku³ów ze zdalnych stacji (zobacz
opcjê ``\fB\-p\fP''). Je¶li w include/config.h zdefiniowano
.IR HAVE_UNIX_DOMAIN_SOCKETS ,
to do odbioru artyku³ów od lokalnych procesów, takich jak 
.IR nnrpd (8)
i
.IR rnews (1)
otwierane jest gzniazdo strumieniowe dziedziny Uniksowej, a dla
.IR ctlinnd (8)
odwierane jest analogiczne gniazdo datagramowe.
Gdy makro to nie jest zdefiniowane, u¿ywane s± ³±cza nazwane.
.IR Ctlinnd (8)
wykorzystywany jest do kierowania serwer na wykonywanie okre¶lonych akcji.
Otwiera równie¿ bazê
.IR history (5)
i dwa pliki raportowe, zastêpuj±ce jego standardowe wyj¶cie i wyj¶cie b³êdu.
.PP
Po otwarciu wszystkich plików i gniazd,
.I innd
oczekuje na po³±czenia i dane na swoich portach, u¿ywaj±c do tego
.IR select (2)
i nieblokuj±cego I/O.
Je¶li nie ma dostêpnych danych, to wypró¿ni od swoje wewn±trzrdzeniowe
struktury danych. Domy¶lna liczba sekund opó¼nienia przed wypró¿nieniem jest
ustawiana jako
.I <DEFAULT_TIMEOUT w config.data>
(zwykle
.\" =()<.IR @<typDEFAULT_TIMEOUT>@ ) >()=
.IR 300 ) 
sekund.
.PP
Je¶li 
.I innd
otrzyma b³±d ENOSPC (zobacz
.IR intro (2))
podczas zapisu pliku
.IR active ,
pliku article, lub bazy historii, to wy¶le sobie komendê ``throttle''.
Stanie siê to równie¿ je¶li otrzyma zbyt wiele b³êdów I/O podczas próby
zapisu do jakiego¶ pliku.
.SH OPCJE
.TP
.B \-a
Domy¶lnie, je¶li host nie jest wymieniony w pliku
.I incoming.conf
to po³±czenie jest przekazywane do
.IR nnrpd .
Po u¿yciu tej flagi dowolny host mo¿e siê pod³±czyæ i przesy³aæ artyku³y.
.TP
.B \-c
.I innd
odrzuca stare artyku³y. Zasadniczo zachowanie to mo¿e byæ sterowane przez
bazê historii, lecz czasem stacja wyrzuca w sieæ paczkê bardzo starych
artyku³ów. Flaga ``\fB\c\fP'' okre¶la odciêcie. Na przyk³ad ``\fB\-c21\fP''
odrzuca wszelkie artyku³y, wys³ane dawniej ni¿ 21 dni temu. Warto¶æ zerowa
powstrzymuje ten test. Domy¶ln± warto¶ci± jest 14 dni, lecz mo¿na to zmieniæ
opcj± ``artcutoff'' w
.IR inn.conf (5)
.TP
.B \-C
Je¶li u¿yta jest flaga ``\fB\-C\fP'', to
.I innd
przyjmie i przepropaguje lecz nie przetwarza wiadomo¶ci anulowania i
powstrzymania. Jest to przeznaczone dla stacji, w których nadu¿ywane s±
anulowania i które wybieraj± mechanizm z lepsz± autoryzacj±.
.TP
.B "\-d \-f"
.I Innd
normalnie przechodzi w t³o, ustawia standardowe wyj¶cia na pliki raportowe i
od³±cza siê od terminala. Po u¿yciu flagi ``\fB\-d\fP'' serwer tego nie
robi, a po u¿yciu flagi ``\fB\-f\fP'', serwer pozostaje na pierwszym planie.
.TP
.B "\-H \-T \-X"
Flagi ``\fB\-H\fP'', ``\fB\-T\fP'' i ``\fB\-X\fP'' steruj± liczb± po³±czeñ
dozwolonych na minutê. Ma to w za³o¿eniach dzia³aæ jako ochrona serwera
przed czytnikami, które wykonuj± w ci±gu minuty zbyt wiele po³±czeñ z
serwerem. Zazwyczaj nie u¿ywa siê tego, chyba ¿e rzeczywi¶cie pojawia siê
jaki¶ problem.
Tablica u¿ywana do tych sprawdzeñ jest ograniczona do 128 wpisów i jest
u¿ywana jako pier¶cieñ (ring). Rozmiar zosta³ wybrany do u³atwienia
obliczania indeksu i do upewnienia siê, ¿e nie zabraknie ci miejsca.
Praktycznie wydaje siê w±tpliwe, ¿eby¶ wykorzysta³ nawet po³owê tablicy
naraz.
.IP
Flaga ``\fB\-H\fP'' ogranicza liczbê razy, do której host mo¿e siê po³±czyæ
z serwerem podczas ``\fB\-X\fP'' sekund. Domy¶lnie 2.
.IP
Flaga ``\fB\-T\fP'' ogranicza ca³kowit± liczbê nadchodz±cych po³±czeñ innda
w okresie ``\fB\-X\fP'' sekund. Maksymaln± warto¶ci± jest 128. Domy¶ln± 60.
.IP
Flaga ``\fB\-X\fP'' ustawia liczbê sekund, u¿ywan± przez  ``\fB\-H\fP'' i
``\fB\-T\fP''. Warto¶æ zerowa wy³±cza sprawdzanie. Domy¶lnie jest 0.
.TP
.B \-i
Flaga ``\fB\-i\fP'' ogranicza liczbê nadchodz±cych po³±czeñ NNTP. Warto¶æ
zerowa wy³±cza to sprawdzenie. Domy¶ln± warto¶ci±, je¶li w \fIinn.conf\fR(5)
nie podano opcji ``maxconnections'' jest 50.
Wymieniona opcja jest zastêpowana warto¶ci± tej opcji.
.TP
.B \-I
Opcja ta umo¿liwia wi±zanie innda do podanego adresu interfejsu IP. Adres IP
musi byæ w postaci kropkowej czwórki liczb (nnn.nnn.nnn.nnn). Zobacz te¿
opcjê ``bindaddress'' w
.IR inn.conf (5).
.TP
.B \-l
Flaga ``\fB\-l\fP'' ogranicza rozmiar artyku³u. Po u¿yciu tej flagi,
wszystkie artyku³y wiêksze ni¿
.I rozmiar
bajtów bêd± odrzucane. Domy¶ln± warto¶ci± jest 1000000L bajtów. Sprawdzanie
mo¿na wy³±czyæ, u¿ywaj±c warto¶ci zerowej.
.TP
.B \-L
Flaga ``\fB\-L\fP'' powoduje, ¿e
.I innd
nie tworzy dowi±zañ do crosspostowanych artyku³ów. Stacja typu
``feed-only'' mo¿e tego u¿yæ do zwiêkszenia wydajno¶ci. Mo¿na to te¿
po³±czyæ z feedem kana³owym do programu
.IR crosspost (8)
i przerzuciæ zadanie tworzenia dowi±zañ poza pêtlê przetwarzania innda.
.TP
.B \-m
Flaga ``\fB\-m\fP'' s³u¿y do uruchamiania serwera w zatrzymanym lub
st³umionym stanie (zobacz
.IR ctlinnd (8)).
Argument rozpoczyna siê pojedyncz± liter±:
.IR g ,
.IR p
lub
.IR t ,
wskazuj±ce na ``go'' (startuj), ``pause'' (zatrzymaj) lub ``throttle''
(st³um).
.TP
.B \-n
Flaga ``\-n'' okre¶la czy pauzowanie lub st³umienie serwera powinno równie¿
wy³±czyæ przysz³e procesy czytnikowe. Warto¶æ ``\fBy\fP'' powoduje, ¿e
czytniki zachowuj± siê jak serwer, a warto¶æ ``\fBn\fP'' umo¿liwia czytanie
nawet gdy serwer nie pracuje.
Domy¶lnie zezwala siê na czytanie, a zmieniæ mo¿na to opcj±
``readerswhenstopped'' z
.IR inn.conf (5).
.TP
.B \-o
Flaga ``\fB\-o\fP'' s³u¿y ograniczaniu ilo¶ci plików, które s± utrzymywane
otwarte dla wychodz±cych feedów plikowych. Domy¶ln± warto¶ci± jest liczba
dostêpnych deskryptorów minus czê¶æ zarezerwowana do u¿ytku wewnêtrznego.
.TP
.B \-p
Po u¿yciu flagi ``\fB\-p\fP'' przyjmuje siê, ¿e port NNTP jest otwierany na
podanym deskryptorze. (Je¶li u¿yta jest ta flaga, to
.I innd
zak³ada, ¿e pracuje z w³a¶ciwymi uprawnieniami i nie bêdzie wo³a³
.IR chown (2)
na ¿adnych z tworzonych plików lub katalogów.)
.TP
.B \-P
Je¶li u¿yta jest flaga ``\fB\-P\fP'', to podany port jest u¿ywany do
nas³uchiwania po³±czeñ.
.I innd
musi mieæ wystarczaj±ce uprawnienia startowe by otworzyæ podany port.
.TP
.B \-r
Je¶li u¿yta jest flaga ``\fB\-r\fP'', serwer przenumeruje plik
.I active
zupe³nie tak, jak po wys³aniu komendy ``renumber''.
.TP
.B \-s
Je¶li u¿yta jest flaga ``\fB\-s\fP'', to
.I innd
nic nie bêdzie robiæ, lecz tylko sprawdzi sk³adniê pliku
.IR newsfeeds .
Je¶li bêd± tam b³êdy, to zg³osi kod b³êdu; rzeczywiste b³êdy bêd± natomiast
zg³oszone w
.IR syslog (3).
.TP
.B \-t
Zmienia czas opó¼nienia przed wypró¿nieniem do
.IR timeout 
sekund.
.TP
.B \-u
Raporty s± normalnie buforowane; flaga ta wy³±cza to zachowanie.
.TP
.B "\-Z"
Flaga ``\fB\-Z\fP'' wy³±cza strumieniowanie, wiêc
.I innd
nie przyjmie `mode stream' i innych poleceñ strumieniowych.
.PP
.I Inndstart
jest ma³ym programem typu front-end, który otwiera port NNTP, ustawia uid i
gid na opiekuna news, a nastêpnie uruchamia demona
.I innd
z flag± ``\fB\-p\fP'' i minimalnym bezpiecznym ¶rodowiskiem.
Jest to ma³y front-end dla stacji, która nie chce uruchamiaæ 
.I innd
z uprawnieniami roota.
.SH "KOMUNIKATY STERUJ¡CE"
Artyku³y przychodz±ce, maj±ce nag³ówek Control, lub nag³ówek Subject, który
rozpoczyna siê piêcioma znakami \&``cmsg\ '',  s± nazywane
.IR "komunikatami steruj±cymi" .
Poza komunikatem anulowania, s± one zaimplementowane przez zewnêtrzne
programy w katalogu
.I <pathcontrol w inn.conf>
o ile
.I <usecontrolchan w inn.conf>
jest ustawione na ``false''. (Komunikaty anulowania (cancel) od¶wie¿aj± bazê
historii, wiêc musz± byæ obs³ugiwane wewnêtrznie; koszt synchronizowania,
blokowania i odblokowywania by³by zbyt wysoki przy odbiorze wielu takich
komunikatów.)
.PP
Gdy nadchodzi komunikat steruj±cy, pierwsze s³owo tekstu jest konwertowane
na ma³e litery i jest u¿ywane jako nazwa uruchamianego programu. Je¶li
program nie istnieje, wywo³ywany jest domy¶lny program, okre¶lony przez
.IR "<pathcontrol w inn.conf>/default" .
.PP
Wszystkie programy steruj±ce s± wywo³ywane z czterema parametrami. Pierwszym
jest adres nadawcy komunikatu; jest to pobierane z nag³ówka Sender. Je¶li
nag³ówek ten jest pusty, to dane s± pobierane z nag³ówka From. Nastêpnym
parametrem jest adres zwrotny replik; pobierany z nag³ówka Reply-To.
Je¶li nag³ówek ten jest pusty, u¿yty zostanie adres nadawcy.
Trzecim parametrem bêdzie nazwa pliku, w którym znajduje siê artyku³
wzglêdem katalogu sk³adowego news.
Czwartym parametrem jest host, który wys³a³ artyku³. Jest to odczytywane z
linii Path.
.PP
Je¶li
.I <usecontrolchan w inn.conf> 
jest ustawione na ``true'', to ¿aden komunikat steruj±cy nie bêdzie
przetwarzany przez program zewnêtrzny, forkowany przez innda. Zamiast tego,
bêdzie przetwarzany przez skrypt
.IR controlchan ,
który jest wywo³ywany jako program kana³owy innda. Nie musisz do u¿ywania
tego skryptu konfigurowaæ
.IR newsfeeds (5).
Przetwarzanie z u¿yciem
.I controlchan
mo¿e zredukowaæ nadmierne obci±¿enie, je¶li zbyt wiele komunikatów
steruj±cych pojawia siê naraz.
.PP
Dystrybucja komunikatu steruj±cego jest odmienna od dystrybucji
standardowych artyku³ów.
.PP
Komunikaty steruj±ce normalnie wpadaj± do grupy dyskusyjnej
.IR control .
Mog± one byæ zapisywane w podgrupach, lecz w oparciu o polecenie komunikatu
steruj±cego.
Na przyk³ad komunikat newgroup mo¿e byæ zapisany w grupie
.I control.newgroup
lub w ogólnym
.IR control ,
je¶li specjalizowana podgrupa nie istnieje.
.PP
Stacje mog± jawnie udostêpniaæ grupê ``control'' w ich listach zapisowych,
lecz zwykle lepiej jest j± wy³±czyæ. Je¶li komunikat steruj±cy jest wysy³any
na grupê, której nazwa koñczy siê czterema znakami ``.ctl'', to przyrostek
jest obcinany, a to co pozostanie jest u¿ywane jako nazwa grupy.
Na przyk³ad komunikat anuluj±cy, wys³any na ``news.admin.ctl'' zostanie
przes³any do wszystkich stacji zapisanych na grupy ``control'' lub
``news.admin''.
.PP
Je¶li
.I <mergetogroups w inn.conf>
jest ustawione na ``true'', to gdy artyku³ jest wysy³any na grupê, która
rozpoczyna siê trzema literami ``to.'', to zostanie potraktowany specjalnie
je¶li grupa ta nie istnieje w pliku
.IR active :
artuku³ jest sk³adowany do grupy ``to'' i jest wysy³any do pierwszej stacji,
nazwanej po przedrostku. Na przyk³ad, wysy³anie do ``to.uunet'' zostanie
z³o¿one do ``to'' i przes³ane do stacji ``uunet''.
file:
.SH "RÓ¯NICE PROTOKO£U"
.I Innd
implementuje komendy NNTP zdefiniowane w RFC 977 z nastêpuj±cymi
odstêpstwami:
.IP 1.
Za
\&``\fIlist\fP''
mo¿e wystêpowaæ dodatkowo argument
\&``\fIactive\fP'',
\&``\fIactive.times\fP'',
\&``\fInewsgroups\fP''
lub
\&``\fIsubscription\fP''.
Jest to popularne rozszerzenie, lecz nie w pe³ni obs³ugiwane; zobacz
.IR nnrpd (8).
.IP 2.
Zaimplementowane s± komendy
\&``\fIauthinfo user\fP''
oraz
\&``\fIauthinfo pass\fP''.
Zobacz draft-barber-nntp-imp-07.txt dla dalszych szczegó³ów.
.IP 3.
Udostêpniona jest nowa komenda,
\&``\fImode reader\fP''.
Komenda ta powoduje, ¿e serwer przekazuje po³±czenie do
.IR nnrpd .
Komenda
\&``\fImode query\fP''
przeznaczona jest dla przysz³ych zastosowañ i obecnie jest traktowana tak
samo.
.IP 4.
Udostêpnione s± komendy wspieraj±ce transfer strumieniowy:
\&``\fIcheck messageid\fP'' i ``\fItakethis messageid\fP''.
.IP 5.
Udostêpniona jest komenda transferu wsadowego ``\fIxbatch
liczba-bajtów\fP''. Komenda ta odczyta \fIliczbê-bajtów\fP bajtów i zapisze
je dla dalszego przetwarzania przez rnews(1) (który nale¿y uruchomiæ
oddzielnie). Obejrzyj programy innxbatch i sendxbatches.sh.
.IP 6.
Pozosta³ymi zaimplementowanymi komendami s±
\&``\fIhead\fP'' ,
\&``\fIhelp\fP'' ,
\&``\fIihave\fP'' ,
\&``\fIquit\fP''
oraz
\&``\fIstat\fP''.
.SH "MODYFIKACJE NAG£ÓWKÓW"
.I Innd
modyfikuje tak ma³o nag³ówków, jak ma³o siê da, lecz móg³by byæ lepszy.
.PP
Oto lista nag³ówków, które, je¶li istniej±, s± usuwane:
.RS
.nf
Date-Received
Posted
Posting-Version
Received
Relay-Version
.fi
.RE
Puste nag³ówki oraz nag³ówki, sk³adaj±ce siê z bia³ych spacji równie¿ s±
opuszczane.
.PP
Do nag³ówka Path doklejana jest nazwa lokalnej stacji 
(okre¶lanej przez warto¶æ ``pathhost'' w
.IR inn.conf (5))
i wyrzyknik (je¶li nazwa pierwszej stacji nag³ówka ró¿ni siê od lokalnej).
.PP
Nag³ówek Xref jest usuwany i tworzony jest nowy.
.PP
W przypadku nieobecno¶ci, nag³ówek Lines jest dodawany.
.PP
.I Innd
nie przepisuje nieprawid³owych nag³ówków. Na przyk³ad nie bêdzie zmieniaæ
nieprawid³owego nag³ówka Lines, ale odrzuci artyku³.
.SH RAPORTOWANIE
.I Innd
raportuje wszystkie nadchodz±ce artyku³y do pliku raportowego. Jest to plik
tekstowy o zmiennej ilo¶ci rozdzielanych spacjami pól o jednym z
nastêpuj±cych formatów:
.RS
.nf
mon dd hh:mm:ss.mmm + feed <Message-ID> stacja...
mon dd hh:mm:ss.mmm j feed <Message-ID> stacja...
mon dd hh:mm:ss.mmm c feed <Message-ID> stacja...
mon dd hh:mm:ss.mmm - feed <Message-ID> powód...
.fi
.RE
.PP
Po polu Message-ID mo¿e byæ równie¿ pole nazwy hosta i rozmiaru, zale¿nie od
opcji ``nntplinklog'' i ``logsize'' z
.IR inn.conf (5).
.PP
Pierwsze trzy pola s± polami daty i czasu w rozdzielczo¶ci milisekundowej.
Pi±te pole jest stacj±, która wys³a³a artyku³ (odczytywane z nag³ówka Path).
Szóste pole jest identyfikatorem artyku³u; je¶li informacja jest
niedostêpna, pojawi siê w jej miejscu pytajnik.
.PP
Czwarte pole okre¶la czy artyku³ zosta³ przyjêty czy nie. Je¶li jest tam
znak plus, to zosta³ przyjêty. Je¶li ``j'', to zosta³ przyjêty, lecz
wszystkie grupy maj± w swoich rekordach
.I active
``j'', wiêc artyku³ zosta³ z³o¿ony do grupy ``junk''.
Je¶li w polu pojawi³a siê litera ``c'', to przed pojawieniem siê
oryginalnego artyku³u odebrany zosta³ komunikat anuluj±cy.
We wszystkich tych przypadkach artyku³ zosta³ przyjêty i pole ``stacja...''
zawiera rozdzielon± spacjami listê stacji, do których artyku³ jest
przesy³any.
.PP
Je¶li czwarte pole zawiera znak minusa, o artyku³ zosta³ odrzucony. Powodami
odrzucenia mog± byæ:
.RS
.nf
"%s" header too long (za d³ugi nag³ówek)
"%s" wants to cancel <%s> by "%s" ("%s" chce anulowaæ <%c> poprzez "%s")
Article exceeds local limit of %s bytes (Artyku³ przekracza lokalny 
                                         limit %s bajtów)
Article posted in the future -- "%s" (Artyku³ wys³any w przysz³o¶ci -- "%s")
Bad "%s" header (Z³y nag³ówek "%s")
Can't write history (Nie mogê zapisaæ historii)
Duplicate (Duplikat)
Duplicate "%s" header (Zduplikowany nag³ówek "%s")
EOF in headers (EOF w nag³ówkach)
Linecount %s != %s +- %s (Liczba linii %s != %s +- %s)
Missing %s header (Brak nag³ówka %s)
No body (Brak cia³a)
No colon-space in "%s" header (Brak dwukropka-spacji w nag³ówku "%s")
No space (Brak spacji (albo miejsca???))
Space before colon in "%s" header (Spacja przed dwukropkiem w nag³ówku "%s")
Too old -- "%s" (Za stare -- "%s")
Unapproved for "%s" (Niezatwierdzone dla "%s")
Unwanted newsgroup "%s" (Niechciana grupa dyskusyjna "%s")
Unwanted distribution "%s" (Niechciana dystrybucja "%s")
Whitespace in "Newsgroups" header -- "%s" (Bia³a spacja w nag³ówku
                                           "Newsgroups" -- "%s")
.fi
.RE
Gdzie ``%s'' jest podmieniane przez konretniejsze informacje.
.PP
Zauwa¿, ¿e je¶li artyku³ jest przyjêty i <wanttrash w inn.conf> jest
ustawione na ``ues'' i ¿adna z grup nie jest odpowiednia, to zostanie
zraportowany w dwóch liniach: w linii ``j'' i ``\-''.
.PP
.I Innd
zg³asza te¿ obszerne raporty poprzez
.IR syslog a.
Pierwsze s³owo komunikatu raportowego bêdzie: nazw± stacji, je¶li wpis jest
dla niej specyficzny (np. komunikat ``connected''); s³owem ``SERVER'', je¶li
komunikat jest zwi±zany z serwerem, np. gdy pojawi siê b³±d odczystu.
.PP
Je¶li drugim s³owem s± cztery litery ``cant'', to zg³aszany jest b³±d.
W tym przypadku nastêpne dwa s³owa ogólnie nazywaj± wywo³anie systemowe lub
funkcjê biblioteczn±, która siê nie powiod³a oraz obiekt, wokó³ którego
wykonywane by³y dzia³ania. Reszta linii mo¿e zawieraæ inne informacje.
.PP
W innych przypadkach, drugie s³owa okre¶la rodzaj zmiany, a reszta linii
u¶ci¶la tê informacjê. S³owo ``internal'' ogólnie oznacza wewnêtrzny b³±d
logiczny.
.SH SYGNA£Y
.I Innd
przechwytuje sygna³y SIGTERM i SIGDANGER i wy³±cza siê po nich. Je¶li u¿yta
jest flaga ``-d'', przechwytywany bêdzie równie¿ SIGINT i bêdzie dzia³a³
analogicznie.
.PP
.I Innd
przechwytuje sygna³ SIGUSR1 i odtwarza kana³ steruj±cy, wykorzystywany
normalnie dla
.IR ctlinnd (8).
.SH HISTORIA
Napisane przez Richa $alza <rsalz@uunet.uu.net> dla InterNetNews.
.de R$
Jest to rewizja \\$3, z daty \\$4.
..
.R$ $Id$
.SH "ZOBACZ TAK¯E"
active(5),
ctlinnd(8),
crosspost(8),
dbz(3),
history(5),
incoming.conf(5),
inn.conf(5),
newsfeeds(5),
nnrpd(8),
rnews(1),
syslog(8).
